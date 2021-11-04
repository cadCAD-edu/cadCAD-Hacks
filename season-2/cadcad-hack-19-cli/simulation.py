# cadCAD configuration modules
from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment

# cadCAD simulation engine modules
from cadCAD.engine import ExecutionMode, ExecutionContext
from cadCAD.engine import Executor

# cadCAD global simulation configuration list
from cadCAD import configs

# Additional dependencies

# For generating a CLI
import click

# For analytics
import pandas as pd
import numpy as np
# For visualization
import plotly.express as px

# Option for rendering figures on GitHub
import plotly.io as pio

@click.command()
@click.option('--path', default='output.csv', help='Path for storing the .csv results')
@click.option('--mc_runs', default=1, help='Number of Monte Carlo runs')
@click.option('--timesteps', default=100, help='Number of timesteps to simulate')
def simulate(path,
             mc_runs,
             timesteps) -> pd.DataFrame:
    """
    Minimal Prey and Predator model encapsulated
    in a function.
    
    Arguments:
    path - location for saving the simulation results
    mc_runs - number of MC runs
    timesteps - number of timesteps to simulate
    """

    initial_state = {
        'prey_population': 100,
        'predator_population': 15
    }

    system_params = {
        "prey_birth_rate": [1.0],
        "predator_birth_rate": [0.01],
        "predator_death_const": [1.0],
        "prey_death_const": [0.03],
        "dt": [0.1]
    }

    def p_predator_births(params, substep, state_history, previous_state):    
        dt = params['dt']
        predator_population = previous_state['predator_population']
        prey_population = previous_state['prey_population']
        birth_fraction = params['predator_birth_rate'] + np.random.random() * 0.0002
        births =  birth_fraction * prey_population * predator_population * dt
        return {'add_to_predator_population': births}


    def p_prey_births(params, substep, state_history, previous_state):
        dt = params['dt']
        population = previous_state['prey_population']
        birth_fraction = params['prey_birth_rate'] + np.random.random() * 0.1
        births =  birth_fraction * population * dt
        return {'add_to_prey_population': births}


    def p_predator_deaths(params, substep, state_history, previous_state):
        dt = params['dt']
        population = previous_state['predator_population']
        death_rate = params['predator_death_const'] + np.random.random() * 0.005
        deaths = death_rate * population * dt
        return {'add_to_predator_population': -1.0 * deaths}


    def p_prey_deaths(params, substep, state_history, previous_state):
        dt = params['dt']
        death_rate = params['prey_death_const'] + np.random.random() * 0.1
        prey_population = previous_state['prey_population']
        predator_population = previous_state['predator_population']
        deaths = death_rate * prey_population * predator_population * dt
        return {'add_to_prey_population': -1.0 * deaths}


    def s_prey_population(params, substep, state_history, previous_state, policy_input):
        y = 'prey_population'
        x = previous_state['prey_population'] + policy_input['add_to_prey_population']
        return (y, x)


    def s_predator_population(params, substep, state_history, previous_state, policy_input): 
        y = 'predator_population'
        x = previous_state['predator_population'] + policy_input['add_to_predator_population']
        return (y, x)


    partial_state_update_blocks = [
        { 
            'policies': {
                'predator_births': p_predator_births,
                'prey_births': p_prey_births,
                'predator_deaths': p_predator_deaths,
                'prey_deaths': p_prey_deaths,
            },
            'variables': {
                'predator_population': s_prey_population,
                'prey_population': s_predator_population
            }
        }
    ]

    sim_config = config_sim({
        "N": mc_runs, # the number of times we'll run the simulation ("Monte Carlo runs")
        "T": range(timesteps), # the number of timesteps the simulation will run for
        "M": system_params # the parameters of the system
    })

    del configs[:] # Clear any prior configs

    experiment = Experiment()
    experiment.append_configs(
        initial_state = initial_state,
        partial_state_update_blocks = partial_state_update_blocks,
        sim_configs = sim_config
    )

    exec_context = ExecutionContext()
    simulation = Executor(exec_context=exec_context, configs=configs)
    raw_result, tensor_field, sessions = simulation.execute()

    # Convert raw results to a Pandas DataFrame
    df = pd.DataFrame(raw_result)

    # Insert cadCAD parameters for each configuration into DataFrame
    for config in configs:
        # Get parameters from configuration
        parameters = config.sim_config['M']
        # Get subset index from configuration
        subset_index = config.subset_id
        
        # For each parameter key value pair
        for (key, value) in parameters.items():
            # Select all DataFrame indices where subset == subset_index
            dataframe_indices = df.eval(f'subset == {subset_index}')
            # Assign each parameter key value pair to the DataFrame for the corresponding subset
            df.loc[dataframe_indices, key] = value

    df.to_csv(path, index=False)
    click.echo(f'Simulation output written at {path}')
    
    return df

if __name__ == '__main__':
    simulate()

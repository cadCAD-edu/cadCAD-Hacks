import numpy as np


# Policy Functions
def calculate_population(rate: float,
                         population_1: float,
                         population_2: float,
                         dt: float) -> float:
    
    return rate * population_1 * population_2 * dt


def p_predator_births(params, substep, state_history, previous_state):
    '''Predator Births Policy Function
    The predator birth rate (rate of predators born per unit of time) is a product of
    the prey population and the predator birth parameter plus a random variable.
    
    i.e. the larger the prey population, the higher the predator birth rate
    '''
    # Parameters   
    dt = params['dt']
    predator_birth_parameter = params['predator_birth_parameter']
    random_predator_birth = params['random_predator_birth']

    # State Variables
    predator_population = previous_state['predator_population']
    prey_population = previous_state['prey_population']

    # Calculate the predator birth rate
    birth_rate = prey_population * (predator_birth_parameter + np.random.random() * random_predator_birth)
    # Calculate change in predator population
    births = calculate_population(
        birth_rate,
        predator_population,
        1,
        dt
    )

    return {'add_to_predator_population': births}


def p_predator_deaths(params, substep, state_history, previous_state):
    '''Predator Deaths Policy Function
    The predator death rate (rate of predators that die per unit of time) is a function of
    the predator death parameter plus a random variable.
    
    i.e. the larger the predator death parameter, the higher the predator death rate
    '''
    # Parameters
    dt = params['dt']
    predator_death_parameter = params['predator_death_parameter']
    random_predator_death = params['random_predator_death']

    # State Variables
    predator_population = previous_state['predator_population']

    # Calculate the predator death rate
    death_rate = predator_death_parameter + np.random.random() * random_predator_death
    # Calculate change in predator population
    deaths = calculate_population(
        death_rate,
        predator_population,
        1,
        dt
    )

    return {'add_to_predator_population': -1.0 * deaths}


def p_prey_births(params, substep, state_history, previous_state):
    '''Prey Births Policy Function
    The prey birth rate (rate of preys born per unit of time) is a function of
    the prey birth parameter plus a random variable.
    
    i.e. the larger the prey birth parameter, the higher the prey birth rate
    '''
    # Parameters
    dt = params['dt']
    prey_birth_parameter = params['prey_birth_parameter']
    random_prey_birth = params['random_prey_birth']

    # State Variables
    prey_population = previous_state['prey_population']

    # Calculate the prey birth rate
    birth_rate = prey_birth_parameter + np.random.random() * random_prey_birth
    # Calculate change in prey population
    births = calculate_population(
        birth_rate,
        1,
        prey_population,
        dt
    )

    return {'add_to_prey_population': births}


def p_prey_deaths(params, substep, state_history, previous_state):
    '''Prey Deaths Policy Function
    The prey death rate (rate of preys that die per unit of time) is a product of
    the predator population and the prey death parameter plus a random variable.
    
    i.e. the larger the predator population, the higher the prey death rate
    '''
    # Parameters
    dt = params['dt']
    prey_death_parameter = params['prey_death_parameter']
    random_prey_death = params['random_prey_death']

    # State Variables
    prey_population = previous_state['prey_population']
    predator_population = previous_state['predator_population']

    # Calculate the prey death rate
    death_rate = predator_population * (prey_death_parameter + np.random.random() * random_prey_death)
    # Calculate change in prey population
    deaths = calculate_population(
        death_rate,
        1,
        prey_population,
        dt
    )

    return {'add_to_prey_population': -1.0 * deaths}

# State Update Functions
def s_predator_population(params, substep, state_history, previous_state, policy_input):
    '''Predator Population State Update Function
    Take the Policy Input `add_to_predator_population`
    (the net predator births and deaths)
    and add to the `predator_population` State Variable.
    '''
    # Policy Inputs
    add_to_predator_population = policy_input['add_to_predator_population']

    # State Variables
    predator_population = previous_state['predator_population']

    # Calculate updated predator population
    updated_predator_population = predator_population + add_to_predator_population

    return 'predator_population', updated_predator_population


def s_prey_population(params, substep, state_history, previous_state, policy_input):
    '''Prey Population State Update Function
    Take the Policy Input `add_to_prey_population`
    (the net prey births and deaths)
    and add to the `prey_population` State Variable.
    '''
    # Policy Inputs
    add_to_prey_population = policy_input['add_to_prey_population']

    # State Variables
    prey_population = previous_state['prey_population']

    # Calculate updated prey population
    updated_prey_population = prey_population + add_to_prey_population

    return 'prey_population', updated_prey_population

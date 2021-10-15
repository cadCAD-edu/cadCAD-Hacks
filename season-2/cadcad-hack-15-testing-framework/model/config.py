# cadCAD configuration modules
from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment

# cadCAD global simulation configuration list
from cadCAD import configs

from model.system_params import system_params
from model.state_variables import initial_state
from model.partial_state_update_blocks import partial_state_update_blocks

sim_config = config_sim({
    "N": 20, # the number of times we'll run the simulation ("Monte Carlo runs")
    "T": range(400), # the number of timesteps the simulation will run for
    "M": system_params # the parameters of the system
})

del configs[:] # Clear any prior configs

experiment = Experiment()
experiment.append_configs(
    initial_state = initial_state,
    partial_state_update_blocks = partial_state_update_blocks,
    sim_configs = sim_config
)

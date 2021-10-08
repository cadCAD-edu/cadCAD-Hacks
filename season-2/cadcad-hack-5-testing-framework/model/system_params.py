system_params = {
    # Parameters describing the interaction between the two populations:
    
    # A parameter used to calculate the rate of predator birth
    "predator_birth_parameter": [0.01], 
    # A parameter used to calculate the rate of predator death
    "predator_death_parameter": [1.0],
    # A parameter used to calculate the rate of prey birth
    "prey_birth_parameter": [0.6, 1.0],
    # A parameter used to calculate the rate of prey death
    "prey_death_parameter": [0.03],

    # Parameters used for random Numpy variable tuning
    # These parameters scale the random variable used to create the random birth / death rate
    
    "random_predator_birth": [0.0002],
    "random_predator_death": [0.005],
    "random_prey_birth": [0.002],
    "random_prey_death": [0.003],

    # Parameter used as conversion factor between 1 unit of time and 1 timestep
    # 10 timesteps == 1 unit of time, i.e. every 10 cadCAD model timesteps, 1 unit of actual model time passes
    
    "dt": [0.1],
}
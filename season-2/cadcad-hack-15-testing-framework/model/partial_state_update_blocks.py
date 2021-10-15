from model.parts.lotka_volterra import *


partial_state_update_blocks = [
    {   
        # Configure the model Policy Functions
        'policies': {
            # Calculate the predator birth rate and number of births
            'predator_births': p_predator_births,
            # Calculate the predator death rate and number of deaths
            'predator_deaths': p_predator_deaths,
            # Calculate the prey birth rate and number of births
            'prey_births': p_prey_births,
            # Calculate the prey death rate and number of deaths
            'prey_deaths': p_prey_deaths,
        },
        # Configure the model State Update Functions
        'variables': {
            # Update the predator population
            'predator_population': s_prey_population,
            # Update the prey population
            'prey_population': s_predator_population
        }
    },
]

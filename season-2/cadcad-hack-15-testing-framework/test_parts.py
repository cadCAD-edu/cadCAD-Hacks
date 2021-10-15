from model.parts.lotka_volterra import p_predator_births, s_predator_population
from model.system_params import system_params


def test_p_predator_births():
    """
    Check that the p_predator_births Policy Function returns expected values
    given a specific State and set of System Parameters.
    """
    previous_state = {
        "predator_population": 15,
        "prey_population": 100,
    }
    system_params = {
        "predator_birth_parameter": 0.01, 
         "random_predator_birth": 0.0002,
         "dt": 0.1,
    }
    result = p_predator_births(params=system_params,
                                      substep=None,
                                      state_history=None,
                                      previous_state=previous_state)

    assert result['add_to_predator_population'] > 0

def test_s_predator_population():
    """
    Check that the s_predator_births State Update Function returns expected values
    given a specific State and Policy Input.
    """
    previous_state = {
        "predator_population": 15,
        "prey_population": 100,
    }
    policy_input = {
        "add_to_predator_population": 2, 
    }
    result = s_predator_population(params=None,
                                   substep=None,
                                   state_history=None,
                                   previous_state=previous_state,
                                   policy_input=policy_input)

    result_predator_population = result[1]
    previous_predator_population = previous_state["predator_population"]
    add_predator_population = policy_input["add_to_predator_population"]

    assert result_predator_population == (previous_predator_population +
                                          add_predator_population)

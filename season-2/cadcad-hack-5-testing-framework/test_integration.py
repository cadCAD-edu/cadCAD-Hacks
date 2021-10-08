from model.run import run


def test_negative_populations():
    """
    Check that there is no negative population in any timestep.
    """

    df = run()

    assert df.predator_population.min() > 0
    assert df.prey_population.min() > 0

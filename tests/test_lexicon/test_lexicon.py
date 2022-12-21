from lexicon import choise_random_gif
from lexicon.animations import hello, help, clouds


def test_random_gif():
    assert choise_random_gif("hello") in hello
    assert choise_random_gif("help") in help
    assert choise_random_gif("clouds") in clouds
    
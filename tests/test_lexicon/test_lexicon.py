import pytest
from lexicon.animations import ImagesSelector


@pytest.fixture
def image_selector():
    return ImagesSelector()


@pytest.mark.parametrize("gif_list_name, expected", [
    ("hello", True),
    ("test", True),
    ("other", True),
    (None, False),
])
def test_random_img(image_selector, gif_list_name, expected):
    result = image_selector.random_img(gif_list_name)
    assert (result is None) != expected

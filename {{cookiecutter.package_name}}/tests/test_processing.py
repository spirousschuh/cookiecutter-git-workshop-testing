from matplotlib import cm
import numpy as np
from PIL import Image
from {{cookiecutter.package_name}}.processing import invert_image


def test_invert_image_one_pixel():
    # given
    test_image = Image.fromarray(
        np.array([[[0, 0, 0, 0]]], dtype=np.uint8)).convert('RGB')

    # when
    inverted_image = invert_image(test_image)

    # then
    expected_pixel = (255, 255, 255)
    assert inverted_image.getpixel((0, 0)) == expected_pixel
    # TODO: Please, check the size of the output image.


def test_invert_image_two_pixel():
    pass

    # TODO: Please try to write a test that checks if the function inverts
    #       images with two pixels

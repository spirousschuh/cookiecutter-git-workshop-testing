import numpy as np
from PIL import Image

def invert_image(image):

    all_pixels = np.array(
        [
            [
                [*image.getpixel((width_counter, height_counter)), 255]
                for width_counter in range(image.width)
            ]
            for height_counter in range(image.height)
        ],
        dtype=np.uint8
    )

    inverted_pixels = 255 - all_pixels

    return Image.fromarray(inverted_pixels).convert('RGB')
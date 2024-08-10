import numpy as np
from insta_stories_cropper.cropper import Cropper


def test_crop():
    width = 100
    height = 200
    image_width = 200
    image_height = 200

    center = [image_width // 2, image_height // 2]

    image = np.zeros([image_width, image_height, 3])

    cropper = Cropper()
    cropper.findCropSize(width, height, image_width, image_height)

    image_cropped = cropper.crop(image, center)

    height_cropped, width_cropped, _ = image_cropped.shape

    assert width == width_cropped
    assert height == height_cropped

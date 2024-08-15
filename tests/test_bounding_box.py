import pytest
from insta_stories_cropper.models.bounding_box import BoundingBox


@pytest.mark.parametrize(
    "bounding_box,expected_center",
    [
        (BoundingBox(0, 0, 10, 10), [5, 5]),
        (BoundingBox(0, 0, 15, 15), [7, 7]),
        (BoundingBox(10, 10, 20, 20), [20, 20]),
        (BoundingBox(10, 10, 15, 15), [17, 17]),
    ],
)
def test_center(bounding_box: BoundingBox, expected_center: list[int]):
    assert expected_center == bounding_box.center

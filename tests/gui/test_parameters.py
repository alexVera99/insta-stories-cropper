import pytest
from insta_stories_cropper.gui.parameters import InputParameters


def test_validate_valid_input_parameters():
    parameters = InputParameters("some/file.mp4", "some/output/folder")

    assert parameters.validate()


@pytest.mark.parametrize(
    "parameters",
    [
        InputParameters(),
        InputParameters(filename="some/file"),
        InputParameters(output_folder="some/output/folder"),
    ],
)
def test_validate_invalid_input_parameters(parameters: InputParameters):
    assert not parameters.validate()

from pathlib import Path

from insta_stories_cropper.app.app import App
from insta_stories_cropper.app.parameters import Parameters
from insta_stories_cropper.gui.exceptions import InvalidInputException
from insta_stories_cropper.gui.parameters import InputParameters
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlButton
from pyforms.controls import ControlDir
from pyforms.controls import ControlFile


class Gui(BaseWidget):
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__("Insta stories cropper")
        self.app = App(
            Parameters(
                time_coherence_history_threshold=50, enable_bounding_box_drawing=False
            )
        )

        # Definition of the forms fields
        self._videofile = ControlFile("Video")
        self._output_folder = ControlDir("Results output file")
        self._runbutton = ControlButton("Run")

        self._videofile.changed_event = self.__video_file_selection_event
        self._output_folder.changed_event = self.__output_folder_selection
        self._runbutton.value = self.__run_event

        # Define the organization of the Form Controls
        self._formset = [
            "_videofile",
            "_output_folder",
            "_runbutton",
        ]

        self.input_parameters = InputParameters()

    def __video_file_selection_event(self) -> None:
        self.input_parameters.filename = self._videofile.value

    def __output_folder_selection(self) -> None:
        self.input_parameters.output_folder = self._output_folder.value

    def __run_event(self) -> None:
        if not self.input_parameters.validate():
            raise InvalidInputException()

        filename = Path(str(self.input_parameters.filename))
        output_filename = self.__generate_output_filename(
            filename, Path(str(self.input_parameters.output_folder))
        )

        self.app.crop(filename, output_filename, [9, 16])

    def __generate_output_filename(
        self, input_filename: Path, output_folder: Path
    ) -> Path:
        return output_folder / f"{input_filename.name}_cropped.avi"

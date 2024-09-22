from insta_stories_cropper.gui.parameters import InputParameters
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlButton
from pyforms.controls import ControlDir
from pyforms.controls import ControlFile


class ComputerVisionAlgorithm(BaseWidget):
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__("Insta stories cropper")

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
            raise Exception("Missing input parameters")


if __name__ == "__main__":
    from pyforms import start_app

    start_app(ComputerVisionAlgorithm)

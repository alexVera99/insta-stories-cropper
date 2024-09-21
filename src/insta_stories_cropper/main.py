from pathlib import Path

from insta_stories_cropper.app.app import App
from insta_stories_cropper.app.parameters import Parameters


def main() -> None:
    ratio = [9, 16]  # [w, h]
    filename = Path("../../videos/1.mp4")
    output_filename = Path("../../videos/output/filename.avi")

    app = App(
        Parameters(
            time_coherence_history_threshold=50, enable_bounding_box_drawing=False
        )
    )

    app.crop(filename, output_filename, ratio)


if __name__ == "__main__":
    main()

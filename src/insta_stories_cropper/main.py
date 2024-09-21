from insta_stories_cropper.app.app import App
from insta_stories_cropper.app.parameters import Parameters


def main() -> None:
    ratio = [9, 16]  # [w, h]
    filename = "../../videos/1.mp4"

    app = App(Parameters(time_coherence_history_threshold=50))

    app.crop(filename, ratio)


if __name__ == "__main__":
    main()

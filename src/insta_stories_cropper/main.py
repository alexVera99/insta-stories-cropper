from insta_stories_cropper.gui.gui import Gui


def main() -> None:
    from pyforms import start_app

    start_app(Gui)


if __name__ == "__main__":
    main()

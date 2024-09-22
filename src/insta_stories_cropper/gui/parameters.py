from dataclasses import dataclass


@dataclass
class InputParameters:
    filename: str | None = None
    output_folder: str | None = None

    def validate(self) -> bool:
        return self.filename is not None and self.output_folder is not None

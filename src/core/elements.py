from dataclasses import dataclass


@dataclass
class TerminalElement:

    value: str
    element_type: str
    row: int
    column: int
    active: bool = True
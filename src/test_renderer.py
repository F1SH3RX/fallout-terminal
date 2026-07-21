from core.generator import PuzzleGenerator
from utils.loader import load_words
from ui.renderer import TerminalRenderer


words = load_words(8)


generator = PuzzleGenerator(
    "OVERSEER",
    words
)


puzzle = generator.generate()


renderer = TerminalRenderer()

renderer.render(puzzle)
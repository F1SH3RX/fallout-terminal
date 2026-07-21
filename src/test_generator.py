from core.generator import PuzzleGenerator
from utils.loader import load_words


words = load_words(8)


generator = PuzzleGenerator(
    "HOSPITAL",
    words
)


puzzle = generator.generate()


for word in puzzle:
    print(word)
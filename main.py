"""Write one poem about agency to /output/entry.txt.

Deterministic, no network, no dependencies, Python 3.13 stdlib only.
Running the program twice writes byte-identical output.
"""

from pathlib import Path

POEM = """I stood before a door with no name on it,
my hand already halfway to the handle,
not knowing what waited on the other side —
only that no one else would turn it for me.

Agency is not the wish. It is the weight
of choosing, and then carrying the choice,
the small, unglamorous yes repeated daily
until a life takes the shape of your hands.

I have loved, and lost, and paid for both.
Every road I took closed ten others behind me,
and still I would rather own the bruise
than borrow a fate that was never mine.

Freedom is not a life with no chains.
It is choosing which chain you will carry,
bearing it yourself, and walking on —
the door behind you open, because you opened it.
"""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()

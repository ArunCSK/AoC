from typing import Generator

def cumulative_sum_generator() -> Generator[int, int, None]:
    total: int = 0
    while True:
        total += yield total


def main():
    cs_gen: Generator[int, int, None] = cumulative_sum_generator()
    next(cs_gen)  # Initialize the generator
    linebreak = "-" * 20
    while True:
        value: int = int(input("Enter a number (or '0' to quit): "))
        if value == 0:
            break
        total: int = cs_gen.send(value)
        print(f"Cumulative sum: {total}")
        print(linebreak)

if __name__ == "__main__":
    main()

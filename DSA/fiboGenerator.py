from typing import Generator


def fibo() -> Generator[int, None, None]:
    """Generate Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main() -> None:
    """Main function to demonstrate the Fibonacci generator."""
    print("Fibonacci numbers:")
    n: int = 10  # Number of Fibonacci numbers to generate
    line_break: str = "-" * 20
    fib_gen: Generator[int, None, None] = fibo()
    while True:
        # try:
        input(f"Press Enter to get the next Fibonacci {n} number (or type 'exit' to quit): ")
        print(line_break)
        for _ in range(n):  # Print the first 10 Fibonacci numbers
            print(next(fib_gen))
        print(line_break)
        # except StopIteration:
        #     break

if __name__ == "__main__":
    main()
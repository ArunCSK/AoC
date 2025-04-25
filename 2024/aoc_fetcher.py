import os
import requests
from pathlib import Path

# Define constants
BASE_URL = "https://adventofcode.com"
YEAR = "2024"  # Update this to the current year
SESSION_TOKEN = os.getenv("AOC_TOKEN")  # Ensure you set your token as an environment variable

# Headers for authentication
HEADERS = {"Cookie": f"session={SESSION_TOKEN}"}

def fetch_input(day):
    """Fetch the input for a specific day and save it locally."""
    input_url = f"{BASE_URL}/{YEAR}/day/{day}/input"
    local_file = Path(f"day_{day:02d}_input.txt")

    # Check if input is already fetched
    if local_file.exists():
        print(f"Input for Day {day} already exists locally.")
        return

    # Fetch input from Advent of Code
    response = requests.get(input_url, headers=HEADERS)
    if response.status_code == 200:
        local_file.write_text(response.text.strip())
        print(f"Fetched input for Day {day} and saved to {local_file}")
    else:
        print(f"Failed to fetch input for Day {day}. Status code: {response.status_code}")
        print("Ensure your session token is correct.")

def create_template(day):
    """Create a Python script template for a specific day."""
    template_file = Path(f"day_{day:02d}_solution.py")
    if template_file.exists():
        print(f"Template for Day {day} already exists.")
        return

    template_content = f"""\"\"\"
Advent of Code {YEAR} - Day {day}
\"\"\"

def part1(input_data):
    # Your solution for Part 1
    pass

def part2(input_data):
    # Your solution for Part 2
    pass

if __name__ == "__main__":
    with open("day_{day:02d}_input.txt") as f:
        input_data = f.read().strip()

    print("Part 1 Solution:", part1(input_data))
    print("Part 2 Solution:", part2(input_data))
"""

    template_file.write_text(template_content)
    print(f"Created solution template for Day {day} at {template_file}")

if __name__ == "__main__":
    day = int(input("Enter the day number: "))
    fetch_input(day)
    create_template(day)
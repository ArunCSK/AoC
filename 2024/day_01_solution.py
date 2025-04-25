"""
Advent of Code 2025 - Day 1

Sample Input:
(Place sample input here)

Part 1:
(Describe your approach here)

Part 2:
(Describe your approach here)
"""

def part1(input_data):
    # Your solution for Part 1
    left_list ,right_list = [], []
    for line in input_data.splitlines():
        left_list.append(int(line.split(" ")[0]))
        right_list.append(int(line.split("  ")[1].lstrip()))
    
    left_sorted_list , right_sorted_list = sorted(left_list), sorted(right_list)
    result_list = 0
    for i in range(len(left_sorted_list)):
        if left_sorted_list[i] > right_sorted_list[i]:
            result_list += left_sorted_list[i] - right_sorted_list[i]
        else:
            result_list += right_sorted_list[i] - left_sorted_list[i]
    
    return result_list

def part2(input_data):
    # Your solution for Part 2
    """Solve part 2."""
    total_points = 0
    left_list, right_list = [], []
    lines = input_data.split("\n")
    for l in lines:
        left_list.append(int(l.split(" ")[0]))
        right_list.append(int(l.split("  ")[1].lstrip()))
    left_list = sorted(left_list)
    right_list = sorted(right_list)

    for i in range(len(left_list)):
        temp_count = right_list.count(left_list[i])
        total_points += left_list[i] * temp_count
        temp_count = 0
    return total_points

if __name__ == "__main__":
    with open("day_01_input.txt") as f:
        input_data = f.read().strip()

    print(f"Part 1 Solution: {part1(input_data)}")
    print("Part 2 Solution:", part2(input_data))

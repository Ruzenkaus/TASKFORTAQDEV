# Task 1: Find the number of red, yellow & green occurrences
def count_occurrences(data):
    red_count = sum(1 for line in data if line[0] == '1')
    yellow_count = sum(1 for line in data if line[1] == '1')
    green_count = sum(1 for line in data if line[2] == '1')
    print("Red =", red_count, ", Yellow =", yellow_count, ", Green =", green_count)
    # looking when in line each color was equal to 1 and summarizing it


# Task 2: Find how long each colour was active for
def color_active_time(data):
    red_time = sum(int(line[0]) * int(line[3]) for line in data)
    yellow_time = sum(int(line[1]) * int(line[3]) for line in data)
    green_time = sum(int(line[2]) * int(line[3]) for line in data)
    print("Red =", red_time, "seconds, Yellow =", yellow_time, "seconds, Green =", green_time, "seconds")
    # Summarizing and occurrences when line with color that we specified is equal to 1


# Task 3: Find all times when Green was active (by time)
def green_active_times(data):
    green_active_times = [line[4] for line in data if line[2] == '1']
    print("Times when Green was active:", green_active_times)
    # We want to see time when green(it has position 2 as index) is euqal to 1 and saving it's time


# Task 4: Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data
def count_cycles(data):
    cycles = 0

    for i in range(len(data) - 4):
        window = data[i:i + 5]

        if (window[0][0] == '1' and
                window[1][1] == '1' and window[2][2] == '1' and
                window[3][1] == '1' and window[4][0] == '1' and window):
            cycles += 1

    print("Number of complete cycles :", cycles)
    # The most difficult for me as task, but as I understood a question it have right answer.
    # So we want to have window with size 5 and iterating with it and when we're hitting or condition of end cycle
    # We increment cycles


# Task 5: Find number of lines with mistakes (multiple colours active at the same time or no colours active)
def count_mistakes(data):
    mistakes = sum(1 for line in data if sum(map(int, line[:3])) != 1 or sum(map(int, line[:3])) == 0)
    print("Number of lines with mistakes:", mistakes)


# Looking for where more than one color in line or no colors by summarizing it

with open("data.txt", "r") as f:
    next(f)
    data = [line.strip().split(',') for line in f]

if __name__ == "__main__":
    print("\nTask1")
    count_occurrences(data)
    print("\nTask2")
    color_active_time(data)
    print("\nTask3")
    green_active_times(data)
    print("\nTask4")
    count_cycles(data)
    print("\nTask5")
    count_mistakes(data)

# My opinion: Good Tasks :) Task 4 was the most difficult

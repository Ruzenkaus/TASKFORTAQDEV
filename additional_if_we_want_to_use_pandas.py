# Made it before Ieva said that I had to use only common libraries Xd

import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data.txt")

    # Task 1: Find the number of red, yellow & green occurrences
    red_count = data['Red'].sum()  # summarizing all reds
    yellow_count = data['Yellow'].sum()  # summarizing all yellows
    green_count = data['Green'].sum()  # summarizing all greens
    print("\nTask1")
    print("Red =", red_count, ", Yellow =", yellow_count, ", Green =", green_count)

    # Task 2: Find how long each colour was active for
    red_time = (data['Red'] * data['TimeActive']).sum()
    yellow_time = (data['Yellow'] * data['TimeActive']).sum()
    green_time = (data['Green'] * data['TimeActive']).sum()
    # As summary of that implementation we're just looking for when color is 1 and addigng it to sum
    print("\nTask2")
    print("Red =", red_time, "seconds, Yellow =", yellow_time, "seconds, Green =", green_time, "seconds")

    # Task 3: Find all times when Green was active (by time)
    green_active_times = data[data['Green'] == 1]['Time'].tolist()
    # Easy way to implement is just find where is green show itself
    print("\nTask3")
    print("Times when Green was active:", green_active_times)

    # Task 4: Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data
    data['Red_shifted'] = data['Red'].shift(-4)
    # adding red_shifted to better finding capability
    # Find rows where the sequence Red-Yellow-Green-Yellow-Red appears
    complete_cycles = (
            (data['Red'] == 1) &
            (data['Red_shifted'] == 1) &
            (data['Yellow'].shift(-3) == 1) &
            (data['Green'].shift(-2) == 1) &
            (data['Yellow'].shift(-1) == 1)
    )

    # Count the number of complete cycles
    cycles = complete_cycles.sum()
    print("\nTask4")
    print("Number of complete cycles:", cycles)

    data.drop(columns=['Red_shifted'], inplace=True)
    # now we dont want that ccolumn

    # Task 5: Find number of lines with mistakes (multiple colours active at the same time or no colours active)
    mistakes = ((data[['Red', 'Yellow', 'Green']].sum(axis=1) != 1) | (
            data[['Red', 'Yellow', 'Green']].sum(axis=1) == 0)).sum()

    # Just findind when all colors is euqal to 1 and summarizing
    print("\nTask5")
    print("Number of lines with mistakes:", mistakes)

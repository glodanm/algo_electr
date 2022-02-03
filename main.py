import math
from collections import Counter


class Electricians:
    def __init__(self, distance, pillar_heights, pillar_numbers):
        self.distance = distance
        self.pillar_heights = pillar_heights
        self.pillar_numbers = pillar_numbers
        self.wire_length = 0

    def count_wire_length(self, start_pillar_height, end_pillar_height, calculated_hypotenuses):
        calculated_hypotenuse = max(calculated_hypotenuses, key=lambda x: x[2] if (
                    start_pillar_height in x[:2] and end_pillar_height in x[:2]) else 0)
        if start_pillar_height == end_pillar_height:
            self.wire_length += self.distance
        elif calculated_hypotenuse:
            self.wire_length += calculated_hypotenuse[2]
        else:
            difference = end_pillar_height - start_pillar_height
            calculate = math.sqrt(math.pow(self.distance, 2) + math.pow(difference, 2))
            calculated_hypotenuses.append([start_pillar_height, end_pillar_height, calculate])
            self.wire_length += calculate
        return self.wire_length

    def get_wire_length(self):
        calculated_hypotenuses = [[]]
        pillar_heights = self.pillar_heights

        for i in range(1, self.pillar_numbers):
            if i + 1 >= self.pillar_numbers:
                if pillar_heights[i] > pillar_heights[i - 1]:
                    pillar_heights[i - 1] = 1
                    break
                if pillar_heights[i] < pillar_heights[i - 1]:
                    pillar_heights[i] = 1
                    break
                break
            if pillar_heights[i - 1] <= pillar_heights[i] and pillar_heights[i + 1] <= pillar_heights[i]:
                pillar_heights[i - 1] = 1
                pillar_heights[i + 1] = 1
            elif pillar_heights[i - 1] > pillar_heights[i]:
                pillar_heights[i] = 1
            elif pillar_heights[i + 1] > pillar_heights[i] and pillar_heights[i - 1] != 1:
                pillar_heights[i] = 1

        for i in range(1, self.pillar_numbers):
            self.count_wire_length(pillar_heights[i - 1], pillar_heights[i], calculated_hypotenuses)

        print(round(self.wire_length, 2))
        return round(self.wire_length, 2)

        
def main():
    try:
        elect_input = open("data/elect.in")
        distance = int(elect_input.readline())
        pillar_heights_line = elect_input.readline()
        pillar_heights = [int(x) for x in pillar_heights_line.split()]
        print(pillar_heights)
        pillar_numbers = len(pillar_heights)

        e = Electricians(distance, pillar_heights, pillar_numbers)

        elect_output = open("data/elect.out", "w")
        elect_output.write(f'You need {e.get_wire_length()} meters of wire')
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()
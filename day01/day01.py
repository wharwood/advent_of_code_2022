class elf:
    def __init__(self, rations: list[int]):
        self.rations = rations
        self.total_calories = sum(rations)

def elves_from_input(input: list[str]) -> list[elf]:
    rations = []
    elves = []
    for line in input:
        if line == "":
            elves.append(elf(rations))
            rations = []
        else:
            rations.append(int(line))
    elves.append(elf(rations))
    return elves

def do_part_1(input: list[str]):
    elves = elves_from_input(input)
    print(max(elves, key= lambda x: x.total_calories).total_calories)

def do_part_2(input: list[str]):
    elves = elves_from_input(input)
    elves.sort(key=lambda x:x.total_calories, reverse=True)
    print(sum([x.total_calories for x in elves[0:3]]))
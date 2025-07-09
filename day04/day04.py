class assignment:
    def __init__(self, first_assignment: tuple[int,int], second_assignment: tuple[int,int]):
        self.sections_1: list[int] = list(range(first_assignment[0], first_assignment[1]+1))
        self.sections_2: list[int] = list(range(second_assignment[0], second_assignment[1]+1))
        self.get_fully_contained()
        self.get_overlap()
    
    def get_fully_contained(self):
        if set(self.sections_1).issubset(set(self.sections_2)) or set(self.sections_2).issubset(set(self.sections_1)):
            self.is_fully_contained = True
        else:
            self.is_fully_contained = False

    def get_overlap(self):
        if len(set(self.sections_1).intersection(set(self.sections_2))) == 0:
            self.is_overlapping = False
        else:
            self.is_overlapping = True

def assignment_from_input(lines: list[str]) -> list[assignment]:
    assignments = []
    for line in lines:
        sections = line.strip().split(",")
        limit_1 = sections[0].split("-")
        limit_2 = sections[1].split("-")
        assignments.append(assignment((int(limit_1[0]),int(limit_1[1])),(int(limit_2[0]),int(limit_2[1]))))
    return assignments
        
def do_part_1(lines: list[str]):
    assignments = assignment_from_input(lines)
    print(sum([1 for x in assignments if x.is_fully_contained]))

def do_part_2(lines: list[str]):
    assignments = assignment_from_input(lines)
    print(sum([1 for x in assignments if x.is_overlapping]))
    
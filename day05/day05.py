from math import floor
import re

class cargo_stack:
    def __init__(self, stack_id: int, crates: list[str]):
        self.stack_id: int = stack_id
        self.crates: list[str] = crates

class move:
    def __init__(self, source: int, destination: int, quanta: int):
        self.source: int = source
        self.destination: int = destination
        self.quanta: int = quanta

class cargo_hold:
    def __init__(self, stacks: list[cargo_stack], moves: list[move]):
        self.stacks: list[cargo_stack] = stacks
        self.moves: list[move] = moves
    
    def __repr__(self):
        stack_str = ''
        str_list = []
        for stack in self.stacks:
            for crate in stack.crates:
                stack_str += crate
            str_list.append(stack_str)
            stack_str = ''
        return str(str_list)

    def do_moves(self):
        for move in self.moves:
            for _ in range(move.quanta):
                moved_crate = next(iter([x.crates.pop() for x in self.stacks if x.stack_id == move.source]))
                next(iter([x.crates.append(moved_crate) for x in self.stacks if x.stack_id == move.destination]))
    
    def get_top_crates(self) -> str:
        return ''.join([x.crates[-1] for x in self.stacks])
    
def parse_input(input: list[str]) -> (list[str,list[str]]):
    stack_strings = []
    move_strings = []
    stacks = True
    for line in input:
        if line == "\n":
            stacks = False
        elif stacks:
            stack_strings.append(line)
        else:
            move_strings.append(line)
    return (stack_strings,move_strings)
    
def initialize_stacks(stack_string: list[str]):
    stacks: list[cargo_stack] = []
    num_stacks = floor(max([len(line) for line in stack_string])/4)
    for i in range(num_stacks):
        stacks.append(cargo_stack(i+1, [x[i*4+1] for x in stack_string if x[i*4+1].isalpha()]))
    for stack in stacks:
        stack.crates.reverse()
    return stacks

def initialize_moves(move_string: list[str]):
    moves = []
    for line in move_string:
        matches = re.findall(r'\d+',line)
        if len(matches) == 3:
            moves.append(move(int(matches[1]),int(matches[2]),int(matches[0])))
    return moves

def do_part_1(input):
    split_input = parse_input(input)
    stacks = initialize_stacks(split_input[0])
    moves = initialize_moves(split_input[1])
    hold = cargo_hold(stacks,moves)
    hold.do_moves()
    print(hold.get_top_crates())
    

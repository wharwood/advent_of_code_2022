def get_index_unique_n(packet: str, n: int) -> int:
    for i in range(len(packet)-n-1):
        if len(packet[i:i+n]) == len(set(packet[i:i+n])):
            return i+n
    return None

def do_part_1(input):
    for line in input:
        print(get_index_unique_n(line, 4))

def do_part_2(input):
    for line in input:
        print(get_index_unique_n(line, 14))
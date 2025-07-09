class pack_item:
    def __init__(self, type: str, container: int):
        self.type = type
        self.priority = self.get_priority()
        self.container = container
    
    def get_priority(self) -> int:
        dec = ord(self.type)
        if dec >= 65 and dec <= 90:
            return dec - 64 + 26
        elif dec >= 97 and dec <= 122:
            return dec - 96
        
class pack:
    def __init__(self):
        self.items = []
        self.error_type = None

    def add_items(self, raw_items:str):
        self.items: list[pack_item] = []
        raw_items = raw_items.strip()
        for i in range(len(raw_items)):
            self.items.append(pack_item(raw_items[i],0))

    def split_items(self, raw_items: str):
        self.items: list[pack_item] = []
        raw_items = raw_items.strip()
        for i in range(len(raw_items)):
            if i < len(raw_items)/2:
                self.items.append(pack_item(raw_items[i],1))
            else:
                self.items.append(pack_item(raw_items[i],2))

    def get_container_items(self, container_id: int):
        return [x for x in self.items if x.container == container_id]

    def get_error_type(self):
        self.items.sort(key=lambda x : x.priority)
        for i in range(1,len(self.items)):
            if self.items[i].type == self.items[i-1].type:
                if self.items[i].container != self.items[i-1].container:
                    self.error_type = self.items[i]

class elf_group:
    def __init__(self):
        self.packs = []
        self.badge = None

    def get_badge(self):
        for i in range(len(self.packs[0].items)):
            for j in range(len(self.packs[1].items)):
                for k in range(len(self.packs[2].items)):
                    if self.packs[0].items[i].type == self.packs[1].items[j].type and self.packs[0].items[i].type == self.packs[2].items[k].type:
                        self.badge = self.packs[0].items[i]

def packs_from_input(input: list[str]) -> list[pack]:
    packs = []
    for line in input:
        pack = pack()
        pack.split_items(line)
        pack.get_error_type()
        packs.append(pack)
    return packs

def elf_groups_from_input(input: list[str]) -> list[elf_group]:
    groups = []
    group = elf_group()
    for line in input:
        if len(group.packs) < 3:
            bag = pack()
            bag.add_items(line)
            group.packs.append(bag)
        else:
            groups.append(group)
            group = elf_group()
            bag = pack()
            bag.add_items(line)
            group.packs.append(bag)
    groups.append(group)
    return groups
        
def do_part_1(input: list[str]):
    bags = packs_from_input(input)
    print(sum([x.error_type.priority for x in bags]))

def do_part_2(input: list[str]):
    groups = elf_groups_from_input(input)
    for g in groups:
        g.get_badge()
    print(sum([x.badge.priority for x in groups]))
class helpers:

    def parse_input(file: str) -> list[str]:
        fp = open(file)
        return fp.readlines()
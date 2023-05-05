def load_file(filename):
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]

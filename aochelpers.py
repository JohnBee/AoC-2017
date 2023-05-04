def load_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]

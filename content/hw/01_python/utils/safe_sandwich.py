class Sandwicher():

    def __init__(self):
        self.entrances, self.exits = 0, 0

    def __enter__(self):
        print("bread")
        self.entrances += 1

    def __exit__(self, *args):
        self.exits += 1
        print("bread")

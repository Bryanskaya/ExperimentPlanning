from Generator import Generator


class Processor(Generator):
    def __init__(self, generator):
        self.generator = generator
        self.isFree = True

    def IsFree(self):
        return self.isFree

    def SetFree(self):
        self.isFree = True

    def SetBusy(self):
        self.isFree = False

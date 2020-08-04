from src.outputs import Output


class StdoutOutput(Output):
    def prepare(self):
        pass

    def compute(self, classified):
        print(classified)

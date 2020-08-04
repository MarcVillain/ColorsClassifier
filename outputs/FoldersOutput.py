from outputs import Output

from helpers.FilesHelper import FilesHelper

class FoldersOutput(Output):
    def prepare(self):
        return FilesHelper.create_dir(self.output_path, self.force)

    def compute(self, classified):
        # FIXME
        pass

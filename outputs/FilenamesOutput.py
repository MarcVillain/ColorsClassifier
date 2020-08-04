from outputs import Output

from helpers.FilesHelper import FilesHelper

class FilenamesOutput(Output):
    def prepare(self):
        return FilesHelper.create_dir(self.output_path, self.force)

    def compute(self, classified):
        # FIXME
        pass

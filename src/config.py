from src.methods.AverageMethod import AverageMethod
from src.methods.DominantMethod import DominantMethod
from src.methods.PaletteMethod import PaletteMethod
from src.outputs.FilenamesOutput import FilenamesOutput
from src.outputs.FoldersOutput import FoldersOutput
from src.outputs.StdoutOutput import StdoutOutput
from src.outputs.YAMLOutput import YAMLOutput
from src.sortings.NameSorting import NameSorting
from src.sortings.RGBSorting import RGBSorting


class Config:
    default_method = "palette"
    methods = {
        "average": AverageMethod,
        "dominant": DominantMethod,
        "palette": PaletteMethod,
    }

    default_sorting = "name"
    sortings = {
        "name": NameSorting,
        "rgb": RGBSorting,
    }

    default_output = "yaml"
    output_types = {
        "yaml": YAMLOutput,
        "filenames": FilenamesOutput,
        "folders": FoldersOutput,
        "stdout": StdoutOutput,
    }

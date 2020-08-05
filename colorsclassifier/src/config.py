from colorsclassifier.src.methods.AverageMethod import AverageMethod
from colorsclassifier.src.methods.DominantMethod import DominantMethod
from colorsclassifier.src.methods.PaletteMethod import PaletteMethod
from colorsclassifier.src.outputs.FilenamesOutput import FilenamesOutput
from colorsclassifier.src.outputs.FoldersOutput import FoldersOutput
from colorsclassifier.src.outputs.StdoutOutput import StdoutOutput
from colorsclassifier.src.outputs.YAMLOutput import YAMLOutput
from colorsclassifier.src.sortings.NameSorting import NameSorting
from colorsclassifier.src.sortings.RGBSorting import RGBSorting


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

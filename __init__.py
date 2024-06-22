from .string_combinations import StringCombinations
from .string_replace import InputStringConstructor
from .split_by_new_line import StringSplitter, UnzipStrings
from .number_of_files_in_dir import FileCounter

NODE_CLASS_MAPPINGS = {
    "InputStringConstructor": InputStringConstructor,
    "StringSplitter": StringSplitter,
    "UnzipStrings": UnzipStrings,
    "FileCounter": FileCounter,
    "StringCombinations": StringCombinations,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "InputStringConstructor": "Input String Constructor Node",
    "StringSplitter": "String Splitter Node",
    "UnzipStrings": "Unzip Strings Node",
    "FileCounter": "File Counter Node",
    "StringCombinations": "String Combinations Node"
}
__all__ = ["InputStringConstructor", "StringSplitter", "UnzipStrings", "FileCounter", "StringCombinations"]
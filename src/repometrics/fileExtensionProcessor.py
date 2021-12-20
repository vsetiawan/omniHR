import os
import json


class FileExtensionProcessor:
    """This class handles processing of file extensions into the language. This allows us to load the extension to language mapping only once 

    Attributes:
        _EXT_TO_LANGUAGE_DATA_FILEPATH: The constant representing the filepath to the extension to language map in json.
        _extToLanguageDict: Dictionary mapping the file extension format to the language that it belongs to.
    """
    _EXT_TO_LANGUAGE_DATA_FILEPATH = "data/extensionLanguage.json"
    _extToLanguageDict = {}

    def __init__(self):
        dirname = os.path.dirname(__file__)
        absolutePath = os.path.join(
            dirname, self._EXT_TO_LANGUAGE_DATA_FILEPATH)
        with open(absolutePath, 'r') as f:
            self._extToLanguageDict = json.load(f)

    def processFileExtension(self, filepath: str) -> str:
        """This class processes the file extension of a given filepath and outputs the language that it belongs to.

        Input:
            filepath: The filepath of the file to be processed
        """
        fileExt = (os.path.splitext(filepath))[1]
        language = ""
        if fileExt != "":
            if fileExt in self._extToLanguageDict:
                language = self._extToLanguageDict[fileExt]
        return language

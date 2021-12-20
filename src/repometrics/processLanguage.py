import json


def processLanguage(filename: str = "languages.json", out_file: str = "extensionLanguage.json") -> None:
    """
    This function processes JSON file containing mapping from languages to its related extensions into a JSON file mapping extensions to the language that it belongs to.

    """
    # Load the file into a dictionary
    with open(filename, 'r') as f:
        data = json.load(f)

    # Map the extension to the language
    extToLanguageDict = {}
    for key in data.keys():
        if "extensions" in data[key]:
            for extension in data[key]["extensions"]:
                extToLanguageDict[extension] = key

    # Save the file
    with open(out_file, 'w') as f:
        json.dump(extToLanguageDict, f, indent=4)


if __name__ == "__main__":
    processLanguage()

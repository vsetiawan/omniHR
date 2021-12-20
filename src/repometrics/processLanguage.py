import json

def processLanguage(filename="languages.json"):
    f = open(filename)
    data = json.load(f)

    extToLanguageDict = {}

    for key in data.keys():
        if "extensions" in data[key]:
            for extension in data[key]["extensions"]:
                extToLanguageDict[extension] = key

    return extToLanguageDict
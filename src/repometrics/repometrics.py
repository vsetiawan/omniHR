import os
import processLanguage
import json

def repometrics(pathToDirectory):
    extToLanguageDict = processLanguage.processLanguage()
    summaryDict = {}
    summaryDict["summary"] = {}
    summaryDict["results"] = []
    totalFileCount = 0
    for root, subdirs, files in os.walk(pathToDirectory):
        for file in files:
            filepath = os.path.join(root, file)
            fileExt = (os.path.splitext(filepath))[1]
            totalFileCount += 1

            # Initialise to 'Others' to cover unknown language type
            language = "Others"
            if fileExt != "":
                if fileExt in extToLanguageDict:
                    language = extToLanguageDict[fileExt]
            resultDict = {
                        "path": filepath,
                        "language": language
            }
            summaryDict["results"].append(resultDict)
            if language in summaryDict["summary"]:
                summaryDict["summary"][language] += 1
            else:
                summaryDict["summary"][language] = 1                    


    for language in summaryDict["summary"].keys():
        summaryDict["summary"][language] = round(summaryDict["summary"][language]/totalFileCount, 6)
    print(json.dumps(summaryDict, indent=4))

if __name__ == '__main__':
    repometrics(".")
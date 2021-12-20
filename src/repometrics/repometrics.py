import os
import json
import fileExtensionProcessor


def repometrics(pathToDirectory):
    """This function generates metrics of a given directory and its subdirectory
    """

    # Initialise variables
    NUM_DECIMAL_PLACE = 6
    processor = fileExtensionProcessor.FileExtensionProcessor()
    summaryDict = {}
    summaryDict["summary"] = {}
    summaryDict["results"] = []
    totalFileCount = 0

    # Process the files
    for root, subdirs, files in os.walk(pathToDirectory):
        for file in files:
            totalFileCount += 1
            filepath = os.path.join(root, file)

            # Process the language
            language = processor.processFileExtension(filepath)
            if language == "":
                language = "Others"

            # Generate and append the result
            resultDict = {
                "path": filepath,
                "language": language
            }
            summaryDict["results"].append(resultDict)
            if language in summaryDict["summary"]:
                summaryDict["summary"][language] += 1
            else:
                summaryDict["summary"][language] = 1

    # Process the statistical summary
    for language in summaryDict["summary"].keys():
        summaryDict["summary"][language] = round(
            summaryDict["summary"][language]/totalFileCount, NUM_DECIMAL_PLACE)

    # Display the output
    print(json.dumps(summaryDict, indent=4))


if __name__ == '__main__':
    repometrics(".")

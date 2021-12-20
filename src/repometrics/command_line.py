import sys
import repometrics.generateSummary as generateSummary

def main():
    pathToDirectory = sys.argv[1]
    generateSummary.generateSummary(pathToDirectory)

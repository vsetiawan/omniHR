# Repometrics

Repometrics takes the list of languages it knows from [`languages.json`](/src/repometrics/data/languages.json) and try to determine the language used by each file and the overall repository breakdown.

Repometrics identify the language used based on the extension of the file.

## Prerequisites
- Python 3 installed
- Pip package management system installed

## Installation
Clone the repository to your local machine

Install it by running pip install, providing path to the repository
```bash
pip install omniHR/
```  

Add the script install directory to the PATH environment variable if it is not on PATH.

## Future Improvements

Repometrics can be further improved by using more strategies to determine language used such as:
- commonly used filename
- Shell Shebang
# ==== Regex
# :: . matching any single character eg. ".at" matches cat hat bat
# :: [] matches single char contained ex. [ch]at matches cat, hat, but not sat [a-z] defines range
# :: [^] matches a single char not contained within brackets [^c] matches hat, sat but no cat

import re

def Main():
        line = "I think I understand regular expressions"

        matchResult = re.match('think', line, re.M|re.I)
        if matchResult:
            print('match found ' + matchResult.group())
        else:
            print('no result found')

        searchResult = re.search('think', line, re.M|re.I)
        if searchResult:
            print('match found ' + searchResult.group())
        else:
            print('no result found')

if __name__ == "__main__":
    Main() 
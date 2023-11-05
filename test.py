import os
from pathlib import Path

if __name__ == '__main__':
    workDir = Path('.')
    asName = 'SpaceClaim.exe'
    aasFile =  workDir / asName

    print(aasFile)

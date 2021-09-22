from wardlooker.WardLooker import WardLooker
from glob import glob

if __name__ == "__main__":
    files = [file for file in glob("resources/*png")]
    print(files)
    looker = WardLooker(files)
    looker.run()

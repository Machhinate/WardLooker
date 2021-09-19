from pyautogui import locateOnScreen
from time import sleep
import winsound


class WardLooker:
    def __init__(self, file_list,
                 sound_file="alert.wav", confidence=0.7):
        self.pings = 0
        self.files = file_list
        self.sound_file = sound_file
        self.confidence = confidence

    def run(self):
        while True:
            self.look()
            sleep(1)

    def look(self):
        if self.pings > 0:
            self.pings -= 1
            return

        sightings = []

        for file in self.files:
            if locateOnScreen(file, confidence=self.confidence):
                sightings.append(file)

        if not sightings:
            return

        for sighting in sightings:
            print(f"unspent {sighting.split('.')[0]} charges")

        self.pings += 20
        self.play_alert()

    def play_alert(self):
        winsound.PlaySound(self.sound_file, winsound.SND_FILENAME)


if __name__ == "__main__":
    files = ["Stealth2.png", "Stealth1.png", "Farsight.png", "Frostfang.png",
             "Harrow.png", "Runesteel.png",  "Vision.png", "Targon.png",
             "BlackMistScyth.png", "BulwarkOfTheMountain.png", "PauldronsOfWhiterock.png",
             "ShardOfTrueIce.png", "VigilantWardstone.png", "WatchfullWardstone.png",
             "ScarecrowEffigy.png"]
    looker = WardLooker(files)
    looker.run()

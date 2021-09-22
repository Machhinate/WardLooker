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
            icon = sighting.split('\\')[1].split('.')[0]
            print(f"unspent {icon} charges")

        self.pings += 20
        self.play_alert()

    def play_alert(self):
        winsound.PlaySound(self.sound_file, winsound.SND_FILENAME)

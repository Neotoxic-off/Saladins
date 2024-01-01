import json
import random

class Randomizer:
    def __init__(self):
        self.config = None

        self.__load_config__()
        self.__randomize__()

    def __load_config__(self):
        with open("config.json", "r") as f:
            self.config = json.loads(f.read())

    def __randomize__(self):
        index = random.randint(0, len(self.config["characters"]) - 1)

        self.__get_character__(index)
        self.__get_skin__(index)

    def __get_character__(self, index):
        print("character: {}".format(
            self.config["characters"][index]["name"]
        ))

    def __get_skin__(self, index):
        skin = random.randint(0, len(self.config["characters"][index]["skins"]) - 1)

        print("skin: {}".format(
            self.config["characters"][index]["skins"][skin]
        ))

if (__name__ == "__main__"):
    Randomizer()

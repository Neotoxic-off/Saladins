import requests
import json
from bs4 import BeautifulSoup

class Extractor:
    def __init__(self):
        self.uri = "https://paladins.fandom.com/wiki"
        self.config = None
        
        self.__load_config__()
        self.__extract__()
        self.__save__()

    def __load_config__(self):
        with open("config.json", "r") as f:
            self.config = json.loads(f.read())

    def __extract__(self):
        for i, character in enumerate(self.config["characters"]):
            r = requests.get(f"{self.uri}/{character['name']}")
            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.find_all(
                'li',
                {
                    'data-hash': True,
                    'class': 'wds-tabs__tab'
                }
            )
            result = [li_tag.find('a').text for li_tag in links][3:]
            if ("Golden" in result):
                result = result[:result.index("Golden") + 1]
            print(f"[{r.status_code}] [{len(result)}] {character['name']}")
            self.config["characters"][i]["skins"] = result

    def __save__(self):
        with open("config.json", "w") as f:
            f.write(json.dumps(self.config, indent=4))


            

if (__name__ == "__main__"):
    Extractor()

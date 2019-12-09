import json
import requests
import settings
from geotext import GeoText

with open("txt/tom.txt", "r") as f1:
    tom = f1.read()

with open("txt/huck.txt", "r") as f2:
    huck = f2.read()

with open("txt/life-on-the-mississippi.txt", "r") as f3:
    life = f3.read()

with open("txt/roughing-it.txt", "r") as f4:
    rough = f4.read()

tom_places = GeoText(tom, "US")
huck_places = GeoText(huck, "US")
life_places = GeoText(life, "US")
rough_places = GeoText(rough, "US")
all_places = (
    tom_places.cities + huck_places.cities + life_places.cities + rough_places.cities
)

past = ""
filtered_places = []

for place in all_places:
    if place != past:
        filtered_places.append(place)
    past = place

pairs = []

for idx, place in enumerate(filtered_places[1:]):
    start = filtered_places[idx]
    end = filtered_places[idx + 1]
    start = start.replace(" ", "+")
    end = end.replace(" ", "+")
    pairs.append((start, end))

for idx, pair in enumerate(pairs):
    resp = requests.get(
        "https://maps.googleapis.com/maps/api/directions/json?origin="
        + pair[0]
        + "+USA&destination="
        + pair[1]
        + "+USA&key="
        + settings.goog
    )
    with open("data/leg-" + str(idx) + ".txt", "w") as filename:
        json.dump(resp.json(), filename)

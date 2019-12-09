import json
from bs4 import BeautifulSoup
from glob import glob
from pprint import pprint


with open("novel.txt", "w") as outfile:
    gl = list(glob("data/*"))
    for item in gl:
        with open(item, "r") as infile:
            data = json.load(infile)

        try:
            outfile.write(
                "Next destination: "
                + data["routes"][0]["legs"][0]["end_address"]
                + "\n\n"
            )

            for step in data["routes"][0]["legs"][0]["steps"]:
                outfile.write("Continue " + step["distance"]["text"] + "\n")
                html = step["html_instructions"]
                soup = BeautifulSoup(html)
                outfile.write(soup.get_text() + "\n")

            outfile.write(
                "\nArrive: " + data["routes"][0]["legs"][0]["end_address"] + "\n\n"
            )
        except IndexError:
            pass

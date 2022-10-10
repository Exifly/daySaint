from bs4 import BeautifulSoup
from saint import Saint
import requests
import os

class Program():
    URL_ENDP: str = "https://www.santodelgiorno.it/"

    def parse(self) :
        resp = requests.get(self.URL_ENDP)
        if not resp.ok:
            print("Error")
            os.exit(-1)
        return resp.content

    def day_saint(self, html: str) -> list:
        saint = Saint()
        soup = BeautifulSoup(html, 'html.parser')
        saint.name = soup.find("div", class_="NomeSantoDiOggi").text
        saint.description = soup.find("div", class_="TipologiaSantoDiOggi").text
        return [santo.serialize() for santo in self.other_saint_list(soup)]

    def other_saint_list(self, soup) -> list:
        saint_list = []
        for s in soup.find_all("a", class_="NomeSantoEl"):
            saint_list.append(Saint(s.text, None))
        return saint_list

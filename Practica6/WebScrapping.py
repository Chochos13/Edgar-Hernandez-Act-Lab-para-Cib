import requests
from bs4 import BeautifulSoup

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def posiciones():
    soup = get_soup("https://www.espn.com.mx/futbol-americano/nfl/posiciones")
    rows = soup.find_all("table")[0].find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        t = [ele.text.strip() for ele in columns]
        print(f"{t}")
        f = open ('TablaDePosiciones.txt','a')
        f.write(f"{t}")
        f.close()

if __name__ == "__main__":
    posiciones()


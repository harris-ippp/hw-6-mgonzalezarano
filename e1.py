import requests
from bs4 import BeautifulSoup

elec_res = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
resp = requests.get(elec_res)
soup = BeautifulSoup(resp.content,"html.parser")

with open("ELECTION_ID","w") as out:
    for result in soup.find_all("tr","election_item"):
        year = result.find("td", "year first").contents[0]
        elect_id = result["id"].split("-")[2]
        out.write("{} {}\n".format(year,elect_id))
        print(year,elect_id)


for line in open("ELECTION_ID"):
    a = line[4:]
    print(a)

import requests
from bs4 import BeautifulSoup

for line in open("ELECTION_ID"):
    year = line.split()[0]
    code = line.split()[-1]

    data = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(code)
    resp = requests.get(data)
    soup = BeautifulSoup(resp.text,"html.parser")

    file_name = year+".csv"
    with open(file_name,"w") as out:
        out.write(resp.text)

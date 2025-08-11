import requests
from bs4 import BeautifulSoup
import csv

class yallaKora: 
    def __init__(self , date): 
        self.date = date
        self.data = { 
            "Championship": [],
            "Team 1" :[],
            "Team 2" :[],
            "Start Time":[],
            "Result":[]
        } 
    
    def show_mathces(self): 
     
        web_page= requests.get(f"https://www.yallakora.com/match-center?date={self.date}")

        if web_page.status_code != 200:
            print(f"Error: date is not found , try again with another date)")
            return

        soup = BeautifulSoup(web_page.content , "lxml")
        championships = soup.find_all("div" , {"class": "matchCard"})
        for championship in championships: 
            nameOfChampion = championship.contents[1].contents[1].find("h2").text.strip()
            matchDetails = championship.contents[3].find_all("div", {"class" : "liItem"})

            for matchDetail in matchDetails:
                teamA = matchDetail.contents[1].contents[1].find("div" , {"class" : "teamCntnr"}).contents[1].find("div" , {"class": "teamA"}).find("p").text.strip()
                teamB = matchDetail.contents[1].contents[1].find("div" , {"class" : "teamCntnr"}).contents[1].find("div" , {"class": "teamB"}).find("p").text.strip()
                details =  matchDetail.contents[1].contents[1].find("div" , {"class" : "teamCntnr"}).contents[1].find("div" , {"class":"MResult"})
                scoreA = details.contents[1].text.strip()
                scoreB = details.contents[5].text.strip()
                time  = details.find("span" , {"class":"time"}).text.strip()
                
                self.data["Championship"].append(nameOfChampion)
                self.data["Team 1"].append(teamA)
                self.data["Team 2"].append(teamB)
                self.data["Start Time"].append(time)
                self.data["Result"].append(f"{scoreA} | {scoreB}")

        with open("Match.csv", mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=self.data.keys())

            writer.writeheader()

            rows = []
            for i in range(len(self.data["Championship"])):
                row = {
                    "Championship": self.data["Championship"][i],
                    "Team 1": self.data["Team 1"][i],
                    "Team 2": self.data["Team 2"][i],
                    "Start Time": self.data["Start Time"][i],
                    "Result": self.data["Result"][i],
                }
                rows.append(row)

            writer.writerows(rows)
            print("\n \n")
            print("You will find file in your directory named 'Match.csv'")
            print("\n\n")



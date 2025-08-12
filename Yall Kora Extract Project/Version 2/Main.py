import requests
from bs4 import BeautifulSoup
import csv
import datetime
import tkinter as tk
from tkinter import messagebox

class yallaKora:
    def __init__(self, date):
        self.date = date
        self.data = {
            "Championship": [],
            "Team 1": [],
            "Team 2": [],
            "Start Time": [],
            "Result": []
        }

    def show_matches(self):
        web_page = requests.get(f"https://www.yallakora.com/match-center?date={self.date}")

        if web_page.status_code != 200:
            messagebox.showerror("Error", "Date not found, try again with another date")
            return

        soup = BeautifulSoup(web_page.content, "lxml")
        championships = soup.find_all("div", {"class": "matchCard"})
        for championship in championships:
            nameOfChampion = championship.contents[1].contents[1].find("h2").text.strip()
            matchDetails = championship.contents[3].find_all("div", {"class": "liItem"})

            for matchDetail in matchDetails:
                teamA = matchDetail.contents[1].contents[1].find("div", {"class": "teamCntnr"}).contents[1].find("div", {"class": "teamA"}).find("p").text.strip()
                teamB = matchDetail.contents[1].contents[1].find("div", {"class": "teamCntnr"}).contents[1].find("div", {"class": "teamB"}).find("p").text.strip()
                details = matchDetail.contents[1].contents[1].find("div", {"class": "teamCntnr"}).contents[1].find("div", {"class": "MResult"})
                scoreA = details.contents[1].text.strip()
                scoreB = details.contents[5].text.strip()
                time = details.find("span", {"class": "time"}).text.strip()

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
        messagebox.showinfo("Success", "You will find the file in your directory named 'Match.csv'")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Yalla Kora Matches")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Welcome To Yalla Kora Matches", font=("Arial", 16))
        self.label.pack(pady=20)

        self.button_today = tk.Button(root, text="Show Today's Matches", command=self.show_today)
        self.button_today.pack(pady=10)

        self.button_other = tk.Button(root, text="Show Matches on Another Day", command=self.show_other)
        self.button_other.pack(pady=10)

        self.button_exit = tk.Button(root, text="Exit", command=root.quit)
        self.button_exit.pack(pady=10)

    def show_today(self):
        x = datetime.datetime.now()
        day = x.day
        month = x.month
        year = x.year
        date = f"{month}/{day}/{year}"
        matchs = yallaKora(date)
        matchs.show_matches()

    def show_other(self):
        def submit():
            day = entry_day.get()
            month = entry_month.get()
            year = entry_year.get()
            date = f"{month}/{day}/{year}"
            matchs = yallaKora(date)
            matchs.show_matches()
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Enter Date")
        top.geometry("300x200")

        label_day = tk.Label(top, text="Day (1-31):")
        label_day.pack(pady=5)
        entry_day = tk.Entry(top)
        entry_day.pack(pady=5)

        label_month = tk.Label(top, text="Month (1-12):")
        label_month.pack(pady=5)
        entry_month = tk.Entry(top)
        entry_month.pack(pady=5)

        label_year = tk.Label(top, text="Year:")
        label_year.pack(pady=5)
        entry_year = tk.Entry(top)
        entry_year.pack(pady=5)

        button_submit = tk.Button(top, text="Submit", command=submit)
        button_submit.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
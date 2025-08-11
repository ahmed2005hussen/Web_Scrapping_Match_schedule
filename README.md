# YallaKora Web Scraper

A Python program that performs **Web Scraping** on [Yalla Kora](https://www.yallakora.com/) to fetch all football matches for a specific date, and saves them into a **CSV** file containing:
- Championship name
- Team 1
- Team 2
- Match result
- Match start time

---

## 📌 Features
- Display today's matches instantly.
- Choose any specific date to display matches.
- Save results into a `Match.csv` file for easy reading or further processing.
- Dynamic scraping from the Yalla Kora website.

---

## ⚙️ Requirements

Make sure you have the following Python libraries installed:

```bash
pip install requests beautifulsoup4 lxml
```

---

## 📂 Project Structure
```
project/
│
├── main.py          # Main program file
├── yalla_kora.py    # Class responsible for fetching and saving data
└── Match.csv        # Generated file after running the program (created automatically)
```

---

## ▶️ How to Run

1. Open your terminal or command prompt.  
2. Navigate to the project directory.  
3. Run the program:

```bash
python main.py
```

You will see the menu:

```
===================
Welcome To you :)
===================
What do you want: 
-----------------
1- show today's matches
2- show matches in another day
3- Exit 
```

- **Option 1**: Show today's matches and save them to CSV.  
- **Option 2**: Enter a specific date and show matches for that date.  
- **Option 3**: Exit the program.  

---

## 📄 Example Output in `Match.csv`
```csv
Championship,Team 1,Team 2,Start Time,Result
Egyptian League,Al Ahly,Zamalek,20:00,2 | 1
Premier League,Manchester United,Chelsea,18:30,1 | 1
...
```

---

## ⚠️ Notes
- You must be connected to the internet while running the program.  
- If you enter a date with no matches or an invalid date, the program will notify you.  
- If Yalla Kora changes its page structure in the future, the scraping logic may need updates.

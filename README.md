# YallaKora Web Scraper  

A Python program that performs **Web Scraping** on [Yalla Kora](https://www.yallakora.com/) to fetch all football matches for a specific date and saves them into a **CSV** file containing:  
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
├── main.py # Main program file  
├── yalla_kora.py # Class responsible for fetching and saving data  
└── Match.csv # Generated file after running the program (created automatically)  
```  

---  

## 🖥️ Project Versions  

This project went through **three main stages** during development:  

### 1️⃣ Initial Terminal Version (CLI)  
- The very first version, fully running in the terminal.  
- Allowed the user to choose between today's matches or matches for a specific date.  
- Data was fetched and saved to `Match.csv` for further use.  

### 2️⃣ Simple GUI Version  
- A lightweight graphical interface replicating the terminal version’s functionality.  
- Easier to interact with compared to the CLI.  
- Still saves match data into `Match.csv`.  

### 3️⃣ Advanced GUI Version  
- A more polished and user-friendly interface.  
- Added extra features and a better layout.  
- Provides a smoother experience while keeping CSV export functionality.  

> Each version helped me better understand **Web Scraping**, **File Handling**, and how to improve usability over time.  

---  

## ▶️ How to Run  

### 🖥️ 1. Terminal Version (CLI)  
1. Open your terminal or command prompt.  
2. Navigate to the project directory.  
3. Run the program:  
 ```bash  
 python main.py  
```  

You will see the menu:  

  
![Terminal Version Screenshot](https://raw.githubusercontent.com/ahmed2005hussen/Web_Scrapping_Match_schedule/main/Screen%20Shoot/Screenshot%202025-08-11%20190916.png)
  

### 🖱️ 2. Simple GUI Version  
Make sure you have all required libraries installed (`tkinter`, `requests`, `beautifulsoup4`, `lxml`).  

 
A small window will appear with options to:  
- Show today’s matches  
- Pick a specific date  
- Save results to Match.csv  

📸 Screenshot:  
![Simple GUI Screenshot](https://raw.githubusercontent.com/ahmed2005hussen/Web_Scrapping_Match_schedule/main/Screen%20Shoot/Screenshot%202025-08-12%20020301.png)

---  

### 🎨 3. Advanced GUI Version  
Install all required dependencies:  
```bash  
pip install requests beautifulsoup4 lxml tk  
```  
 
You will get a larger, user-friendly window with:  
- Better layout and navigation  
- More match filtering options  
- One-click CSV saving  

📸 Screenshot:  
![Advanced GUI Screenshot](https://raw.githubusercontent.com/ahmed2005hussen/Web_Scrapping_Match_schedule/main/Screen%20Shoot/Screenshot%202025-08-12%20020720.png)

---  
---  

## ⚠️ Notes  
- You must be connected to the internet while running the program.  
- If you enter a date with no matches or an invalid date, the program will notify you.  
- If Yalla Kora changes its page structure in the future, the scraping logic may need updates.

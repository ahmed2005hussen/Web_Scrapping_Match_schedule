import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import datetime
import requests
from bs4 import BeautifulSoup
import csv
import threading
import pandas as pd

class YallaKoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("يلا كورة - مواعيد المباريات")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        self.font_arabic = ('Arial', 12)
        
        self.setup_ui()
        
    def setup_ui(self):
        title_label = tk.Label(self.root, text="يلا كورة - مواعيد المباريات", 
                              font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=20)
        
        date_frame = tk.Frame(self.root, bg='#f0f0f0')
        date_frame.pack(pady=10)
        
        today_btn = tk.Button(date_frame, text="مباريات اليوم", 
                             command=self.get_today_matches,
                             font=self.font_arabic, bg='#3498db', fg='white',
                             padx=20, pady=10, cursor='hand2')
        today_btn.grid(row=0, column=0, padx=10, pady=5)
        
        custom_date_btn = tk.Button(date_frame, text="اختيار تاريخ آخر", 
                                   command=self.show_date_picker,
                                   font=self.font_arabic, bg='#27ae60', fg='white',
                                   padx=20, pady=10, cursor='hand2')
        custom_date_btn.grid(row=0, column=1, padx=10, pady=5)
        
        self.date_picker_frame = tk.Frame(self.root, bg='#f0f0f0')
        
        tk.Label(self.date_picker_frame, text="اليوم:", font=self.font_arabic, bg='#f0f0f0').grid(row=0, column=0, padx=5)
        self.day_var = tk.StringVar(value=str(datetime.datetime.now().day))
        day_spinbox = tk.Spinbox(self.date_picker_frame, from_=1, to=31, textvariable=self.day_var, width=5)
        day_spinbox.grid(row=0, column=1, padx=5)
        
        tk.Label(self.date_picker_frame, text="الشهر:", font=self.font_arabic, bg='#f0f0f0').grid(row=0, column=2, padx=5)
        self.month_var = tk.StringVar(value=str(datetime.datetime.now().month))
        month_spinbox = tk.Spinbox(self.date_picker_frame, from_=1, to=12, textvariable=self.month_var, width=5)
        month_spinbox.grid(row=0, column=3, padx=5)
        
        tk.Label(self.date_picker_frame, text="السنة:", font=self.font_arabic, bg='#f0f0f0').grid(row=0, column=4, padx=5)
        self.year_var = tk.StringVar(value=str(datetime.datetime.now().year))
        year_spinbox = tk.Spinbox(self.date_picker_frame, from_=2020, to=2030, textvariable=self.year_var, width=8)
        year_spinbox.grid(row=0, column=5, padx=5)
        
        get_matches_btn = tk.Button(self.date_picker_frame, text="جلب المباريات", 
                                   command=self.get_custom_date_matches,
                                   font=self.font_arabic, bg='#e74c3c', fg='white',
                                   padx=15, pady=5, cursor='hand2')
        get_matches_btn.grid(row=0, column=6, padx=10)
        
        self.progress = ttk.Progressbar(self.root, mode='indeterminate')
        
        self.status_label = tk.Label(self.root, text=" اختر التاريخ لعرض المباريات", 
                                    font=self.font_arabic, bg='#f0f0f0', fg='#7f8c8d')
        self.status_label.pack(pady=5)
        
        self.setup_table()
        
        self.setup_action_buttons()
        
    def setup_table(self):
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        columns = ('البطولة', 'الفريق الأول', 'الفريق الثاني', 'وقت البداية', 'النتيجة')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor='center')
        
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def setup_action_buttons(self):
        action_frame = tk.Frame(self.root, bg='#f0f0f0')
        action_frame.pack(pady=10)
        
        save_btn = tk.Button(action_frame, text="حفظ كـ CSV", 
                            command=self.save_to_csv,
                            font=self.font_arabic, bg='#9b59b6', fg='white',
                            padx=20, pady=8, cursor='hand2')
        save_btn.grid(row=0, column=0, padx=10)
        
        refresh_btn = tk.Button(action_frame, text="تحديث", 
                               command=self.refresh_data,
                               font=self.font_arabic, bg='#f39c12', fg='white',
                               padx=20, pady=8, cursor='hand2')
        refresh_btn.grid(row=0, column=1, padx=10)
        
        clear_btn = tk.Button(action_frame, text="مسح الجدول", 
                             command=self.clear_table,
                             font=self.font_arabic, bg='#95a5a6', fg='white',
                             padx=20, pady=8, cursor='hand2')
        clear_btn.grid(row=0, column=2, padx=10)
        
    def show_date_picker(self):
        if not hasattr(self, '_date_picker_visible') or not self._date_picker_visible:
            self.date_picker_frame.pack(pady=10)
            self._date_picker_visible = True
        else:
            self.date_picker_frame.pack_forget()
            self._date_picker_visible = False
            
    def get_today_matches(self):
        today = datetime.datetime.now()
        date_str = f"{today.month}/{today.day}/{today.year}"
        self.fetch_matches(date_str)
        
    def get_custom_date_matches(self):
        try:
            day = int(self.day_var.get())
            month = int(self.month_var.get())
            year = int(self.year_var.get())
            date_str = f"{month}/{day}/{year}"
            self.fetch_matches(date_str)
        except ValueError:
            messagebox.showerror("خطأ", "تأكد من صحة التاريخ المدخل")
            
    def fetch_matches(self, date_str):
        self.progress.pack(pady=5)
        self.progress.start()
        self.status_label.config(text="جاري تحميل المباريات...")
        
        thread = threading.Thread(target=self._fetch_matches_thread, args=(date_str,))
        thread.start()
        
    def _fetch_matches_thread(self, date_str):
        try:
            matches_data = self.scrape_matches(date_str)
            self.root.after(0, self._update_table, matches_data)
        except Exception as e:
            self.root.after(0, self._show_error, str(e))
            
    def scrape_matches(self, date):
        url = f"https://www.yallakora.com/match-center?date={date}"
        response = requests.get(url)
        
        if response.status_code != 200:
            raise Exception(f"لا يمكن الوصول للموقع. كود الخطأ: {response.status_code}")
            
        soup = BeautifulSoup(response.content, "lxml")
        championships = soup.find_all("div", {"class": "matchCard"})
        
        if not championships:
            raise Exception("لا توجد مباريات في هذا التاريخ")
        
        matches_data = []
        
        for championship in championships:
            try:
                championship_name = championship.contents[1].contents[1].find("h2").text.strip()
                match_details = championship.contents[3].find_all("div", {"class": "liItem"})
                
                for match_detail in match_details:
                    team_container = match_detail.contents[1].contents[1].find("div", {"class": "teamCntnr"}).contents[1]
                    
                    team_a = team_container.find("div", {"class": "teamA"}).find("p").text.strip()
                    team_b = team_container.find("div", {"class": "teamB"}).find("p").text.strip()
                    
                    result_div = team_container.find("div", {"class": "MResult"})
                    score_a = result_div.contents[1].text.strip()
                    score_b = result_div.contents[5].text.strip()
                    time = result_div.find("span", {"class": "time"}).text.strip()
                    
                    matches_data.append({
                        'championship': championship_name,
                        'team1': team_a,
                        'team2': team_b,
                        'time': time,
                        'result': f"{score_a} | {score_b}"
                    })
                    
            except Exception as e:
                continue  
                
        return matches_data
    
    def _update_table(self, matches_data):
        self.progress.stop()
        self.progress.pack_forget()
        
        self.clear_table()
        self.current_matches = matches_data
        
        for match in matches_data:
            self.tree.insert('', tk.END, values=(
                match['championship'],
                match['team1'], 
                match['team2'],
                match['time'],
                match['result']
            ))
            
        self.status_label.config(text=f"تم تحميل {len(matches_data)} مباراة بنجاح")
        
    def _show_error(self, error_msg):
        self.progress.stop()
        self.progress.pack_forget()
        self.status_label.config(text="حدث خطأ أثناء تحميل المباريات")
        messagebox.showerror("خطأ", error_msg)
        
    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
    def refresh_data(self):
        if hasattr(self, 'current_matches'):
            self.get_today_matches()
        else:
            messagebox.showinfo("معلومات", "قم بجلب المباريات أولاً")
            
    def save_to_csv(self):
        if not hasattr(self, 'current_matches') or not self.current_matches:
            messagebox.showwarning("تحذير", "لا توجد بيانات للحفظ")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="حفظ الملف"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
                    writer = csv.writer(file)
                    writer.writerow(['البطولة', 'الفريق الأول', 'الفريق الثاني', 'وقت البداية', 'النتيجة'])
                    
                    for match in self.current_matches:
                        writer.writerow([
                            match['championship'],
                            match['team1'],
                            match['team2'], 
                            match['time'],
                            match['result']
                        ])
                        
                messagebox.showinfo("نجح", f"تم حفظ الملف في:\n{file_path}")
                self.status_label.config(text="تم حفظ الملف بنجاح")
                
            except Exception as e:
                messagebox.showerror("خطأ", f"فشل في حفظ الملف:\n{str(e)}")

def main():
    root = tk.Tk()
    app = YallaKoraGUI(root)
    
    root.resizable(True, True)
    root.minsize(800, 600)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        root.quit()

if __name__ == "__main__":
    main()

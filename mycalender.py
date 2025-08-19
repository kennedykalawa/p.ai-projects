import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personalized Calendar App")
        
        self.current_date = datetime.now()
        self.notes = {}
        
        self.create_widgets()
        self.display_calendar()

    def create_widgets(self):
        # Calendar navigation
        nav_frame = ttk.Frame(self.root)
        nav_frame.pack(pady=5)

        prev_btn = ttk.Button(nav_frame, text="<< Prev", command=self.prev_month)
        prev_btn.grid(row=0, column=0, padx=5)

        self.title_label = ttk.Label(nav_frame, text="", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=1, padx=10)

        next_btn = ttk.Button(nav_frame, text="Next >>", command=self.next_month)
        next_btn.grid(row=0, column=2, padx=5)

        # Calendar frame
        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack(pady=10)

        # Notes box
        self.note_text = tk.Text(self.root, height=5, width=40)
        self.note_text.pack(pady=10)

        # Save button
        self.save_button = ttk.Button(self.root, text="Save Note", command=self.save_note)
        self.save_button.pack()

        # Theme button
        self.theme_button = ttk.Button(self.root, text="Change Theme", command=self.change_theme)
        self.theme_button.pack()

    def display_calendar(self):
        # Clear old calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # Month title
        self.title_label.config(text=self.current_date.strftime("%B %Y"))

        # Weekday headers
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(weekdays):
            label = ttk.Label(self.calendar_frame, text=day, padding=5)
            label.grid(row=0, column=i)

        # First day and number of days in month
        first_day = self.current_date.replace(day=1)
        first_weekday = first_day.weekday()
        days_in_month = calendar.monthrange(self.current_date.year, self.current_date.month)[1]

        # Fill in days
        day = 1
        for row in range(1, 7):
            for col in range(7):
                if row == 1 and col < first_weekday:
                    continue
                if day > days_in_month:
                    break
                btn = ttk.Button(self.calendar_frame, text=str(day), command=lambda d=day: self.select_date(d))
                btn.grid(row=row, column=col, padx=2, pady=2)
                day += 1

    def select_date(self, day):
        self.selected_date = self.current_date.replace(day=day)
        note = self.notes.get(self.selected_date.strftime("%Y-%m-%d"), "")
        self.note_text.delete(1.0, tk.END)
        self.note_text.insert(tk.END, note)

    def save_note(self):
        if hasattr(self, 'selected_date'):
            self.notes[self.selected_date.strftime("%Y-%m-%d")] = self.note_text.get(1.0, tk.END).strip()
            messagebox.showinfo("Saved", "Note saved successfully!")

    def change_theme(self):
        current_bg = self.root.cget("bg")
        new_bg = "lightgreen" if current_bg != "lightgreen" else "white"
        self.root.configure(bg=new_bg)
        self.calendar_frame.configure(style="Custom.TFrame")
        style = ttk.Style()
        style.configure("Custom.TFrame", background=new_bg)

    def prev_month(self):
        month = self.current_date.month - 1
        year = self.current_date.year
        if month == 0:
            month = 12
            year -= 1
        self.current_date = self.current_date.replace(year=year, month=month)
        self.display_calendar()

    def next_month(self):
        month = self.current_date.month + 1
        year = self.current_date.year
        if month == 13:
            month = 1
            year += 1
        self.current_date = self.current_date.replace(year=year, month=month)
        self.display_calendar()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()

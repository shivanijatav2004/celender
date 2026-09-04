import calendar
yy = 2025 #year
mm = 12 # month
print(calendar.month(yy, mm))


import tkinter as tk
import calendar

root = tk.Tk()
root.title("Calendar")

year = 2025
month = 12

cal = calendar.month(year, month)

label = tk.Label(root, text=cal, font=("Consolas", 12), bg="white")
label.pack(padx=20, pady=20)

root.mainloop()


import calendar

year = 2025
month = 12

print("="*28)
print(f"{calendar.month_name[month]} {year}".center(28))
print("="*28)
print(calendar.month(year, month))


import calendar

year = 2025
month = 12

print("\033[1;36m" + "="*30)
print(f"{calendar.month_name[month]} {year}".center(30))
print("="*30 + "\033[0m")

print("\033[1;33m" + calendar.month(year, month) + "\033[0m")


import calendar

year = 2026

print("="*40)
print(f"CALENDAR {year}".center(40))
print("="*40)

print(calendar.calendar(year))

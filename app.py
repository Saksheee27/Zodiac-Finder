import tkinter as tk
from datetime import datetime

# Function to find zodiac sign
def find_zodiac():
    try:
        dob = entry.get()
        date = datetime.strptime(dob, "%d-%m-%Y")
        day, month = date.day, date.month

        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            zodiac = "Aries (मेष)"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            zodiac = "Taurus (वृषभ)"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            zodiac = "Gemini (मिथुन)"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            zodiac = "Cancer (कर्क)"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            zodiac = "Leo (सिंह)"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            zodiac = "Virgo (कन्या)"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            zodiac = "Libra (तुला)"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            zodiac = "Scorpio (वृश्चिक)"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            zodiac = "Sagittarius (धनु)"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            zodiac = "Capricorn (मकर)"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            zodiac = "Aquarius (कुंभ)"
        else:
            zodiac = "Pisces (मीन)"

        # Show result on same window
        result_label.config(text=f"Your Zodiac Sign is: {zodiac}", fg="green")

    except ValueError:
        result_label.config(text="❌ Please enter DOB in dd-mm-yyyy format", fg="red")


# ---------------- GUI ----------------
root = tk.Tk()
root.title("What's Your Rashi")
root.geometry("600x600")
root.config(bg="#FFB6C1")

# Heading
header = tk.Label(root, text="✨ WHAT'S YOUR RASHI ✨ - Zodiac Finder", 
                  font=("Helvetica", 22, "bold"), 
                  bg="#E9967A", fg="khaki", pady=10)
header.pack(fill="x")


# Frame for input
frame = tk.Frame(root, bg="#F5DEB3", bd=2, relief="groove")
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Input label
lbl = tk.Label(frame, text="Enter DOB (dd-mm-yyyy)", font=("Arial", 16, "bold"), bg="#DB7093")
lbl.pack(pady=30)

# Entry box
entry = tk.Entry(frame, font=("Arial", 16), width=20, justify="center", bd=2, relief="solid")
entry.pack(pady=5)
entry.insert(0, "")

# Button
btn = tk.Button(frame, text="Find Rashi / Zodiac", font=("Arial", 16, "bold"), 
                bg="#0A2C53", fg="white", activebackground="#DB7093", 
                relief="raised", padx=10, pady=5, command=find_zodiac)
btn.pack(pady=15)

# Result label (output shown here)
result_label = tk.Label(frame, text="", font=("Arial", 16, "bold"), bg="#A0CAFA")
result_label.pack(pady=10)


root.mainloop()

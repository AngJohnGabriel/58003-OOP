import tkinter as tk

def convert():

    length_cm = float(entry_cm.get())

    length_m = length_cm / 100
    entry_m.delete(0, tk.END)
    entry_m.insert(0, str(length_m))

    length_km = length_cm / 100000
    entry_km.delete(0, tk.END)
    entry_km.insert(0, str(length_km))

window = tk.Tk()
window.title("Midterm Exam Problem 2")

label_cm = tk.Label(window, text="Metric Units of Length")
label_cm.grid(row=50, column=150)

label_cm = tk.Label(window, text="Centimeters:")
label_cm.grid(row=100, column=100)
entry_cm = tk.Entry(window)
entry_cm.grid(row=100, column=150)

label_m = tk.Label(window, text="Meters:")
label_m.grid(row=150, column=100)
entry_m = tk.Entry(window)
entry_m.grid(row=150, column=150)

label_km = tk.Label(window, text="Kilometers:")
label_km.grid(row=200, column=100)
entry_km = tk.Entry(window)
entry_km.grid(row=200, column=150)

button_convert = tk.Button(window, text="Convert", command=convert)
button_convert.grid(row=300, column=125, columnspan=2)

window.mainloop()
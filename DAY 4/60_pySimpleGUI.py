import tkinter as tk

def tombol_diklik():
     print("Tombol diklik")
window = tk.Tk()
window.title("contoh program TKinter")

btn = tk.Button(window, text="klik sya", command= tombol_diklik)
btn.pack(padx=20, pady=20)

window.mainloop()
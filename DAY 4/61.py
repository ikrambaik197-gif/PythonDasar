import tkinter as tk

def show_text():
    # Ambil teks dari input
    teks = entry.get()
    # Tampilkan ke label output
    output_label.config(text=teks)

def exit_app():
    window.destroy()

# Membuat window
window = tk.Tk()
window.title("Pattern 2B")

# Baris 1: Label judul + output
label_info = tk.Label(window, text="Your typed chars appear here:")
label_info.grid(row=0, column=0, padx=5, pady=5)

output_label = tk.Label(window, text="", width=15, anchor="w", relief="sunken")
output_label.grid(row=0, column=1, padx=5, pady=5)

# Baris 2: Input
entry = tk.Entry(window)
entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Baris 3: Tombol
btn_show = tk.Button(window, text="Show", command=show_text)
btn_show.grid(row=2, column=0, padx=5, pady=5)

btn_exit = tk.Button(window, text="Exit", command=exit_app)
btn_exit.grid(row=2, column=1, padx=5, pady=5)

# Supaya kolom bisa melebar
window.columnconfigure(1, weight=1)

# Menjalankan aplikasi
window.mainloop()
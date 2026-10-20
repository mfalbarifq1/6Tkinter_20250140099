import tkinter as tk

BG = "#10142e"      # warna latar gelap
FG = "white"


def hasil_prediksi():
    # Buka jendela kecil baru (Toplevel) berisi label hasil prediksi
    # Apapun nilai yang diinput, hasilnya selalu Teknologi Informasi
    win = tk.Toplevel(root)
    win.title("Hasil Prediksi")
    win.geometry("300x100")
    win.configure(bg=BG)
    label_hasil = tk.Label(win, text="Prediksi Prodi: Teknologi Informasi",
                           font=("Arial", 12, "bold"), bg=BG, fg="#00d4ff")
    label_hasil.pack(expand=True)


# Jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("420x720")
root.configure(bg=BG)

# 1 label judul
tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan",
         font=("Arial", 16, "bold"), bg=BG, fg=FG).pack(pady=20)

# 10 input nilai (label + entry sejajar memakai grid di dalam Frame)
frame = tk.Frame(root, bg=BG)
frame.pack(pady=5)

entries = []
for i in range(10):
    tk.Label(frame, text=f"Nilai Mata Pelajaran {i + 1}:",
             bg=BG, fg=FG, anchor="e", width=22).grid(row=i, column=0, padx=5, pady=5)
    e = tk.Entry(frame, width=10, justify="center")
    e.grid(row=i, column=1, padx=5, pady=5)
    entries.append(e)

# Input pilihan jurusan (dropdown)
tk.Label(root, text="Pilihan Jurusan Anda:", bg=BG, fg=FG).pack(pady=(15, 2))
var_jurusan = tk.StringVar(value="Teknologi Informasi")
opsi = tk.OptionMenu(root, var_jurusan, "Teknologi Informasi", "Sistem Informasi",
                     "Teknik Informatika", "Teknik Elektro", "Manajemen")
opsi.config(bg=BG, fg=FG, activebackground=BG, activeforeground=FG,
            highlightthickness=0)
opsi.pack()

# 1 button
tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi,
          font=("Arial", 11, "bold"), padx=10, pady=4).pack(pady=20)

root.mainloop()
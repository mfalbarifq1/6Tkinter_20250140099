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

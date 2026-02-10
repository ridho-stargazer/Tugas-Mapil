import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Membuat aplikasi awal")
root.geometry("300x250")
root.configure(bg="skyblue")

# Membuat label dengan teks berbeda
label1 = tk.Label(root, text="Ridho", font=("Arial", 14))
label1.pack(pady=5)

label2 = tk.Label(root, text="Owen", font=("Arial", 14))
label2.pack(pady=5)

label3 = tk.Label(root, text="Ilham", font=("Arial", 14))
label3.pack(pady=5)

label4 = tk.Label(root, text="Noval", font=("Arial", 14))
label4.pack(pady=5)

# Fungsi untuk mengubah teks masing-masing label
def tampil_pesan():
    label1.config(text="Cantika ")
    label2.config(text="Naura")
    label3.config(text="Aulia")
    label4.config(text="Anggun")

# Membuat tombol
tombol = tk.Button(root, text="Klik Aku", command=tampil_pesan)
tombol.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import filedialog
import time
import os
import subprocess
import threading
import sys
selected_files = []

def browse_files():
    file_paths = filedialog.askopenfilenames()
    global selected_files
    selected_files = list(file_paths)
    print("Seçili dosyalar:", selected_files)
    create_interval_entries()

def create_interval_entries():
    interval_frame.pack_forget()
    global interval_entries
    interval_entries = []
    interval_frame.pack(fill="both", expand="yes", padx=20, pady=10)
    for file_path in selected_files:
        file_name = os.path.basename(file_path)
        label = tk.Label(interval_frame, text=file_name, font=("Arial", 12))
        label.pack(padx=10, pady=5)
        entry = tk.Entry(interval_frame, font=("Arial", 12))
        entry.pack(padx=10, pady=5)
        interval_entries.append(entry)

def start_scheduling():
    intervals = []
    for entry in interval_entries:
        interval = int(entry.get())
        intervals.append(interval)
    print(f"Saatte {intervals} saniyede bir çalışacak.")
    def run_periodically(intervals):
        threads = []
        for i, file_path in enumerate(selected_files):
            interval = intervals[i]
            file_name = os.path.basename(file_path)
            print(f"{file_path} dosyası çalıştırılıyor...")
            with open('app_logs.txt','a') as log_file:
                log_file.write(f"{file_name}      {interval}\n")
            thread = threading.Thread(target=run_script, args=(file_path, interval))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        print("Tüm dosyalar çalıştırıldı.")
    threading.Thread(target=run_periodically, args=(intervals,)).start()

def save_host():
    with open("../../host.txt", "w") as f:
        f.write(host_entry.get() + "\n")
        print("Host kaydedildi:", host_entry.get())

def run_script(file_path, interval):
    while True:
        subprocess.run([file_path])
        time.sleep(interval)

root = tk.Tk()
root.geometry("400x600")
root.title("Python Script Scheduler")
if hasattr(sys, '_MEIPASS'):
    logo_path = os.path.join(sys._MEIPASS, 'indirico.png')
else:
    logo_path = 'indirico.png'

icon_image = tk.PhotoImage(file=logo_path)
root.iconphoto(False, icon_image)

# Dosya seçme LabelFrame
file_frame = tk.LabelFrame(root, text="Python dosyalarını seçin")
file_frame.pack(fill="both", expand="yes", padx=20, pady=10)
file_button = tk.Button(file_frame, text="Göz At", command=browse_files)
file_button.pack(padx=10, pady=10)

# Saat aralığı LabelFrame
interval_frame = tk.LabelFrame(root, text="Her dosya için saat aralığını belirleyin (saniye cinsinden)")
interval_frame.pack(fill="both", expand="yes", padx=20, pady=10)
# Host giris LabelFrame
host_frame = tk.LabelFrame(root, text="MySQL Host Adresi Girin")
host_frame.pack(fill="both", expand="yes", padx=20, pady=10)
host_entry = tk.Entry(host_frame, font=("Arial", 14))
host_entry.pack(padx=10, pady=10)

# Başlat butonu
start_button = tk.Button(root, text="Başlat", command=start_scheduling, bg="#4CAF50", fg="white", font=("Arial", 16), padx=10, pady=10)
start_button.pack(pady=10)

# Host Kaydet butonu
save_button = tk.Button(root, text="Host Kaydet", command=save_host, bg="#008CBA", fg="white", font=("Arial", 16), padx=10, pady=10)
save_button.pack(pady=10)

# Program hakkında bilgi etiketi
info_label = tk.Label(root, text="Python Script Scheduler", font=("Arial", 14), fg="#777")
info_label.pack(side="bottom", pady=10)

# Yapımcı etiketi
creator_label = tk.Label(root, text="Made by Lightfield", font=("Arial", 12), fg="#777")
creator_label.pack(side="bottom", pady=5)

root.mainloop()

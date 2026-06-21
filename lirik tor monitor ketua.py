import time

def tampilkan_lirik_tor_monitor_ketua():
    """
    Menampilkan lirik lagu "Tor Monitor Ketua" di konsol dengan jeda.
    """
    lirik = [
        "Tor Monitor Ketua,",
        "Anggota mau lapor ketua.",
        "Kondisi lagi gacor ketua,",
        "", # Baris kosong untuk jeda antar bait
        "Yang ini baru bilang maitua,",
        "My trip mantan hancur.",
        "Stop suda jangan ko atur,",
        "Ko bukan lagi donatur.",
        "",
        "Skakmat selesai main catur,",
        "Lupa nama tapi masih ingat rasa.",
        "Rasa yang dulu pernah ada,",
        "Waktu tong sama-sama.",
        "",
        "Lupa wajah tapi ingat rasa,",
        "Sayang cinta lama so anyor.",
        "tamba so ancor,",
        "leba so ancor.",
        "yang baru labe gacor,",
        "yang lalu biarlah yang berlalu.",
        "Kita cari orang baru,",
        ".",
        "",
        "adoh e cinta lama so ba bu.",
        "Buat apa kita pusing,",
        "Orang lama kita rating.",
        "Goyang Mending.",
        "Yang penting jangan salting,",

    ]

    print("--- Lirik Lagu: Tor Monitor Ketua ---")
    print("-" * 35)

    for baris in lirik:
        print(baris)
        time.sleep(1)  # Jeda 2 detik per baris

    print("-" * 35)
    print("Selesai.")

if __name__ == "__main__":
    tampilkan_lirik_tor_monitor_ketua()
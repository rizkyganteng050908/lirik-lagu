import time

def tampilkan_lirik_tor_monitor_ketua():
    """
    Menampilkan lirik lagu "Tor Monitor Ketua" di konsol dengan jeda.
    """
    lirik = [
        "Aku yang dulu bukanlah yang sekarang,",
        "Dulu ditendang sekarangku disayang.",
        "Dulu dulu dulu ku menderita,",
        "Sekarang aku bahagia.",
        "", # Baris kosong untuk jeda antar bait
        "Cita-citaku menjadi orang kaya,",
        "Dulu ku susah sekarang alhamdulillah.",
        "Bersyukurlah pada yang mahakuasa,",
        "Memberi jalan untukku semua.",
        "",
        "Hidupku dulunya seorang pengamen,",
        "Pulang malam selalu bawa uang recehan.",
        "Mengejar cita-cita paling mulia,",
        "Membantu keluarga di rumah.",
        "",
        "Sekolah dulu kunggak punya biaya,",
        "Terpaksa ku harus mencari nafkah.",
        "Tetapi aku tak berputus asa,",
        "Pasti yang kuasa memberi jalannya.",
        "",
        "Hidupku dulunya seorang pengamen.",
        "Pulang malam selalu bawa uang recehan",
        "Mengejar cita-cita paling mulia",
        "Bersyukur masuk dapur rekaman.",
        "",
        "Hidupku dulunya seorang pengamen.",
        "Pulang malam selalu bawa uang recehan.",
        "Mengejar cita-cita paling mulia,",

    ]

    print("--- Lirik Lagu: Tor Monitor Ketua ---")
    print("-" * 35)

    for baris in lirik:
        print(baris)
        time.sleep(3)  # Jeda 2 detik per baris

    print("-" * 35)
    print("Selesai.")

if __name__ == "__main__":
    tampilkan_lirik_tor_monitor_ketua()
team_gilak = {}
team_random = {}

# Method non-return type
def bagan_tim():
    print("\n===== Struktur Tim ===== ")
    print("1. Menambah Jumlah Tim Gilak")
    print("2. Menambah Jumlah Tim Random")
    print("3. Tampilkan Tim Gilak")
    print("4. Tampilkan Tim Random")
    print("5. Pindahkan Player Tim Gilak ke Tim Random")
    print("6. Pindahkan Player Tim Random ke Tim Gilak")
    print("7. Tampilkan Statistik Keseluruhan Tim Gilak")
    print("8. Tampilkan Statistik Keseluruhan Tim Random")
    print("9. Keluar")

# Fungsi dengan return type dan parameter
def masukan_namadanrole(team, name, role, statistik):
    team[name] = {'role': role, 'statistik': statistik}
    return f"Player '{name}' mengisi role '{role}' dengan statistik '{statistik}' telah ditambahkan ke {team_name(team)}."

# Fungsi dengan non return type dan parameter
def tampilkan_(team):
    if not team:
        print("Player tidak tersedia di tim ini.")
    else:
        print(f"===== Daftar Pemain di Tim {team_name(team)} =====")
        for name, details in team.items():
            print(f"{name}: {details['role']}: {details['statistik']}")

# Fungsi return type dengan parameter untuk memindahkan player          
def pindah_pemain(pindah_team, lokasi_team, name):
    if name in pindah_team:
        details = pindah_team.pop(name)  # Menghapus pemain dari tim
        lokasi_team[name] = details  # Memindahkan pemain ke tim
        return f"Pemain '{name}' telah dipindahkan ke {team_name(lokasi_team)}."
    else:
        return f"Pemain '{name}' tidak ditemukan di {team_name(pindah_team)}."

# Fungsi untuk menghitung rata-rata statistik
def perhitungan_average(team):
    if not team:
        return 0
    total = sum(details['statistik'] for details in team.values())
    average = total / len(team)
    return average

# Fungsi untuk menampilkan rata-rata nilai di tim
def show_average(team):
    average = perhitungan_average(team)
    print(f"Rata-rata statistik di {team_name(team)}: {average:.2f}")        

# Fungsi untuk mendapatkan nama tim berdasarkan bagan
def team_name(team):
    return "Tim Gilak" if team is team_gilak else "Tim Random" 

from data import DataLoader

loader = DataLoader()
band = loader.load_band()

honor = 45000000

sum_ranking = sum(anggotaband.ranking for anggotaband in band)

for anggotaband in band:
    share = anggotaband.ranking / sum_ranking * honor
    print(f"Nama: {anggotaband.nama}, Posisi: {anggotaband.posisi}, Honor: Rp {share}")
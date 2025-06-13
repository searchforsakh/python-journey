import datetime as dt

# print("masukkan tanggal, bulan, tahun lahir anda")
tanggal = int(input("masukkan tanggal \t\t= "))
bulan = int(input("masukkan bulan \t\t\t= "))
tahun = int(input("masukkan tahun \t\t\t= "))

data_lahir = dt.date(tahun, bulan, tanggal)
# print(f"""tanggal lahir anda adalah \t= {data_lahir}
# hari lahir anda adalah \t\t= {data_lahir:%A}
# bulan lahir anda adalah \t= {data_lahir:%B}
# pada hari ke \t\t\t= {data_lahir:%j} pada tahun {tahun}
# """)

# # menghitung umur hari ini
hari_ini = dt.date.today()
umur_hari_ini = hari_ini - data_lahir
print(umur_hari_ini)
umur_tahun = umur_hari_ini.days // 365
umur_bulan = (umur_hari_ini.days % 365) // 30
umur_hari = umur_hari_ini.days % 30
print(f'{umur_tahun} tahun, {umur_bulan} bulan, {umur_hari} hari.')
# tahun_sekarang = umur_hari_ini.days // 365
# bulan_sekarang = (umur_hari_ini.days % 365) // 30
# hari_sekarang = 
# print(f'umur sekarang = {tahun_sekarang} tahun, {bulan_sekarang} bulan, ')



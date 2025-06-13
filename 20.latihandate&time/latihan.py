""" date object
class datetime.date(year, month, day)
MINYEAR <= year <= MAXYEAR
1 <= month <= 12
1 <= day <= number of days in the given month and year
"""
""" datetime object
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
MINYEAR <= year <= MAXYEAR,
1 <= month <= 12,
1 <= day <= number of days in the given month and year,
0 <= hour < 24,
0 <= minute < 60,
0 <= second < 60,
0 <= microsecond < 1000000,
fold in [0, 1].
"""
""" time object
class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
0 <= hour < 24,
0 <= minute < 60,
0 <= second < 60,
0 <= microsecond < 1000000,
fold in [0, 1].
"""

# import datetime as dtm
# hari_ini = dtm.datetime(2006,11,30, hour=21, minute = 1)
# print(f"\n{hari_ini}")
# print(f"""hari ini adalah  = {hari_ini:%A, %B, %Y}
# Pukul            = {hari_ini:%X}
# Hari ke          = {hari_ini:%j}""")

import datetime as dt
print("\nMasukkan Tanggal, Bulan, dan Tahun Lahir anda")

tanggal = int(input("Masukkan Tanggal\t  = "))
bulan = int(input("Masukkan Bulan\t\t  = "))
tahun = int(input("Masukkan Tahun\t\t  = "))

data_lahir = dt.date(tahun, bulan, tanggal)
print(f"""tanggal lahir anda adalah = {data_lahir}
Hari lahir anda adalah    = {data_lahir:%A}
Hari ke                   = {data_lahir:%j} pada {tahun}""")

hari_ini = dt.date.today()
umur_hari = hari_ini - data_lahir
print(umur_hari.days)
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
umur_hari_sekarang = umur_hari.days % 30
print(f"Umur anda sekarang        = {umur_tahun} tahun, {umur_bulan} bulan, {umur_hari_sekarang} hari")



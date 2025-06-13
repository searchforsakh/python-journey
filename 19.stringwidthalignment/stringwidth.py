# width and multiline
# data

data_nama = "sakha pratama"
data_umur = 17 
data_tinggi = 190.9
data_nomorsepatu = 43

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomorsepatu}"
print("\n" + 5*"=" + "DATA STRING" + "="*5)
print(data_string)

# string multiline, dengan menggunakan enter atau multiline (\n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomorsepatu}"
print("\n" + 5*"=" + "DATA STRING" + "="*5)
print(data_string)

# string multiline dengan kutip tiga
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
nomor sepatu = {data_nomorsepatu}"""
print("\n" + 5*"=" + "DATA STRING" + "="*5)
print(data_string)

# mengatur lebar
data_string = f"""nama         = {data_nama:>18}
umur         = {data_umur:>18}
tinggi       = {data_tinggi:>18}
nomor sepatu = {data_nomorsepatu:>18}
"""
print("\n" + 5*"=" + "DATA STRING" + "="*5)
print(data_string)

# %A digunakan untuk mengetahui nama hari pada tanggal tersebut 
# %B digunakan untuk nama bulan
# %y digunakan untuk nama tahun





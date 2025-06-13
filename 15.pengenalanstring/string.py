data = "Ini adalah String"
print(data)
print(type(data))
print()
## 1.Cara membuat string 
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print("'Halo, Apa Kabar ?'")
print('"Halo, Apa Kabar ?"')

## 2. menggunakan tanda \ (Konveni String)

# membuat tanda ' menjadi string 
print('ini adalah hari jum\'at')

# membuat tanda \ menjadi string
print('C:\\User\\sakha')

## membuat tab (\t)
print("Sakha\taulia")

## membuat backspace (\b)
print("Sakha \bAulia")

## membuat enter/newline (\n)
print('ini baris pertama\nini baris kedua') # LF = Line Feed = unix, macos, linux
print('ini baris pertama\rini baris kedua') # CR = Carriage Return = commodore, acorn, lisp
print('ini baris pertama\r\nini baris kedua') # Carriage Return Line Feed = Digunakan oleh windows

# 3. String Literal atau Raw

# Hati hati
print("C:\new folder")
## Gunakan Raw String r'...' = menghilangkan semua bentuk konvensi string
print(r'C:\New folder')

## multiline literal string
print("""
Nama : Sakha
Kelas : Mahasiswa
""")

## multiline literal string dan raw
print(r"""
    Nama : Sakha
    Kelas : Mahasiswa\new
""")


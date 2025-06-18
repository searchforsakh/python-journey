buahbuahan = {
    'apl' : 'apel',
    'bnn' : 'banana',
    'jrk' : 'jeruk'
}
print(buahbuahan)
for buah in buahbuahan: # hanya mengambil key nya saja
    print(buah)


# operator untuk mengambil item/iterables
# keys() >> untuk mengambil item key
x = buahbuahan.keys()
print(x)
for i in buahbuahan.keys():
    print(f"key = {i}")

# values() >> untuk mengambil item value
x = buahbuahan.values()
print(x)
for i in buahbuahan.values():
    print(f"values = {i}")

# items() >> untuk mengambil key dan value sekaligus dalam bentuk tuples
x = buahbuahan.items()
print(x)
for i in buahbuahan.items():
    print(i)
for a,b in buahbuahan.items(): # dapat mr 
    print(f"{a} : {b}")
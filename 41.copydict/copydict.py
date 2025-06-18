buahbuahan = {
    'apl' : 'apel',
    'psg' : 'pisang',
    'jrk' : 'jeruk',
    'smk' : 'semangka'
}

fruits = buahbuahan.copy()
print(f'friends = {fruits}')
print(hex(id(fruits)))
print(f'buahbuahan = {buahbuahan}')
print(hex(id(buahbuahan)))

fruits['smk'] = 'semongko' #mengganti value dari key 'smk'
fruits['srk'] = 'sirsak' #menambahkan value dan nilai baru
fruits.update({'mgs' : 'manggis'}) #menambahkan value dan nilai baru menggunakan .update({})
print(fruits)
print(hex(id(fruits)))
print(buahbuahan)
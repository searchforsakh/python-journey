buahbuahan = {
    'apl' : 'apel',
    'psg' : 'pisang',
    'jrk' : 'jeruk',
    'smk' : 'semangka'
}

hewanhewan = {
    'myt' : 'monyet',
    'sng' : 'singa',
    'mcn' : 'macan'
}

# menambahkan/mengganti item
buahbuahan['smk'] = 'semongko' #mengganti value dari key 'smk'
buahbuahan['srk'] = 'sirsak' #menambahkan value dan nilai baru
buahbuahan.update({'mgs' : 'manggis'}) #menambahkan value dan nilai baru menggunakan .update({})
buahbuahan.update(hewanhewan) #menambahkan item dari dict berbeda
print(buahbuahan)

# mengambil value dari key
print(buahbuahan['apl']) #mengambil value dari key 'apl'
print(buahbuahan.get('apl')) #mengambil value dari key 'apl' menggunakan get

# menghapus item
del buahbuahan['mcn'] #menghapus value dari key 'mcn' menggunakan del
print(buahbuahan)
buahbuahan.pop('psg') #menghapus value dari key 'psg' menggunakan .pop()
print(buahbuahan)
buahbuahan.popitem() ##menghapus value terakhir dari dictionary menggunakan .popitem()
print(buahbuahan)

# untuk mengambil semua key/value/items
print(buahbuahan.keys()) #untuk mengambil semua keys didalam data dict
print(buahbuahan.values()) #untuk mengambil semua values didalam data dict
print(buahbuahan.items()) #untuk mengambil semua items(key dan value) didalam data dict


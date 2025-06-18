# .update({})
# .get()
# .keys()
# .values()

# sintaks 
# dict = {
#     'key' : 'value',
#     'key' : 'value'
# }

data_dict = {
    'skh' : 'sakha pratama',
    'shs' : 'shesa aulia',
    'ski' : 'sakhi adhitama'
}

# MENGAMBIL DATA (KEY : VALUE) DALAM DICTIONARY
# .get("...") = untuk mengambil value didalam key (jika tidak ada maka output=none)
print(data_dict["shs"])
print(data_dict.get("skh"))
print(data_dict.get("shs"))

# MENAMBAHKAN DATA BARU (KEY : VALUE) DALAM DICTIONARY
# .update({"new key" : "new value"}) = untuk menambahkan item keys dan value dalam data dict
data_dict.update({"ach" : "achmad", "fzz" : "faiz"})
print(data_dict) 
data_dict['prtm'] = "pratama" # cara lain menambahkan item keys dan value dalam data dict
print(data_dict)


print(data_dict.keys()) # .keys() = untuk mengambil semua keys didalam data dict
print(data_dict.values()) # .values() = untuk mengambil semua values didalam data dict
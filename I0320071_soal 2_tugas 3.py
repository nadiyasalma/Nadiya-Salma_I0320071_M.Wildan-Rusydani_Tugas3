#dictionary
myself1 = {"Nama":"nadiya salma",
            "Hobi1":"Travelling",
           "Hobi2" : "dengerin lagu",
           "hobi3" : "nonton film",
            "Sosmed1": "nadiyarosyida_",
            "Sosmed2" : " nadiyarsyda, ",
           "sosmed3" : "nadiyas13",
            "lagu1": "blue-keshi",
           "lagu2" : "you were good to me-jeremy zucker",
           "lagu3" : "malibu night-lany",
            "makanan1": "cheese cake",
            "makanan2" : "olahan daging ayam dan sapi",
           "makanan3" : "seafood"}
print(myself1)

#mengubah salah satu hobi dan sosmed
myself1 =  {"Nama":"nadiya salma",
            "Hobi1":"Travelling",
           "Hobi2" : "dengerin lagu",
           "Hobi3" : "nonton film",
            "Sosmed1": "nadiyarosyida_",
            "Sosmed2" : " nadiyarsyda, ",
           "sosmed3" : "nadiyas13",
            "lagu1": "blue-keshi",
           "lagu2" : "you were good to me-jeremy zucker",
           "lagu3" : "malibu night-lany",
            "makanan1": "cheese cake",
            "makanan2" : "olahan daging ayam dan sapi",
           "makanan3" : "seafood"}
myself1['Hobi3'] = "memasak"
myself1['sosmed2'] = "nadiya salma"
print("myself1['sosmed2']: ", myself1['sosmed2'])
print("myself1['Hobi3']: ", myself1['Hobi3'])

#hapus 2 makanan favorit
myself1 =  {"Nama":"nadiya salma",
            "Hobi1":"Travelling",
           "Hobi2" : "dengerin lagu",
           "hobi3" : "nonton film",
            "Sosmed1": "nadiyarosyida_",
            "Sosmed2" : " nadiyarsyda, ",
           "sosmed3" : "nadiyas13",
            "lagu1": "blue-keshi",
           "lagu2" : "you were good to me-jeremy zucker",
           "lagu3" : "malibu night-lany",
            "makanan1": "cheese cake",
            "makanan2" : "olahan daging ayam dan sapi",
           "makanan3" : "seafood"}
del myself1['makanan2']
del myself1['makanan3']

#menambahkan 1 hobi
myself1['hobi3'] = "membaca"

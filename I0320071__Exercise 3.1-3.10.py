#exercise 3.1
#cara mengakses nilai di dalam list python

list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1;5]: ", list2[1:5])

#exercise 3.2
list = ['fisika', 'kimia', 1993, 2017]
print("Nilai ada pada index 2: ", list[2])
list[2] = 2001
print("Nilai baru ada pada index 2: ", list[2])

#exercise 3.3
#contoh cara menghapus nilai pada list python

list = ['fisika', 'kimia', 1993, 2017]

print(list)
del list[2]
print("setelah dihapus nilai pada index 2: ", list)

#exercise 3.4
#contoh cara membuat dictionary pada python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

#exercise 3.5
#contoh cara membuat dictionary pada python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

#exercise 3.6
#update dictionary python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; #mengubah entru yang sudah ada
dict['School'] = "DPS School" #Menambah entri baru
print("dict['Age']; ", dict['Age'])
print("dict['School']: ", dict['School'])

#exercise 3.7
#cara menghapus pada dictionary python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name'] #hapus entri dengan key 'Name'
dict.clear() #hapus semua entri dict
del dict #hapus dictionary yang sudah ada
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

#exercise 3.8
#cara mengakses nilai tuple

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

#xercise 3.9
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
#aksi seperti dibawahini tidak bisa dilakukan pada tuple python
#karena memang nilai pada tuple python tidakbisa diiubah
#tup1[0] - 100

#jadi, buatlah tuple baru sebagai berikut
tup3 = tup1 + tup2
print(tup3)

#exercise 3.10
tup = ('fisia', 'kimia', 1993, 2017)
#hapus tupe statement del
del tup

#lalu buat kembali tuple yang baru dnegan elemen yang di inginkan
tup = ('Bahasa', 'Literasi', 2020)
print("Setelah menghapus ti[e:", tup)




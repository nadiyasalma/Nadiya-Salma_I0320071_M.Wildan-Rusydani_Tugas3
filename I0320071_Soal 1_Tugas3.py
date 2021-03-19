#list 10 teman
list1 = ['Hasna', 'Halidya', 'Narista', 'Nadia', 'Rafly', 'Ivan', 'Ilham','Nurki', 'Nanda', 'Oktavian']
print(list1)

#list index
list1 = ['Hasna', 'Halidya', 'Narista', 'Nadia', 'Rafly', 'Ivan', 'Ilham', 'Nurki', 'Nanda', 'Oktavian']
print("list index dari 4,6,7 adalah: ", list[4], list[6], list[7])

#mengganti list nama
ganti_list = ['Hasna', 'Halidya', 'Narista', 'Nadia', 'Rafly', 'Ivan', 'Ilham', 'Nurki', 'Nanda', 'Oktavian']
print("item awal: ", ganti_list)
ganti_list[3] = ('ayu')
ganti_list[5] = ('Rara')
ganti_list[9] = ('Hilmy')
print(ganti_list)

#menambah 2 teman
tambah_teman = ['Hasna', 'Halidya', 'Narista', 'Nadia', 'Rafly', 'Ivan', 'Ilham', 'Nurki', 'Nanda', 'Oktavian']
tambah_teman.append('Hafid')
tambah_teman.append('Laras')
print(tambah_teman)

#menampilkan semua teman dengan perulangan
teman = []
nama_teman = input('ketik nama teman: ')
while nama_teman != '':
    teman.append(nama_teman)
    nama_teman = input('ketik nama teman: ')
    print(teman)

#menampilkan panjang list
list1 = ['Hasna', 'Halidya', 'Narista', 'Nadia', 'Rafly', 'Ivan', 'Ilham','Nurki', 'Nanda', 'Oktavian']

print(list1,'panjang listnya adalah: ', len(list1))
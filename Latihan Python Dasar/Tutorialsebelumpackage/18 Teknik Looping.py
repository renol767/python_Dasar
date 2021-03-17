#Loop teknik
nama_band = ['Om PMR',
             'Om Nada Indah',
             'Om Psp',
             'Fill The Blanks',
             'Semut Merah']
lagu = ['Malam Jumat Kliwon',
        'Majalengka Sejuta Makna',
        'Andeca',
        'Antara Benci dan Rindu',
        'Aw Aw Aw']
#enumerate
for a,b in enumerate(nama_band):
    print(a, ':', b)
#zip
for c,d in zip(nama_band,lagu):
    print(c,'Lagunya',d)
#set
playlist = {'meraih bintang','meraih awan','meraih piala'}
for play in sorted(playlist): # memakai sorted(urutan huruf)
    print(play)

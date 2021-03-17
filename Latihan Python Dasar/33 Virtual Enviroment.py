# Jika kita mempunyai file yang dibuat tahun lalu, ketika kita buka file di tahun sekarang
# Maka Package package nya sudah berubah(paling terbaru) otomatis syntax/lainya berubah
# Nah bagaimana mengatasi ini, Ada sebuah cara yaitu virtual enviromen
# Virtual enviroment : Projek kita akan di isolasi/dipisahkan misal
# project1 : dibuat pada tahun 2018 dengan package numpy 9.1,django 9.5 (misal!)
# project2 : diuat pada tahun 2020 dengan package numpy 10,5,django 12.3 (misal!)
# Ketika kita membuka project1 pada tahun 2020 maka package didalam nya akan tetap
# Metode ini berguna ketika kita membuat web/aplikasi/dll yang akan berguna jangka panjang :)
# Jadi intinya kita di dalam folder project kita terdapat folder venv(virtual enviroment)
# Misalkan kita ada di tahun 2018 dan project tersebut sudah selesai dengan versi package package pada tahun tsb
# Ketika kita mendapatkan projek lagi di tahun 2019 tapi project 2019 itu membutuhkan package versi terbaru
# Maka kita harus membuat venv pada project yang baru agar venv project 2018 tidak ikut terupdate
# Caranya buka cmd lalu ketikan "python -m venv Project2019"
# Setelah itu barulah install package package terbaru yang dibutuhkan program tsb
# Kalau kita ingin mengubah codingan di project 2018 tinggal klik open lalu arahkan ke folder Project2018
# Atau bisa dengan cara klik setting, klik project,klik project interpeter, nanti ketika sudah di klik dibagian project interpeter akan ada 2 pilihan
# Misal pada tahun 2018 python nya v 3.2 dan pada tahun 2019 v python nya v 3.6 nah jika kita ingin berganti venv project kita
# Tinggal pilih versi python pada saat itu dan directory project nya
# Ada 1 trik lagi ketika kita ingin migrasi PC tetapi saya ingin di PC yang baru Project2018 bisa saya jalankan/ubah
# Buat Requirement(isi nya package dan versi package yang kita gunakan di Project2018), buka terminal lalu pip3 freeze --local > requirements.txt
# Pindah/copy requirement.txt secara manual. lalu ketikan pip3 install -r requirements.txt maka akan otomatis diinstal package yang sama di PC Baru

# Nama : Fadhil Syafiq Abdullah (312510161)

## Program ini adalah aplikasi sederhana pendataan mahasiswa yang menggunakan konsep OOP (Object-Oriented Programming) dan pemisahan tugas antar kelas.

1. Class student
   Berfungsi sebagai penyimpan data mahasiswa, yang terdiri dari:

   nim → Nomor Induk Mahasiswa

   name → nama mahasiswa

   score → nilai mahasiswa
2. Class studentprocess
Mengelola proses data mahasiswa:

   Menyimpan data mahasiswa dalam list students

   input_student() → menerima input NIM, nama, dan nilai, melakukan validasi, lalu menyimpan data

   get_students() → mengembalikan data mahasiswa

3. Class StudentView
   Menampilkan data mahasiswa ke layar:

   show_table() → menampilkan data dalam bentuk tabel berisi nomor, NIM, nama, dan nilai

4. Fungsi Main
   Merupakan program utama yang menyediakan menu:
   Menambah data mahasiswa
   Menampilkan data mahasiswa
   Keluar dari program
# Kesimpulan:
   Kode ini memisahkan data (Student), proses (StudentProcess), dan tampilan (StudentView) sehingga program menjadi rapi, mudah
   dipahami, dan mudah dikembangkan.



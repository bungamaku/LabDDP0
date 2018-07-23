# Soal Tutorial

## Disini Maba Disana Maba

Ruben adalah seorang maba Fasilkom UI. Seperti kebanyakan maba, Ruben suka 
bergerombol kesana kemari. Saat Ruben sedang bergerombol ria bersama maba-maba
yang lain, ia tersandung dan terjatuh, namun bisa bangkit lagi. Lalu Ruben pun 
melihat kebawah untuk mengecek apa yang membuatnya tersandung. Ternyata ada 
sebuah kertas disana, Ruben kebingunan, bagaimana bisa kertas membuat orang
tersandung. Menyadari keganjilan tersebut, Ruben pun memungut kertas tersebut 
untuk menguak misteri dibaliknya. Kertas tersebut ternyata bukan kertas biasa, 
didalamnya terdapat algoritma untuk menghasilkan sebuah nomor unik yang akan
digunakan saat puncak OKK UI 2018. 

Setelah Ruben membacanya berkali-kali, akhirnya ia memahami cara kerja 
algoritma tersebut, yaitu sebagai berikut:

- Nomor unik dihasilkan menggunakan nama lengkap mahasiswa sebagai input

- Semua alphabet pada nama mahasiswa dianggap sebagai huruf besar

- Character selain alphabet diabaikan

- Jumlahan nilai desimal ascii dari setiap character yang diperhitungkan 
  (berdasarkan 2 aturan diatas) pada nama mahasiswa akan menghasilkan sebuah 
  nilai, sebut saja nilai X
  
- Nilai X tidak boleh melebihi 400, jika nilai x melebihi 400 maka perhitungan
  akan dimulai lagi dari 1.
  
  > Misal X = 401, maka X akan menjadi 1  
  > Misal X = 420, maka X akan menjadi 20  
  > Misal X = 1232, maka X akan menjadi 32

Ruben berencana membuat program untuk menghasilkan nomor unik berdasarkan
algoritma tersebut, namun karena terlalu mudah, ia tidak ingin mengerjakannya
sendiri dan meminta kalian, teman Ruben sesama maba Fasilkom UI 2018 untuk 
membuatkan program tersebut untuknya. 

Ketentuan Tambahan Untuk Program :
- Program akan terus meminta input sampai program diberhentikan
- Program diberhentikan dengan memberikan input `-`
- Input dan Output mengikuti format

### Format Input
> Masukkan Nama : `[nama]`

### Format Output
> Nomor unik untuk `[nama]` adalah `[nomor]`

Jika input berupa `-` maka outputnya adalah :
> Program Berhenti


#### Contoh Eksekusi Program :
##### Kata yang dicetak tebal menandakan input dari user
<pre>
Masukkan Nama : <b>Ruben Adipati Dhirgantara</b>
Nomor unik untuk Ruben Adipati Dhirgantara adalah 93
Masukkan Nama : <b>Ahmad Fauzan A.I.</b>
Nomor unik untuk Ahmad Fauzan A.I. adalah 138
Masukkan Nama : <b>Bunga    Amalia     Kurniawati</b>
Nomor unik untuk Bunga    Amalia     Kurniawati adalah 353
Masukkan Nama : <b>Ma'rufudin Anhar</b>
Nomor unik untuk Ma'rufudin Anhar adalah 245
Masukkan Nama : <b>Lily The 1st Fairy</b>
Nomor unik untuk Lily The 1st Fairy adalah 285
Masukkan Nama : <b>-</b>
Program Berhenti
</pre>

### Hint
Kalian dapat menggunakan fungsi built-in python untuk membuat program ini,
seperti `ord()` untuk mendapatkan nilai desimal character ascii. Kalian
dapat mencarinya di 
- https://docs.python.org/3/
- https://stackoverflow.com
- https://google.com

## Soal Bonus
##### *"Tak akan kubiarkan bisnisku hancur"* - Ruben

Ruben yang menyadari nomor unik tersebut adalah nomor yang sangat penting
dan rahasia berencana membuat bisnis jual beli nomor tersebut secara ilegal.
Untuk menghindari pengawasan panitia OKK, Ruben melakukan jual beli nomor
tersebut dalam bentuk bilangan biner. Sekali lagi, Ruben mengajak kalian,
teman-teman sesama maba Fasilkom UI 2018 untuk mengupgrade programnya agar
bisa melakukan konversi nomor unik tersebut menjadi bilangan biner.

#### Catatan
- Tidak boleh menggunakan fungsi built-in python `bin()`  
- Untuk materi sistem bilangan (konversi desimal ke biner dan sebagainya)
  kalian bisa melihatnya di [sini][Sistem Bilangan]

### Format Output
> Nomor unik untuk `[nama]` adalah `[nomor]`  
> Nomor unik untuk `[nama]` dalam bentuk biner adalah `[nomor_biner]`

Jika input berupa `-` maka outputnya adalah :
> Program Berhenti

<pre>
Masukkan Nama : <b>Ruben Adipati Dhirgantara</b>
Nomor unik untuk Ruben Adipati Dhirgantara adalah 93
Nomor unik untuk Ruben Adipati Dhirgantara dalam bentuk biner adalah 1011101
Masukkan Nama : <b>Ahmad Fauzan A.I.</b>
Nomor unik untuk Ahmad Fauzan A.I. adalah 138
Nomor unik untuk Ahmad Fauzan A.I. dalam bentuk biner adalah 10001010
Masukkan Nama : <b>Bunga    Amalia     Kurniawati</b>
Nomor unik untuk Bunga    Amalia     Kurniawati adalah 353
Nomor unik untuk Bunga    Amalia     Kurniawati dalam bentuk biner adalah 101100001
Masukkan Nama : <b>Ma'rufudin Anhar</b>
Nomor unik untuk Ma'rufudin Anhar adalah 245
Nomor unik untuk Ma'rufudin Anhar dalam bentuk biner adalah 11110101
Masukkan Nama : <b>Lily The 1st Fairy</b>
Nomor unik untuk Lily The 1st Fairy adalah 285
Nomor unik untuk Lily The 1st Fairy dalam bentuk biner adalah 10001110
Masukkan Nama : <b>-</b>
Program Berhenti
</pre>

<p style="text-align: center; font-size: 1.5em;"><strong>SELAMAT MENGERJAKAN
DAN BERSENANG-SENANG</strong></p>

[Sistem Bilangan]: https://github.com/laymonage/TarungLabDDP1/blob/master/lab_instructions/lab03.md#sistem-bilangan


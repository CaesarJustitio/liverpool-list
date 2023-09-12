Caesar Justitio
2206082373
PBP E
Liverpoolist

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

a. Membuat sebuah proyek 
Pertama, saya membuat repositori bernama liverpool-list di local. Lalu, saya menjalankan virtual environment pada direktori tersebut untuk mengatur package, setelah itu saya mengatur dependencies yang diperlukan di dalam file requirements.txt. Setalah itu, saya membuat proyek Django dengan cara menjalankan 'django-admin startproject liverpool_list .' pada terminal folder tersebut. Langkah terakhir adalah mengaktifkan server dengan cara menjalankan './manage.py runserver'.

b. Membuat aplikasi main
Untuk membuat aplikasi main, saya memasukkan perintah 'python manage.py startapp main' ke terminal. Lalu, saya menambahkan 'main' ke settings agar terdaftar ke proyek.

c. Melakukan routing
Untuk mengakses aplikasi main melalui web, perlu dilakukan routing URL. Saya mengatur file urls.py yang berada di direktori proyek agar terhubung. Dalam kata lain, mengarahkan url-url yang secara umum terkait dengan seluruh proyek, bukan hanya satu aplikasi. Step ini penting untuk menghubungkan file urls pada aplikasi dan memungkinkan proyek modular dan terpisah antaraplikasi.

d. Membuat model pada aplikasi main
Pada file models.py saya membuat class Item yang berisi 'name' bertipe CharField, 'amount' bertipe IntegerField, 'description' bertipe TextField, dan 'color' bertipe TextField. Lalu, saya migrasi modelnya untuk memastikan bahwa skema basis data tetap sejalan dengan definisi model-model aplikasi pada proyek dan membantu menjaga konsistensi data dalam aplikasi.

e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Saya menghubungkan view dengan template dengan cara mengintegrasikan komponen MVT. Pada file views.py di main saya membuat fungsi 'show_main' dan menambahkan context app, name, dan class untuk dipakai dalam template. Lalu, karena sudah ada context yang berisi dictionary data yang diperlukan, saya mengubah file main.html saya untuk menggunakan variabel yang telah didefinisikan.

f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Saya membuat file urls.py dalam direktori main yang berisi komponen penting dalam pengaturan aplikasi Django. Saya mendefinisikan app_name menjadi 'main' dan urlpatterns agar mengarah ke path show_main. Step ini memungkinkan URL proyek terarah ke tampilan yang sesuai dengan fitur-fitur di dalam aplikasi.

g. Melakukan deployment ke Adaptable 
Saya membuat app baru di Adaptable dengan menghubungkannya ke repositori GitHub My-Wardrobe. Saya memilih Python Template App dan PostgreSQL untuk template dan tipe basis data. Lalu, saya memastikan versi python sudah sesuai dengan yang ada di aplikasi dan di bagian start command saya memasukkan 'python manage.py migrate && gunicorn shopping_list.wsgi' ntuk memastikan bahwa struktur basis data sesuai dengan definisi model-model aplikasi. Lalu saya mendeploy aplikasi saya agar aktif dan bisa diaskes di internet.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Alur Permintaan dan Respon dalam Aplikasi Django](assets/bagan.jpg)

Permintaan HTTP dari klien/user pertama-tama akan mencapai file urls.py. File urls.py mengandung pengaturan untuk mengarahkan URL ke tampilan (views) yang sesuai. Pada tahap ini, Django mencocokkan URL yang diterima dari permintaan dengan pola URL yang telah didefinisikan dalam file urls.py.

Setelah URL cocok dengan pola yang ada dalam berkas urls.py, permintaan akan diteruskan ke tampilan yang sesuai dalam berkas views.py.

Lalu, jika diperlukan akses ke model-model yang didefinisikan dalam berkas models.py aplikasi. Jika tampilan membutuhkan data dari basis data, mereka akan memanggil query ke model-model ini.

Ketika views melakukan query ke model-model ini, Django akan menghasilkan SQL yang sesuai dan mengirimkannya ke database. Database akan mengembalikan hasil dari query tersebut ke Django, yang kemudian akan membentuknya menjadi objek Python yang dapat digunakan dalam views.

Setelah tampilan selesai memproses permintaan dan mendapatkan data yang dibutuhkan, selanjutnya views akan dirender menggunakan template HTML.

Hasil proses yang disiapkan dalam template HTML akan dikirimkan sebagai respons HTTP kepada klien (pengguna). Respons ini berisi HTML yang akan ditampilkan di browser pengguna, bersama dengan semua elemen seperti gambar, teks, dan data lain yang telah diproses.

Akhirnya, respons yang dihasilkan akan diterima oleh klien (pengguna), yang akan melihat dan berinteraksi dengan halaman web yang dihasilkan.


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment adalah ruang kerja yang terpisah untuk proyek Python. Dengan menggunakan virtual environment, kita dapat menginstal dan menggunakan versi Python dan pustaka yang berbeda untuk setiap proyek, tanpa mengganggu proyek lain.
Ada beberapa alasan mengapa kita menggunakan virtual environment, antara lain:

Untuk menghindari konflik pustaka: Jika kita memiliki dua proyek Python yang menggunakan versi Python yang berbeda, atau pustaka yang berbeda, maka kita dapat menggunakan virtual environment untuk memisahkan proyek-proyek tersebut.
Untuk meningkatkan kinerja: Virtual environment dapat membantu meningkatkan kinerja dengan mengisolasi proyek-proyek dari satu sama lain.
Untuk memudahkan manajemen pustaka: Virtual environment dapat membantu memudahkan manajemen pustaka dengan memungkinkan kita untuk menginstal dan memperbarui pustaka secara independen untuk setiap proyek.
Ya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, ada beberapa potensi masalah yang dapat terjadi jika kita tidak menggunakan virtual environment, antara lain:

Konflik pustaka: Jika kita memiliki dua aplikasi web berbasis Django yang menggunakan versi Django yang berbeda, atau pustaka yang berbeda, maka kita mungkin akan mengalami konflik pustaka.
Kerusakan proyek: Jika kita menginstal pustaka yang tidak kompatibel dengan proyek Django kita, maka pustaka tersebut dapat merusak proyek kita.
Kerusakan sistem: Jika kita menginstal pustaka yang berbahaya, maka pustaka tersebut dapat merusak sistem kita.
Oleh karena itu, penggunaan virtual environment sangat disarankan untuk pengembangan aplikasi web berbasis Django.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC, MVT, dan MVVM adalah tiga model arsitektur perangkat lunak yang umum digunakan untuk pengembangan aplikasi web.
MVC (Model-View-Controller) adalah model arsitektur yang membagi aplikasi web menjadi tiga komponen utama:

Model: Komponen yang menangani data dan logika bisnis.
View: Komponen yang menampilkan data ke pengguna.
Controller: Komponen yang menerima input dari pengguna dan mengarahkannya ke model atau view yang sesuai.
MVT (Model-View-Template) adalah model arsitektur yang mirip dengan MVC, tetapi tidak memiliki controller. Dalam MVT, view bertanggung jawab untuk menangani input dari pengguna dan mengarahkannya ke model atau template yang sesuai.

MVVM (Model-View-ViewModel) adalah model arsitektur yang membagi view menjadi dua komponen utama:

View: Komponen yang menampilkan data ke pengguna.
ViewModel: Komponen yang menangani logika antarmuka pengguna dan komunikasi dengan model.
Perbedaan utama antara ketiga model arsitektur ini adalah pada peran controller dan view. Dalam MVC, controller bertanggung jawab untuk menangani input dari pengguna dan mengarahkannya ke model atau view yang sesuai. Dalam MVT, view bertanggung jawab untuk menangani input dari pengguna dan mengarahkannya ke model atau template yang sesuai. Dalam MVVM, view tidak memiliki logika apa pun dan hanya bertanggung jawab untuk menampilkan data dari view model.

Secara umum, MVC adalah model arsitektur yang paling umum digunakan untuk pengembangan aplikasi web. MVT dan MVVM adalah model arsitektur yang lebih spesifik dan biasanya digunakan untuk aplikasi web yang lebih kompleks.
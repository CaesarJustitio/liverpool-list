Caesar Justitio
2206082373
PBP E
Liverpoolist

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

a. Membuat sebuah proyek 
Pertama, saya membuat repositori bernama liverpool-list di local. Lalu, saya menjalankan virtual environment pada direktori tersebut untuk mengatur package, setelah itu saya mengatur dependencies yang diperlukan di dalam file requirements.txt. Setalah itu, saya membuat proyek Django dengan cara menjalankan 'django-admin startproject liverpool_list .' pada terminal folder tersebut. Langkah terakhir adalah mengaktifkan server dengan cara menjalankan './manage.py runserver'.

b. Membuat aplikasi main
Untuk membuat aplikasi main, saya memasukkan perintah 'python manage.py startapp main' ke terminal. Lalu, saya menambahkan 'main' ke settings.py.

c. Melakukan routing
Mengatur file urls.py yang berada di direktori proyek agar bisa mengakses web dengan domains / yang kita inginkan, contoh '/main'. Routing adalah menghubungkan file kita dengan suatu domain yang kita ingin kan dengan cara menentukan app namenya yaitu 'main'.

d. Membuat model pada aplikasi main
Pada file models.py, membuat class Item dengan atribut 'name' bertipe CharField, 'amount' bertipe IntegerField, 'description' bertipe TextField, 'goals' bertipe IntegerField, dan marketPrice bertipe 'IntegerField'. Kemudian model dilakukan migrasi supaya data dapat berjalan secara konsisten.

e. Membuat sebuah fungsi pada views.py
Membuat fungsi show_main pada views.py dengan isi variable-variable yang akan ditempilkan pada main.html. Views merupakan salah satu komponen utama MVT. Pada T yaitu template, pada file main.html, kita bisa menggunakan variable yang telah didefinisikan pada views.py

f. Melakukan routing pada urls.py aplikasi main 
Mengatur file urls.py yang berada di direktori proyek agar bisa memetakan fungsi yang telah dibuat pada views.py, isi dari urls.py pada aplikasi main adalah app name dan urlpatterns yang berisi path untuk mengakses show_main.

g. Melakukan deployment ke Adaptable 
Deployment ke Adaptable dilakukan dengan cara menghubungkan repository di gihub dengan Adaptable, kita memilih main sebagai branch utama, lalu memilih mendevelop web menggunakan python environment dan PostgreSQL sebagai template data. Setalah itu Adaptable akan meminta versi python dari yang sedang berjalan di komputer kita dan akan meminta input start command untuk bisa menjalankan aplikasi, start command aplikasi yang saya buat adalah 'python manage.py migrate && gunicorn liverpool_list.wsgi'. Setelah menjalankan semua step di atas, tinggal menunggu proses deployment berjalan dan selesai

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Alur Permintaan dan Respon dalam Django](assets/bagan.jpg)

a. Permintaan HTTP dari user menuju file urls.py. Dalam file ini, ada konfigurasi yang mengarahkan URL ke tampilan yang diminta. Django akan mencocokkan URL yang diterima dengan pola URL yang telah dideclare dalam file urls.py. Setelah URL cocok dengan pola yang ada dalam file tersebut, maka permintaan akan dijalankan ke tampilan yang ada dalam file views.py.

b. Akses akan diberikan dengan atribut model yang telah didefinisikan dalam file models.py. Query akan berjalan pada model-model jika data-data dibutuhkan untuk tampilan. Saat views melakukan query ke model, Django akan melakukan request kepada basis data lalu akan diterima dan diberi data yang bisa digunakan pada tampilan yang kita inginkan.

c. Setelah data berhasil direquest, html akan dirender. Outputnya akan dikirimkan sebagai respons HTTP kepada user yang akan digunakan pada browser untuk menampulkan semua elemen yang sudah kita buat.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment adalah suatu workspace yang terpisah untuk proyek dari Python. Dengan menggunakan virtual environment, kita dapat menginstal dan menggunakan versi Python dan library yang berbeda untuk setiap proyek, tanpa mengganggu proyek lain, hal itu bisa sangat membantu dalam manajemen proyek yang menjadi sangat teratur. Alasan lain memakai virtual environment antara lain:
a. Proyek tidak tercampur
Dalam pengembangan sebuah proyek, bisa jadi dibutuhkan requirements yang berbeda antar proyek lainnya dan penggunaan library yang berbeda juga untuk menunjang dari masing-masing proyek yang dikerjakan, dengan menggunakan virtual environemnt kita bisa memisahkan antar proyek dengan tujuan untuk menghindari konflik dari versi pythonnya itu sendiri maupun dari library.

b. Clean management
Dengan menggunakan virtual environment, keteraturan dalam manajemen bisa dimaksimalkan yang membuat kemudahan pengembangan seluruh proyek dan menjadikan clean agar tidak terjadi kerancuan saat mengerjakan proyek bersama developer lainnya.

c. Management Dependensi
Memastikan bahwa kita menggunakan versi yang benar dari setiap paket. Karena dalam melakukan develop proyek-proyek, kita membutuhkan library atau modul pihak ketiga.


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
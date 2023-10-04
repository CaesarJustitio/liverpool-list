Caesar Justitio
2206082373
PBP E
Liverpoolist

- TUGAS 2

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

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
Deployment ke Adaptable dilakukan dengan cara menghubungkan repository di gihub dengan Adaptable, kita memilih main sebagai branch utama, lalu memilih mendevelop web menggunakan python environment dan PostgreSQL sebagai template data. Setalah itu Adaptable akan meminta versi python dari yang sedang berjalan di komputer kita dan akan meminta input start command untuk bisa menjalankan aplikasi, start command aplikasi yang saya buat adalah 'python manage.py migrate && gunicorn liverpool_list.wsgi'. Setelah menjalankan semua step di atas, tinggal menunggu proses deployment berjalan dan selesai.


## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Alur Permintaan dan Respon dalam Django](assets/bagan.jpg)

a. Permintaan HTTP dari user menuju file urls.py. Dalam file ini, ada konfigurasi yang mengarahkan URL ke tampilan yang diminta. Django akan mencocokkan URL yang diterima dengan pola URL yang telah dideclare dalam file urls.py. Setelah URL cocok dengan pola yang ada dalam file tersebut, maka permintaan akan dijalankan ke tampilan yang ada dalam file views.py.

b. Akses akan diberikan dengan atribut model yang telah didefinisikan dalam file models.py. Query akan berjalan pada model-model jika data-data dibutuhkan untuk tampilan. Saat views melakukan query ke model, Django akan melakukan request kepada basis data lalu akan diterima dan diberi data yang bisa digunakan pada tampilan yang kita inginkan.

c. Setelah data berhasil direquest, html akan dirender. Outputnya akan dikirimkan sebagai respons HTTP kepada user yang akan digunakan pada browser untuk menampulkan semua elemen yang sudah kita buat.


## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment adalah suatu workspace yang terpisah untuk proyek dari Python. Dengan menggunakan virtual environment, kita dapat menginstal dan menggunakan versi Python dan library yang berbeda untuk setiap proyek, tanpa mengganggu proyek lain, hal itu bisa sangat membantu dalam manajemen proyek yang menjadi sangat teratur. Alasan lain memakai virtual environment antara lain:
a. Proyek tidak tercampur
Dalam pengembangan sebuah proyek, bisa jadi dibutuhkan requirements yang berbeda antar proyek lainnya dan penggunaan library yang berbeda juga untuk menunjang dari masing-masing proyek yang dikerjakan, dengan menggunakan virtual environemnt kita bisa memisahkan antar proyek dengan tujuan untuk menghindari konflik dari versi pythonnya itu sendiri maupun dari library.

b. Clean management
Dengan menggunakan virtual environment, keteraturan dalam manajemen bisa dimaksimalkan yang membuat kemudahan pengembangan seluruh proyek dan menjadikan clean agar tidak terjadi kerancuan saat mengerjakan proyek bersama developer lainnya.

c. Management Dependensi
Memastikan bahwa kita menggunakan versi yang benar dari setiap paket. Karena dalam melakukan develop proyek-proyek, kita membutuhkan library atau modul pihak ketiga.


## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC, MVT, dan MVVM adalah tiga model arsitektur perangkat lunak yang umum digunakan untuk pengembangan aplikasi web.
MVC (Model-View-Controller)
MVT (Model-View-Template)
MVVM (Model-View-ViewModel)

* MVC (Model-View-Controller):
Model: Mewakili data aplikasi dan logic. Model bertanggung jawab untuk mengelola data dan interaksi dengan database.
View: Menampilkan data kepada user dalam bentuk tampilan yang memungkinkan user melakukan interaksi dengan aplikasi.
Controller: Mengatur aliran informasi antara Model dan View. Controller merespons tindakan user dan memutuskan apa yang harus dilakukan berdasarkan perintah yang ada.

* MVT (Model-View-Template):
Model: Mewakili data aplikasi dan logic. Model bertanggung jawab untuk mengelola data dan interaksi dengan database.
View: Menampilkan data kepada user dalam bentuk tampilan yang memungkinkan user melakukan interaksi dengan aplikasi.
Template: Template dalam MVT adalah lapisan tampilan dan presentasi yang terpisah dari View. Template digunakan untuk mengatur tampilan data dalam halaman dari sebuah web.

* MVVM (Model-View-ViewModel):
Model: Mewakili data aplikasi dan logic. Model bertanggung jawab untuk mengelola data dan interaksi dengan database.
View: Menampilkan data kepada user dalam bentuk tampilan yang memungkinkan user melakukan interaksi dengan aplikasi.
ViewModel: Ini adalah konsep yang memungkinkan hubungan data antara Model dan View. ViewModel berisi logic untuk mengambil data dari file Model dan mengirim ke View dalam format yang siap ditampilkan.

* Perbedaan:
a. Dalam MVC, Model dan View terpisah, dan Controller bertindak sebagai penghubung di antara Model dan View. Konsep ini banyak digunakan pada pengembangan web tradisional.

b. Dalam MVT, pemisahan terjadi antara Template dan View, sementara dalam MVC, View bertanggung jawab atas tampilan dan logic presentasi dari sebuah web.

c. Dalam MVVM, hubungan data bisa terjadi dua arah antara Model dan View, fitur ini sangat berguna untuk pengembangan aplikasi yang membutuhkan otomasi tampilan saat ada perubahan pada data.


# TUGAS 3

## 1. Apa perbedaan antara form POST dan form GET dalam Django?

### POST
- Data dikirim dalam bagian permintaan HTTP
- Data tidak terlihat pada URL
- Dapat digunakan untuk mengirimkan data besar dan data sensitif

### GET
- Data dikirim dalam URL permintaan HTTP
- Data terliihat pada URL
- Tidak dapat digunakan untuk mengirimkan data besar dan data sensitif karena rawan terjadi kebocoran data sensitif dan disalahgunakan oleh orang-orang tidak bertanggund jawab

## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

### XML

- Format data tekstual yang dapat dibaca oleh manusia dan mesin
- Dapat digunakan untuk beragam jenis data dan bisa digunakan untuk struktur data yang kompleks
- Dapat digunakan untuk mengirimkan data besar

### JSON

- Data text yang bisa dibaca oleh mesin
- Efisien untuk melakukan transmisi data
- Lebih mudah dilakukan pemrosesan

### HTML

- Format data mewakili halaman web
- Tidak dapat digunakan untuk data-data yang kompleks
- Tidak efisien untuk mengirimkan data yang besar

## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Keunggulannya yang membuat JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena:
- Ringkas, efisien, dan cepat
- Readable: Mudah dimengerti oleh manusia dan mesin
- Kapabiilitas: Bisa memproses beragam jenis data

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

### 1) Membuat input form untuk menambahkan objek model pada app sebelumnya.

- Membuat forms.py pada folder main dengan isian "from main.models import Item" dan dengan isi "fields = ["name", "amount", "description", "goals", "marketPrice"]" 

- Membuat fungsi create_product dalam file views.py yang bertujuan untuk membuat form yang dapat menambahkan data produk ke dalam databaser. Jangan lupa untuk menambahkan import (HttpResponseRedirect, ProductForm, dan reverse) pada line paling atas

- Memodifikasi fungsi show_main dengan menambahkan 'items': items pada context

- Menambahkan path url yang sesuai pada urls.py yaitu

```py
path('create-product', create_product, name='create_product')
```

- Membuat create_product.html pada folder templates yang ada pada folder main. Membuat tabel untuk menunjukkan data yang telah tersimpan di dalam database:

```py
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

- Menambahkan kode pada file main.html untuk menampilkan data:

```py
  <table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Description</th>
        <th>Goals</th>
        <th>Market Price</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.description}}</td>
            <td>{{item.goals}}</td>
            <td>{{item.marketPrice}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>
```

### 2) Menambahkan 5 fungsi views untuk melihat objek dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Saya menambahkan kode berikut dalam file views.py yang berada di main.
```py
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from django.core import serializers
from main.models import Item

def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Caesar Justitio',
        'class': 'PBP E',
        'appname': 'Liverpoolist',
        'position1': 'Goalkeeper',
        'position2': 'Defender',
        'position3': 'Midfielder',
        'position4': 'Attacker',
        'items': items
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

context bisa disesuaikan dengan keinginan pembuat

### 3) Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Routing URL memungkinkan aplikasi untuk menghubungkan URL tertentu dengan view yang sesuai. Ketika user mengakses URL tertentu, Django akan menggunakan routing URL untuk menentukan view yang harus dipanggil. Pada file urls.py pada direktori main, saya menambahkan kode berikut:

```py
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
]
```

## 5. Screenshoot

1. HTML
![HTML](assets/html.jpg)

2. XML
![XML](assets/xml.jpg)

3. JSON
![JSON](assets/json.jpg)

4. XML by ID
![XML by ID](assets/xml_by_id.jpg)

5. JSON by ID
![JSON by ID](assets/json_by_id.jpg)


# TUGAS 4

## 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Django UserCreationForm adalah sebuah form bawaan yang disediakan oleh Django untuk memudahkan proses pembuatan user pada aplikasi web yang dibangun dengan menggunakan framework Django. Form ini memiliki beberapa kelebihan dan kekurangan, antara lain:

### Kelebihan:

- Memudahkan proses pembuatan user pada aplikasi web yang dibangun dengan menggunakan framework Django.
- Memiliki validasi bawaan yang dapat memastikan data yang dimasukkan oleh user sesuai dengan format yang diinginkan.

### Kekurangan:

- Tampilan form bawaan kurang menarik dan tidak sesuai dengan kebutuhan desain aplikasi web tertentu.
- Tidak dapat melakukan customisasi secara maksimal, sehingga jika ingin menambahkan fitur atau mengubah tampilan form, perlu dilakukan secara manual.


## 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi dan otorisasi adalah dua konsep penting dalam keamanan web. Autentikasi adalah proses memverifikasi identitas pengguna, sedangkan otorisasi adalah proses menentukan apakah pengguna memiliki izin untuk mengakses sumber daya tertentu.

### Autentikasi
Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi Anda. Dalam konteks Django, autentikasi dilakukan oleh model User. Model ini menyimpan informasi tentang pengguna, seperti nama pengguna, email, dan password.

### Otorisasi
Otorisasi memastikan bahwa pengguna hanya dapat mengakses sumber daya yang mereka miliki izinnya untuk diakses. Otorisasi dilakukan oleh sistem izin Django. Sistem izin ini memungkinkan Anda untuk menentukan izin apa yang dimiliki pengguna.

### Kesimpulan
Autentikasi dan otorisasi sangat penting karena membantu melindungi data dan aplikasi Anda dari akses yang tidak sah. Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi Anda dan Otorisasi memastikan bahwa pengguna hanya dapat mengakses sumber daya yang mereka miliki untuk diakses.


## 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah berkas teks yang berisi informasi seperti nama pengguna dan kata sandi yang digunakan untuk membantu komputer dalam mengenali pengguna. Cookies ini diciptakan oleh server saat pengguna terhubung. Informasi dalam cookie diberi label dengan ID yang unik untuk pengguna dan komputer mereka. Ketika ada pertukaran cookie antara komputer pengguna dan server jaringan, server dapat membaca ID ini dan mengakses informasi yang relevan untuk pengguna tersebut. Dengan bantuan cookies, pengembang dapat memberikan pengalaman yang disesuaikan untuk pengguna, seperti mengingat pengguna serta data seperti barang dalam keranjang belanja, halaman yang telah mereka simpan.

Dalam Django, cookies digunakan untuk menyimpan ID sesi yang unik untuk mengidentifikasi setiap browser dan sesi yang terkait dengan peramban tersebut. Data sesi ini biasanya disimpan dalam database situs secara default. Framework sesi Django memungkinkan pengguna untuk menyimpan dan mengambil data sesuai dengan akun pengguna di situs web. Ketika ada permintaan berikutnya dari peramban, peramban akan mengirimkan cookie sessionid ke server. Django akan menggunakan cookie ini untuk mengambil data sesi yang sesuai dan membuatnya dapat diakses di berbagai bagian situs web.


## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Secara default, cookie dalam pengembangan web tidak membawa risiko yang signifikan. Namun, jika data cookie diakses oleh individu dengan niat jahat seperti cyber attacker, mereka dapat memanfaatkannya untuk mengakses riwayat pencarian, mencuri informasi pribadi, atau menyalahgunakan data cookie pengguna, Ada juga kemungkinan bahwa suatu situs web dapat menjual data dari cookie kepada pihak ketiga atau bahkan menggunakan data tersebut untuk melakukan peretasan pada akun pengguna. Oleh karena itu, bijaksana untuk tidak menerima cookie dari situs web yang tidak aman. Selain itu, pengguna memiliki pilihan untuk menolak penggunaan cookie. Sebagian besar situs web dapat berfungsi dengan baik tanpa mengumpulkan informasi pribadi pengguna melalui cookie.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

Fungsi registrasi memungkinkan pengguna baru untuk mendaftar dan membuat akun di aplikasi. Fungsi login memungkinkan pengguna yang telah memiliki akun terdaftar untuk masuk ke dalam akun mereka. Fungsi logout memungkinkan pengguna untuk keluar dari akun mereka dan mengakhiri sesi mereka.

Pertama-tama, dalam file views.py di direktori utama, saya mengimpor beberapa modul, yaitu redirect, UserCreationForm, messages, authenticate, login, dan logout.

Selanjutnya, saya menambahkan beberapa fungsi di dalam file views.py di direktori utama sebagai berikut:

```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Kemudian, dalam direktori "main" > "templates", saya telah membuat dua file HTML baru. Pertama, file "register.html" yang berisi formulir registrasi untuk mengumpulkan masukan dari pengguna, mengirimkannya menggunakan metode POST, dan juga menampilkan pesan kepada pengguna. Saya juga telah menghias halaman ini dengan menambahkan gaya (CSS) ke dalam file HTML tersebut.

Kemudian, saya juga membuat file "login.html" di dalam direktori "main" > "templates". File ini berfungsi sebagai halaman login dalam aplikasi web. Halaman ini berisi formulir login yang mengambil input dari pengguna berupa username dan password. Ketika formulir ini di-submit, data akan dikirimkan menggunakan metode POST. Selain itu, halaman ini dapat menampilkan pesan-pesan kepada pengguna, misalnya jika terdapat pesan kesalahan saat proses login gagal. Halaman ini juga menyertakan tautan untuk mengarahkan pengguna ke halaman registrasi jika mereka belum memiliki akun, dengan menggunakan tautan yang mengarah ke URL halaman registrasi.

Untuk fungsi logout, saya hanya menambahkan tombol logout pada halaman "main.html". Selain itu, saya telah membatasi akses ke halaman "main.html" hanya untuk pengguna yang sudah login dengan menambahkan dekorator "login_required" di dalam file "views.py" di direktori "main".

pada file urls.py saya menambahkan import register, login_user, dan logout_user. Saya juga menambahkan path-path yang sesuai pada urlpatterns;

```py
path('register/', register, name='register'), 
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout')
```


### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Pembuatan akun pengguna sudah berhasil dan sudah berhasil manambahkan banyak dummy data yaitu Name, Amount, Description, Goals, dan MarketPrice

### Menghubungkan model Item dengan User.

Pertama-tama, dalam file "models.py" di direktori "main", saya melakukan impor modul "User". Dengan melakukan impor ini, aplikasi saya mendapatkan kemampuan untuk membuat, mengelola, dan mengautentikasi akun pengguna. Saya juga dapat menggunakannya sebagai referensi ketika perlu menampilkan data yang terkait dengan pengguna. Selanjutnya, saya menambahkan kode berikut:

```py
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Kemudian, dalam fungsi "create_product" dalam file "views.py" di direktori "main", saya memodifikasi fungsinya dengan menambahkan kode berikut:
```py
if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()

        players = Item.objects.count()

        messages.success(request, f"Kamu berhasil menyimpan {players} pemain pada liverpoolist. You'll Never Walk Alone")
        return HttpResponseRedirect(reverse('main:show_main'))
```

Selanjutnya, dalam fungsi "create_product" di dalam file "views.py" di direktori "main", saya telah mengubah fungsinya agar dapat memproses data yang dikirim melalui formulir, mengaitkannya dengan pengguna yang saat ini telah login, serta menyimpannya ke dalam database. Setelah berhasil tersimpan, pengguna akan diarahkan ke halaman utama. Selain itu, dalam fungsi "show_main", saya telah memperbarui nilai konteks "nama" menjadi "request.user.username" untuk menggantikannya dengan nama pengguna yang sedang login. Selanjutnya, saya juga menambahkan baris kode "items = Item.objects.filter(user=request.user)" untuk hanya menampilkan data yang berasal dari pengguna yang saat ini telah login.

Terakhir, saya menjalankan proses migrasi untuk menyimpan perubahan data yang telah dilakukan.

### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

Di dalam file "models.py," saya telah membuat hubungan antara objek "item" dan objek "user" menggunakan relasi "foreign key." Ini dilakukan dengan menambahkan kode berikut:
```py
User = models.ForeignKey(User, on_delete=models.CASCADE)
```

Dalam konteks ini, "ForeignKey" digunakan untuk menghubungkan setiap objek "item" dengan pengguna yang membuatnya. Untuk menampilkan informasi tentang pengguna yang sedang login dalam aplikasi, saya telah mengubah fungsi "show_main." Saya mengganti nilai konteks "nama" menjadi "request.user.username" agar sesuai dengan pengguna yang saat ini login.

Untuk menampilkan data waktu terakhir login dalam aplikasi, saya pertama-tama mengimpor modul "datetime" di dalam file "views.py" di direktori "main." Lalu, saya memodifikasi bagian kode dalam fungsi "login_user" sebagai berikut:

```py
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

Selanjutnya, saya menambahkan konteks pada fungsi "show_main" dengan menambahkan:

```py
'last_login': last_login
```

dan untuk mendefinisikan variable last_login saya menambahkan kode:

```py
last_login = request.COOKIES.get('last_login', 'N/A')
```

Di dalam fungsi "logout_user," saya juga menambahkan baris kode berikut:

```py
"response = HttpResponseRedirect(reverse('main:login'))"
"response.delete_cookie('last_login')"
```

Hal ini dilakukan untuk menghapus data cookie pengguna yang baru saja logout.
Di dalam file "main.html," saya menggunakan konteks "last_login" dengan cara berikut:

```py
<h5>Last Login To Liverpool: {{ last_login }}</h5>
```

# TUGAS 5

## 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

Element selector CSS digunakan untuk memilih elemen HTML mana yang akan diubah style-nya.

### Type/Element Selector
Manfaat: Mengaplikasikan style ke semua elemen dengan jenis khusus.
Waktu yang tepat: Mengatur gaya default untuk elemen tertentu di seluruh halaman atau website. Misalnya, mengatur semua elemen <p> agar berwarna merah.

### Class Selector
Manfaat: Mengaplikasikan style ke semua elemen yang memiliki kelas tertentu.
Waktu yang tepat: Mengatur style khusus untuk sekelompok elemen tanpa mengubah elemen lain. Misalnya, beberapa elemen h2 akan berwarna merah hanya pada kelas "login", sementara h2 lainnya tetap dengan warna default.

### ID Selector
Manfaat: Mengaplikasikan style ke elemen yang memiliki ID tertentu.
Waktu yang tepat: Mengatur style khusus untuk elemen dengan ID tertentu yang unik.

### Universal Selector
Manfaat: Mengaplikasikan style ke seluruh elemen di file html.
Waktu yang tepat: Mengatur style yang akan dipakai di seluruh halaman html. Misalnya, semua font di halaman ingin diatur menjadi Verdana.

### Grouping Selector
Manfaat: Menggabungkan beberapa selector untuk menerapkan style yang sama.
Waktu yang tepat: ingin memberi style yang sama untuk beberapa elemen, agar tidak mengulang kode. Misalnya, <h1>,<h2>, dan <h3> ingin menerapkan background color yang sama.

### Descendant Selector
Manfaat: Mengaplikasikan style berdasarkan hubungan keturunan elemen.
Waktu yang tepat: Mengatur style untuk elemen yang berada di dalam elemen lain dan merupakan keturunan elemen tersebut.     


## 2. Jelaskan HTML5 Tag yang kamu ketahui.

<!DOCTYPE html> : Mendefinisikan tipe dokumen HTML
<a> : Mendefinisikan hyperlink/anchor
<body> : Mendefinisikan elemen "body"
<br> : Break line, elemen setelahnya akan berada di baris berikutnya
<th> : Mendefinisikan header tabel
<td> : Mendefinisikan data pada tabel
<tr> : Mendefinisikan row tabel
<header> : Mendefinisikan konten header atau navigasi.
<link> : Untuk memberi referensi sumber
<table> : Mendefinisikan table

## 3. Jelaskan perbedaan antara margin dan padding.

Margin adalah area yang terletak di luar batas elemen. Margin digunakan untuk mengatur jarak antara elemen tersebut dan elemen lainnya atau dinding kontainer. Margin dapat mempengaruhi tata letak elemen-elemen di sekitarnya, karena ia mengatur ruang di luar elemen.

Padding adalah area yang terletak di antara konten elemen dan batas elemen tersebut. Penggunaan padding adalah untuk mengatur jarak antara konten dan batas elemen, sehingga konten elemen akan terletak lebih jauh dari batas elemen tersebut. Warna latar belakang pada padding akan menyesuaikan dengan background color yang telah ditentukan.


## 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Bootstrap merupakan sebuah framework berorientasi komponen yang menyediakan sejumlah komponen desain yang telah tersedia, seperti tombol, kartu, navigasi, modals, dan berbagai elemen lainnya yang dapat digunakan dengan mudah. Penggunaan komponen-komponen tersebut dapat dilakukan secara langsung. Namun, untuk melakukan penyesuaian (customization) pada desain dengan Bootstrap, memerlukan upaya yang cukup besar karena harus mengubah banyak variabel agar sesuai dengan preferensi desain yang diinginkan. Bootstrap lebih baik digunakan untuk:
- Menginginkan solusi cepat dengan komponen siap pakai
- Pemula-friendly
- Proyek lebih berfokus pada backend

Tailwind adalah sebuah kerangka kerja (framework) yang berfokus pada penggunaan utilitas. Dalam Tailwind, pengembang diberikan kemampuan untuk dengan cepat membuat desain dengan menggunakan sejumlah kelas utilitas yang kecil, di mana setiap kelas mengontrol satu aspek spesifik dari desain, seperti margin, padding, warna, dan sebagainya. Keunggulan dari Tailwind adalah kemudahan dalam melakukan kustomisasi, karena ia memiliki tingkat fleksibilitas yang tinggi dan tidak mengikat pengembang pada gaya bawaan (default) dari kerangka kerja tersebut. Tailwind lebih baik digunakan untuk:
- Ingin design yang unik
- Menginginkan fleksibilitas yang lebih 
- Ingin mengurangi jumlah CSS kustom


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

### Login

```py
<style>
    .login-container {
        background-color: #FF0000;
        color: #FF0000;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    .login-box {
        background-color: #FFFFFF;
        color: #FF0000;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
    }

    .login h1 {
        font-size: 24px;
        color: #FF0000;
        margin-bottom: 20px;
    }

    .login table {
        width: 100%;
        max-width: 300px;
        margin: 0 auto;
    }

    .login input[type="text"],
    .login input[type="password"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        color: #FF0000;
        border: 1px solid #FF0000;
    }

    .login .login-btn {
        background-color: #FFC0CB;
        color: #FF0000;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .login .login-btn:hover {
        background-color: #FFB6C1;
    }
</style>
```

### Register

```py
<style>
    body {
        background-color: #FF0000;
        color: #FFFFFF;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        margin: 0;
        padding: 0;
    }

    .login {
        text-align: center;
        background-color: #FF0000;
        color: #FFFFFF;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        padding: 20px;
        width: 80%;
        max-width: 400px;
    }

    h1 {
        color: #FF0000;
    }

    table {
        width: 100%;
        margin-top: 20px;
    }

    input[type="text"],
    input[type="password"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        color: #FF0000;
        border: 1px solid #FF0000;
    }

    input[type="submit"] {
        background-color: #FFC0CB;
        color: #FF0000;
        padding: 15px 20px;
        border: none;
        border-radius: 20px;
        cursor: pointer;
    }

    input[type="submit"]:hover {
        background-color: #FFB6C1;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        color: #FFFFFF;
    }
</style>
```

### Create Product

```py
<style>
    body {
        background-color: red;
        margin: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }

    .center-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: white;
        border: 2px solid red;
        padding: 20px;
        border-radius: 10px;
    }

    h1 {
        color: red;
        text-align: center;
    }

    label {
        color: red;
    }

    input[type="text"], input[type="number"], textarea {
        border: 1px solid red;
        color: red;
    }

    input[type="submit"] {
        background-color: red;
        color: white;
        border: none;
        padding: 10px 20px;
        margin-top: 20px;
        border-radius: 5px;
        cursor: pointer;
    }
</style>
```

### Main

```py
<style>
    body {
        background-color: #FFC0CB;
        color: #FFFFFF;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        margin: 0;
        padding: 0;
    }

    .navbar {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
    }

    .navbar-text {
        color: #FF0000;
    }

    .container {
        text-align: center;
        padding: 20px;
        background-color: #FF0000;
        color: #FFFFFF;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        width: 70%;
        max-width:
        margin: 0 auto;
    }

    h1, h5 {
        color: #FFFFFF;
        padding: 10px;
    }

    .messages {
        margin-top: 20px;
    }

    .btn-container {
        display: flex;
        justify-content: space-between;
    }

    button {
        background-color: #FFFFFF;
        color: #FF0000;
        padding: 15px 20px;
        border: none;
        border-radius: 20px;
        cursor: pointer;
    }

    button:hover {
        background-color: #FFB6C1;
    }

    .btn-logout {
        background-color: #FF0000;
        color: #FFFFFF;
        padding: 10px 20px;
        border: none;
        border-radius: 20px;
        cursor: pointer;
        position: absolute;
        top: 10px;
        right: 10px;
    }
    

    .btn-logout:hover {
        background-color: #FF3333;
    }

    .card {
        background-color: #FFFFFF;
        color: #FF0000;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin: 0 auto;
        max-width: 300px;
        width: 100%;
        margin-bottom: 20px;
    }

    .card-img-top {
        width: 100%;
        height: auto;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }

    .card-body {
        text-align: center;
    }

    .card {
        background-color: #FFFFFF;
        color: #FF0000;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
        padding: 20px;
        width: 300PX;
    }

</style>
```

### Navbar

```py
<div class="container">
    <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container-fluid">
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <span class="navbar-text">
                            User: {{ name }}
                        </span>
                    </li>
                </ul>
            </div>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'main:logout' %}">
                        <button class="btn btn-logout">Logout</button>
                    </a>
                </li>
            </ul>
        </div>
    </nav>

```
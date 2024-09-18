Nama : Azzahra Salsabila
NPM : 2306219934
Kelas : PBP A

# TUGAS 2
* ***Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).***
Cara saya membuat proyek django baru adalah dengan:
  1. Membuat Proyek Django Baru
  Langkah: Membuat proyek Django baru di direktori terpisah dengan nama proyek **SeoulnSound**, dengan membuat folder proyek, mengaktifkan virtual environment, install Django, dan menjalankan server lokal untuk memastikan instalasi berjalan lancar.
  2. Membuat Aplikasi dengan Nama **main**
  Langkah: Di dalam proyek, saya membuat aplikasi dengan nama main dengan menggunakan perintah ```python manage.py startapp main``` dan menambahkan aplikasi ini ke INSTALLED_APPS di settings.py.
  3. Mengimplementasikan Template dasar
  Langkah: Membuat file HTML lalu diisi dengan atribut application name, self name, pbp class, product name, price, description dan rating.
  4. Membuat Model "Product" pada Aplikasi "main"
  Langkah: Membuat model Product dengan atribut application name, self name, pbp class, product name, price, description dan rating di models.py aplikasi main, lalu lakukan migrasi dengan ```makemigrations``` dan ```migrate```.
  5. Mengintegrasikan komponen MVT
  Langkah: Membuat fungsi di views.py dengan menggunakan render untuk mengembalikan template HTML dengan application name, self name, pbp class, product name, price, description dan rating.
  6. Membuat Routing di urls.py Aplikasi "main"
  Langkah: Menambahkan routing di urls.py aplikasi main untuk mengarahkan URL spesifik ke fungsi yang telah dibuat.
  7. Deployment ke Pacil Web Service (PWS)
  Langkah: Melakukan deploy proyek Django ke PWS agar dapat diakses oleh mahasiswa lain dengan mengikuti prosedur PWS untuk deployment, unggah perubahan ke server, dan memastikan aplikasi dapat diakses melalui internet.

* ***Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.***
![Bagan request client](https://github.com/user-attachments/assets/4283ae2a-6b46-443a-ae0d-3b341c2b8339)
User akan mengakses URL melalui internet lalu akan dilakukan HTTP Request yang akan diterima oleh urls.py, setelah itu urls.py akan mencocokkan URL dengan fungsi yang tepat di views.py. Kita menggunakan template yang akan ditampilkan di views.py, dan memanggil data yang diperlukan dari database melalui models.py, data-data ini diproses di views.py untuk menampilkan halaman yang sesuai.  Setelah itu, tampilan halaman ini dikirim kembali ke pengguna sebagai respons HTTP yang berisi kode HTML.

* ***Jelaskan fungsi git dalam pengembangan perangkat lunak!***
Git berguna sebagai alat kontrol sistem yang membantu dalam pelacakan setiap perubahan yang terjadi dalam proyek. Git bisa digunakan untuk bekerja sama dalam tim, kembali ke versi sebelumnya, menyimpan catatan perubahan, serta mengatur branch untuk pengembangan fitur tanpa mengganggu proyek utama atau proyek lain.

* ***Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?***
Django dipilih sebagai awal dalam pembelajaran pengembangan perangkat lunak karena menyederhanakan proses pengembangan dengan adanya fitur-fitur bawaan seperti autentikasi, ORM, dan manajemen admin. Django juga memiliki tata letak yang teratur dan mendukung pola MVC (Model-View-Controller) atau MVT (Model-View-Template), sehingga mempermudah pemahaman dasar pengembangan web. Selain itu, Django memiliki dokumentasi yang lengkap dan komunitas yang besar, sehingga memudahkan developer dalam mempelajari dan mengatasi masalah yang dihadapi.

* ***Mengapa model pada Django disebut sebagai ORM?***
Model di Django dinamakan sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara database dan kode Python. ORM membantu developer bekerja dengan database dengan menggunakan objek Python dibanding menggunakan query SQL secara langsung. Hal ini membuat manipulasi data menjadi lebih mudah tanpa harus memiliki pengetahuan yang mendalam tentang SQL, dan memastikan konsistensi dan efisiensi interaksi dengan berbagai jenis database.

---

# TUGAS 3
* ***Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?***
Data delivery diperlukan dalam pengimplementasian platform untuk memastikan data yang dikirimkan dari server ke client atau sebaliknya dapat diterima dengan baik. Data delivery memastikan data yang dikirimkan tidak hilang, tidak rusak, dan tidak terduplikasi, serta dapat diakses oleh pengguna dengan cepat dan aman. Data delivery juga memastikan data yang dikirimkan sesuai dengan format yang diinginkan oleh pengguna, sehingga dapat meningkatkan kualitas pengalaman pengguna dalam menggunakan platform.

* ***Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?***
Menurut saya, JSON lebih baik daripada XML karena JSON lebih ringan, mudah dibaca, dan mudah dipahami oleh manusia. JSON juga lebih efisien dalam penggunaan memori dan lebih cepat dalam proses parsing data. JSON juga lebih populer dibandingkan XML karena JSON lebih sederhana, lebih ringan, dan lebih mudah digunakan dalam pengembangan aplikasi web dan mobile, dan lebih fleksibel dalam penggunaan serta lebih mudah diintegrasikan dengan berbagai bahasa pemrograman.

* ***Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?***
Method ```is_valid()``` pada form Django digunakan untuk memvalidasi data yang dimasukkan oleh pengguna melalui form. Method ini memeriksa apakah data yang dimasukkan sesuai dengan aturan yang telah ditentukan dalam form. Kita membutuhkan method ```is_valid()``` untuk memastikan data yang dimasukkan oleh pengguna valid dan aman, sehingga dapat mencegah terjadinya serangan seperti SQL injection, XSS, dan CSRF. Method ```is_valid()``` juga membantu dalam mengurangi kesalahan input data dan memastikan data yang disimpan dalam database sesuai dengan format yang diinginkan.

* ***Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?***
Kita membutuhkan ```csrf_token``` saat membuat form di Django untuk mencegah serangan CSRF (Cross-Site Request Forgery) yang dapat membahayakan keamanan aplikasi web. CSRF adalah serangan yang memanfaatkan kepercayaan pengguna terhadap situs web yang sah untuk melakukan tindakan yang tidak diinginkan, seperti mengirimkan data palsu atau merusak data yang ada. Jika kita tidak menambahkan ```csrf_token``` pada form Django, maka form tersebut rentan terhadap serangan CSRF, di mana penyerang dapat memanfaatkan form tersebut untuk mengirimkan data palsu atau merusak data yang ada. Penyerang dapat memanfaatkan kelemahan ini untuk mencuri data pengguna, merusak data yang ada, atau mengubah data yang disimpan dalam database.

* ***Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).***
Cara saya mengimplementasikan checklist di atas adalah dengan:
1. Implementasi skeleton sebagai kerangka views
Langkah: Membuat skeleton sebagai kerangka views agar tidak terjadi redudancy pada kode dan agar tampilan pada website tetap konsisten.
2. Mengimport UUID
Langkah: Mengimport UUID untuk membuat unique identifier pada setiap data yang dimasukkan ke dalam database.
3. Membuat form input untuk menambahkan data
Langkah: Membuat file ```forms.py``` untuk membuat form input yang berisi product name, price, description, dan rating.
4. Membuat fungsi ```create_shop_entry```
Langkah: Lalu membuat fungsi ```create_shop_entry``` yang menerima request lalu menghasilkan form yang dapat menambahkan data yang telah diisi.
5. Membuat berkas ```create_shop_entry.html```
Langkah: Membuat berkas ```create_shop_entry.html``` sebagai template untuk menampilkan form input yang telah dibuat.
6. Mengembalikan data dalam bentuk XML, JSON, dan ID
Langkah: Pada ```views.py``` buat fungsi baru dengan nama ```show_xml, show_json, show_json_by_id, dan show_xml_by_id``` yang mengembalikan data dalam bentuk XML, JSON, dan ID. Lalu di tiap bentuk, tambahkan path url dalam ```urlpatterns``` dan melakukan import.
7. Menggunakan postman sebagai data viewer
Langkah: Menginstall postman lalu membuat request baru dengan menginput local host.

***Hasil screenshot dari hasil akses URL pada Postman***
1. XML
![alt text](image.png)
2. JSON
![alt text](image-1.png)
3. XML by ID
![alt text](image-2.png)
4. JSON by ID
![alt text](image-3.png)
Nama : Azzahra Salsabila

NPM : 2306219934

Kelas : PBP A

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

* ***Jelaskan fungsi git dalam pengembangan perangkat lunak!***
Git berguna sebagai alat kontrol sistem yang membantu dalam pelacakan setiap perubahan yang terjadi dalam proyek. Git bisa digunakan untuk bekerja sama dalam tim, kembali ke versi sebelumnya, menyimpan catatan perubahan, serta mengatur branch untuk pengembangan fitur tanpa mengganggu proyek utama atau proyek lain.

* ***Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?***
Django dipilih sebagai awal dalam pembelajaran pengembangan perangkat lunak karena menyederhanakan proses pengembangan dengan adanya fitur-fitur bawaan seperti autentikasi, ORM, dan manajemen admin. Django juga memiliki tata letak yang teratur dan mendukung pola MVC (Model-View-Controller) atau MVT (Model-View-Template), sehingga mempermudah pemahaman dasar pengembangan web. Selain itu, Django memiliki dokumentasi yang lengkap dan komunitas yang besar, sehingga memudahkan developer dalam mempelajari dan mengatasi masalah yang dihadapi.

* ***Mengapa model pada Django disebut sebagai ORM?***
Model di Django dinamakan sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara database dan kode Python. ORM membantu developer bekerja dengan database dengan menggunakan objek Python dibanding menggunakan query SQL secara langsung. Hal ini membuat manipulasi data menjadi lebih mudah tanpa harus memiliki pengetahuan yang mendalam tentang SQL, dan memastikan konsistensi dan efisiensi interaksi dengan berbagai jenis database.

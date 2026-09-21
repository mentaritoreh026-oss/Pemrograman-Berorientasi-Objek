<div align="center">

<h1>Pemrograman Berorientasi Objek</h1>

<img src="https://img.shields.io/badge/Property%20Visibility%20%26%20Enkapsulasi%20di%20Python-0d9488?style=for-the-badge" alt="subjudul" />

![Python](https://img.shields.io/badge/Python-3.12-14b8a6?style=for-the-badge&logo=python&logoColor=white)
![Topik](https://img.shields.io/badge/Topik-Enkapsulasi-0d9488?style=for-the-badge)
![Kelas](https://img.shields.io/badge/Kelas-B-2dd4bf?style=for-the-badge&labelColor=134e4a)
![Minggu](https://img.shields.io/badge/Praktikum-Minggu%205-5eead4?style=for-the-badge&labelColor=134e4a)

</div>

---

## 👩‍💻 Identitas

| Data | Keterangan |
|---|---|
| **Nama** | Mentari Kristen Rachaelea Toreh |
| **Kelas** | B |
| **Institusi** | Teknik Informatika, Universitas Sam Ratulangi |

## 📖 Deskripsi

Sistem sederhana untuk mengelola karyawan sebuah perusahaan dengan konsep **enkapsulasi**.

| Class | Fungsi |
|---|---|
| `Employee` | Menyimpan nama dan gaji karyawan |
| `Company` | Mengelola daftar karyawan |

Fitur enkapsulasi di dalam `Company`:

- 🔒 `self.__employees` adalah list private, tidak bisa diakses langsung dari luar class.
- ✅ `add_employee()` memakai `isinstance()` supaya hanya object `Employee` yang bisa masuk.
- 🔐 `__calculate_payroll()` adalah private method yang hanya dipanggil dari dalam class.

> [!NOTE]
> Python tidak punya keyword `private`. Awalan `__` bekerja lewat *name mangling*, sebagai pelindung dari akses tidak sengaja.

## ▶️ Cara menjalankan

```bash
python "Mentari Toreh_Kelas B.py"
```

## 🖥️ Contoh output

```
Tari berhasil ditambahkan.
Chelya berhasil ditambahkan.
Mentari berhasil ditambahkan.
Object yang dimasukkan bukan Employee!

Daftar Karyawan Tech Company
---------------------------
Nama: Tari
Gaji: Rp5,000,000
Nama: Chelya
Gaji: Rp4,500,000
Nama: Mentari
Gaji: Rp6,000,000
---------------------------
Total Payroll: Rp15,500,000
```

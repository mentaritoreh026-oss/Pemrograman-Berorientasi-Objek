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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 140" width="100%" preserveAspectRatio="none">
  <defs>
    <linearGradient id="g1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5eead4" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#5eead4" stop-opacity="0.15"/>
    </linearGradient>
    <linearGradient id="g2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#14b8a6" stop-opacity="0.65"/>
      <stop offset="1" stop-color="#14b8a6" stop-opacity="0.25"/>
    </linearGradient>
    <linearGradient id="g3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0d9488"/>
      <stop offset="1" stop-color="#115e59"/>
    </linearGradient>
  </defs>

  <g transform="translate(0,15)">
    <g>
      <animateTransform attributeName="transform" type="translate" from="0 0" to="-500 0" dur="14s" repeatCount="indefinite"/>
      <path fill="url(#g1)" d="M0 60 C83 30,167 30,250 60 S417 90,500 60 S667 30,750 60 S917 90,1000 60 S1167 30,1250 60 S1417 90,1500 60 S1667 30,1750 60 S1917 90,2000 60 V140 H0 Z"/>
    </g>
  </g>

  <g transform="translate(0,35)">
    <g>
      <animateTransform attributeName="transform" type="translate" from="-250 0" to="-750 0" dur="9s" repeatCount="indefinite"/>
      <path fill="url(#g2)" d="M0 60 C83 30,167 30,250 60 S417 90,500 60 S667 30,750 60 S917 90,1000 60 S1167 30,1250 60 S1417 90,1500 60 S1667 30,1750 60 S1917 90,2000 60 V140 H0 Z"/>
    </g>
  </g>

  <g transform="translate(0,55)">
    <g>
      <animateTransform attributeName="transform" type="translate" from="0 0" to="-500 0" dur="6s" repeatCount="indefinite"/>
      <path fill="url(#g3)" d="M0 60 C83 30,167 30,250 60 S417 90,500 60 S667 30,750 60 S917 90,1000 60 S1167 30,1250 60 S1417 90,1500 60 S1667 30,1750 60 S1917 90,2000 60 V140 H0 Z"/>
    </g>
  </g>
</svg>

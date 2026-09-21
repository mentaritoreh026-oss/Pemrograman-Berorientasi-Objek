# Pemrograman Berorientasi Objek

Tugas praktikum mandiri Minggu 5: **Property Visibility & Enkapsulasi di Python**.

**Nama:** Mentari Kristen Rachaelea Toreh
**Kelas:** B
**Institusi:** Teknik Informatika, Universitas Sam Ratulangi

## Deskripsi

Sistem sederhana untuk mengelola karyawan sebuah perusahaan dengan konsep enkapsulasi.

- `Employee`: menyimpan nama dan gaji karyawan.
- `Company`: mengelola daftar karyawan.
  - `self.__employees` adalah list private, tidak bisa diakses langsung dari luar class.
  - `add_employee()` memakai `isinstance()` supaya hanya object `Employee` yang bisa masuk.
  - `__calculate_payroll()` adalah private method yang hanya dipanggil dari dalam class.

## Cara menjalankan

```bash
python "Mentari Toreh_Kelas B.py"
```

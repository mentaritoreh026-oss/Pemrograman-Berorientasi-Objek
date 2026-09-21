class Employee:
    # class untuk merepresentasikan data seorang karyawan
    def __init__(self, name, salary):
        # menyimpan nama dan gaji ke dalam object Employee
        self.name = name
        self.salary = salary

    # method untuk menampilkan informasi karyawan
    def display_info(self):
        print(f"Nama: {self.name}")
        print(f"Gaji: Rp{self.salary:,}")


class Company:
    # class untuk mengelola data karyawan dalam sebuah perusahaan
    def __init__(self, name):
        self.name = name

        # private attribute: menyimpan kumpulan object Employee
        self.__employees = []

    # method untuk menambahkan employee ke dalam list
    def add_employee(self, employee):

        # validasi: memastikan object yang dimasukkan adalah instance dari Employee
        if isinstance(employee, Employee):

            # jika valid, object Employee dimasukkan ke dalam private list
            self.__employees.append(employee)

            print(f"{employee.name} berhasil ditambahkan.")

        # jika object bukan Employee, maka tidak dimasukkan ke list
        else:
            print("Object yang dimasukkan bukan Employee!")


    # private method untuk menghitung total gaji seluruh employee
    def __calculate_payroll(self):

        # variabel awal untuk menyimpan total gaji
        total = 0

        # mengambil setiap employee dari private list
        for employee in self.__employees:

            # menambahkan gaji setiap employee ke total payroll
            total += employee.salary

        # mengembalikan hasil total payroll
        return total


    # method untuk menampilkan seluruh data employee dan total payroll
    def show_employees(self):

        # menampilkan nama perusahaan
        print(f"\nDaftar Karyawan {self.name}")
        print("---------------------------")

        # menampilkan informasi setiap employee dalam list
        for employee in self.__employees:    #kemudian gajinya dijumlahkan satu per satu.
            employee.display_info()

        print("---------------------------")

        # memanggil private method untuk mendapatkan total payroll
        print(f"Total Payroll: Rp{self.__calculate_payroll():,}")


# membuat object Employee
employee1 = Employee("Tari", 5000000)
employee2 = Employee("Chelya", 4500000)
employee3 = Employee("Mentari", 6000000)


# membuat object Company
company = Company("Tech Company")


# menambahkan setiap object Employee ke dalam Company
company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)


# pengujian validasi dengan memasukkan object yang bukan Employee
company.add_employee("Budi")


# menampilkan seluruh data karyawan dan total payroll
company.show_employees()
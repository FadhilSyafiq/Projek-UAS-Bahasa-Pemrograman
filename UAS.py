# ===== Class Data =====
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


# ===== Class Process =====
class StudentProcess:
    def __init__(self):
        self.students = []

    def input_student(self):
        try:
            name = input("Masukkan nama mahasiswa: ")
            if not name.strip():
                raise ValueError("Nama tidak boleh kosong")

            score = float(input("Masukkan nilai (0 - 100): "))
            if score < 0 or score > 100:
                raise ValueError("Nilai harus antara 0 sampai 100")

            self.students.append(Student(name, score))
            print("Data berhasil ditambahkan!\n")

        except ValueError as e:
            print(f"Input tidak valid: {e}\n")

    def get_students(self):
        return self.students


# ===== Class View =====
class StudentView:
    def show_table(self, students):
        if not students:
            print("Belum ada data.")
            return

        print("\n+----+----------------------+-------+")
        print("| No | Nama                 | Nilai |")
        print("+----+----------------------+-------+")

        for i, student in enumerate(students, start=1):
            print(f"| {i:<2} | {student.name:<20} | {student.score:>5} |")

        print("+----+----------------------+-------+")


# ===== Main Program =====
def main():
    process = StudentProcess()
    view = StudentView()

    while True:
        print("=== Menu ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data")
        print("3. Keluar")

        choice = input("Pilih menu (1-3): ")

        if choice == "1":
            process.input_student()
        elif choice == "2":
            view.show_table(process.get_students())
        elif choice == "3":
            print("Program selesai.")
            break
        else:
            print("Menu tidak valid!\n")


if __name__ == "__main__":
    main()

class Manusia:
    def __init__(self, nama, umur, jenis_kelamin, pekerjaan, kewarganegaraan):
        self.nama = nama
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin
        self.pekerjaan = pekerjaan
        self.kewarganegaraan = kewarganegaraan
    
    def Info_KTP(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        print(f"Jenis Kelamin: {self.jenis_kelamin}")
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Kewarganegaraan: {self.kewarganegaraan}")

def main():
    print("\nMasukkan Data Diri Anda")
    print("--------------------------")
    nama = input("\nNama Lengkap: ")
    umur = int(input("Umur: "))
    jenis_kelamin = input("Jenis Kelamin: ")
    pekerjaan = input("Pekerjaan: ")
    kewarganegaraan = input("Kewarganegaraan: ")
     
    manusia = Manusia(nama, umur, jenis_kelamin, pekerjaan, kewarganegaraan)
    print("\nData berhasil disimpan!\n")

if __name__ == "__main__":
    main()
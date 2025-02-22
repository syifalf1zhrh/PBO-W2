class Pakaian:
    def __init__(self, jenis, merek, warna):
        self.jenis = jenis
        self.merek = merek
        self.warna = warna
    
    def info(self):
        print("Jenis: ", self.jenis, ",Merek: ", self.merek, ",Warna: ", self.warna)
    
Pakaian1 = Pakaian ("Baju", "Polo", "Navy")
Pakaian2 = Pakaian ("Celana", "Uniqlo", "Beige")
Pakaian3 = Pakaian ("Jilbab", "Lafiye", "Beige")

Pakaian1.info()
Pakaian2.info()
Pakaian3.info()
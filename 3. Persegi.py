class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi * self.sisi
    
    def kell(self):
        return 4*self.sisi

def main():
    sisi_persegi = float(input("\nMasukkan panjang sisi persegi: "))
    persegi = Persegi(sisi_persegi)
    print(f"\nLuas Persegi: {persegi.luas()}")
    print(f"\nKeliling Persegi: {persegi.kell()}")

if __name__=="__main__":
    main()

    
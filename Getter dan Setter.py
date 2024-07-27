class Orang:
    def __init__(self, nama, usia, pekerjaan):
        self._nama = nama
        self._usia = usia
        self._pekerjaan = pekerjaan

    def get_nama(self):
        return self._nama
    
    def set_nama(self, nama):
        self._nama = nama

    def get_usia(self):
        return self._usia
    
    def set_usia(self, usia):
        self._usia = usia 

    def get_pekerjaan(self):
        return self._pekerjaan
    
    def set_pekerjaan(self, pekerjaaan):
        self._pekerjaan = pekerjaaan

orang = Orang("Favian Agus", 30, "Buruh Pabrik")

print("Nama:", orang._nama)
print("Usia:", orang._usia)
print("Pekerjaan:", orang._pekerjaan)

orang.nama = "Putri Ammanda"
orang.usia = 28
orang.pekerjaan = "Desainer Baju"

print("Nama:", orang.nama)
print("Usia:", orang.usia)
print("Pekerjaan:", orang.pekerjaan)
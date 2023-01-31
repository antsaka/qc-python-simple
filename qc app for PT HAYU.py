print("QC PT HAYU")
print("QC KHUSUS JENIS BARANG NGAB, HUFT dan SAE")
print("----------------------------------")

i=0
Jenis=[]
NGAB=[]
SAE=[]
HUFT=[]
reject=[]

jumlah = int(input("Masukkan Jumlah Barang: "))
print("----------------------------------")

for i in range(jumlah):
    InputJenis = input("Masukkan Jenis Barang: ")
    if InputJenis == "NGAB":
        InputNGAB = float(input("Masukkan Dimensi Display NGAB: "))
        if 5.48<=InputNGAB<=5.58:
            print("Dimensi Display Sesuai Spesifikasi NGAB")
            NGAB.append(InputNGAB)
        else:
            print("Dimensi Display Tidak Sesuai Spesifikasi NGAB")
            reject.append(InputNGAB)
    elif InputJenis == "SAE":
        InputSAE = float(input("Masukkan Dimensi Display SAE: "))
        if 6.70<=InputSAE<=6.89:
            print("Dimensi Display Sesuai Spesifikasi SAE")
            SAE.append(InputSAE)
        else:
            print("Dimensi Display SAE Tidak Sesuai Spesifikasi SAE")
            reject.append(InputSAE)
        
    elif InputJenis == "HUFT":
        InputHUFT = float(input("Masukkan Dimensi Display HUFT: "))
        if 7.58<=InputHUFT<=7.69:
            print("Dimensi Display Sesuai Spesifikasi HUFT")
            HUFT.append(InputHUFT)
        else:
            print("Dimensi Display Tidak Sesuai Spesifikasi HUFT")
            reject.append(InputHUFT)
        
    else :
        print("Jenis Barang Tidak Ada")
        reject.append(InputJenis)
    Jenis.append(InputJenis)
    print("----------------------------------")

sumNGAB = len(NGAB)
sumSAE = len(SAE)
sumHUFT = len(HUFT)
sumREJECT = len(reject)
totalProduk = len(Jenis)

print("Jenis Barang: ",Jenis)
print("Produk NGAB Diterima: ", sumNGAB)
print("Produk HUFT Diterima: ", sumHUFT)
print("Produk SAE Diterima: ", sumSAE)
print("Produk Ditolak: ", sumREJECT)
print("----------------------------------")

diterima = (sumNGAB+sumSAE+sumHUFT) / totalProduk * 100
direject = sumREJECT / totalProduk * 100
if diterima >= 100:
    print("Semua Produk Diterima")
else:
    if diterima > 60:
        print("Sebagian diterima")
    else:
        print("Seluruh Komponen dikembalikan ke supplier")



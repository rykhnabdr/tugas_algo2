PERSENTASE_PAJAK = 0.2
PENGIRIMAN_FEE = 100

def hitung_pajak(jumlah_pembelian): 
    return jumlah_pembelian * PERSENTASE_PAJAK

def hitung_total_biaya(jumlah_pembelian):
     pajak = hitung_pajak(jumlah_pembelian) 
     return jumlah_pembelian + pajak + PENGIRIMAN_FEE

def main(): 
    print("Selamat datang di toko kami!") 
    jumlah_pembelian = float(input('Masukkan jumlah pembelian Anda: '))
    total_biaya = hitung_total_biaya(jumlah_pembelian) 
    print(f'Total biaya: {total_biaya}') 
    print("Terima kasih telah berbelanja di toko kami!")

if __name__ == '__main__': 
    main()


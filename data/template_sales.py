import pandas as pd
from datetime import datetime

# Template struktur kolom CSV
COLUMNS = [
    "Tanggal",
    "Kode Akun",
    "Deskripsi",
    "Debit",
    "Kredit",
    "Kuantitas",
    "SKU/Produk"
]

# Contoh data dummy untuk uji
DUMMY_DATA = [
    {
        "Tanggal": datetime.now().strftime("%Y-%m-%d"),
        "Kode Akun": "4100-01",
        "Deskripsi": "Penjualan Selimut Motif A ke Budi",
        "Debit": 500000,
        "Kredit": 450000,
        "Kuantitas": 5,
        "SKU/Produk": "Selimut Motif A"
    }
]

def export_sales_csv(data=DUMMY_DATA, filename="data/jurnal_penjualan.csv"):
    """Ekspor data ke CSV sesuai template"""
    df = pd.DataFrame(data, columns=COLUMNS)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"✅ File CSV berhasil dibuat: {filename}")

if __name__ == "__main__":
    export_sales_csv()

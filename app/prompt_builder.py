import json

def build_parsing_prompt(chat_text):
    """
    Membangun prompt untuk Gemini agar bisa mengonversi chat pelanggan
    menjadi data transaksi dalam format JSON yang rapi dan terstruktur.
    """

    # --- 🧩 Definisi Skema JSON ---
    json_schema = {
        "nama_pelanggan": "string",
        "alamat_kirim": "string",
        "items": [
            {
                "nama_produk": "string",
                "kuantitas": "integer",
                "harga_unit": "integer"
            }
        ],
        "subtotal": "integer",
        "ongkir": "integer",
        "total_pembayaran": "integer"
    }

    # --- 🎓 Contoh Few-Shot Learning ---

    # Contoh 1: Chat rapi dengan ongkir
    example_input_1 = (
        "Kak, pesan 5 Selimut Bunga (120rb/pc) dan 1 Bantal Polos (50rb). "
        "Total bayar ke Bpk. Agus Jl. Sudirman 100 Jakarta adalah 650.000, sudah termasuk ongkir 50rb."
    )
    example_output_1 = {
        "nama_pelanggan": "Bpk. Agus",
        "alamat_kirim": "Jl. Sudirman 100 Jakarta",
        "items": [
            {"nama_produk": "Selimut Bunga", "kuantitas": 5, "harga_unit": 120000},
            {"nama_produk": "Bantal Polos", "kuantitas": 1, "harga_unit": 50000}
        ],
        "subtotal": 600000,
        "ongkir": 50000,
        "total_pembayaran": 650000
    }

    # Contoh 2: Chat agak berantakan
    example_input_2 = (
        "Sist, jadi saya ambil 2 pcs yang warna hijau itu. Harga barangnya 400.000 ya? "
        "Kirimnya ke Fitri di rumah yang ada pohon besar. Ongkir 25 ribu. Transfer 425rb."
    )
    example_output_2 = {
        "nama_pelanggan": "Fitri",
        "alamat_kirim": "rumah yang ada pohon besar",
        "items": [
            {"nama_produk": "Produk Warna Hijau (Tidak Spesifik)", "kuantitas": 2, "harga_unit": 200000}
        ],
        "subtotal": 400000,
        "ongkir": 25000,
        "total_pembayaran": 425000
    }

    # --- 🧠 Prompt Utama ---
    prompt = f"""
Anda adalah **AI Data Parser Back-Office**.
Tugas Anda adalah mengekstrak *semua detail transaksi* dari teks chat pelanggan ke dalam format JSON **yang sesuai dengan skema berikut:**

{json.dumps(json_schema, indent=2)}

### Aturan Penting:
1. Gunakan nilai numerik murni tanpa tanda titik/koma.
2. Selalu pastikan total_pembayaran = subtotal + ongkir.
3. Jika data tidak disebutkan, isi dengan nilai 0 atau string kosong.
4. Jika nama produk ambigu, gunakan deskripsi terbaik yang mungkin.
5. Semua output HARUS berupa JSON valid tanpa komentar, tanpa teks tambahan.

### CONTOH 1 (Chat Rapi)
INPUT:
{example_input_1}

OUTPUT:
{json.dumps(example_output_1, ensure_ascii=False, indent=2)}

### CONTOH 2 (Chat Ambigu)
INPUT:
{example_input_2}

OUTPUT:
{json.dumps(example_output_2, ensure_ascii=False, indent=2)}

### TRANSAKSI YANG HARUS ANDA PARSING:
{chat_text}

Keluarkan hasil dalam **format JSON saja** sesuai struktur di atas.
Jangan tambahkan kata-kata lain di luar JSON.
    """

    return prompt

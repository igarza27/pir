#!/bin/bash

# Curl script to test AYVA API endpoints running at localhost:5000

# Test /parse endpoint with sample chat text
echo "Testing POST /parse"
curl -X POST http://127.0.0.1:5000/parse \
  -H "Content-Type: application/json" \
  -d '{"text":"Pesan contoh untuk pengujian parsing"}'
echo -e "\n"

# Test /stats endpoint
echo "Testing GET /stats"
curl http://127.0.0.1:5000/stats
echo -e "\n"

# Test /db/list endpoint
echo "Testing GET /db/list"
curl http://127.0.0.1:5000/db/list
echo -e "\n"

# Test /export_csv endpoint with sample cleaned data
echo "Testing POST /export_csv"
curl -X POST http://127.0.0.1:5000/export_csv \
  -H "Content-Type: application/json" \
  -d '[{
        "id_transaksi": "TX001",
        "nama_pelanggan": "John Doe",
        "alamat_kirim": "Jakarta",
        "items": [
          {
            "nama_produk": "Produk A",
            "kuantitas": 2,
            "harga_unit": 10000
          }
        ],
        "subtotal": 20000,
        "ongkir": 5000,
        "total_pembayaran": 25000,
        "tag_auto": ["pesanan baru"]
      }]'
echo -e "\n"

# Note: Download endpoint /download/<filename> cannot be tested reliably with curl without knowing filename returned from /export_csv

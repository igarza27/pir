from flask import Blueprint, request, jsonify
import pandas as pd
import os
from app.prompt_builder import build_parsing_prompt

routes = Blueprint('routes', __name__)

@routes.route('/api/parse', methods=['POST'])
def parse_transaction():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "Text is required"}), 400

        # 🔹 Panggil fungsi AI (sementara dummy dulu)
        ai_response = {
            "Tanggal": "2025-10-12",
            "Kode Akun": "4100-01",
            "Deskripsi": f"Penjualan berdasarkan input: {text}",
            "Debit": 500000,
            "Kredit": 450000,
            "Kuantitas": 5,
            "SKU/Produk": "Selimut Motif A"
        }

        df = pd.DataFrame([ai_response])
        output_path = os.path.join("data", "output_jurnal.csv")
        df.to_csv(output_path, index=False)

        return jsonify({
            "message": "Data berhasil diproses dan disimpan.",
            "output_file": output_path,
            "data": ai_response
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

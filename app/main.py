from flask import Flask, request, jsonify, render_template
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from app.prompt_builder import build_parsing_prompt

# --- Inisialisasi Flask ---
app = Flask(__name__)

# --- Load API Key dari .env ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY tidak ditemukan di file .env")

# --- Konfigurasi Gemini ---
genai.configure(api_key=API_KEY)

# --- Halaman utama (input chat) ---
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# --- Endpoint untuk parsing chat ---
@app.route('/parse', methods=['POST'])
def parse_chat():
    if request.is_json:
        data = request.get_json()
        chat_text = data.get('chat_input')
    else:
        chat_text = request.form.get('chat_input')

    if not chat_text or chat_text.strip() == "":
        return jsonify({"error": "⚠️ Input kosong"}), 400

    try:
        # 1️⃣ Buat prompt
        full_prompt = build_parsing_prompt(chat_text)

        # 2️⃣ Gunakan model Gemini terbaru (update di sini)
        model_name = "models/gemini-2.5-flash"  # bisa diganti ke gemini-2.5-pro jika ingin lebih cerdas
        model = genai.GenerativeModel(model_name)

        # 3️⃣ Kirim ke Gemini
        response = model.generate_content(full_prompt)

        # 4️⃣ Ambil hasil teks model
        output_text = response.text.strip()

        # 5️⃣ Coba parse JSON
        try:
            parsed_data = json.loads(output_text)
        except json.JSONDecodeError:
            parsed_data = {"raw_output": output_text}

        # 6️⃣ Tampilkan ke halaman hasil
        return render_template('results.html', data=parsed_data)

    except Exception as e:
        import traceback
        print("=== ERROR TRACEBACK ===")
        traceback.print_exc()
        print("=======================")

        return jsonify({
            "error": "Gagal memproses data dengan AI.",
            "detail": str(e)
        }), 500


# --- Jalankan Aplikasi ---
if __name__ == '__main__':
    app.run(debug=True)

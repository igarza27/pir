import google.generativeai as genai
from dotenv import load_dotenv
import os

# --- Load API key ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY tidak ditemukan di file .env")

genai.configure(api_key=API_KEY)

print("🔍 Mengecek daftar model yang tersedia...\n")

try:
    models = genai.list_models()

    for m in models:
        print(f"🧩 Model: {m.name}")
        if hasattr(m, "supported_generation_methods"):
            print(f"   ➜ Metode: {m.supported_generation_methods}")
        print("-" * 50)

except Exception as e:
    print("❌ Gagal mengambil daftar model:")
    print(str(e))

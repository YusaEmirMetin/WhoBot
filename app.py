import os
from google.genai import Client
from dotenv import load_dotenv

# 1. Ayarları ve API Anahtarını Yükle
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Gemini Client Yapılandırması
client = Client(api_key=api_key)

def kim_bu(isim):
    """Verilen isim hakkında Gemini'dan özet bilgi alır."""
    prompt = f"Sen bir Twitter botusun. Aşağıdaki kişi hakkında kısa, etkileyici ve maksimum 250 karakterlik bir özet bilgi ver: {isim}"
    
    try:
        # Model ismini başına 'models/' eklemeden, sadece isim olarak yazıyoruz
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Hata oluştu: {e}"

# --- VS CODE İÇİNDE TEST ---
if __name__ == "__main__":
    kullanici_sorgusu = input("Bilgi istediğin kişinin adını yaz: ")
    print("\n[WhoBot Araştırıyor...]\n")
    print(kim_bu(kullanici_sorgusu))
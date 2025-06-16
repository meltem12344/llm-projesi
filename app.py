import gradio as gr
import json
from transformers import pipeline

# JSON'dan veriyi yükle
with open("sorular.json", "r", encoding="utf-8") as f:
    kartlar = json.load(f)

# Açıklama üretecek küçük model
generator = pipeline("text2text-generation", model="google/flan-t5-small")

def kart_goster(index):
    sira = int(index.split(".")[0]) - 1  # "1. Python'da..." → 1 → 0. index
    kart = kartlar[sira]
    return kart["soru"], kart["cevap"], ""

def aciklama_getir(index):
    sira = int(index.split(".")[0]) - 1  # "1. Python'da..." → 1 → 0. index
    kart = kartlar[sira]
    prompt = (
        f"Give a short educational explanation for the following biology concept.\n"
        f"Question: {kart['soru']}\n"
        f"Answer: {kart['cevap']}"
    )
    sonuc = generator(prompt, max_new_tokens=40)[0]["generated_text"]
    return sonuc

# Arayüz
with gr.Blocks() as demo:
    gr.Markdown("## Soru-Cevap Kartları")
    dropdown = gr.Dropdown(choices=[f"{i+1}. {k['soru']}" for i, k in enumerate(kartlar)], label="Kart Seç")
    soru = gr.Textbox(label="Soru")
    cevap = gr.Textbox(label="Cevap")
    aciklama = gr.Textbox(label="Açıklama")

    goster_btn = gr.Button("Kartı Göster")
    aciklama_btn = gr.Button("Açıklama Ver")

    goster_btn.click(kart_goster, inputs=[dropdown], outputs=[soru, cevap, aciklama])
    aciklama_btn.click(aciklama_getir, inputs=[dropdown], outputs=[aciklama])

demo.launch()

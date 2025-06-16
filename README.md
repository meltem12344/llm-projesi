# llm-soru-cevap-kartlari

Bu proje, **Gradio** arayüzü ve **Transformers** kütüphanesi kullanarak etkileşimli bir şekilde soru-cevap kartları sunar. Kullanıcılar belirli bir soruyu seçip cevabını görebilir ve aynı zamanda LLM (Large Language Model) ile kısa bir açıklama talep edebilir.

9. sınıf biyoloji dersi gibi eğitim içeriklerinde kullanılabilecek **etkileşimli bir yapay zeka destekli soru-cevap kartları uygulamasıdır**. Kullanıcılar hazır kartları seçip yanıtlarını görebilir, ayrıca her bir kart için **LLM (Large Language Model)** desteğiyle **kısa ama anlamlı açıklamalar** alabilir.


---

##  Özellikler

- JSON formatında tanımlanmış soru-cevap verileri
- Kart seçme, cevabı gösterme ve açıklama üretme
- `flan-t5-small` modeli ile otomatik kısa açıklama üretimi
- Web arayüzü: Gradio ile kullanıcı dostu tasarım

---

##  Gereksinimler

```bash
pip install -r requirements.txt

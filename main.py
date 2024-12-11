from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load pre-trained model dan tokenizer
model_name = "t5-base"  # Model T5 dapat digunakan untuk tugas parafrase
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

def paraphrase(text):
    # Persiapkan input untuk model
    input_text = f"paraphrase: {text} </s>"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Hasilkan parafrase menggunakan model
    outputs = model.generate(input_ids, max_length=256, num_beams=5, early_stopping=True)

    # Decode hasil output dan kembalikan sebagai teks
    paraphrased_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return paraphrased_text

# Contoh penggunaan
input_text = "Ini adalah contoh kalimat yang ingin diparafrase."
paraphrased_text = paraphrase(input_text)
print("Original:", input_text)
print("Paraphrased:", paraphrased_text)

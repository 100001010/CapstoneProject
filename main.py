from transformers import pipeline

# 文字生成
generator = pipeline("text-generation", model="gpt2")

text = generator("Once upon a time", max_length=50, num_return_sequences=1)
print(text[0]['generated_text'])

from transformers import AutoModelForCausalLM, AutoTokenizer
import os

model_name = "gpt2"
save_directory = "./gpt2-model"

os.makedirs(save_directory, exist_ok=True)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

tokenizer.save_pretrained(save_directory)
model.save_pretrained(save_directory)
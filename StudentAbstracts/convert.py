import os
from docx import Document

input_dir = "./CocktailWord/"
output_dir = "./Cocktail/"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".docx"):
        doc = Document(os.path.join(input_dir, filename))
        text = "\n".join([para.text for para in doc.paragraphs])
        
        out_path = os.path.join(output_dir, filename.replace(".docx", ".txt"))
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)

print("Done!")
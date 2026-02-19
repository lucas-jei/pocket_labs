import os
from PIL import Image

input_folder = "input"
output_folder = "output"
width = 800

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith((".jpg",".png",".jpeg")):

        path = os.path.join(input_folder, file)
        img = Image.open(path)

        w, h = img.size
        height = int(h * (width / w))

        resized = img.resize((width, height), Image.LANCZOS)

        out_path = os.path.join(output_folder, file)
        resized.save(out_path)

print("완료")

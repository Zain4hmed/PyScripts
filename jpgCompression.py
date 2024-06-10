from PIL import Image
import os

def compress_images(source_folder, target_folder, quality=8):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img = Image.open(os.path.join(source_folder, filename))
            target_path = os.path.join(target_folder, filename)
            img.save(target_path, "JPEG", quality=quality)
            print(f"Compressed {filename} and saved to {target_path}")

source_folder = 'C:\\Users\\zaina\\htmlMocks\\imagesQuality'
target_folder = 'C:\\Users\\zaina\\htmlMocks\\images'

compress_images(source_folder, target_folder)

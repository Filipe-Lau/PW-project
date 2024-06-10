import zipfile
import os

def unzip_images(zip_path, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_extensions = ('.svg')

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename.lower().endswith(image_extensions):
                zip_ref.extract(file_info, output_folder)
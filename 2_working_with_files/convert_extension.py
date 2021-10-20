import os.path
from PIL import Image
import send2trash

images_directory = "example_files/image_files"
jpg_file_names = [file for file in os.listdir(images_directory) if
                  os.path.isfile(os.path.join(images_directory, file)) and file.endswith(".jpg")]

for jpg_file_name in jpg_file_names:
    img = Image.open(os.path.join(images_directory, jpg_file_name))
    image_name, image_extension = jpg_file_name.split(".")
    img.save(os.path.join(images_directory, f"{image_name}.png"))
    # safer than using os.remove - because if something went wrong, files can be retrieved from recycle bin
    send2trash.send2trash(os.path.join(images_directory, jpg_file_name))

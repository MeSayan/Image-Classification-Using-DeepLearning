import gdown
import zipfile
from shutil import unpack_archive

link = "https://drive.google.com/file/d/1ZgdqcGyUFATKelU_jdX2YXh6oTx7Tyhw/view?usp=sharing"
id = "1ZgdqcGyUFATKelU_jdX2YXh6oTx7Tyhw"
zip_file_name = "CL2_Assignment_8_Task_2_Part_1.zip"
extract_directory_name = "CL2_Assignment_8_Task_2_Part_1_Weights"

gdown.download(id=id, output=zip_file_name)
unpack_archive(zip_file_name, extract_directory_name)

import os
os.remove(zip_file_name)
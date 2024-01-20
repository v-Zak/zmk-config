import shutil
import zipfile
from pathlib import Path
import os

# simple script to upload firmware. No error handling!

# change to suit board and zip file location
left = "\\vee_board_left-nice_nano_v2-zmk.uf2"
right = "\\vee_board_right-nice_nano_v2-zmk.uf2"
zip_path = str(Path.home() / "Downloads//firmware.zip")
temp_path = str(Path.home() / "Downloads//zmk")

# no need to change the rest

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(temp_path)

left_path = temp_path + left
right_path = temp_path + right 

destination_path = "E:"

print(f"Input: {temp_path}\nOutput: {destination_path}\n")

# copy files to keyboard sides 
input("Reset left then press ENTER:")
shutil.copyfile(left_path, destination_path + left)
print("Left uploaded")
input("Reset right then press ENTER:")
shutil.copyfile(right_path, destination_path + right)
print("Right uploaded")

delete = input("Press ENTER to delete input: ").lower()

if delete == "":
    Path.unlink(zip_path)
    shutil.rmtree(temp_path)
    print("Input deleted")
else:
    shutil.rmtree(temp_path)
    print("Input retained")


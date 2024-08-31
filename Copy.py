import os
import shutil

folder_zrodlowy = os.path.dirname(os.path.abspath(__file__))
folder_docelowy = r"" #Target path

os.makedirs(folder_docelowy, exist_ok=True)

for filename in os.listdir(folder_zrodlowy):
    if filename == os.path.basename(__file__):
        continue

    zrodlo = os.path.join(folder_zrodlowy, filename)

    cel = os.path.join(folder_docelowy, filename)

    if os.path.isfile(zrodlo):
        shutil.copy2(zrodlo, cel)
    elif os.path.isdir(zrodlo):
        shutil.copytree(zrodlo, cel)
from PIL import Image
import os
from PyPDF2 import PdfFileMerger
from datetime import datetime
import subprocess

# variables
directory = 'pre'
merger = PdfFileMerger()
has_files = False

# loop through all jpgs
for file in os.listdir(directory):
    # set has files for not stopping later on
    has_files = True
    # all paths
    save_path = directory + '/' + file.replace('.JPG', '.pdf')
    og_path = directory + '/' + file

    # read and convert jpg to pdf
    Image.open(og_path).convert('RGB').save(save_path)
    # add to merger
    merger.append(save_path)
    # delete og jpg file
    os.remove(og_path)

if has_files:
    # merge and write
    stamp = datetime.now().strftime('%m%d%Y_%H%M%S')
    merger.write('final/' + stamp + '.pdf')
    merger.close()

    # delete the preprocessed files
    for file in os.listdir(directory):
        os.remove(directory + '/' + file)

    # open the windows file explorer at result directory
    subprocess.Popen(r'explorer /select,"D:\files\scan\final\ok"')

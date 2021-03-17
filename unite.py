"""
convert jpgs to pdfs and compose one single pdf in the end
then clear pre folder
"""

from PIL import Image
import os
import subprocess
import utils
from fpdf import FPDF

# variables
directory = 'pre'
merger = FPDF()
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
    merger.add_page()
    merger.image(save_path, 0, 0, 210, 297)
    # delete og jpg file
    os.remove(og_path)

if has_files:
    # merge and write
    merger.output('final/' + utils.stamp() + '.pdf', 'F')
    merger.close()

    # delete the preprocessed files
    for file in os.listdir(directory):
        os.remove(directory + '/' + file)

    # open the windows file explorer at result directory
    subprocess.Popen(r'explorer /select,"D:\files\scan\final\ok"')

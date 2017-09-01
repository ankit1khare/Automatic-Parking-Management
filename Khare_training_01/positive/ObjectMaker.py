#
import sys
import os
from PIL import Image

input_directory = os.getcwd() + "\\rawdata"
output_file = os.getcwd() + "\\info.txt"

# Get a file listing of all files within the input directory
try:
    files = os.listdir(input_directory)
except OSError:
    sys.stderr.write("Failed to open directory %s\n" % input_directory)
    exit(0)

files.sort()
str_prefix = "rawdata/"

try:
    output = open(output_file, "r+")
except IOError:
    sys.stderr.write("Failed to open file %s.\n" % output_file)
    exit(0)

for file in files:
    img = str_prefix + file
    current_img = Image.open(img)
    width, height = current_img.size
    output.write(img + " " + str(1) + " " + str(1) + " " + str(1) + " " + str(width) + " " + str(height) + "\n")

output.close()

import os
import glob

images = glob.glob('*.jpeg')        # path of file to be converted
for image in images:
    file_name = image[:-4]          # to get the file_name without extension
    pngfile = file_name + 'png'     # naming file as png
    os.system('convert ' + image + ' ' + pngfile)       # converting file to png type
    jpgfile = file_name + 'jpg'
    os.system('convert ' + image + ' ' + jpgfile)       # converting file to jpg type

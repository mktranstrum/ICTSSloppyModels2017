#!/usr/bin/env python
'''
File: autorotate.py
Author: Damien Riquet <d.riquet@gmail.com>
Description: This script provides an auto-rotate feature of pictures based on Exif data
http://www.lifl.fr/~damien.riquet/auto-rotating-pictures-using-pil.html
3/6/2016: Added expand kwarg to image.rotate - mkt
'''

import os, re, argparse
from PIL import Image

picture_re = re.compile(r'.*\.jpg$', re.IGNORECASE)

def autorotate(path):
    """ This function autorotates a picture """
    image = Image.open(path)
    exif = image._getexif()
    if not exif:
        return False

    orientation_key = 274 # cf ExifTags
    if orientation_key in exif:
        orientation = exif[orientation_key]

        rotate_values = {
            3: 180,
            6: 270,
            8: 90
        }

        if orientation in rotate_values:
            # Rotate and save the picture
            image = image.rotate(rotate_values[orientation], expand = True)
            image.save(path, quality=100)
            return True

    return False


def process_directory(path, recursive=False):
    """ This function processes all elements from a directory """
    if not os.path.isdir(path):
        print path, 'is not a directory'

    else:
        for elt in os.listdir(path):
            elt_path = os.path.join(path, elt)
            if os.path.isdir(elt_path) and recursive:
                process_directory(elt_path, recursive)

            elif os.path.isfile(elt_path):
                if re.match(picture_re, elt_path):
                    if autorotate(elt_path):
                        print 'autorotate: %s/%s' % (path, elt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', nargs='+')
    parser.add_argument('--recursive', '-r', action='store_true')
    args = parser.parse_args()

    for directory in args.directory:
        process_directory(directory, args.recursive)

#
# Vojtovo utility
# Ruzne uzitecne funkce, ktere stale se opakujici problemy
#
import os
from termcolor import colored  # https://pypi.org/project/termcolor/


# @todo Zrusit a Pouzivat misto toho  os.makedirs()
def mymkdir(*folders):
    """
    Makes folder(s) if not exist
    """
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)


def red(value):
    return colored(value, 'red')


def green(value):
    return colored(value, 'green')


def yellow(value):
    return colored(value, 'yellow')


def cyan(value):
    return colored(value, 'cyan')


def blue(value):
    return colored(value, 'blue')


# Detect top-left pixel color
def get_background_color(img):
    pixdata = img.load()
    return pixdata[0, 0]


# If image has correct background, return array of brightness
# If not, returns False
def has_correct_background(img, background_config):
    try:
        line_width = background_config['line_width']
        width, height = img.size
        sensor_crops = {
            'top':    img.crop((0, 0, width - 1, line_width)),
            'left':   img.crop((0, 0, line_width, height - 1)),
            'right':  img.crop((width - 1 - line_width, 0, width - 1, height - 1)),
            'bottom': img.crop((0, height - 1 - line_width, width - 1, height - 1)),
        }

        result = {}

        for key, sensor in background_config['sensors'].items():
            brightness_range = range(sensor[0], sensor[1] + 1)
            pixel = sensor_crops[key].resize((1, 1)).load()[0, 0]
            pixel_brightness = int((pixel[0] + pixel[1] + pixel[2]) / 3)  # RGB average
            result[key] = pixel_brightness
            # print(green(key), cyan("pixel_brightness:"), pixel_brightness, cyan("brightness_range:"), brightness_range)

            if pixel_brightness not in brightness_range:
                # print(red("Zamitam:"), cyan(pixel), "\n")
                return False

    except Exception as e:
        print(red(Exception), e.args, e)
        return False

    print(green(key), result)
    return result

#
# @todo Nakonec asi nebudeme pouzivat. Zdrzuje o a nemame pro to vyuziti.
# Nechavam jen pro zajimavost, kdyz uz to funguje
#
# from libxmp import XMPFiles, consts, XMPMeta
# def update_xmp(image):
#     return
#     print(cyan("- Updating XMP"))
#     rating = ceil(image['rank'] / (max_rank / 5))
#     try:
#         xmpfile = XMPFiles(file_path=image['local_file'], open_forupdate=True)
#         xmp = XMPMeta()  # Clear new xmp
#         xmp.set_property_int(consts.XMP_NS_XMP, u'Rating', rating)
#         xmp.set_property(consts.XMP_NS_XMP, u'Source', image['url'])
#         xmp.set_property(consts.XMP_NS_DC, u'Title', image['name'])
#         xmp.set_property(consts.XMP_NS_DC, u'Subject', image['category'])
#         xmp.set_property(consts.XMP_NS_DC, u'Identifier', image['image_id'])
#         xmpfile.put_xmp(xmp)
#         xmpfile.close_file()
#     except Exception as e:
#         print(red("- Updating XMP FAILED!"), e)

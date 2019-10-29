import os
from PIL import Image

image_extensions = ['jpg', 'jpeg']


def get_pictures():
    pictures = []
    for root, subfolders, files in os.walk(os.getcwd()):
        for file in files:
            if file.split('.')[-1] in image_extensions:
                pictures.append(os.path.join(root, file))
    return pictures


def get_pictures_size(image):
    print("Current working dir : %s" % os.getcwd())

    for i in image:
        with Image.open(i) as img:
            width, height = img.size
            img = img.resize((560, 300))
            img.save(i, optimize=True, quality=80)
        print('Размер {} байт, ширина {}, высота {}, {}'.format(os.stat(i).st_size, width, height,
                                                                i.split('/')[-1]))


if __name__ == '__main__':
    get_pictures_size(get_pictures())


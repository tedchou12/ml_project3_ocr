from PIL import Image
import glob

# counter = 1
mode = 'training'

for file in glob.glob('./' + mode + '/unprocessed/*.jpg') :
    path_parts = file.split('/')
    # name = path_parts[-1].split('.')
    name = path_parts[-1]

    im = Image.open(file)
    # im_crop0 = im.crop((3, 0, 15, 25))
    im.convert('L').save(mode + '/processed/' + str(name), quality=95)
    # counter = counter + 1

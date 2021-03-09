from PIL import Image
import glob


# counter = 1
mode = 'training'

for file in glob.glob('./' + mode + '/processed/*.jpg') :
    path_parts = file.split('/')
    name_parts = path_parts[-1].split('.')
    name = name_parts[0]

    window = 0
    while window < 176 :
        window_size = 25
        frame_x1 = window
        frame_x2 = window + window_size
        window_name = name + '_' + str(frame_x1) + '_' + str(frame_x2) + '.jpg'
        # print(window_name)

        im = Image.open(file)
        im_crop = im.crop((frame_x1, 0, frame_x2, 50))
        im_crop.convert('L').save(mode + '/split/' + str(window_name), quality=95)

        window = window + 10

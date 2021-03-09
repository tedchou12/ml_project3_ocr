from PIL import Image
import glob
from natsort import natsorted


mode = 'training'
matrix = []

files = []
for file in glob.glob('./' + mode + '/split/*.jpg') :
    files.append(file)

files = natsorted(files)


for file in files :
    im = Image.open(file)
    px = im.load()

    row = []
    i = 0
    j = 0
    for i in range(0, 25) :
        for j in range(0, 50) :
            hex = str(px[i, j])
            # parts = hex.replace('(', '').replace(')', '').split(',')
            # hex = parts[0]
            row.append(hex)

    matrix.append(','.join(row))

matrix_string = '\n'.join(matrix)

handle = open(mode + '/matrix/data.txt', 'w')
handle.write(matrix_string)
handle.close()

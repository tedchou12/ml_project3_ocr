import requests
import random
from PIL import Image
import os
import numpy as np


file = open('pipeline2_image_present/theta.txt', 'r')
theta1 = file.readlines()
file.close()

theta_1 = []
for row in theta1 :
    row = row.replace('\n', '')
    theta_1.append(float(row))

file = open('pipeline3_digit_ocr/theta.txt', 'r')
theta2 = file.readlines()
file.close()

theta_2 = []
for row in theta2 :
    row = row.replace('\n', '')
    row_vals = row.split(' ')
    row_processed = []
    for row_val in row_vals :
        if row_val != '' :
            row_processed.append(float(row_val))

    theta_2.append(row_processed)

temp = 1

file_path = 'data/' + str(temp) + '.jpg'

with open(file_path, 'wb') as handle :
    response = requests.get('https://www.chief070.com.tw/verify_code.aspx', stream=True)

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)

if os.path.exists(file_path) :
    im = Image.open(file_path)
    im.convert('L').save(file_path, quality=95)

    path_parts = file_path.split('/')
    name_parts = path_parts[-1].split('.')
    name = name_parts[0]

    window = 0
    while window < 176 :
        window_size = 25
        frame_x1 = window
        frame_x2 = window + window_size
        window_name = name + '_' + str(frame_x1) + '_' + str(frame_x2) + '.jpg'

        im = Image.open(file_path)
        im_crop = im.crop((frame_x1, 0, frame_x2, 50))
        im_crop.convert('L').save('data/split/' + str(window_name), quality=95)

        window = window + 10

        im = Image.open('data/split/' + str(window_name))
        px = im.load()

        matrix = [0]
        i = 0
        j = 0
        for i in range(0, 25) :
            for j in range(0, 50) :
                hex = str(px[i, j])
                matrix.append(int(hex))

        # print(window_name)
        if np.dot(theta_1, matrix) > 0 :
            predict_matrix = list(np.dot(theta_2, matrix))
            val = predict_matrix.index(max(predict_matrix))
            print('predict:' + str(val + 1) + ', certainty: ' + str(max(predict_matrix)) + ', present: ' + str(np.dot(theta_1, matrix)))

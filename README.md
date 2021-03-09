# ml_project3_ocr
Machine Learning classification (Logistic Regression) with Sliding Window
Application written for Machine Learning OCR. App written to defeat Verification Codes on https://www.chief070.com.tw/member/apply/register.aspx.

![website](https://user-images.githubusercontent.com/10494709/110477460-87156a00-8126-11eb-820e-14a2bc4ede98.png)

# Pipeline 1 Get Data
1. Collecting captcha from https://www.chief070.com.tw/verify_code.aspx and download all the codes.
2. Split 200 x 50 image into window frame size of 25 x 50 sizes, move window by 10. Greyscale 0-255.
3. Generated 18 images for each 200 x 50 image.
![greyscale splitted](https://user-images.githubusercontent.com/10494709/110477722-db204e80-8126-11eb-8f6b-92c7186ba314.jpg)

# Pipeline 2 
Using LR to determine if digit is in the center of the file or is recognizable.
1 if is recognizable or in the center, 0 if the digit is not present or unrecognizable.

# Pipleline 3
Train digit in the frame from 0-9. (0 as 10)

# Test
`ml_1_sliding_window.py` will use theta1 and theta 2 from Pipeline 2 and Pipeline 3 to predict the digits.
Because the digits are not as neat and can be at different places, the accuracy is lower, but there is about 2/10 to 3/10 of getting all the digits correct.
![result](https://user-images.githubusercontent.com/10494709/110478194-7285a180-8127-11eb-811f-9ca4b7451461.png)

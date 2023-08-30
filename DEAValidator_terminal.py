import easyocr
import cv2
import numpy as np
import re

IMAGE_PATH = input(r'Please enter image path: ')
print('Extracting potential DEA number from ' + str(IMAGE_PATH))

reader = easyocr.Reader(['en'], gpu=False)

result = reader.readtext(IMAGE_PATH)
OCRtext = []

for OCR_ITEM in result:
    OCRtext.append(OCR_ITEM[1])

#check for valid DEA number format with a regex
DEA_FORMAT = r'[ABCDEFGHJKLMPRSTUX]+[A-Z]{1}\d{7}'
IS_DEA_FORMAT = []
for ID in OCRtext:
    UNCHECKED_DEA = re.findall(DEA_FORMAT, ID)
    IS_DEA_FORMAT.extend(UNCHECKED_DEA)
print(f'Found potential DEA#:')
if IS_DEA_FORMAT == []:
        print('None found')
else:
    for num in IS_DEA_FORMAT:
        print(num)

    

#validates each DEA number
IS_VALID_DEA = []
for DEA_NUMBER in IS_DEA_FORMAT:
    # calculates sum of digits 1, 3 and 5 
    CALC1_3_5 = sum(int(DEA_NUMBER[i]) for i in [2, 4, 6])
    
    #calculates sum of digits 2, 4 and 6, multiplied by 2
    CALC2_4_6 = 2*sum(int(DEA_NUMBER[i]) for i in [3, 5, 7])
    
    #sum of both values
    CHECK = CALC1_3_5 + CALC2_4_6
    
    #isolate the last digit of the sum
    check_lastdigit = CHECK % 10
    dea_lastdigit = int(DEA_NUMBER[-1])
   
    #compares last digit of sum to checksum
    if dea_lastdigit == check_lastdigit:
        IS_VALID_DEA.append(DEA_NUMBER)

if IS_VALID_DEA == []:
    pass
else:
    print('\nValidated DEA #:')
    for num in IS_VALID_DEA:
        print(num)
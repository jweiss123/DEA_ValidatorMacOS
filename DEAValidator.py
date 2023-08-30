from tkinter import *
# initializing tkinter
root = Tk()
# setting geometry
root.geometry('350x350')
# setting title
root.title('DEA Validation')

def DEAvalidator():
    import os
    import easyocr
    import cv2
    import numpy as np
    import re
    try:
        # updating root
        root.update()
        # getting countries names entered by the user
        IMAGE_PATH = user_input.get()
        DEA_FORMAT = r'[ABCDEFGHJKLMPRSTUX]+[A-Z]{1}\d{7}'
        IS_DEA_FORMAT = []
        if os.path.isfile(IMAGE_PATH):
            OCRtext = []
            reader = easyocr.Reader(['en'], gpu=False)
            result = reader.readtext(IMAGE_PATH)
            for OCR_ITEM in result:
                OCRtext.append(OCR_ITEM[1])

            #check for valid DEA number format with a regex
            
            for ID in OCRtext:
                UNCHECKED_DEA = re.findall(DEA_FORMAT, ID)
                IS_DEA_FORMAT.extend(UNCHECKED_DEA)
        else:
            UNCHECKED_DEA = re.findall(DEA_FORMAT, IMAGE_PATH)
            IS_DEA_FORMAT.extend(UNCHECKED_DEA)
            print(IS_DEA_FORMAT)


        print(f'Found potential DEA#:')
        if IS_DEA_FORMAT == []:
                print('None found')
        else:
            for num in IS_DEA_FORMAT:
                print(num)

        #validates each DEA number
        IS_VALID_DEA = []
        IS_NOT_VALID_DEA = []
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
            else:
                IS_NOT_VALID_DEA.append(DEA_NUMBER)


        
        if IS_VALID_DEA == [] and IS_DEA_FORMAT != []:
            for invalid_dea in IS_NOT_VALID_DEA:
                result_text.insert('end', f'{invalid_dea} ')
                result_text.tag_configure('invalid_tag', foreground='red')
                result_text.insert('end-2c', ' INVALID', 'invalid_tag')
                result_text.insert('end-1c', '\n')
        elif IS_VALID_DEA == []:
            result_text.insert('end', 'No DEA number found.\n')
        else:
            for valid_dea in IS_VALID_DEA:
                result_text.insert('end', f'{valid_dea} ')
                result_text.tag_configure('valid_tag', foreground='green')
                result_text.insert('end-2c', ' VALID', 'valid_tag')
                result_text.insert('end-1c', '\n')
            for invalid_dea in IS_NOT_VALID_DEA:
                result_text.insert('end', f'{invalid_dea} ')
                result_text.tag_configure('invalid_tag', foreground='red')
                result_text.insert('end-2c', ' INVALID', 'invalid_tag')
                result_text.insert('end-1c', '\n')

    except Exception as e:
        result_text.delete(1.0, 'end')  # Clear the text widget
        result_text.insert('end', 'An error occurred. Please enter correct details again.')


#input GUI
Label(root, text='DEA VALIDATION', font='Consolas 15 bold').pack()
Label(root, text='Input source image path OR directly enter DEA#: ').pack()
user_input = StringVar()
user_input.set('Insert Image Path or DEA #')
entry = Entry(root, textvariable=user_input, width=50).pack()
Button(root, text='Validate', command=DEAvalidator).pack()

# Text widget to display results
result_text = Text(root, wrap='word', height=10, width=20)  # Specify height and width
result_text.pack()

root.mainloop()

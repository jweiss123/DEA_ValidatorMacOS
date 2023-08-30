# DEA-Validator 1.0
https://web.archive.org/web/20170120164502/https://www.deadiversion.usdoj.gov/faq/general.htm#sec-2

*A DEA number (DEA Registration Number) is an identifier assigned to a health care provider (such as a physician, physician assistant, nurse practitioner, optometrist, podiatrist, dentist, or veterinarian) by the United States Drug Enforcement Administration allowing them to write prescriptions for controlled substances. DEA registration numbers are generally used for authenticating and tracking prescriptions for controlled substances.*

This program aims to expedite the verification process for pharmacists who receive hard copies of C-II through C-V prescriptions by using optical character recognition (OCR). 

[MacOS Version](https://github.com/jweiss123/DEA-Validator/tree/MacOS)

[Windows Version](https://github.com/jweiss123/DEA-Validator/tree/Windows)

### 1.1 INTRODUCTION

This program allows the user to input a DEA number via one of the following methods to validate its legitimacy:

1) An image as a file path using EasyOCR 
   - The image can have multiple DEA numbers as long as they are legible
   - As of August 2023, EasyOCR can not interpret handwritten text (yet) 
2) A direct DEA number 
   - Only one DEA number can be input at a time
   - Must use the following format with no additional characters: "AB1234567"
   - Can input an additional DEA number after clicking "Validate"

*Note: Use DEAValidator_terminal.py for a terminal only version. This version can only interpret image files and not direct input.

--------------------------------------------

### 1.2 DEPENDENCIES

BEFORE running the program, be sure to install the following dependencies either manually or via **_run.sh_**:

1) PYTORCH (https://pytorch.org)
   - copy/paste into terminal (verify correct version on website first):
      - MacOS: **pip3 install torch torchvision torchaudio**
      - Windows: **pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117**

2) EASYOCR (https://pypi.org/project/easyocr/)
   - copy/paste into terminal:
      - **pip install easyocr**

3) PILLOW 9.5.0
   - copy/paste into terminal:
      - **pip uninstall Pillow**
      - **pip install Pillow==9.5.0**

To uninstall these dependencies, simply run **_uninstall.sh_**

--------------------------------------------

### 1.3 TERMS OF USE

GNU Affero General Public License v3.0

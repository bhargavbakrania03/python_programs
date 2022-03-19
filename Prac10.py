"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK : https://github.com/bhargavbakrania03/python_programs/blob/main/Prac10.py
"""

from PIL import Image

# Opening the Image from its path
img = Image.open(r'D:\4RTH SEM\CE259 PIP\PRACTICALS\PRACTICAL SCREENSHOTS\3rd Semester Marksheet.jpg')

# Converting the opened image into pdf file
image_ms = img.convert('RGB')

# Saving the generated pdf file at specified address
image_ms.save(r'D:\4RTH SEM\CE259 PIP\PRACTICALS\Prac10.pdf')


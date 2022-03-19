"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK :
"""

from PIL import Image

# Path for your image where it is
img = Image.open(r'D:\4RTH SEM\CE259 PIP\PRACTICALS\PRACTICAL SCREENSHOTS\3rd Semester Marksheet.jpg')

# Converting it into pdf
image_ms = img.convert('RGB')

# Path where your PDF file will be saved
image_ms.save(r'D:\4RTH SEM\CE259 PIP\PRACTICALS\Prac10.pdf')


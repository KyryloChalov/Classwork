from rembg import remove
from PIL import Image
# input_path = '20230620_091912.jpg'
# input_path = '6_5x9_2_1.png'
input_path = '6x9_c.png'
output_path = 'output.png'
inp = Image.open(input_path)
inp.show()
# display(inp)
output = remove(inp)
output.show()
output.save(output_path)
# Image.open(output_path)
# Image.open('620230620_091912__.jpg')
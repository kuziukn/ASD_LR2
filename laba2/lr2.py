from PIL import Image
from PIL import ImageDraw

file = open('DS2.txt')
	
back = Image.new('RGB', (540, 960), '#000000')
front = ImageDraw.Draw(back)

for line in file.readlines():
	A = line.split()
	front.point((float(A[0]), float(A[1])), '#ff0000')
back.save('img.png')
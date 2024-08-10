from os import listdir as ls
from jpg_n_classes import JPGFile

valid_files = ls("setters_images")
valid_format = (500, 747) 	# If this isn't a suitable resolution for ur images change it... it should be a tuple (100, 999)
files_to_analize = ls("lab_images") # Extend this later... first fix valid images to get the average on the matrix of every file

### Current supported type
for files in valid_files:
	if not files.endswith(".jpeg"):
		raise Exception(f"Invalid file in the directory - '{files}'")

valid_files = ls("setters_images")
valid_format = (500, 747) 	# Change later...should be a tuple

for i in valid_files:
	potinga = JPGFile(i, valid_files, valid_format)
	matriz = potinga.to_matrix()
	print(matriz)
	Image.fromarray(matriz).save("hola.png")
	

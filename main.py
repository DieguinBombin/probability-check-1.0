from os import listdir as ls
from jpg_n_classes import JPGFile, MatrixMeanList

valid_files = ls("setters_images")
valid_format = (500, 747) 	# If this isn't a suitable resolution for ur images change it... it should be a tuple (100, 999)
files_to_analize = ls("lab_images") # Extend this later... first fix valid images to get the average on the matrix of every file

### Current supported type
for files in valid_files:
	if not files.endswith(".jpeg"):
		raise Exception(f"Invalid file in the directory - '{files}'")

valid_files = ls("setters_images")
valid_format = (500, 747) 	# Change later...should be a tuple

matrices = list()

for i in valid_files:
	current_image = JPGFile(i, valid_files, valid_format)
	print(current_image)
	current_image.save(f"transformed/{i}_transformed") # CAMBIAR
	matrices.append(current_image.matrix_list)

a = MatrixMeanList(matrices, valid_format).get_mean()
a.final_matrix_list

print(current_image.matrix)
print(current_image.matrix_list)

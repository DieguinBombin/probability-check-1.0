from PIL import Image
import numpy as np

class JPGFile:
	def __init__(self, name: str, valid_files: list, pred_resolution: tuple) -> None:

		self.file_name = name
		is_valid = name in valid_files
		self.resolution = pred_resolution

		if not is_valid: # Trivial exception, maybe removable
			raise Exception(f"{name} not in directory nor 'valid files'")

		jpg_pil = Image.open(f"setters_images/{name}")
		jpg_size = jpg_pil.size

		if jpg_size != pred_resolution:
			raise Exception(f"Image doesn't has the required format '{pred_resolution}'. Has '{jpg_size}' instead.")

		self.jpg_pil = jpg_pil
		self.jpg_size = jpg_size

	def to_matrix(self) -> np.array:

		matrix = list()
		temp_list = False
		for x in range(0, self.resolution[0]):
			if temp_list == False:
				pass
			else:
				matrix.append(temp_list)
			temp_list = list()
			for y in range(0, self.resolution[1]):
				temp_list.append(self.jpg_pil.getpixel((x,y)))
		return np.array(matrix, np.uint8)

	def __str__(self) -> str:

		return f"The image '{self.file_name}' has a resolution of {self.jpg_size}. \nThe class PIL of the image it's '{self.jpg_pil}'"



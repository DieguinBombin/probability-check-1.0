from PIL import Image
import numpy as np
from statistics import mean

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
        self.to_matrix()

    def to_matrix(self) -> None:
        matrix = list()
        temp_list = False

        for x in range(0, self.resolution[0]):
            temp_list = list()
            for y in range(0, self.resolution[1]):
                temp_list.append(self.jpg_pil.getpixel((x,y)))
            matrix.append(temp_list)

        self.matrix_list = matrix
        matrix = np.array(matrix, np.uint8)
        self.matrix = matrix
        self.fix_format()
        return None

    def fix_format(self) -> None:
        matrix_rotated = np.rot90(self.matrix, 3)
        matrix_flip = np.fliplr(matrix_rotated)
        self.matrix = matrix_flip

    def save(self, name: str) -> None:
        Image.fromarray(self.matrix).save(f"{name}.jpeg")
        return None

    def matrix(self):
        return self.matrix

    def __str__(self) -> str:
        return f"The image '{self.file_name}' has a resolution of {self.jpg_size}. \nThe class PIL of the image it's '{self.jpg_pil}'"

class MatrixMeanList:

    def __init__(self, matrix:[[list]], matrices_resolution:tuple):
        self.matrix = matrix
        self.matrices_resolution = matrices_resolution

    def get_mean(self):
        final_matrix_mean = list()
        r_list = list()
        g_list = list()
        b_list = list()
        for x in range(0, self.matrices_resolution[1]): # Here we make the assumption that all the matrices are of the same resolution too :3
            temp_row = list()
            for y in range(0, self.matrices_resolution[0]):
                for matrices in self.matrix:
                    component_tuple = matrices[x][y]
                    r = component_tuple[0]
                    g = component_tuple[1]
                    b = component_tuple[2]
                    r_list.append(r)
                    g_list.append(g)
                    b_list.append(b)
                mean_r = mean(r_list)
                mean_g = mean(g_list)
                mean_b = mean(b_list)
                temp_row.append((mean_r, mean_g, mean_b))
            final_matrix_mean.append(temp_row)
        self.final_matrix_list = final_matrix_mean
        return (final_matrix_mean)






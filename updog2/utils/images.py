import io
import os
from PIL import Image


class Images:
    def __init__(self, base_directory: str) -> None:
        self.base_directory = base_directory

    def get_imagesss(self, dir: str) -> list[dict]:
        r"""
        Get a list of images in a directory.  
        :param dir: The directory to search for images.

        Example:
        >>> get_images("C:/Users/username/Pictures")
        >>> get_images("/home/username/Pictures")
        """
        images = []

        for file in os.listdir(dir):
            if self.is_image(os.path.join(dir, file)):
                tmp = {}
                tmp["filename"] = file
                tmp["path"] = os.path.relpath(
                    os.path.join(dir, file), self.base_directory)
                tmp["size"] = round(os.path.getsize(
                    os.path.join(dir, file)) / 1024 / 1024, 2)
                images.append(tmp)

        return images

    def is_image(self, path: str) -> bool:
        r"""
        Check if a file is an image.  
        :param path: The path to the file.

        Example:
        >>> is_image("C:/Users/username/Pictures/image.jpg")
        >>> is_image("/home/username/Pictures/image.jpg")
        """

        try:
            with Image.open(path) as img:
                return True
        except:
            return False

    def reduce_image(self, path: str) -> io.BytesIO:
        r"""
        Reduce the size of an image.  
        :param path: The path to the image.

        Example:
        >>> reduce_image("~/Pictures/image.jpg")
        """
        if not self.is_image(path):
            return None

        with Image.open(path) as img:
            aspect_ratio = img.height / img.width

            if img.width > 750:
                new_height = int(750 * aspect_ratio)

                img = img.resize((750, new_height))

            img_format = img.format if img.format else "JPEG"
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format=img_format)
            img_byte_arr.seek(0)

            return img_byte_arr

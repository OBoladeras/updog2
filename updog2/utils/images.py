import io
import os
from PIL import Image
from zipfile import ZipFile

ZIP_NAME = 'images.zip'


def get_images(base_directory: str, dir: str = '') -> list[dict]:
    r"""
    Get a list of images in a directory.  
    :param dir: The directory to search for images.

    Example:
    >>> get_images("C:/Users/username/Pictures")
    >>> get_images("/home/username/Pictures")
    """
    images = []

    for file in os.listdir(dir):
        if is_image(os.path.join(dir, file)):
            tmp = {}
            tmp["filename"] = file
            tmp["path"] = os.path.relpath(
                os.path.join(dir, file), base_directory)
            tmp["size"] = round(os.path.getsize(
                os.path.join(dir, file)) / 1024 / 1024, 2)
            tmp["date"] = os.path.getmtime(os.path.join(dir, file))
            images.append(tmp)

    return images


def is_image(path: str) -> bool:
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


def reduce_image(path: str) -> io.BytesIO:
    r"""
    Reduce the size of an image.  
    :param path: The path to the image.

    Example:
    >>> reduce_image("~/Pictures/image.jpg")
    """
    if not is_image(path):
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


def generate_zip(path: str) -> str:
    r"""
    Create a zip file with all images in a directory.  
    :param directory: The directory containing the images.  
    :param path: The path to the images.

    Example:
    >>> generate_zip("C:/Users/username/Pictures", "C:/Users/username/Pictures")
    """
    zipfile_path = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), ZIP_NAME)

    # Create a zip file with all images
    with ZipFile(zipfile_path, 'w') as zipf:
        for file in os.listdir(path):
            if is_image(os.path.join(path, file)):
                zipf.write(os.path.join(path, file), file)

    return zipfile_path


def clean_zip() -> None:
    r"""
    Clean the zip file.
    """
    zipfile_path = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), ZIP_NAME)

    if os.path.exists(zipfile_path):
        os.remove(zipfile_path)

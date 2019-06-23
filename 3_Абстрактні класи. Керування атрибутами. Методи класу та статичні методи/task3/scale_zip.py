from PIL import Image
from pathlib import Path


class Scalezip:
    """
    Class for scales representation
    """
    def __init__(self, filename, new_size):
        self.filename = filename
        self.new_size = new_size
        self.temp_directory = Path("unzipped-{}".format(filename[:-4]))

    def process_files(self):
        """
        (Scalezip) -> NoneType
        The function resize image and save it.
        """
        for filename in self.temp_directory.iterdir():
            if filename.name == "__MACOSX":
                continue
            im = Image.open(str(filename))
            scaled = im.resize(self.new_size)
            scaled.save(str(filename))

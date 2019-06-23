import shutil
import zipfile
from pathlib import Path
from PIL import Image


class ZipProcessor:

    def unzip_files(self):
        self.temp_directory.mkdir()

        with zipfile.ZipFile(str(self.filename)) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(str(self.filename), 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
                if filename.name == "__MACOSX":
                    continue
        shutil.rmtree(str(self.temp_directory))

    def process_zip(self):
        """
        Does main job
        """
        self.unzip_files()
        self.process()
        self.zip_files()


class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        """
        Initiate parameters
        :param filename: archieve
        :param search_string : string to replace
        :param replace_string :replacement string
        """
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path("unzipped-{}".format(filename))

    def process(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
        contents = contents.replace(self.search_string, self.replace_string)
        with filename.open("w") as file:
            file.write(contents)

class ScaleZip(ZipProcessor):

    def __init__(self, filename, x, y):
        """
        Initiate parameters
        :param filename: archieve

        """
        self.filename = filename
        self.temp_directory = Path("unzipped-{}".format(self.filename))
        self.user_input1 = x
        self.user_input2 = y

    def process(self):
        """Scale each image in the directory to 640x480"""
        print(self.temp_directory)
        print(self.temp_directory.iterdir)
        for filename in self.temp_directory.iterdir():
            if filename.name == "__MACOSX":
                continue
            im = Image.open(str(filename))
            scaled = im.resize((self.user_input1, self.user_input2))
            scaled.save(str(filename))



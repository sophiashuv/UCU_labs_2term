import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    """
    Class for zip processor representation.
    """
    def __init__(self, zipname, object):
        self.zipname = zipname
        self.object = object
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

    def process_zip(self):
        """
        (ZipProcessor) -> NoneType
        The function processes files, unzip and zip functions.
         """
        self.unzip_files()
        self.object.process_files()
        self.zip_files()

    def unzip_files(self):
        """
        (ZipProcessor) -> NoneType
        The function unzip the given file.
        """
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        """
        (ZipProcessor) -> NoneType
        The function creates zip file.
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))

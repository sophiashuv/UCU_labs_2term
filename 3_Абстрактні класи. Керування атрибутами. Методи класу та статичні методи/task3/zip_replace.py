from pathlib import Path


class ZipReplace:
    """
    Class for replacing Zip
    """
    def __init__(self, zipname, search_string, replace_string):
        self.filename = zipname
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

    def process_files(self):
        """
        (ZipReplace) -> NoneType
        The function replaces the old string with new one
        """
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)



from zip_processor import ZipProcessor
from zip_replace import ZipReplace
from scale_zip import Scalezip


def test_picture():
    """
    The function creating new zip with reformed photo
    """
    zip_link = "python-basics.jpg.zip"
    width = str(input("Enter width:"))
    height = str(input("Enter height:"))
    object = Scalezip(zip_link, (width, height))
    ZipProcessor(zip_link, object).process_zip()


def test_text():
    """
    The function creating new zip with replaced text
    """
    text_link = "data.txt.zip"
    replace_string = str(input("Enter what string to replace to:"))
    object = ZipReplace(text_link, "Sleeping", replace_string)
    ZipProcessor(text_link, object).process_zip()


if __name__ == '__main__':
    test_text()
    test_picture()

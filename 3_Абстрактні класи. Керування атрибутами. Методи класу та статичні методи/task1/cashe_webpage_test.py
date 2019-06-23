from cashe_webpage import WebPage
import time

if __name__ == "__main__":
    webpage = WebPage("https://www.fest.lviv.ua/uk/projects/uku/")
    content1 = webpage.content
    print("Sleeping")
    time.sleep(5)
    content2 = webpage.content
    print(content1 == content2)
3


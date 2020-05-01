import time

from PIL import Image
from urllib import request
from selenium import webdriver


def find_album_art(author: str, title: str) -> Image.Image:
    try:
        options = webdriver.ChromeOptions()
        # Параметр для браузера, чтобы не открывалось окно
        options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options)
        
        # Гугл для поиска обложки
        driver.get('https://www.google.com/imghp')
        
        # Через селектор находим форму поиска
        text_field = driver.find_element_by_css_selector('.gLFyf.gsfi')
        # Передаём в неё автора и название песни и дополнительные слова
        # для уточнения поиска
        text_field.send_keys(f"{author} {title} album art cover")
        
        # Жмём кнопку поиска
        driver.find_element_by_css_selector('button[type="submit"]').click()
        # Выбираем первый результат из списка
        image = driver.find_element_by_css_selector('img.rg_i')
        # Получаем ссылку на обложку альбома
        src = image.get_attribute('src')
        return Image.open(request.urlopen(src))
    finally:
        driver.quit()


if __name__ == "__main__":
    author = input("Введите автора песни > ")
    title = input("Введите название песни > ")
    
    image = find_album_art(author, title)
    image.show()
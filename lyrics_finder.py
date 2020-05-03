from selenium import webdriver


def get_lyrics(driver: webdriver.Chrome,
               author: str, title: str) -> str:
    # Сайт с текстами песен
    driver.get('https://lyricsworld.ru/')

    # Через селектор находим форму поиска
    text_field = driver.find_element_by_css_selector('.searchW.input')
    # Передаём в неё автора и название песни
    text_field.send_keys(f"{author} {title}")

    # Жмём кнопку поиска
    driver.find_element_by_class_name('submit-input-wrapped').click()
    # Выбираем первый результат из списка
    driver.find_element_by_css_selector('.serpresult :nth-child(2) a').click()

    # Извлекаем текст песни
    return driver.find_element_by_id('songLyricsDiv').text


if __name__ == "__main__":
    author = input("Введите автора песни > ")
    title = input("Введите название песни > ")

    print('Текст песни')
    try:
        options = webdriver.ChromeOptions()
        # Параметр для браузера, чтобы не открывалось окно
        options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options)
        print(get_lyrics(author, title))
    finally:
        driver.quit()

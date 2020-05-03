import time
from selenium import webdriver
from lyrics_finder import get_lyrics
from PIL import Image
from io import BytesIO
from typing import Tuple, Dict
from json import loads


def get_statistics_screenshot(driver: webdriver) -> Image.Image:
    # Ресайз окна, чтобы поместилась вся статистика
    driver.set_window_size(1920, 600)

    # Область со статистикой
    summary = driver.find_element_by_class_name('summary--emotion')
    statistics_location = summary.location_once_scrolled_into_view
    statistics_size = summary.size

    # Скриншот всего окна
    statistics = Image.open(BytesIO(driver.get_screenshot_as_png()))

    # Получаем ROI
    left = int(statistics_location['x'])
    top = int(statistics_location['y'])
    right = left + int(statistics_size['width'])
    bottom = top + int(statistics_size['height'])
    roi = (left, top, right, bottom)
    return statistics.crop(roi)


def get_scores(driver) -> Dict[str, float]:
    # Открываем окно с json
    selector = '.summary-json pre .json--code'
    driver.find_element_by_class_name('js-toggle-summary-json_show').click()
    
    # Сохраняем json как словарь
    json = driver.find_element_by_css_selector(selector)
    json = loads(json.text)

    # Извлекаем только название эмоции и её балл
    scores = {tone_score['tone_name']: tone_score['score'] 
              for tone_score in json['document_tone']['tones']}

    return scores


def get_tone(author: str, title: str) -> Tuple[Image.Image,
                                               Dict[str, float]]:
    try:
        lyrics = get_lyrics(author, title)
        options = webdriver.ChromeOptions()
        # Параметр для браузера, чтобы не открывалось окно
        options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options)

        # Сайт с текстами песен
        driver.get('https://tone-analyzer-demo.ng.bluemix.net/')

        # Через селектор находим кнопку переключения режимов
        driver.find_element_by_css_selector(
            '.input--radio-label[for="input-own-text"]').click()

        # Находим область для текста и вставляем в неё слова песни
        text_area = driver.find_element_by_class_name('input--textarea')
        text_area.send_keys(lyrics)

        # Нажимаем "Анализировать""
        button_selector = 'button.input--submit-button'
        driver.find_element_by_css_selector(button_selector).click()
        # Ждём результатов
        time.sleep(5)
        statistics_img = get_statistics_screenshot(driver)
        scores = get_scores(driver)
        return statistics_img, scores
    finally:
        driver.quit()


if __name__ == "__main__":
    author = input("Введите автора песни > ")
    title = input("Введите название песни > ")

    image, scores = get_tone(author, title)
    image.show()
    print(scores)

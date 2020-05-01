# Install

Для полного функционирования нужно установить все зависимости из файла ```requirements.txt``` через команду
```bash
pip install -r requirements.txt
```

Также нужен браузер Chrome и chromedriver [отсюда](https://chromedriver.chromium.org/downloads). Чтобы узнать, какая версия необходима, введите в адресной строке:
```
chrome::/version
```

Скачанный архив распаковать в какую-либо папку, которую добавить в переменную Path. Если всё прошло успешно, то, набрав в консоли `chromedriver`, будет выведено
```
Starting ChromeDriver 81.0.4044.69 (6813546031a4bc83f717a2ef7cd4ac6ec1199132-refs/branch-heads/4044@{#776}) on port 9515
Only local connections are allowed.
Please protect ports used by ChromeDriver and related test frameworks to prevent access by malicious code.
```

# Практика по материалам 3

import os
from selenium import webdriver # инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager # инициализация драйвера Chrome из webdriver.manager
from selenium.webdriver.chrome.service import Service # импорт класса Service (открытие/закрытие браузера)

# опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

# объекты
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10) # используем неявное ожидание

# локаторы
MORE_LINK = ("xpath", "//a[text()='More']") # ссылка more в меню навигации сайта
FILE_UPLOAD_LINK = ("xpath", "//a[text()='File Upload']") # ссылка file upload в выпадающем списке more
ADD_FILE_BUTTON = ("xpath", "//input[@type='file']") # кнопка выбора файла для загрузки
REMOVE_BUTTON = ("xpath", "//button[@title='Clear selected files']") # кнопка удаления файла
ERROR_CLOSE_ICON = ("xpath", "//span[contains(@class, 'close')]") # кнопка закрытия сообщения об ошибке
UPLOAD_BUTTON = ("xpath", "//button[contains(@class, 'fileinput-upload-button')]") # кнопка загрузки изображения

BASE_URL = "https://demo.automationtesting.in/WebTable.html"

# открытие страницы
driver.get(BASE_URL)

more_link = driver.find_element(*MORE_LINK)
more_link.click()

file_upload_link = driver.find_element(*FILE_UPLOAD_LINK)
file_upload_link.click()

upload_btn = driver.find_element(*ADD_FILE_BUTTON)
upload_btn.send_keys(f"{os.getcwd()}/avatar.png")

remove_btn = driver.find_element(*REMOVE_BUTTON)
remove_btn.click()

driver.find_element(*ADD_FILE_BUTTON).send_keys(f"{os.getcwd()}/Test.txt")

error_close_icon = driver.find_element(*ERROR_CLOSE_ICON)
error_close_icon.click()

upload_btn_status = driver.find_element(*UPLOAD_BUTTON).get_attribute("disabled")

assert upload_btn_status == "true", "Кнопка загрузки изображения всё ещё активна"





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

# открытие страницы
driver.get("https://demo.automationtesting.in/WebTable.html")

# локаторы
MORE_LINK = ("xpath", "//a[text()='More']") # ссылка more в меню навигации сайта
FILE_UPLOAD_LINK = ("xpath", "//a[text()='File Upload']") # ссылка file upload в выпадающем списке more
ADD_FILE_BUTTON = ("xpath", "//input[@type='file']") # кнопка выбора файла для загрузки
REMOVE_BUTTON = ("xpath", "//button[@title='Clear selected files']") # кнопка удаления файла
ERROR_CLOSE_ICON = ("xpath", "//span[contains(@class, 'close')]") # кнопка закрытия сообщения об ошибке
UPLOAD_BUTTON = ("xpath", "//button[contains(@class, 'fileinput-upload-button')]") # кнопка загрузки изображения

moreLink = driver.find_element(*MORE_LINK)
moreLink.click()

fileUploadLink = driver.find_element(*FILE_UPLOAD_LINK)
fileUploadLink.click()

uploadBtn = driver.find_element(*ADD_FILE_BUTTON)
uploadBtn.send_keys(f"{os.getcwd()}/avatar.png")

removeBtn = driver.find_element(*REMOVE_BUTTON)
removeBtn.click()

driver.find_element(*ADD_FILE_BUTTON).send_keys(f"{os.getcwd()}/Test.txt")

errorCloseIcon = driver.find_element(*ERROR_CLOSE_ICON)
errorCloseIcon.click()

uploadBtnStatus = driver.find_element(*UPLOAD_BUTTON).get_attribute("disabled")

assert uploadBtnStatus == "true", "Кнопка загрузки изображения всё ещё активна"




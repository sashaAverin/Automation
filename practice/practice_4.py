
# Практика по материалам 4

from selenium import webdriver # инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager # инициализация драйвера Chrome из webdriver.manager
from selenium.webdriver.chrome.service import Service # импорт класса Service (открытие/закрытие браузера)
from selenium.webdriver.support.ui import WebDriverWait # импорт класса ожиданий
from selenium.webdriver.support import expected_conditions as EC # импорт класса явных ожиданий

# опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

# объекты
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.implicitly_wait(10)

# локаторы
MORE_LINK = ("xpath", "//a[text()='More']") # ссылка more в меню навигации сайта
JQUERY_LINK = ("xpath", "//a[text()='JQuery ProgressBar']") # ссылка jquery progressbar в выпадающем списке more
START_DOWNLOAD_BUTTON = ("xpath", "//button[@id='downloadButton']") # кнопка вызова окна с прогрессом загрузки
CANCEL_DOWNLOAD_BUTTON = ("xpath", "//button[text()='Cancel Download']") # кнопка отмены загрузки
COMPLETE_TEXT = ("xpath", "//div[@class='progress-label']") # текст подтверждения успешной загрузки
CLOSE_BUTTON = ("xpath", "//button[text()='Close']") # кнопка закрытия окна загрузки

BASE_URL = "https://demo.automationtesting.in/WebTable.html"

# открытие страницы
driver.get(BASE_URL)

more_link = driver.find_element(*MORE_LINK)
more_link.click()

jquery_link = driver.find_element(*JQUERY_LINK)
jquery_link.click()

# явное ожидание, что кнопка "close" невидима
wait.until(EC.invisibility_of_element_located(CLOSE_BUTTON))

start_download = driver.find_element(*START_DOWNLOAD_BUTTON)
start_download.click()

wait.until(EC.text_to_be_present_in_element(CANCEL_DOWNLOAD_BUTTON, "Cancel Download"))
driver.find_element(*CANCEL_DOWNLOAD_BUTTON).click()

driver.find_element(*START_DOWNLOAD_BUTTON).click()
wait.until(EC.text_to_be_present_in_element(COMPLETE_TEXT, "Complete!"))



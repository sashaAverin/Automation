
# Практика по материалам 1

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

# локаторы
MORE_LINK = ("xpath", "//a[text()='More']") # ссылка more в меню навигации сайта
LOADER_LINK = ("xpath", "//a[text()='Loader']") # ссылка loader в выпадающем списке more
RUN_BUTTON = ("xpath", "//button[@id='loader']") # кнопка для вызова окна с текстом
MODAL_TEXT = ("xpath", "//div[@class='modal-body']/p") # контейнер с текстом
SAVE_BUTTON = ("xpath", "//button[text()='Save changes']") # кнопка сохранения

BASE_URL = "https://demo.automationtesting.in/WebTable.html"

# открытие страницы
driver.get(BASE_URL)

wait.until(EC.element_to_be_clickable(MORE_LINK)).click()
wait.until(EC.element_to_be_clickable(LOADER_LINK)).click()
wait.until(EC.text_to_be_present_in_element(RUN_BUTTON, "Run"))
driver.find_element(*RUN_BUTTON).click()
wait.until(EC.text_to_be_present_in_element(MODAL_TEXT, "Lorem"))
wait.until((EC.element_to_be_clickable(SAVE_BUTTON))).click()



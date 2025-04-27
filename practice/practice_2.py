
# Практика по материалам 2

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
DYNAMIC_LINK = ("xpath", "//a[text()='Dynamic Data']") # ссылка dynamic data в выпадающем списке more
TITLE = ("xpath", "//h3") # заголовок страницы
GET_BUTTON = ("xpath", "//button[@id='save']") # кнопка получения данных
IMG = ("xpath", "//div[@id='loading']/img") # получаемое изображение

BASE_URL = "https://demo.automationtesting.in/WebTable.html"

# открытие страницы
driver.get(BASE_URL)

more_link = driver.find_element(*MORE_LINK)
more_link.click()

dynamic_link = driver.find_element(*DYNAMIC_LINK)
dynamic_link.click()

title_text = driver.find_element(*TITLE).text
assert title_text == "Loading the data Dynamically", "Текст заголовка не соответствует ожидаемому"

get_dynamic_data = driver.find_element(*GET_BUTTON)
get_dynamic_data.click()

img_link = driver.find_element(*IMG).get_attribute("src")
print(img_link)



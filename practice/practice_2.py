
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

# открытие страницы
driver.get("https://demo.automationtesting.in/WebTable.html")

# локаторы
MORE_LINK = ("xpath", "//a[text()='More']") # ссылка more в меню навигации сайта
DYNAMIC_LINK = ("xpath", "//a[text()='Dynamic Data']") # ссылка dynamic data в выпадающем списке more
TITLE = ("xpath", "//h3") # заголовок страницы
GET_BUTTON = ("xpath", "//button[@id='save']") # кнопка получения данных
IMG = ("xpath", "//div[@id='loading']/img") # получаемое изображение

moreLink = driver.find_element(*MORE_LINK)
moreLink.click()

dynamicLink = driver.find_element(*DYNAMIC_LINK)
dynamicLink.click()

titleText = driver.find_element(*TITLE).text
assert titleText == "Loading the data Dynamically", "Текст заголовка не соответствует ожидаемому"

getDynamicData = driver.find_element(*GET_BUTTON)
getDynamicData.click()

imgLink = driver.find_element(*IMG).get_attribute("src")
print(imgLink)



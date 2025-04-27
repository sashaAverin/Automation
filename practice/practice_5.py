
# Практика по материалам 5
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
SWITCH_TO_LINK = ("xpath", "//a[text()='SwitchTo']") # ссылка switch to в меню навигации сайта
WINDOWS_LINK = ("xpath", "//a[text()='Windows']") # ссылка windows в выпадающем списке more
TABBED_CLICK_BUTTON = ("xpath", "//div[@id='Tabbed']//button") # кнопка открытия новой вкладки
MULTIPLE_WINDOWS_LINK = ("xpath", "//ul[contains(@class, 'nav-tabs')]//li[3]") # ссылка multiple windows
MULTIPLE_CLICK_BUTTON = ("xpath", "//div[@id='Multiple']//button") # кнопка открытия окон
EMAIL_FIELD = ("xpath", "//input[@id='email']") # поле ввода e-mail
SEND_BUTTON = ("xpath", "//img[@id='enterimg']") # кнопка отправки формы

BASE_URL = "https://demo.automationtesting.in/WebTable.html"

# открытие страницы
driver.get(BASE_URL)

switch_to_link = driver.find_element(*SWITCH_TO_LINK)
switch_to_link.click()
windows_link = driver.find_element(*WINDOWS_LINK)
windows_link.click()

tabbed_click_btn = driver.find_element(*TABBED_CLICK_BUTTON)
tabbed_click_btn.click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])
driver.close()
driver.switch_to.window(tabs[0])

wait.until(EC.element_to_be_clickable(MULTIPLE_WINDOWS_LINK)).click()
multiple_click_btn = driver.find_element(*MULTIPLE_CLICK_BUTTON)
multiple_click_btn.click()

tabs = driver.window_handles
driver.switch_to.window(tabs[2])
wait.until(EC.url_to_be("https://demo.automationtesting.in/Index.html"))

print(wait.until(EC.number_of_windows_to_be(3)))

wait.until(EC.element_to_be_clickable(EMAIL_FIELD)).send_keys("test@gmail.com")
send_btn = driver.find_element(*SEND_BUTTON)
send_btn.click()

wait.until(EC.url_to_be("https://demo.automationtesting.in/Register.html"))
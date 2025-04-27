from selenium import webdriver # инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager # инициализация драйвера Chrome из webdriver.manager
from selenium.webdriver.chrome.service import Service # импорт класса Service (открытие/закрытие браузера)
from selenium.webdriver.support.ui import WebDriverWait # импорт класса ожиданий
from selenium.webdriver.support import expected_conditions as EC # импорт класса явных ожиданий
from selenium.webdriver.support.select import Select # импорт класса Select для работы с селекторами (старая реализация)
from selenium.webdriver import Keys # импорт класса Keys для ввода в поле клавиш с клавиатуры

# опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

# объекты
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# локаторы
SELECT = ("xpath", "//select[@id='field-language']")
LOGIN_BUTTON = ("xpath", "//button[@id='btn-login']")
TASK_LINK = ("xpath", "//li[@data-name='Task']")
ALL_FILTER = ("xpath", "//div[contains(@class, 'left-dropdown')]")
ONLY_MY_CHECKBOX = ("xpath", "(//li[@class='checkbox'])[1]")
SELECT_ALL = ("xpath", "//input[contains(@class, 'select-all')]")
ACTIONS_BUTTON = ("xpath", "//div[contains(@class, 'actions')]/button")
MASS_UPDATE = ("xpath", "//div[contains(@class, 'open')]//li[3]")
UPDATE_DISABLED = ("xpath", "//button[text()='Update']")
CLOSE_ICON = ("xpath", "//a[@class='close']")
CREATE_TASK_BUTTON = ("xpath", "//div[contains(@class, 'header-buttons')]")
NAME_FIELD = ("xpath", "//input[@data-name='name']")
STATUS_FIELD = ("xpath", "//select[@data-name='status']")
SAVE_BUTTON = ("xpath", "//button[text()='Save']")
TASKS_LINK = ("xpath", "//a[text()='Tasks']")
SEARCH_FIELD = ("xpath", "//input[@data-name='textFilter']")
REMOVE_BUTTON = ("xpath", "//button[text()=' Remove ']")
FIRST_TASK_CHECKBOX = ("xpath", "//tr[@class='list-row '][1]//input")
REMOVE = ("xpath", "//div[contains(@class, 'open')]//li[1]")
TIME_SLEEP = ("xpath", "//button[text()='Edit']")

BASE_URL = "https://demo.us.espocrm.com/"

# открытие страницы
driver.get(BASE_URL)

dropdown = Select(wait.until(EC.element_to_be_clickable(SELECT)))
dropdown.select_by_visible_text("English (UK)")

wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
wait.until(EC.element_to_be_clickable(TASK_LINK)).click()
wait.until(EC.element_to_be_clickable(ALL_FILTER)).click()
wait.until((EC.element_to_be_clickable(ONLY_MY_CHECKBOX))).click()
wait.until(EC.element_to_be_clickable(SELECT_ALL)).click()
wait.until(EC.element_to_be_clickable(ACTIONS_BUTTON)).click()
wait.until(EC.element_to_be_clickable(MASS_UPDATE)).click()
wait.until(EC.visibility_of_element_located(UPDATE_DISABLED))
update_btn_status = driver.find_element(*UPDATE_DISABLED).get_attribute("disabled")
assert update_btn_status == "true"

driver.find_element(*CLOSE_ICON).click()
driver.find_element(*CREATE_TASK_BUTTON).click()

wait.until(EC.element_to_be_clickable(NAME_FIELD)).send_keys("Test")

status_field_check = driver.find_element(*STATUS_FIELD).get_attribute("value")
assert status_field_check == "Not Started"
driver.find_element(*SAVE_BUTTON).click()
wait.until(EC.visibility_of_element_located(TIME_SLEEP))
wait.until(EC.element_to_be_clickable(TASKS_LINK)).click()
wait.until(EC.element_to_be_clickable(SEARCH_FIELD)).send_keys("Test" + Keys.ENTER)
wait.until(EC.element_to_be_clickable(FIRST_TASK_CHECKBOX)).click()
wait.until(EC.element_to_be_clickable(ACTIONS_BUTTON)).click()
wait.until(EC.element_to_be_clickable(REMOVE)).click()
wait.until(EC.visibility_of_element_located(REMOVE_BUTTON)).click()



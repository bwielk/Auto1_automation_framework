from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys as Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import logging


def get_element_by_css_selector(context, selector, timeout=5):
    found_element = None
    try:
        found_element = WebDriverWait(context.browser, timeout)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR(selector))))
    except TimeoutException as e:
        logging.error(e)
    return found_element

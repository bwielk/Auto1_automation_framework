from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import logging


def get_element_by_css_selector(context, selector, timeout=5):
    found_element = None
    try:
        found_element = WebDriverWait(context.driver, timeout)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException as e:
        logging.error(e)
    return found_element


def get_element_by_name(context, selector, timeout=5):
    found_element = None
    try:
        found_element = WebDriverWait(context.driver, timeout)\
            .until(EC.presence_of_element_located((By.NAME, selector)))
    except TimeoutException as e:
        logging.error(e)
    return found_element


def get_multiple_elements_by_xpath(context, selector):
    found_elements = None
    try:
        found_elements = context.driver.find_elements_by_xpath(selector)
    except NoSuchElementException as e:
        logging.error(e)
    return found_elements

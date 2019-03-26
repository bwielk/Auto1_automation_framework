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
        logging.info('Found element with selector "%s"' % selector)
    except TimeoutException as e:
        logging.error(e)
    return found_element


def get_element_by_name(context, name, timeout=5):
    found_element = None
    try:
        found_element = WebDriverWait(context.driver, timeout)\
            .until(EC.presence_of_element_located((By.NAME, name)))
        logging.info('Found element with name attribute %s' % name)
    except TimeoutException as e:
        logging.error(e)
    return found_element


def get_multiple_elements_by_xpath(context, xpath):
    found_elements = None
    try:
        found_elements = context.driver.find_elements_by_xpath(xpath)
        logging.info('Found element with xpath "%s"' % xpath)
    except NoSuchElementException as e:
        logging.error(e)
    return found_elements

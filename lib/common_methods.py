from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
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


def filter_results_by_first_reg_year(context, year):
    css_locator_of_reg_year_section = '#app > div > main > div.root___3C6lR.container > div > div.col-md-3 > div >' \
                                      ' div > div > div:nth-child(3) > div.label___3agdr'

    reg_year_section = get_element_by_css_selector(context, css_locator_of_reg_year_section)
    reg_year_section.click()
    reg_year_dropdown = get_element_by_name(context, 'yearRange.min')
    select_reg_date = Select(reg_year_dropdown)
    select_reg_date.select_by_visible_text(year)


def sort_displayed_results(context, category, order):
    sort_dropdown = get_element_by_name(context, 'sort')

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
import logging
import time

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
    select_sort_type = Select(sort_dropdown)
    order_to_sort_by = None
    if category == 'price':
        if order == 'ascending':
            order_to_sort_by = 'Niedrigster Preis'
        else:
            order_to_sort_by = 'Höchster Preis'
    select_sort_type.select_by_visible_text(order_to_sort_by)


def get_multiple_elements_by_xpath(context, selector):
    found_elements = context.driver.find_elements_by_xpath(selector)
    return found_elements


def extract_first_reg_data_from_displayed_search_results(context):
    time.sleep(5)
    results = []
    num_of_elements_displayed = get_element_by_name(context, 'pageSize')
    select_page_size = Select(num_of_elements_displayed)
    num_of_elements = int(select_page_size.first_selected_option.text)
    for i in range(1, num_of_elements+1):
        xpath_to_search_for = '//*[@id="app"]/div/main/div[4]/div/div[2]/div/div[3]/div/div[1]/div[' + str(i) + \
                              ']/div/a/ul/li[1]'
        found_element = context.driver.find_element_by_xpath(xpath_to_search_for)
        results.append(found_element.text)
    results_years_only_as_ints = [int(x[5:len(x)]) for x in results]
    return results_years_only_as_ints

def extract_price_from_displayed_search_results(context):
    found_elements = get_multiple_elements_by_xpath('item___T1IPF')

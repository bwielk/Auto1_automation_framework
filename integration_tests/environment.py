from selenium import webdriver
import logging
import datetime
import time


def before_all(context):
    logging.info("Running a new set of tests")


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    logging.info("Running scenario %s" % scenario)
    context.driver.get('https://www.autohero.com/de/search/')
    context.driver.implicitly_wait(4)
    time.sleep(5)


def after_scenario(context, scenario):
    logging.info("Test result: %s" % scenario.status)


def after_all(context):
    logging.info("All behave steps terminated their execution at %s" % datetime.now())

import behave
import selenium
import logging
import datetime


def before_all(context):
    logging.info("Running a new set of tests")


def before_scenario(context, scenario):
    logging.info("Running scenario %s" % scenario)


def after_scenario(context, scenario):
    logging.info("Test result: %s" % scenario.status)


def after_all(context):
    logging.info("All behave steps terminated their execution at %s" % datetime.now())

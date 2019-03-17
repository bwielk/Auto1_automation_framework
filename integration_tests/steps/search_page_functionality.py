from behave import step
from lib import common_methods as common


@step('results are filtered by first registration year - {year}')
def filter_results_by_year(context, year):
    common.filter_results_by_first_reg_year(context, year)


@step('the results are sorted by {category} in {order} order')
def sort_results(context, category, order):
    common.sort_displayed_results(context, category, order)


@step('the results are filtered by first registration - {year}')
def verify_results_are_filtered_by_registration_year(context, year):
    pass


@step('the results are sorted in {order} order by {category}')
def verify_results_are_sorted_by_category_in_specific_order(context, order, category):
    pass
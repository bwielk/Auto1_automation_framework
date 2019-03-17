from behave import step
from lib import step_implementation as impl


@step('results are filtered by first registration year - {year}')
def filter_results_by_year(context, year):
    impl.filter_results_by_first_reg_year(context, year)
    css_locator_of_selected_sort_banner = '#app > div > main > div.root___3C6lR.container > div > div.col-md-9 > div >'\
                                          ' div.root___10o2f > ul > li:nth-child(1) > button'
    selected_sort_banner = impl.get_element_by_css_selector(context, css_locator_of_selected_sort_banner)
    assert selected_sort_banner is not None and selected_sort_banner.text == 'Erstzulassung von: 2015'


@step('the results are sorted by {category} in {order} order')
def sort_results(context, category, order):
    impl.sort_displayed_results(context, category, order)


@step('the results are filtered by first registration - {year}')
def verify_results_are_filtered_by_registration_year(context, year):
    results = impl.extract_first_reg_data_from_displayed_search_results(context)
    assert all(x >= int(year) for x in results)


@step('the results are sorted in {order} order by {category}')
def verify_results_are_sorted_by_category_in_specific_order(context, order, category):
    results = impl.extract_price_from_displayed_search_results(context)
    if category == 'price':
        if order == 'descending':
            sorted_results = sorted(results, reverse=True)
        else:
            sorted_results = sorted(results)
        assert sorted_results == results

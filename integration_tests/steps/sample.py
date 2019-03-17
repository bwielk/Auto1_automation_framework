from behave import step
import selenium


@step('I am running the tests')
def test1(context):
    print('Tests begin')
    driver = context.driver
    driver.find_element_by_id('name')

@step('running the tests')
def test2(context):
    print('running the tests')


@step('response is {message}')
def test2(context, message):
    assert message == 'Tests have run'

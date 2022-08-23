from behave import *
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException  

@given('a user visit "{website}"') 
def open(context, website):
    context.helperfunc.open(website)

@when('the user input "{input}" in search box')
def input_search(context, input):
    context.helperfunc.find_by_selector(".css-rl8xd2 > input:nth-child(2)").send_keys(input)

@step('the user click search button')
def click_search(context):
    context.helperfunc.find_by_selector(".css-1ymn4im").click()

@then('search result page will display')
def search_displayed(context):
    filter_info=context.helperfunc.find_by_selector(".css-gwtn89-unf-heading").text
    assert filter_info == "Filter"

@Given('the user in search result page')
def search_displayed(context):
    filter_info=context.helperfunc.find_by_selector(".css-gwtn89-unf-heading").text
    assert filter_info == "Filter"

@When ('the user select Official Store filter checkbox')
def select_official_store_checkbox(context):
    context.helperfunc.find_by_selector("div.css-sdclqg:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)").click()

@Then ('search result page filtered by Official Store')
def search_result_filtered(context):
    try:
        context.helperfunc.find_by_selector(".css-1enpcoo > div:nth-child(1)")
    except NoSuchElementException:
        return False
    return True
from behave import given, when, then


@given("Open {url} home page")
def open_page(context, url):
    context.app.home_page.open_home_page(url)


@then("Verify user can see the 10 header menu")
def verify_visibility_header_menu(context):
    context.app.home_page.verify_visibility_header_menu()

@then("Verify user can click on all 10 header menu and a correct page is display")
def verify_user_can_click_header_menu(context):
    context.app.home_page.verify_user_can_click_header_menu()

@when("Click on the search icon to navigate away from the home page" )
def click_search_icon(context):
    context.app.home_page.click_search_icon()

@then("Verify clicking on the logo takes user to the home page")
def verify_clicking_logo_home_page(context):
    context.app.home_page.verify_clicking_logo_home_page()

@when("Click on the search icon")
def click_search_icon(context):
    context.app.home_page.click_search_icon()

@when("Populate the search field with {input_data}")
def populate_search_field(context, input_data):
    context.search_data = input_data
    context.app.home_page.populate_search_field(input_data)

@when("Click on the search submit icon")
def search_submit(context):
    context.app.home_page.search_submit()

@when("Click on the language button")
def click_language_button(context):
    context.app.home_page.click_language_button()

@then("Verify search results are displayed")
def verify_search_result(context):
    context.app.home_page.verify_search_result(context.search_data)

@then("Verify user can change language")
def verify_changing_language(context):
    context.app.home_page.verify_changing_language()





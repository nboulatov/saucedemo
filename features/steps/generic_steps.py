from behave import given, when, then, step


@step('I navigate to: {url}')
def open_saucedemo(context, url):
    context.app.base_page.open(url)


@when('I logout')
def logout(context):
    context.app.base_page.log_out()


@when('I click shopping cart icon')
def click_shopping_cart_icon(context):
    context.app.base_page.click_shopping_cart_icon()


@then('I see URL contains text: {expected_text_in_url}')
def verify_url(context, expected_text_in_url):
    context.app.base_page.verify_url(expected_text_in_url)

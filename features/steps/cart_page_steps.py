from behave import given, when, then


@then('I verify number of items in cart: {number_of_items}')
def verify_cart_items(context, number_of_items):
    context.app.cart_page.verify_cart_items(number_of_items)


@when('I click button: {button}')
def click_checkout_button(context, button):
    context.app.cart_page.click_checkout_button(button)

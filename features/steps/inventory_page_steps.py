from behave import given, when, then


@when('I select a number of items to add to cart: {number_of_items}')
def add_items_to_cart(context, number_of_items):
    context.app.inventory_page.add_items_to_cart(number_of_items)


@when('I collect data before sort')
def get_default_data(context):
    context.app.inventory_page.get_default_data()


@when('I select sort option: {sort_option}')
def select_sort_option(context, sort_option):
    context.app.inventory_page.select_sort_option(sort_option)


@then("I verify sorting order: {sort_option}")
def verify_sort_option(context, sort_option):
    context.app.inventory_page.verify_sort_option(sort_option)


@then("I validate all images")
def validate_images(context):
    context.app.inventory_page.validate_images()

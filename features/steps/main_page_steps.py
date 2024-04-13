from behave import given, when, then


@given('I am authorized as: {user}')
def login_as(context, user):
    context.app.main_page.login_as(user)


@then('I see login button')
def verify_login_button(context):
    context.app.main_page.verify_login_button()


@then('I verify page contains text: {error_message}')
def verify_error_message(context, error_message):
    context.app.main_page.verify_error_message(error_message)

Feature: saucedemo.com tests

  @smoke
  Scenario Outline: standard_user flow: sort, add to cart, checkout, and logout
    Given I navigate to: https://www.saucedemo.com/
    And I am authorized as: standard_user
    Then I see URL contains text: inventory
    When I collect data before sort
    When I select sort option: <sort_option>
    Then I verify sorting order: <sort_option>
    When I select a number of items to add to cart: <number_of_items>
    When I click shopping cart icon
    Then I see URL contains text: cart
    Then I verify number of items in cart: <number_of_items>
    When I click button: Checkout
    Then I see URL contains text: checkout
    When I logout
    Then I see login button

    Examples:
      | sort_option | number_of_items |
      | az          | 3               |
      | za          | 4               |
      | hilo        | 5               |
      | lohi        | 6               |

  @smoke
  Scenario: Verification of error message display for locked_out_user
    Given I navigate to: https://www.saucedemo.com/
    And I am authorized as: locked_out_user
    Then I verify page contains text: Epic sadface

  @smoke
  Scenario: Testing image validations for problem_user
    Given I navigate to: https://www.saucedemo.com/
    And I am authorized as: problem_user
    Then I validate all images

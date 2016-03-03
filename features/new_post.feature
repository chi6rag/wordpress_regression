Feature: New Post

  Scenario Outline: New Post - Happy Path
    Given On home page I login as a valid user and tap on New Post Icon
    When I enter Title as "<title>" and Message as "<message>"
    And I press Publish
    Then I should be taken to home page
    Examples:
      | title       | message       |
      | Valid Title | valid message |

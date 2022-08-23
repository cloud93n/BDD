Feature: Test search filter

  Scenario: User searches for a working desk
     Given a user visit "https://www.tokopedia.com/"
      When the user input "working desk" in search box
      And the user click search button
      Then search result page will display

  Scenario: User filters search by Jenis Toko
    Given the user in search result page
    When the user select Official Store filter checkbox
    Then search result page filtered by Official Store

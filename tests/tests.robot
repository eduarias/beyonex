*** Settings ***
Documentation     QA technical task for Beyonnex.
Library           SeleniumLibrary
Variables        ../resources/variables.py
Library          ../resources/Service.py
Suite Setup      Open Home Page On Browser and Get Temperature
Suite Teardown   Close All Browsers

*** Test Cases ***
Buy Moisturizers
    [Setup]  Select Moisturizers If Weather Is Below 19 Degrees Otherwise Skip
    Given A Cart Selecting The Least Expensive Product That Contains "Aloe"
    And A Cart Selecting The Least Expensive Product That Contains "Almond"
    When Checking Out The Right Products On The Cart
    And Paying With A Valid Test Card
    Then Payment Should Be Successful

Buy Suncreens
    [Setup]  Select Sunscreens If Weather Is Above 34 Degrees Otherwise Skip
    Given A Cart Selecting The Least Expensive Product That Contains "SPF-50"
    And A Cart Selecting The Least Expensive Product That Contains "SPF-30"
    When Checking Out The Right Products On The Cart
    And Paying With A Valid Test Card
    Then Payment Should Be Successful

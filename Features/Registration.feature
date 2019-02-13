Feature: Login Functionality

 Scenario: Registration with valid data
		   Given User is on registration page
		   When user enter username
		   And user enter email id
		   And user enter password
		   And click on submit button
		   Then user should be logged in successfully

 Scenario: Registration with duplicate username data
		   Given User is on registration page
		   When user enter duplicate username
		   And user enter email id
		   And user enter password
		   And click on submit button
		   Then user should be logged in successfully

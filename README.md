
# Django Rest Test Task

**URLs description**

	1. "/api/companies/": API endpoint to create company with office information.
	2. "/api/offices/": API endpoint to add office for a company.
	3. "/api/companies/<company_id>/offices/": API endpoint to list all offices of a company.
	4. "/api/companies/list/": API endpoint to get all companies in the database with headquater office information.
	5. "/api/companies/<company_id>/_change_headquater/<office_id>/": API to update company headquater.


1. Please change the models so that the following functionality works.

	- A Company can have one or more offices
	- Offices can be an headquarter.
	- A company should at all times have exactly one headquarter

		a. How do you test it?
		solution: To test this I will create a company object and then create multiple offices for a company and test this via test cases. 

2. Please add an API with the help of django-rest-framework.

	- Write an API endpoint to create the company along with office information
	- Write an simple read-only API endpoint for companies to get the company name + street+postal_code+city from the headquarter office
	- Write an simple read-only API endpoint to get all the offices for a company
	- Write an API endpoint to change the headquarter of the company

		a. How would you test the functionality?
		solution: To test api functionality I can write unit test cases, where I perpare all possible scenarios for an API such as test API for 200 success response, for 201 object created success response, for 400 error response or 404 error response etc.  
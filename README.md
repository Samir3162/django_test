# URLs description

`
1. "/api/companies/": API endpoint to create company with office information.
2. "/api/offices/": API endpoint to add office for a company.
3. "/api/companies/detail/<company_id>/": API endpoint to get company detail of headquater office.
4. "/api/companies/<company_id>/": API endpoint to list all offices of a company.
5. "/api/companies/list/": API endpoint to get all companies in the database.
6. "/api/companies/<company_id>/_change_headquater/<office_id>/": API to update company headquater.`

# 1. Please change the models so that the following functionality works. How do you test it?

# - A Company can have one or more offices
# - Offices can be an headquarter.
# - A company should at all times have exactly one headquarter

# 2. Please add an API with the help of django-rest-framework. How would you test the functionality?

# - Write an API endpoint to create the company along with office information
# - Write an simple read-only API endpoint for companies to get the company name + street+postal_code+city from the headquarter office
# - Write an simple read-only API endpoint to get all the offices for a company
# - Write an API endpoint to change the headquarter of the company

Development notes
===================

Login workflow
----------------
1. Aparment Owners can add users through hidden signup.
2. A token is associated with each apartment complex
3. A user can signup using a token and is assigned the apartment complex via the token value.
4. A user associated with an apartment complex can only modify apartments for that complex.
5. Each apartment complex can have one or more admin users who can modify base contact info



Adding apartment workflow
--------------------------
* Apartment complex is chosen automatically by token, and default contact values are filled in using this as well
* Should be a form wizard (docs here: http://django-formtools.readthedocs.io/en/latest/wizard.html)

### First page:
1. Name (Might be a dropdown of apartment properties)
2. Address (Autofilled by property with field for unit number)
3. Point of contact (autofilled by Property)
4. Number of bedrooms
5. Max Occupants
6. Lease Term
7. Rent

### Second page:
8. Min and max income requirements, with some sort of calculator for tenants.


### Third page:
9. Transit options (for now just a simple landlord-assigned rating, but should be objective in the future)






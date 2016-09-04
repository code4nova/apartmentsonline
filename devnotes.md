Development notes
===================



Login workflow
----------------
#. Aparment Owners can add users through hidden signup.
#. A token is associated with each apartment complex
#. A user can signup using a token and is assigned the apartment complex via the token value.
#. A user associated with an apartment complex can only modify apartments for that complex.
#. Each apartment complex can have one or more admin users who can modify base contact info



Adding apartment workflow
--------------------------
#. Apartment complex is chosen automatically by token, and default contact values are filled in using this as well
#. Should be a form wizard (docs here: http://django-formtools.readthedocs.io/en/latest/wizard.html)

### First page:
#. Name (Might be a dropdown of apartment properties)
#. Address (Autofilled by property with field for unit number)
#. Point of contact (autofilled by Property)
#. Number of bedrooms
#. Max Occupants
#. Lease Term
#. Rent

### Second page:
#. Min and max income requirements, with some sort of calculator for tenants.


### Third page:
#. Transit options (for now just a simple landlord-assigned rating, but should be objective in the future)






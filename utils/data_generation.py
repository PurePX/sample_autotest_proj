from faker import Faker

fake = Faker()
fake_zip = fake.zipcode()

class Generate:
    # Main user details
    main_user_fname = fake.first_name()
    main_user_lname = fake.last_name()
    main_user_email = fake.email()
    main_user_phone = fake.basic_phone_number()
    main_user_credit_card_number = '4671984481848245'  # Tried to use faker, but not passing validation
    main_user_credit_card_expiration = fake.credit_card_expire()
    main_user_credit_card_cvv = fake.credit_card_security_code()
    main_user_billing_address_street1_address = fake.street_address()
    main_user_billing_address_street2_address = fake.building_number()
    main_user_billing_address_zip = '10016'  # Tried to use faker, but not passing validation

    # Someones user details
    some_user_fname = fake.first_name()
    some_user_lname = fake.last_name()
    some_user_email = fake.email()
    some_user_hidden_email = some_user_email.split('@')[0][0] + '•' * (len(some_user_email.split('@')[0]) - 2) + \
                             some_user_email.split('@')[0][-1] + '@' + some_user_email.split('@')[
                                 1]  # Returns like this a••••••z@example.net
    some_user_phone = fake.basic_phone_number()
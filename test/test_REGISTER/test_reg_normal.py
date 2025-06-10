import requests
from assertpy import assert_that
from setting.endpoint import api_register
from faker import Faker
fake = Faker()

def test():
    random_name = fake.name()
    random_email = fake.email()
    random_password = fake.password()
    head = {
        "Accept" : "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 8|krySy127N54gG7dj8bkZXB2xVTLLXBZugdAN0sTO74ddb575"
    }
    payload = {
        "user_name": random_name,
        "email": random_email,
        "password":random_password ,
        "password_confirmation": random_password,
        "user_type": "admin",
        "access_level": "admin"
    }
    req = requests.post(api_register, headers=head, json=payload)
    print(req.json())

    # VALIDATION
    status_code = req.status_code
    resp_id = req.json()["data"]["user"]["id"]
    resp_user_name = req.json()["data"]["user"]["name"]
    resp_email = req.json()["data"]["user"]["email"]
    resp_access_level = req.json()["data"]["user"]["access_level"]

    #  # ASSERT
    assert_that(status_code).is_equal_to(201)
    assert_that(resp_id).is_not_none()
    assert_that(resp_user_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_access_level).is_not_none()




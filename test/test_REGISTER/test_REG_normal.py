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
        "Accept" : "aplication/json",
        "Content_Type": "aplication/json",
        # "Authorization": "Bearer 15|M9WvuouyaXiDCoki3LaQMrmI8mjsSR8jdZnHYWI285010cd6"
    }
    payload = {
        "user_name": random_name,
        "email": random_email,
        "password":random_password ,
        "password_confirmation": random_password
    }
    req = requests.post(api_register, headers=head, json=payload)
    print(req.json())

     # VALIDATION
    status_code = req.status_code
    resp_user_name = req.json()["data"]["user"]["name"]
    resp_email = req.json()["data"]["user"]["email"]
     # ASSERT
    assert_that(status_code).is_equal_to(201)
    assert_that(resp_user_name).is_not_none()
    assert_that(resp_email).is_not_none()



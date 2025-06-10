import requests
from assertpy import assert_that
from setting.endpoint import api_register
from faker import Faker
fake = Faker()

def test():
    head = {
        "Accept" : "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 8|krySy127N54gG7dj8bkZXB2xVTLLXBZugdAN0sTO74ddb575"
    }
    payload = {
        "user_name": "Admin 11",
        "email": "admin12@cansativa.com",
        "password": "",
        "password_confirmation": "password1234",
        "user_type": "admin",
        "access_level": "admin"
    }
    req = requests.post(api_register, headers=head, json=payload)
    print(req.json())

     # VALIDATION
    status_code = req.status_code
    resp_status = req.json()["status"]
    resp_message = req.json()["message"]
    resp_password = req.json()["errors"]["password"][0]

     # ASSERT
    assert_that(status_code).is_equal_to(422)
    assert_that(resp_status).is_false()
    assert_that(resp_message).is_equal_to("Validation error")
    assert_that(resp_password).is_equal_to("The password field is required.")




import requests
from setting.endpoint import api_login
from assertpy import assert_that



def test():
    head ={
        "Accept": "application/json",
        "Content-Type": "application/json",
        # "Authorization": "Bearer 15|M9WvuouyaXiDCoki3LaQMrmI8mjsSR8jdZnHYWI285010cd6",
    }

    payload = {
        "email": "adminexample.com",
        "password": "password1234",

    }
    req = requests.post(api_login, headers=head, json=payload)
    print(req.json())

    # VALIDATION
    status_code = req.status_code
    resp_status = req.json()["status"]
    resp_message = req.json()["message"]
    resp_email = req.json()["errors"]["email"][0]

    # ASSERT
    assert_that(status_code).is_equal_to(422)
    assert_that(resp_status).is_false()
    assert_that(resp_message).is_equal_to("Validation error")
    assert_that(resp_email).is_equal_to("The email field must be a valid email address.")




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
        "email": "admin@example.com",
        "password": "password",

    }
    req = requests.post(api_login, headers=head, json=payload)
    print(req.json())

    # VALIDATION
    status_code = req.status_code
    resp_status = req.json()["status"]
    resp_message = req.json()["message"]

    # ASSERT
    assert_that(status_code).is_equal_to(401)
    assert_that(resp_status).is_false()
    assert_that(resp_message).is_equal_to("Invalid login credentials")





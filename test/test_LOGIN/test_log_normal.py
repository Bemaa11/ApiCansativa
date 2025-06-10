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
        "password": "password12345",

    }
    req = requests.post(api_login, headers=head, json=payload)
    print(req.json())

    # VALIDATION
    statuscode = req.status_code
    resp_id = req.json()["data"]["user"]["id"]
    resp_name = req.json()["data"]["user"]["name"]
    resp_email = req.json()["data"]["user"]["email"]
    resp_access_level = req.json()["data"]["user"]["access_level"]

    # #ASSERT
    assert_that(statuscode).is_equal_to(200)
    assert_that(resp_id).is_not_none()
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_access_level).is_not_none()

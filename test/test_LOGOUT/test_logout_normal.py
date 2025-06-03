import requests
from setting.endpoint import api_login
from setting.endpoint import api_logout
from assertpy import assert_that



def test():
    # ============================= LOGIN USER ==============================
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        # "Authorization": "Bearer 15|M9WvuouyaXiDCoki3LaQMrmI8mjsSR8jdZnHYWI285010cd6",
    }

    payload = {
        "email": "test@example.com",
        "password": "password123",

    }
    req = requests.post(api_login, headers=head, json=payload)
    print(req.json())

    # VALIDATION
    statuscode = req.status_code
    resp_name = req.json()["data"]["user"]["name"]
    resp_email = req.json()["data"]["user"]["email"]
    resp_access_level = req.json()["data"]["user"]["access_level"]
    token = req.json()["data"]["token"]


    #
    # # #ASSERT
    assert_that(statuscode).is_equal_to(200)
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_access_level).is_not_none()
    assert_that(token).is_not_none()


    # ============================= LOGOUT USER ==============================#

    head ={
        "Accept": "application/json",
        # "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    req = requests.post(api_logout, headers=head)


    # VALIDATION
    statuscode = req.status_code

    # # #ASSERT
    assert_that(statuscode).is_equal_to(200)


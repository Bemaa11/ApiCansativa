import requests
from setting.endpoint import api_req_otp
from assertpy import assert_that



def test():
    head ={
        "Accept": "application/json",
        "Content-Type": "application/json",
        # "Authorization": "Bearer 15|M9WvuouyaXiDCoki3LaQMrmI8mjsSR8jdZnHYWI285010cd6",
    }

    payload = {
        "email": "adminexample.com",
    }
    req = requests.post(api_req_otp, headers=head, json=payload)
    print(req.json())

    # VALIDATION
    statuscode = req.status_code
    resp_status = req.json()["status"]
    resp_message = req.json()["message"]
    resp_otp = req.json()["errors"]["email"][0]

    # # #ASSERT
    assert_that(statuscode).is_equal_to(422)
    assert_that(resp_status).is_false()
    assert_that(resp_message).is_equal_to("Validation error")
    assert_that(resp_otp).is_equal_to("The email field must be a valid email address.")

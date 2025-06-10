import requests
from setting.endpoint import api_req_otp
from setting.endpoint import api_res_pass
from assertpy import assert_that



def test():
    # ============================= REQUEST OTP ==============================
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        # "Authorization": "Bearer 15|M9WvuouyaXiDCoki3LaQMrmI8mjsSR8jdZnHYWI285010cd6",
    }

    payload = {
        "email": "admin@example.com",
    }
    req = requests.post(api_req_otp, headers=head, json=payload)
    print(req.json())

    # VALIDATION
    statuscode = req.status_code
    resp_status = req.json()["status"]
    resp_message = req.json()["message"]
    otp = req.json()["data"]["otp"]

    # # #ASSERT
    assert_that(statuscode).is_equal_to(200)
    assert_that(resp_status).is_true()
    assert_that(resp_message).is_equal_to("OTP sent to your email")
    assert_that(otp).is_not_none()

   # ============================= VERIFIKASI OTP ==============================
    head = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    # "Authorization": "Bearer 15|M9WvuouyaXiDCoki3LaQMrmI8mjsSR8jdZnHYWI285010cd6",
    }

    payload = {
    "email": "admin@example.com",
    "otp": otp,
    "password": "password12345",
    "password_confirmation": "password12345"}
    req = requests.post(api_res_pass, headers=head, json=payload)
    print(req.json())


    # VALIDATION
    statuscode = req.status_code
    resp_message = req.json()["message"]

    # # #ASSERT
    assert_that(statuscode).is_equal_to(200)
    assert_that(resp_message).is_equal_to("Password has been reset successfully")

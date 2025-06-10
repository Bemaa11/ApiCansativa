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
        "email": "admin@example.com",
        "password": "password12345",
    }
    # ========== LOGIN USER ==========
    login_req = requests.post(api_login, headers=head, json=payload)
    login_json = login_req.json()
    print("Login Response:", login_json)

    # VALIDATION (from login)
    statuscode = login_req.status_code
    resp_id = login_json["data"]["user"]["id"]
    resp_name = login_json["data"]["user"]["name"]
    resp_email = login_json["data"]["user"]["email"]
    resp_access_level = login_json["data"]["user"]["access_level"]
    token = login_json["data"]["token"]

    # ASSERT
    assert_that(statuscode).is_equal_to(200)
    assert_that(resp_id).is_not_none()
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_access_level).is_not_none()
    assert_that(token).is_not_none()

    # ========== LOGOUT USER ==========
    logout_headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer ",
    }
    logout_req = requests.post(api_logout, headers=logout_headers)
    logout_json = logout_req.json()
    print("Logout Response:", logout_json)

    # ASSERT
    assert_that(logout_req.status_code).is_equal_to(401)
    assert_that(logout_json["message"]).contains("Unauthenticated.")

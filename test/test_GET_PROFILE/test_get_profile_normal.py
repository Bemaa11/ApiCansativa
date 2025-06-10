import requests
from assertpy import assert_that
from setting.endpoint import api_get_profile


def test():
    head = {
        "Accept" : "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 8|krySy127N54gG7dj8bkZXB2xVTLLXBZugdAN0sTO74ddb575"

    }
    req = requests.get(api_get_profile, headers=head)
    print(req.json())


    # VALIDATION
    statuscode = req.status_code
    resp_status = req.json()["status"]
    resp_message = req.json()["message"]
    resp_id = req.json()["data"]["user"]["id"]
    resp_name = req.json()["data"]["user"]["name"]
    resp_email = req.json()["data"]["user"]["email"]
    resp_access_level = req.json()["data"]["user"]["access_level"]

    # # #ASSERT
    assert_that(statuscode).is_equal_to(200)
    assert_that(resp_status).is_true()
    assert_that(resp_message).is_equal_to("Success")
    assert_that(resp_id).is_not_none()
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_access_level).is_not_none()

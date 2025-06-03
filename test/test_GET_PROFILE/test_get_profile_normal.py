import requests
from assertpy import assert_that
from setting.endpoint import api_get_profile


def test():
    head = {
        "Accept" : "aplication/json",
        "Content_Type": "aplication/json",
        "Authorization": "Bearer 55|EVzmRT3HXMAKyvQJPLL3gtTxiJtzOHTeokejd2ya797238d3"

    }
    req = requests.get(api_get_profile, headers=head)
    print(req.json())


    # VALIDATION
    statuscode = req.status_code
    resp_name = req.json()["data"]["user"]["name"]
    resp_email = req.json()["data"]["user"]["email"]
    resp_access_level = req.json()["data"]["user"]["access_level"]

    # # #ASSERT
    assert_that(statuscode).is_equal_to(200)
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_access_level).is_not_none()

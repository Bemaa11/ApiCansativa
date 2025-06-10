import requests
from assertpy import assert_that
from setting.endpoint import api_get_profile


def test():
    head = {
        "Accept" : "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer asadaaaa"

    }
    req = requests.get(api_get_profile, headers=head)
    print(req.json())


    # VALIDATION
    statuscode = req.status_code
    resp_message = req.json()["message"]


    # # #ASSERT
    assert_that(statuscode).is_equal_to(401)
    assert_that(resp_message).is_equal_to("Unauthenticated.")

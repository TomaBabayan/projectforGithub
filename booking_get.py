import pytest
import requests
import allure

@allure.feature('??')
@allure.description("???")
def test_get_all_booking():
    response = requests.get('https://restful-booker.herokuapp.com/booking')
    assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    data = response.json()
    assert len(data) > 0, 'Expected at least one booking, but got an empty list'


def test_get_one_booking():
    response = requests.get('https://restful-booker.herokuapp.com/booking/1')
    assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    data = response.json()
    assert 'firstname' in data, 'Missing firstname in booking details'
    assert 'lastname' in data, 'Missing lastname in booking details'
    assert 'totalprice' in data, 'Missing totalprice in booking details'
    assert 'depositpaid' in data, 'Missing depositpaid in booking details'
    assert 'bookingdates' in data, 'Missing bookingdates in booking details'

    assert 'checkin' in data['bookingdates'], 'Missing checkin date in bookingdates'
    assert 'checkout' in data['bookingdates'], 'Missing checkout date in bookingdates'

    assert 'additionalneeds' in data, 'Missing additionalneeds in booking details'




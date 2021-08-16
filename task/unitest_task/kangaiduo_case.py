import unittest
from kangaiduo_method import HttpRequests

login_url = 'https://user.360kad.com/Login/AjaxLoginV2'
login_body = {"userName": 15900571886, "pass": "123zhc", "isRemberName": "false", "loginPlatform": 1}
add_car_url = 'https://www.360kad.com/cart/AddCart?id=67886&quantity=1&buyType=0&sellerCode=&rd=0.25383327657350985'


class TestLoginMethod(unittest.TestCase):
    def test_login_forward(self):
        res = HttpRequests.http_requests("post", login_url, data=login_body)
        self.assertIn("登录成功", res.text)

    def test_login_reverse(self):
        pass


if __name__ == '__main__':
    unittest.main()

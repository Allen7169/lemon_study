import requests


class HttpRequests(object):
    """
    利用requests封装get请求和post请求
    """
    @classmethod
    def http_requests(cls, method, url, data=None, cookie=None):
        if method.lower() == "post":
            res = requests.post(url, data)
            print(res.text)
            return res
        elif method.lower() == "get":
            res = requests.post(url, cookies=cookie)
            print(res.json())
            return res


if __name__ == '__main__':
    login_url = 'https://user.360kad.com/Login/AjaxLoginV2'
    login_body = {"userName": 15900571886, "pass": "123zhc", "isRemberName": "false", "loginPlatform": 1}
    HP = HttpRequests()
    res_login = HP.http_requests(method="post", url=login_url, data=login_body)

    add_car_url = 'https://www.360kad.com/cart/AddCart?id=67886&quantity=1&buyType=0&sellerCode=&rd=0.25383327657350985'
    HP.http_requests(method="get", url=add_car_url, cookie=res_login.cookies)



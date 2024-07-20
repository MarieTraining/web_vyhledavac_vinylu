from flask import request
import json

class Cookie_Manager:
    def __init__(self, cookie_name):
        self.cookie_name = cookie_name

    def get_cookie(self, hledany_vyraz):
        cookie_value = request.cookies.get(self.cookie_name)
        if cookie_value:
            list_of_cookies = json.loads(cookie_value)
        else:
            list_of_cookies = []
        if hledany_vyraz != None : 
            list_of_cookies.append(hledany_vyraz)
        return (list_of_cookies)

    def set_cookie(self, response, list_of_cookies):
        response.set_cookie(self.cookie_name, json.dumps(list_of_cookies))
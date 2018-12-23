#!/usr/bin/python
#coding = utf-8
from typing import Union,List
class User_List:
    def __init__(self):
        self.User = []
        self.Password = []
        return None

    def _add_user(self,usename:str,password:str) -> None:
        self.name = usename
        self.User.append(self.name)
        self.password = password
        self.Password.append(self.password)
        return self.User,self.Password

test_us = User_List()
test_us._add_user("zhaixiaofan","123")
print(test_us.User,test_us.Password)
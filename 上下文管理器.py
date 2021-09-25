class User(object):
    def __init__(self, username, password):

        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def __enter__(self):
        print('before：auto do something before statements body of with executed')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('after：auto do something after statements body of with executed')


if __name__ == '__main__':
    # boy = User('faker', 'faker2021')
    # print(boy.password)
    print("上下文管理器with语句：")
    with User('faker', 'faker2021') as user:
        print(user.password)
    print('---------end-----------')
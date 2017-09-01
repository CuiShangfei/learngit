import time
import hashlib

db = {}
def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    print('注册成功，请登录')

def login(username, password):
    if username not in db:
        print('用户不存在！')
    elif db[username] == get_md5(password + username + 'the-Salt'):
        print('登陆成功！')
    else:
        print('用户名或密码错误！')

print('请注册')
print('请输入用户名和密码！')
username = input('username = ')
password = input('password = ')
time.sleep(1)
register(username,password)
time.sleep(1)
print('请登入！')
username = input('username = ')
password = input('password = ')
print('正在登录。。。')
time.sleep(1)
login(username,password)

#login page
d={}
print('registration page-------')
d.setdefault('name',input('enter username'))
d.setdefault('pass',input('enter password'))

print('log in page-------')
username=input('enter username')
password=input('enter username')

if username==d['name'] and password==d['pass']:
    print('access granted')
else:
    print('access denied')

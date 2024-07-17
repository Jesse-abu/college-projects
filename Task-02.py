user, code = 'AJames273', 'p@ssword123'
print('Secure Login')
name, key = input('Username: '), input('Password: ')
if name != user and key != code:
    print('Invalid Login: go away!')
else:
    print(f'Welcome {user}')

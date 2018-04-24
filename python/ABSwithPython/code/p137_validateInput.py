while True:
    print('年齢を入力して下さい: ')
    age = input()
    if age.isdecimal():
        break
    print('年齢は数字で入力して下さい。')

while True:
    print('新しいパスワードを入力して下さい（英数字のみ）: ')
    password = input()
    if password.isalnum():
        break
    print('パスワードは英数字で入力して下さい。')


import sys

while True:
    print('終了するには exit と入力して下さい ')
    response = input()
    if response == 'exit':
        sys.exit()
    print(response + 'と入力されました')


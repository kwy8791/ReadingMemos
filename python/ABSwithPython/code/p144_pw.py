#! python3

PASSWORDS = {'email': 'jka;ldkfjaweoaigvjagwei',
             'blog': 'Ffa;oeijrweofmnwf324fm',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: python3 pw.py アカウント名')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1] # 最初のコマンドライン引数がアカウント名

if account in PAWWSORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウントは存在しません')


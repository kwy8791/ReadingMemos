- インクリメント、デクリメントに ++/-- は存在しない。 +=/-= を使う

- 変数名はスネークケース（ _ でつなぐ ）で記述

- 変数名の頭に数字は使えない。また、アンダースコアで始まる変数には特殊な意味がある（ P28 時点）

- / の結果は自動的に float になる。整数値を得たい場合は // を使う 

- 算術演算は「カッコ、累乗、（掛け算、割り算）、（足し算、引き算）」の順に優先される

- and, or は1つの文に複数回使用できる

- （用語）文には単純文と複合文がある。複合文の例は if 文。複合文は1行のヘッダー部分（条件判断部分とか）と、それに続くスイート部分で構成されている

- ヘッダー部分はコロンで終わる

- switch は無い。

- elif 族

- インデントの前にはコロンが必要と覚えておけばいい？

- 関数宣言は
```
def 関数名:
    内容
```

- 関数定義に result がない場合は None が返る

- オプション引数は必須引数の後に記述する

- ローカルスコープからグローバル変数の値をいじる際は、 global キーワードを付ける
  - p63_interscope.py

- 例外処理の書き方は以下スクリプトを参考に
  - p65_exception.py
  - p67_exceptions.py
  - 
  - 
  - 

- 例外処理は、ざっくり「例外の代わりに except ブロックのコードが実行される」と思っておく？

- except 節内で、 try 節で定義した変数は使用しない。理由は「変数定義の前に例外が起きていた場合、 except 節内で新たな例外が発生するから」
  - p67_exception_in_except_clause.py

- 関数宣言の次に、 docstring （ドキュメンテーション文字列）と呼ばれるコメントを書く。
  - 最初の行で「この関数が何をするか」を書く
  - 残りの行で「引数、引数の型、関数が返す値」について書く
    - p67_docstring.py

- コンテナ

| 種類 | 記号 | mutable | 呼出し |
|:-----|:-----|:-------:|:-------|
|リスト|[]    |yes      |インデックス|
|タプル|()    |no       |インデックス|
|辞書  |{}    |yes      |key|

- コンテナの中にコンテナを格納することができる。この場合、要素となるコンテナを変更すると、上位のコンテナも更新される
  - p83_containers_in_a_container.py

- コンテナには set という型もある。これは集合を扱うもので、要素の重複がなく、また、要素の順番を持たないという特徴がある。簡単な例は

```python
set1 = set([1, 2, 3])
set2 = set([1, 2, 3, 3, 1])
print(set1)
print(set2)

set1.add(4)
print(set1)

set1.remove(2)
print(set1)

set1.clear()
print(set1)
```

- 添字を使った文字列操作時、範囲外の添字を使用するとエラー（ IndexError ）になる

- 文字列はイミュータブルなので、文字の変更を行う際は新しい文字列を作成する必要がある
  - 文字の置換えであれば replace メソッドを使う手もある

- format メソッドを使った書式操作
  - p92_format.py

- format メソッドはプログラム利用者が入力した文字を使って文字列を組み立てる時に便利

- split メソッドは指定した文字で区切った文字列をリストにして返す

- join メソッドは各文字間に指定した文字列を追加する

- index メソッドは指定した文字が最初に現れた部分のインデックスを返す

- in / not in 演算子を使用して、指定した文字が文字列内に存在するか否かの判定ができる

- for ループ

```
for 変数名 in イテラブル :
    コードブロック
```

例
```python
name = "Ted"
for character in name:
    print(character)
```

- 文字列から文字、リストやタプルの要素、辞書のキーなどを取得できる

- for ループを使用してリストなどのミュータブルないてラブルを更新できる
  - p106_change_by_for.py
  - p107_change_by_for2.py （enumarate 関数を使用してインデックスを自動的に取得した例）
  - p07_double_list.py

- ループは入れ子にできるが、何段も重ねると可読性が落ちる。3段ループを書くときには「なにかマズい事が起きていないか」と疑ってみると良い
 
- モジュールの読み込みは import
  - p118_import.py

- 自作モジュールの読み込み例
  - p121_hello.py
  - p121_project.py

- モジュールを import すると、そのモジュールの内容がすべて実行される（ print があれば標準出力に表示されるなど）
  - これを避けるには import されるモジュールを `if __name__ == "__main__": ` という文の下に書くようにする（P.123 時点での原理説明無し）

- ファイルを読み書きする際には、組み込み関数 open を使用する。
  - p126_file_basic.py
  - p126_file_basic_jp.py

- ファイルパスは手書きではなく、 os モジュールを使用する

- r: read, w: write, w+: read write

- open 関数は、ファイルオブジェクトと言われるオブジェクトを返す。このファイルオブジェクトを介してファイルを読み書きする。

- close 忘れを防止する方法として、ファイルオブジェクトを使うすべてのコードを with 文の中に書く、というものがある

```
with open(ファイルパス, モード) as 変数名:
    コード

```

  - p126_with.py

- CSV ファイルも組み込みの csv モジュールで操作できる

- Python ではクラス名はキャメルケースで記述する

```
class クラス名:
    スイート

```

- Python の慣習として、1つ目の必須な引数には self という名前を使う。この引数は、このメソッドを呼び出す時に使ったオブジェクトで、 Python が自動的に渡してくれる。

- self 変数は、インスタンス変数の定義に使う。

- 通常、インスタンス変数は __init__ という特別なメソッドの中で定義され、オブジェクトを作る時に Python から呼び出される
  - p151_class.py

- __init__ のように、二重のアンダースコアで囲まれたメソッドは、特殊メソッドと呼ばれ、 Python がオブジェクトの作成など特別な目的で使用する

- オブジェクトを作成することを、クラスのインスタンス化、と言う
  - p151_class2.py
  - p152_class3.py
  - p154_class4.py

- インスタンス変数を client(クラスの外側からオブジェクトを利用するコード) から直接変更してはいけない。なぜならば、クラス変数の定義が変わった際に、 client 側のコードにも変更が必要になるからだ。この問題に対しては、変数を変更するメソッドを別途定義して、 client は常にそれを利用するようにすることで回避する。

- Python にはプライベート変数がない。その代わり、 client から直接アクセスされたくない変数やメソッドには、名前の前にアンダースコアをつけることになっている（ただし、あくまでも慣例なので、自己責任で使用することは可能）
  - p160_underscore.py

- 子クラスを作る時は、クラスの引数に親クラスの名前を入れる
  - p166_inheritance.py

- コンポジションは「 has-a 関係」を表し、別クラスのオブジェクトを変数としてもたせる。
  - p167_composition.py

- self.hoge はインスタンス変数。 fuga はクラス変数。クラス変数はそのクラスから作られたインスタンスオブジェクトのどこからでも利用できるデータとして使うことができる
  - p172_class_variables.py

- クラス変数の定義は __init__ メソッドの外で行う。クラスオブジェクトを通してクラス変数にアクセスするときには __init__ は呼ばれない（呼ばれるのはクラスのインスタンスを作成したときのみ）

- is キーワードは、前後のオブジェクトが同一なら True を、異なるなら False を返す

- p185_war.py は後で読み直すこと

- Windows での Bash の使い方
  - http://www.atmarkit.co.jp/ait/articles/1608/08/news039.html

- 非貪欲な正規表現: できるだけ少ない文字列に一致する。Linux の grep には存在しないが、 Python では "*?" という書き方で実行できる。詳しくはP212
  - p213_mad_libs.py

- pipインストール方法
  - https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip

- pip 実行時は sudo する（ユーザーごとのインストールではない場合）

- パッケージ一覧表示は `pip freeze` アンインストールは `pip uninstall パッケージ名` 

- とりあえず `git clone リポジトリURL`, `git remote -v`, `git status`, `git add ファイルパス`, `git reset ファイルパス` （ add の取り消し）, `git commit -m "コミットメッセージ"`, `git push origin master` を覚える

- チーム開発で、中央リポジトリのほうが新しくなった場合は `git pull origin master`

- 以前のバージョンに戻すには `git log` で目的のバージョンのハッシュを探し、 `git checkout ハッシュ` する

- Git の詳細は
  - http://theselftaughtprogrammer.io/git
  - https://www.udemy.com/intro_git/
  - https://learngitbranching.js.org/

- Windows Subsystem for Linux の Ubuntu ファイルをエクスプローラーから見る場合 %AppDataLocal%\Packages\CanonicalGroupLimited.UbuntuonWindows_(ランダムな文字列)\LocalState\rootfs\home\(username) がホームディレクトリになる。ただしWindows 側からファイル操作を行うと、不具合が起きることが多いので触らないようにする

- スタックとキューのサンプルは以下ファイル。読んでおこう。なお、キューは Python の組み込みクラス collections.deque で実装されている。
  - p249_stack.py
  - p251_stack2.py
  - p253_queue.py

- これも後で読んでおく
  - p255_ticket_line.py

- FizzBuzz, 線形探索、回文、アナグラム
  - p259_fizzbuzz.py
  - p260_linear_search.py
  - p261_palindrome.py
  - p261_anagram.py

- 再帰
  - p264_recursive.py
  - http://wa3.i-3-i.info/word14899.html
  - http://www.geocities.jp/m_hiroi/light/pyalgo01.html

- 自習用ドリルサイト （どちらも登録必要）
  - https://leetcode.com
  - https://pyq.jp （三日間無料のキャンペーンコードが本書に記載）

- 解決したい問題を前にして最初に考えるべきは「どうやってこれを解こうか」ではなく、「ほかの誰かがすでにこの問題を解決しているだろうか？　その解決方法は自分も使えるだろうか？」である

- 直交性: a は b に影響するべきではない

- データは一箇所で定義する

- 1つの関数には1つのことだけをさせる
  - 「ソフトウェアの複雑さは、1つのことに2つのことをさせてしまうことから生じる」

- PEP8 を読んで Python の慣例を学ぶ
  - http://pep8-ja.readthedocs.io/ja/latest
  - https://www.python.org/dev/peps/pep-0008/

- logging モジュールを有効に使う
  - https://docs.python.org/ja/3/howto/logging.html

- unittest モジュールを使う
  - https://docs.python.org/ja/3/library/unittest.html

- 仕事にはどんな種類があるのかを知る
  - https://www.python.jp/category/jobboard.html
  - https://www.python.org/jobs/


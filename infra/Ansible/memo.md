- 自動化に対する成熟度に併せて適用範囲を特定すると効率的
  * バージョン管理: 日常作業全体に置いて、インフラリソースの変更情報を記録し、過去のある時点の状態を復元したり変更内容の差分を表示したりできる
  * 継続的インテグレーション: 開発環境のデプロイ、テストに置いて、定期的かつ反復可能な作業を自動化し、繰り返し実行できる
  * 継続的デリバリー: 本番環境に置いて、テスト済みのサービスが、完全な状態で継続的にリリースできる
  * 継続的アセスメント、継続的オペレーション: 運用業務の一環として、サービスのリリースに対する評価ができ、継続的なサービス改善が提示できる

- Ansible 単体にはテスト機能が含まれていないため、テストは別途用意する必要がある

-----

## Ansible のインストール

- 推奨はpip からのインストール
- OS パッケージマネージャーは、stable だが進歩についていけないことも
- ソースコードからは、最新すぎることも

- pip からインストールする場合は、virtualenv を利用して仮想実行環境内にAnsible をインストールするのがおすすめ
  - virtualenv は同一Python バージョン内で異なるPython ライブラリの利用環境を切り替えるためのツール

- ざっくり
```
yum install curl
curl -kL "https://bootstrap.pypa.io/get-pip.py" |sudo python
sudo pip install virtualenv
cd
virtualenv venv
source venv/bin/activate
pip install ansible
```
  - インストール完了後は必ずvirtualenv を有効にしてからAnsible を利用する

- 事前作業
  - Ansible 運用ユーザーの作成 sys_ops:sys_ops
  - SSH 公開鍵認証の設定
  ```
  ssh-keygen -t rsa -b 4096
  ssh-copy-id -o StrictHostKeyChecking=no -i $HOME/.ssh/id_rsa.pub localhost
  ssh-copy-id -o StrictHostKeyChecking=no -i $HOME/.ssh/id_rsa.pub REMOTE_HOST
  ```
  - 作業ディレクトリの作成 $HOME/ansible
  - ansible.cfg の設定 $HOME/.ansible.cfg

- ansible.cfg のパラメーター（抜粋）
  - forks: ターゲットノードでの並列処理数
  - log_path: 実行コマンドログのパス
  - host_key_checking: ターゲットノードにSSH 接続するときの公開鍵のフィンガープリントチェックを行うかどうか
  - gathering: ターゲットノードの詳細情報取得に関する設定
    - implicit: キャッシュが無視され、常に情報収集がおこなわれる
    - explicit: キャッシュを利用し、情報収集がおこなわれない
    - smart: 新規に接続した場合のみ情報収集をおこなう
  - transport: ターゲットノードへの接続方法
    - smart: OpenSSH かControlPersist 機能対応時にはOpenSSH 接続を行い、未対応であればPython モジュールのparamiko を利用する
    - paramiko: Python のssh 機能で、アクションのたびに各ホストに再接続する
    - local: SSH を利用せずに、直接ローカルホストに接続する

  * 


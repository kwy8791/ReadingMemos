# IT 技術者のための現場ノウハウ　CentOS7 実践ガイド
### 古賀政純
### ISBN978-4-8443-3753-9

- P.34 GRUB2 の設定の基本は、/etc/default/grub ファイルの編集と、grub-mkconfig コマンドによる設定ファイルの生成です。GRUB2 の設定ファイル/etc/default/grub にパラメーターを設定し、grub2-mkconfig によって、その設定を含んだファイル/boot/grub2/grub2.cfg を生成します。
- P.36 /boot/grub2/grub.cfg ファイルは直接編集せず、/etc/grub.d/40_customファイルを利用する。このファイルにカスタムのエントリを追加できる。
- P.45 HDD イメージの転送（レスキューモード）
```
time dd if=/dev/sda bs=1k |gzip -c |ssh 172.16.25.4 "cat > /backup/n01sda_c70_20151007.img.gz"
```
- systemctl のいろいろ
  - systemctl get-default : ランレベルの確認
  - systemctl list-units --type=target --all --no-pager : 利用可能なターゲット一覧を表示
  - systemctl set-default graphical.target : グラフィカルターゲットをデフォルトにする
  - systemctl isolate rescue.target : 再起動なしにシングルユーザーモードに遷移する
- systemd とランレベルの対応
| 状態                   | CentOS6  | systemd                             |
|:-----------------------|:---------|:------------------------------------|
| システム停止           |0         | systemctl isolate poweroff.target   |
| シングルユーザーモード |1         | systemctl isolate rescue.target     |
| マルチユーザーモード   |3         | systemctl isolate multi-user.target |
| グラフィカルログイン   |5         | systemctl isolate graphical.target  |
| OS 再起動              |6         | systemctl isolate reboot.target     |
| 緊急モード             |-         | systemctl isolate emergency.target  |
- systemd の管理の単位となるユニットには以下のタイプが有る
  - service : 各種デーモンやサービスの起動
  - target : 起動プロセスやサービスなどの複数のユニットをグループにしてまとめたもの
  - mount : ファイルシステムのマウントポイント制御
  - device : ディスクデバイス
  - socket : FIFO, UNIX ドメインソケット、ぽ＾と番号などに関する通信資源
- systemd とinit の対応
| 状態                           | init                      | systemd                                                               |
|:-------------------------------|:--------------------------|:----------------------------------------------------------------------|
| サービスの開始                 | service httpd start       | systemctl start httpd                                                 |
| サービスの停止                 | service httpd stop        | systemctl stop httpd                                                  |
| サービスの再起動               | service httpd restart     | systemctl restart httpd                                               |
| サービス設定ファイルの読み込み | service httpd reload      | systemctl reload httpd                                                |
| サービスの状態確認             | service httpd status      | systemctl status httpd                                                |
| サービス起動時に再起動する     | service httpd condrestart | systemctl condrestart httpd                                           |
| 次回OS起動時に自動起動する     | chkconfig httpd on        | systemctl enable httpd                                                |
| 次回OS起動時に自動起動しない   | chkconfig httpd off       | systemctl disable httpd                                               |
| ランレベルごとの有効/無効表示  | chkconfig --list          | systemctl -t service list-unit-files / ls /etc/systemd/system/*.wants |
- システムのロケールについて
  - `localectl` : 現在のロケールの状態を表示する
  - `localectl set-locale LANG=ja_JP.utf8` : ロケールを変更する
  - `cat /etc/locale.conf` : ロケールの設定が変更されていることを確認する
- キーボード設定について
  - `localectl list-keymaps` : 利用可能なキーマップを表示する
  - `localectl set-keymap jp106` : 日本語106キーボードに設定する
  - `cat /etc/vconsole.conf` : 設定が反映されていることを確認する。
- 日付、時刻、タイムゾーンについて
  - `timedatectl` : 現在の日付、時刻、タイムゾーン、NTP の同期設定の有無などを表示する
  - `timedatectl set-time 2014-09-06` : システム日付を設定する
  - `timedatectl set-time 19:51:00` : システム時刻を設定する
  - `timedatectl set-time "2014-09-06 19:55:00"` : 日付と時刻の一括設定
  - `timedatectl list-timezones` : タイムゾーンの表示
  - `timedatectl set-timezone Asia/Tokyo` : タイムゾーンの設定
- `systemctl status systemd-journald` : journald の起動確認
- `journalctl -b` : ブートログの確認
- `journalctl --since="2014-09-05 01:23:45" --until="2014-09-07 04:56:00"` : 時間帯によるフィルタリング
- `jounalctl --since="2013-09-05 01:23:45" --until="2014-09-07 04:56:00" -u sshd.service` : サービスのユニット名によるフィルタリング
- `journalctl --since=today` : 単純な時刻フィルタリング。yesterday, tommorow の指定も可能
- `journalctl -f` : tail -f チックな使い方
- `journalctl -p プライオリティ` : emerge, alert, crit, err, warning, notice, debug が指定可能
- `journalctl -k` : カーネルログのみの表示
- `journalctl _PID=12345` : PID 12345 についてのログのみを出力
- OS 再起動後もログが保管されるようにするためには、journald の設定ファイル /etc/systemd/journald.conf で、 `Storage=persistent` を指定して、journald を再起動する。
- ログに使用するディスク容量を制限するには、 /etc/systemd/journald.conf で、 `SystemMaxUse=128M` の用に指定して、journald を再起動する
- 現在ログに使用しているディスク量を確認するには、 `journalctl --disk-usage` を実行する
- nmcli コマンド
  - nmcli connection : 現在の接続状態を表示する
  - nmcli connection show : 現在の接続状態を表示する
  - nmcli connection down eno1 : インターフェースeno01 を切断
  - nmcli connection up eno1 : インターフェースeno01 を接続
  - nmcli device : インターフェースのデバイス名とその状態を表示する
  - nmcli device show : 各デバイスの詳細を表示する
  - nmcli connection modify eno1 ipv4.addresses "10.0.0.82/24 10.0.0.1" : IPアドレスとゲートウェイの設定（この後に切断/接続が必要）
  - nmcli connection modify eno1 ipv4.dns "10.0.0.254 10.0.0.253" : DNS サーバーの設定
  - nmcli connection modify eno1 ipv4.route "10.0.0.0/24 10.0.0.1" : 静的ルーティングの設定
  - nmcli general hostname : ホスト名の確認
  - nmcli general hostname ホスト名 : ホスト名の設定（/etc/hostname を直接編集しても良い）
- iproute パッケージに含まれるコマンド一覧
| コマンド          | 機能                                                               |
|:------------------|:----------------------------------------------------------------------|
| /usr/sbin/arpd    | ARP キャッシュの更新やIP アドレスの重複の検出に利用されるGratuitousARP 情報を収集するデーモン                                                 |
| /usr/sbin/bridge  | ブリッジデバイスの操作、表示、監視を行う                                                  |
| /usr/sbin/cbq     | ネットワークを流れるパケットのキューイングの仕組みを提供する。帯域制限などに用いられる                                               |
| /usr/sbin/ctstat  | lnstat コマンドへのシンボリックリンク                                                |
| /usr/sbin/genl    | netlink ライブラリのフロントエンドを提供する                                                |
| /usr/sbin/ifcfg   | ip コマンドのラッパースクリプト。IP アドレスの追加、削除などをおこなう |
| /usr/sbin/ifstat  | ネットワークインターフェースの統計情報を出力する |
| /usr/sbin/ip      | ルーティング、ネットワークデバイスなどを設定、管理する |
| /usr/sbin/lnstat  | キャッシュされているルーティングの各種統計情報を表示する |
| /usr/sbin/nstat   | ネットワークインターフェースの統計情報やSNMP カウンタを監視する |
| /usr/sbin/routef  | ルーティング情報をフラッシュする |
| /usr/sbin/routel  | ルーティング情報をリストアップする |
| /usr/sbin/rtacct  | ネットワークインターフェースの統計情報やSNMP カウンターを監視する |
| /usr/sbin/rtmon   | ルーティングテーブルの更新を監視する |
| /usr/sbin/rtpr    | tr コマンドのラッパースクリプト |
| /usr/sbin/rtstat  | lnstat コマンドへのシンボリックリンク |
| /usr/sbin/ss      | ソケットの統計情報、TCP/UDP 情報、タイマー、各種ネットワークサービスの接続情報などを表示する |
| /usr/sbin/tc      | ネットワークトラフィックの制御をおこなう |
- ip コマンド
  - ip a : IP アドレス、MAC アドレスの確認
  - ip addr add 192.168.0.82/255.255.255.0 dev eno3 : eno3 にIPアドレスを付与（一時的）
  - ip link : NIC のリンクアップの確認
  - ip route add default via 192.168.0.254 : デフォルトゲートウェイの追加
  - ip route del default via 192.168.0.254 : デフォルトゲートウェイの削除
  - ip neigh : ARP テーブルの確認
  - ip neigh flush 172.16.1.115 dev enp0s25 : ARP キャッシュのクリア
  - ip -s l : インターフェースごとのパケットの確認
  - ss -ant : TCP ソケットの状態の確認
  - ss -anu : UDP ソケットの状態の確認
- CentOS 7 でのNIC チーミング設定
```
# yum install -y teamd
# nmcli connection add type team con-name team0 ifname team0 config '{"runner": {"name": "roundrobin"}}'
# nmcli connection modify team0 ipv4.method manual ipv4.addresses "172.16.70.99/16 172.16.1.1" ipv4.dns 172.16.1.1
# nmcli connection add type team-slave autoconnect no ifname eth0 master team0
# nmcli connection add type team-slave autoconnect no ifname ens7 master team0
# systemctl restart network
# nmcli connection modify team-slave-ens7 connection.autoconnect yes
# ip a
# cat /etc/sysconfig/network-scripts/ifcfg-team0
# cat /etc/sysconfig/network-scripts/ifcfg-team-slave-eth0
# cat /etc/sysconfig/network-scripts/ifcfg-team-slave-ens7
```
- runner の種類
| runner       | 機能                                                               |
|:-------------|:----------------------------------------------------------------------|
| broadcast    | 全てのポートにブロードキャストで伝送される |
| roundrobin   | 全てのポートを順にラウンドロビンで伝送される |
| activebackup | 通信をおこなうアクティブなポートと障害時のバックアップ用のポートで構成する |
| loadbalance  | 負荷分散でデータが伝送される |
| lacp         | 802.3ad で規定されたポート同士のネゴシエーションのためのプロトコル |
- CentOS7 からはNIC のネーミングルールが変わったが、これをCentOS6 以前と同様の命名規則にするには
  - /etc/default/grub のGRUB_CMDLINE_LINUX に渡すパラメーターに、 `net.ifnames=0 biosdevname=0` を追記する
  - `grub2-mkconfig -o /boot/grub2/grub.cfg`
  - reboot
- firewalld-cmd
  - firewalld-cmd --state : firewalld サービスの起動状態確認
  - firewalld-cmd --get-zones : firewalld で現在管理対象になっている全てのゾーン名を表示する
  - firewalld-cmd --get-active-zones : 現在アクティブになっているゾーンの表示
  - firewalld-cmd --parmanent --zone=public --add-service=nfs : public ゾーンに NFS サービスを追加する
  - firewalld-cmd --parmanent --zone=public --remove-service=nfs : public ゾーンから NFS サービスを削除する
  - firewalld-cmd --reload : 変更した設定を反映する
  - firewalld-cmd --zone=public --list-services : public ゾーンとサービスの紐付けを確認する
  - firewalld-cmd --list-all : 全てのゾーンとサービスの紐付けを確認する
- firewalld によるIP マスカレード
  - /etc/sysctl.conf の `net.ipv4.ip_forward = 1` を設定する
  - firewalld-cmd --get-active-zones
  - firewalld-cmd --permanent --zone=trusted --change-interface=ens7
  - systemctl restart firewalld
  - firewalld-cmd --get-active-zones
  - firewalld-cmd --permanent --zone=public --add-masquerade
  - firewalld-cmd --reload
  - firewalld-cmd --list-all --zone=public
  - firewalld-cmd --list-all --zone=trusted
- PXE サーバーの構築
  - 省略
- 全自動インストールISO イメージの作成
  - CentOS7 のオリジナルISO イメージを/root/dvd/ ディレクトリにコピーしマウントしたイメージの内容全てを /root/ksiso ディレクトリにコピーする
  - isolinux ディレクトリにあるisolinux.cfg ファイルを作成する
```
default linuxks
timeout 50
label linuxks
  menu label ^Kickstart Install CentOS 7
  kernel vmlinuz
  append initrd=initrd.img inst.stage2=hd:LABEL=CentOS\x207\x20x86_64 xdriver=vesa nomodeset inst.ks=cdrom:/dev/cdrom:/ks.cfg inst.geoloc=0
```
  - /root/ksiso/ks.cfg を作成する
```
#version=RHEL7
install
text
cdrom
firewall   --disabled
selinux    --disabled
authconfig --enableshadow --passalgo=sha512
keyboard   --vckeymap=us  --xlayouts='us'
lang       en_US.utf8
network    --bootproto=static --device=eno1 --gateway=172.16.1.1 --ip=172.16.1.254 --netmask=255.255.255.0 --noipv6
timezone   Asia/Tokyo --nontp
rootpw     --iscrypted hogefuga
user       --name=fugahoge --password=hoge --iscrypted
bootloader --location=mbr --boot-drive=sda
ignoredisk --only-use=sda
part biosboot --asprimary --fstype="biosboot" --size=1
part /boot    --asprimary --fstype="xfs"      --size=500
part swap     --asprimary --fstype="swap"     --size=1024
part /        --asprimary --fstype="xfs"      --size=1    --grow
reboot
firstboot --disabled
services --enabled=NetworkManager,sshd
eula --agreed
skipx

%pre
/usr/sbin/parted -s /dev/sda mklabel gpt
%end

%packages --ignoremissing
@core
%end
```
  - yum install -y genisoimage
  - cd /root/ksiso
  - mkisofs -o /root/cents7ks.iso -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -V 'CentOS 7 x86_64' -boot-load-size 4 -boot-info-table -R -J -v -R ./
  - 出来上がったcentos7ks.iso をメディアに焼き付ける


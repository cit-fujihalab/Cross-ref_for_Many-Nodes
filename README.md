# Failure-resistance
<br>4月27日 実行方法追記

## 必要モジュール
$ apt install python3-pip

$ pip3 install numpy

pycrypto<br>
$ pip3 install PyCryptodome

websocket<br>
$ pip3 install websocket_server==0.4<br>
↑バージョン指定しないと実行不可

websocket<br>
$ pip3 websocket_client

leveldb<br>
$ pip3 install plyvel

tkinter<br>
$ apt-get -y install python3-tk

以上のモジュールのインストールが必要.<br>
一括インストールを行う場合は, <br>
equirements.shでインストールすることができる.

## 実行方法
実行するうえでIPアドレスとPORT番号の設定が必要である.<br>
APP/settings.py内<br>
<br>IPアドレスの変更(1行目):HOST_IP_LAYER_0 = 'xx.xx.xxx.xx'
<br>ポート番号の変更(18行目):HOST_PORT_LAYER_0_origin
sh 0_domain_start_up.sh

sh X-X_domain_start_up.sh
<br>必要なノード数分実行（改変したりなどにして）

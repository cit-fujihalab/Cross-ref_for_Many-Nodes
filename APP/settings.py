HOST_IP_LAYER_0 = '10.84.240.77'
# HOST_IP_LAYER_0 = '10.0.2.15'
LEADER_UPDATE_INTERVAL = 20 # ハートビートを送る間隔 [min]
LEADER_CHECK_INTERVAL =  30 # リーダーが故障不在じゃないか確認するループのインターバル [min]
FAILURE = False
CR_INTERVAL = 600
ALLOWABLE_TIME = 90 # HEART_BEATの検証許容時間[min]
tkinter_state = False # tkinterを起動するかどうか.
CR_STATE = True # 履歴交差を行うか.

MINIMUM_DOMAIN = 3 # 履歴交差を開始させる最低ドメイン数
NEW_CONNECTION = 60 # [sec] 新しい接続があった場合はNEW_CONNECTION
CONFIRMED_BLOCK = 3 # 確定ブロック 履歴交差で共有するブロック
REF_RECHECK = 1 # [sec] 履歴交差部未完時の再チェック待ち時間
MINING_BLOCK_CHECK = 5 # [sec] 履歴交差ブロックマイニングの再チェック待ち時間


HOST_PORT_LAYER_0_origin = 50050 # 0番目のオリジンノードのポート番号(Layer-0)
HOST_PORT_LAYER_1_origin = HOST_PORT_LAYER_0_origin + 1 # 0番目のオリジンノードのポート番号(Layer-1)

#Layer-1
CHECK_INTERVAL = 5 # [min]ブロック生成間隔　# TransactionPoolの確認頻度
TRANSACTION = 'AD9B477B42B22CDF18B1335603D07378ACE83561D8398FBFC8DE94196C65D806'
#APP/transaction/transaction_pool.pyのcreate_transactionでtransactionを生成中

#他ドメインとIPアドレスとPORT番号設定値はsettings_connection.pyに記載

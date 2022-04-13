
#!/bin/bash

find APP/LOG/ -maxdepth 1 -type f -name "*.log" -delete
echo 'APP/LOG/内の.logファイルの全削除を実行'

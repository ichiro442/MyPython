mport schedule
import time

print("待機中・・・")
def job():
    print("実行しました。")
 
 
def execute():
    # 待機時間の設定（例として60分を設定）
    schedule.every(1).minutes.do(job)
 
    while True:
        # ジョブの実行
        schedule.run_pending()
        time.sleep(1)
  print("実行しました2")
execute()

import schedule
print("待機中・・・")
def job():
    print("実行しました。")

schedule.every().day.at("22:24").do(job)

schedule.every(10).minutes.do(job)
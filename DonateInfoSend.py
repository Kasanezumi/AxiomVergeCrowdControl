import queue
import threading
import DonateActionDecide
import logging
import time

# 寄付情報キュー作成
donate_que = queue.Queue()


# 寄付情報キューから取り出して処理部分に渡すループ処理
def donate_que_get_loop():
    print("donate_que_get_loop関数実施")
    while True:
        try:
            donate_info = donate_que.get()
            DonateActionDecide.DecideAction(donate_info[0], donate_info[1])
            logging.info("寄付情報キューから取り出し：アクション名[" + donate_info[0]
                         + "]/金額[" + str(donate_info[1]) + "]")

        # キューからのget処理がデフォルト(block=True)で無限に待ち続けるためここの処理は動作しない
        except queue.Empty:
            logging.info("寄付情報キューから取り出し：無し")


thread = threading.Thread(target=donate_que_get_loop, daemon=False)
thread.start()


# # 実行動作テスト用
# time.sleep(3)
# donate_que.put(["武器変更5", 10000])
# donate_que.put(["武器変更3", 100])
# time.sleep(10)
# donate_que.put(["武器変更7", 1000])

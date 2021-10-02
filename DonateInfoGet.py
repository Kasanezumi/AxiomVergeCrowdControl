import json
import requests
import threading
import queue
from bs4 import BeautifulSoup
import time
import DonateInfoSend
import gui

# グローバル変数
Last_donateID: int = -1  # jsonのpkのこと

# イベント毎にURLを変更する
url = "https://tracker.rtain.jp/search"
event_kind = {"type": "donation", "event": 1}


# ローカル環境での確認用
# local_path = r"D:\tracker.rtain.jp.json"
# with open(local_path, encoding="utf-8") as local_file:
#     response = local_file.read()
# print(response)


# 前回収集時の最後の寄付情報が今回収集した情報の何番目の位置にあるか
def donate_last_donateID_get(donateinfo):
    print("donate_last_donateID_get関数実施")
    for i in range(len(donateinfo)):
        # print(donateinfo[i]["pk"])
        if donateinfo[i]["pk"] == Last_donateID:
            print("前回寄付情報は" + str(i) + "番目にある")
            return i

    print("前回寄付情報無し")
    return -1


# donate_queに情報を積み込む
def donate_que_put(que_donate):
    # print(que_donate)
    for i in range(len(que_donate)):
        # 2次元配列で0番目にアクション名、1番目に金額を設定
        que = [que_donate[i]['fields']['donor__public'],
               int(que_donate[i]['fields']['amount'])]
        # print(que)
        # キューに積み込む
        DonateInfoSend.donate_que.put(que)


# 寄付情報をサイトより取得して寄付情報キューに積み込むループ処理
def donate_info_get_loop():
    print("donate_info_get_loop関数実施")
    global Last_donateID
    while True:
        # 寄付情報をサイトより取得
        response = requests.get(url, params=event_kind)
        response_json = response.json()
        # 配列の順序を逆転して古→新になるように変更
        response_json.reverse()

        # 最後の寄付情報IDが取得した情報のどこにあるか
        last_donateid_now = donate_last_donateID_get(response_json)

        # donate_queに積み込む関数を呼び出し
        if last_donateid_now == -1:
            print("新規500件分積み込み")
            donate_que_put(response_json)

            # 最後の寄付情報更新
            print("最後の寄付情報更新前：" + str(Last_donateID))
            print(response_json[-1]["pk"])
            Last_donateID = response_json[-1]["pk"]
            print("最後の寄付情報更新後：" + str(Last_donateID))

        else:
            # 前回の最後の寄付情報
            del response_json[:last_donateid_now + 1]
            print(response_json)

            if not response_json:
                print("追加寄付情報無し")

            else:
                print("追加寄付情報有り")
                print("追加" + str(499 - last_donateid_now) + "件分積み込み")
                donate_que_put(response_json)

                # 最後の寄付情報更新
                print("最後の寄付情報更新前：" + str(Last_donateID))
                print(response_json[-1]["pk"])
                Last_donateID = response_json[-1]["pk"]
                print("最後の寄付情報更新後：" + str(Last_donateID))

        # 次の寄付情報取得処理実施まで10秒のスリープ
        print("次の寄付情報取得処理実施実施までスリープ")
        time.sleep(10)


def donate_info_get_main():
    thread = threading.Thread(target=donate_info_get_loop, daemon=False)
    thread.start()

    # mainloop開始
    print("mainloop開始")
    gui.GuiMake()


# 動作テスト用
# Last_donateID = 5746

if __name__ == '__main__':
    donate_info_get_main()

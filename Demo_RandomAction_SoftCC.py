# テストプレイ用にランダムで実行するアクションを送信する

# 外部ライブラリ
import random
import time
import threading
# アクション呼び出し用の内数呼び出し用
import ActionSend
import gui
import DonateInfoGet
import DonateInfoSend
import DonateActionDecide

# グローバル変数
Last_donateID: int = -1  # jsonのpkのこと


# def old_SoftCCStart():
#     ActionList = ["KillPlayer",
#                   "GodMode",
#                   "Weapon1",
#                   "Weapon2",
#                   "Weapon3",
#                   "Weapon4",
#                   "Weapon5",
#                   "Weapon6",
#                   "Weapon7",
#                   "Weapon8",
#                   "Weapon9",
#                   "Weapon0",
#                   ]
#
#     # ゲームウィンドウ切り替え用のスリープ
#     time.sleep(3)
#
#     while True:
#         action = random.choices(ActionList, k=1, weights=[5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
#         print(action[0])
#         ActionSend.ActionSeparate(action[0])
#         # 60秒毎に実施
#         time.sleep(60)


# 寄付情報をサイトより取得して寄付情報キューに積み込むループ処理
def demo_donate_info_get_loop(testdonateinfo):
    print("donate_info_get_loop関数実施")
    global Last_donateID

    # 寄付情報をサイトより取得
    response_json = testdonateinfo
    # 配列の順序を逆転して古→新になるように変更
    response_json.reverse()

    # 最後の寄付情報IDが取得した情報のどこにあるか
    last_donateid_now = DonateInfoGet.donate_last_donateID_get(response_json)

    # donate_queに積み込む関数を呼び出し
    if last_donateid_now == -1:
        print("新規500件分積み込み")
        DonateInfoGet.donate_que_put(response_json)

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
            DonateInfoGet.donate_que_put(response_json)

            # 最後の寄付情報更新
            print("最後の寄付情報更新前：" + str(Last_donateID))
            print(response_json[-1]["pk"])
            Last_donateID = response_json[-1]["pk"]
            print("最後の寄付情報更新後：" + str(Last_donateID))


def SoftCCStart_donate():
    testdonateinfo = [{'model': 'tracker.donation', 'pk': 0, 'fields': {'event': 1, 'domain': 'PAYPAL', 'transactionstate': 'COMPLETED', 'readstate': 'PENDING', 'commentstate': 'ABSENT', 'amount': 100000000.0, 'currency': 'JPY', 'timereceived': '2021-08-15T15:41:28.091Z', 'pinned': False, 'canonical_url': 'https://tracker.rtain.jp/donation/5747', 'public': '(匿名) (2500.00) 2021-08-15 15:41:28.091230+00:00', 'donor__public': '(匿名)'}}]
    testpk = 1

    ActionList = ["プレイヤーキル",
                  "無敵時間",
                  "武器変更1",
                  "武器変更2",
                  "武器変更3",
                  "武器変更4",
                  "武器変更5",
                  "武器変更6",
                  "武器変更7",
                  "武器変更8",
                  "武器変更9",
                  "武器変更0",
                  ]

    # ゲームウィンドウ切り替え用のスリープ
    print("ゲームウィンドウに切り替えてください(後3秒で開始)")
    time.sleep(3)

    while True:
        action = random.choices(ActionList, k=1, weights=[5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        # print(action[0])

        # テスト用リストに入れていく
        testdonateinfo[0]["pk"] = testpk
        testdonateinfo[0]["fields"]["donor__public"] = action[0]
        print(testdonateinfo)

        # 呼び出し
        demo_donate_info_get_loop(testdonateinfo)

        # 後処理
        testpk += 1

        # 10秒毎に実施
        print("次のテスト寄付情報積み込み迄10秒のスリープ")
        time.sleep(30)


def SoftCCStart():
    print("SoftCCStart開始")
    thread = threading.Thread(target=SoftCCStart_donate, daemon=False)
    thread.start()

    # mainloop開始
    print("mainloop開始")
    gui.GuiMake()


if __name__ == '__main__':
    SoftCCStart()

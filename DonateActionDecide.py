import logging
import queue
import threading
import time
import ActionSend
import gui

KillPlayer_price: int = 1000
GodMode_price: int = 100
WeaponChange_price: int = 100

# アクション実施キュー作成
action_que = queue.Queue()


def Decide_KillPlayer(Amount):
    # global宣言
    global KillPlayer_price
    if Amount >= KillPlayer_price:
        action_que.put("KillPlayer")
        KillPlayer_price *= 2
        logging.info("プレイヤーキルの最低価格は" + str(KillPlayer_price) + "円です。")
        gui.set_label_next_KillPlayer_price("次のプレイヤーキルの最低金額："
                                            + str(KillPlayer_price) + "円")


def Decide_GodMode(Amount):
    # global宣言
    global GodMode_price
    if Amount >= GodMode_price:
        action_que.put("GodMode")
        GodMode_price *= 2
        logging.info("無敵時間の最低価格は" + str(GodMode_price) + "円です。")
        gui.set_label_next_GodMode_price("次の無敵時間の最低金額："
                                         + str(GodMode_price) + "円")


def Decide_WeaponChange(Amount, WeaponNum):
    # global宣言
    global WeaponChange_price
    if Amount >= WeaponChange_price:
        weapon_kinds: str = "Weapon" + str(WeaponNum)
        action_que.put(weapon_kinds)
        logging.info("武器変更：" + weapon_kinds)


def DecideAction(ActionName, Amount):
    if ActionName == "プレイヤーキル":
        Decide_KillPlayer(Amount)
    elif ActionName == "無敵時間":
        Decide_GodMode(Amount)
    # 武器変更（10種類）
    elif ActionName == "武器変更1":
        Decide_WeaponChange(Amount, 1)
    elif ActionName == "武器変更2":
        Decide_WeaponChange(Amount, 2)
    elif ActionName == "武器変更3":
        Decide_WeaponChange(Amount, 3)
    elif ActionName == "武器変更4":
        Decide_WeaponChange(Amount, 4)
    elif ActionName == "武器変更5":
        Decide_WeaponChange(Amount, 5)
    elif ActionName == "武器変更6":
        Decide_WeaponChange(Amount, 6)
    elif ActionName == "武器変更7":
        Decide_WeaponChange(Amount, 7)
    elif ActionName == "武器変更8":
        Decide_WeaponChange(Amount, 8)
    elif ActionName == "武器変更9":
        Decide_WeaponChange(Amount, 9)
    elif ActionName == "武器変更0":
        Decide_WeaponChange(Amount, 0)
    else:
        logging.error("寄付者名に該当する対象アクション無し")


# アクションキューから取り出して処理部分に渡すループ処理
def action_que_get_loop():
    print("action_que_get_loop関数実施")
    while True:
        try:
            action_kinds = action_que.get()
            ActionSend.ActionSeparate(action_kinds)
            logging.info("アクションキューから取り出し：" + action_kinds)

        # キューからのget処理がデフォルト(block=True)で無限に待ち続けるためここの処理は動作しない
        except queue.Empty:
            logging.info("アクションキューから取り出し：無し")

        # 次のアクション実施まで10秒のスリープ
        num = 10
        print("次のアクション実施までスリープ")
        # gui.set_label_now_action("現在実施のアクション：無し")
        for i in range(10):
            gui.set_label_next_action_time("次のアクション実施まで" + str(num) + "秒")
            num -= 1
            time.sleep(1)
        gui.set_label_next_action_time("寄付待ち")


thread = threading.Thread(target=action_que_get_loop, daemon=False)
thread.start()

# # 実行動作テスト用
# time.sleep(3)
# action_que.put("Weapon5")
# action_que.put("Weapon2")
# time.sleep(60)
# action_que.put("Weapon3")

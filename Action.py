import pyautogui
import time
import pydirectinput
import logging
import gui
import winsound

logging.basicConfig(level=logging.INFO)


# プレイヤーをキルする
def KillPlayer():
    gui.set_label_now_action("現在実施のアクション：プレイヤーキル")
    logging.info("KillPlayer実施")
    logging.info("後10秒で実施します")
    logging.info("コントローラーから手を離してください")
    # ビープ音を鳴らす
    winsound.Beep(500, 1500)

    # 実施までのカウントダウン処理
    num = 10
    for i in range(10):
        gui.set_label_next_action_time("プレイヤーキル実施まで" + str(num) + "秒")
        num -= 1
        time.sleep(1)
    gui.set_label_next_action_time("プレイヤーキル実施")

    pydirectinput.press("enter")
    time.sleep(0.2)
    pydirectinput.press("space")
    time.sleep(0.2)
    pydirectinput.press(",")
    time.sleep(0.2)
    pydirectinput.press("tab")
    pydirectinput.write('kill')
    pydirectinput.press("enter")
    gui.set_label_now_action("現在実施のアクション：無し")


# GOD MODE(プレイヤーが無敵)
def GodMode():
    gui.set_label_now_action("現在実施のアクション：無敵時間")
    logging.info("GodMode実施")
    # ビープ音を鳴らす
    winsound.Beep(1000, 1500)
    pydirectinput.press("f6")
    # 効果時間：30秒
    logging.info("効果時間：30秒")

    # 有効時間終了までのカウントダウン処理
    num = 30
    for i in range(30):
        gui.set_label_next_action_time("無敵時間終了まで" + str(num) + "秒")
        num -= 1
        time.sleep(1)
    gui.set_label_next_action_time("無敵時間終了")

    pydirectinput.press("f6")
    logging.info("GodMode終了")
    gui.set_label_now_action("現在実施のアクション：無し")
    # ビープ音を鳴らす
    winsound.Beep(1000, 1500)


# 武器変更
# 引数の番号の武器に切り替え
def WeaponChange(WeaponNum):
    gui.set_label_now_action("現在実施のアクション：武器変更" + str(WeaponNum))
    # gui.setLabel("武器番号：" + WeaponNum + "に変更")
    logging.info("WeaponChange実施")
    logging.info("武器番号：" + WeaponNum + "に変更")
    pydirectinput.press(WeaponNum)

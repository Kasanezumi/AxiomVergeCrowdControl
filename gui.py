import tkinter as tk
import DonateActionDecide

gui = tk.Tk()
gui.title("Axiom Verge クラウドコントロール")
gui.geometry("1000x300")
gui.geometry('+2000+10')

label_next_action_time = tk.Label(
    gui,
    text="寄付待ち",
    width=100,
    font=("", 15, "bold")
)
label_next_action_time.pack(expand=True)

label_now_action = tk.Label(
    gui,
    text="現在実施のアクション：無し",
    width=100,
    font=("", 15, "bold")
)
label_now_action.pack(expand=True)

label_next_KillPlayer_price = tk.Label(
    gui,
    text="次のプレイヤーキルの最低金額：",
    width=100,
    font=("", 15, "bold")
)
label_next_KillPlayer_price.pack(expand=True)

label_next_GodMode_price = tk.Label(
    gui,
    text="次の無敵時間の最低金額：",
    width=100,
    font=("", 15, "bold")
)
label_next_GodMode_price.pack(expand=True)

label_WeaponChange_price = tk.Label(
    gui,
    text="武器変更の最低金額",
    width=100,
    font=("", 15, "bold")
)
label_WeaponChange_price.pack(expand=True)


def set_label_next_action_time(text):
    print("setLabel開始")
    label_next_action_time["text"] = text


def set_label_now_action(text):
    print("setLabel開始")
    label_now_action["text"] = text


def set_label_next_KillPlayer_price(text):
    print("setLabel開始")
    label_next_KillPlayer_price["text"] = text


def set_label_next_GodMode_price(text):
    print("setLabel開始")
    label_next_GodMode_price["text"] = text


def set_label_WeaponChange_price(text):
    print("setLabel開始")
    label_WeaponChange_price["text"] = text


def GuiMake():
    set_label_next_KillPlayer_price("次のプレイヤーキルの最低金額：" + str(DonateActionDecide.KillPlayer_price) + "円")
    set_label_next_GodMode_price("次の無敵時間の最低金額：" + str(DonateActionDecide.GodMode_price) + "円")
    set_label_WeaponChange_price("武器変更の最低金額：" + str(DonateActionDecide.WeaponChange_price) + "円")
    gui.mainloop()


if __name__ == '__main__':
    GuiMake()




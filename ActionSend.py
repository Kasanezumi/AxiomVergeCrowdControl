import Action
import logging


def ActionSeparate(Value):
    if Value == "KillPlayer":
        Action.KillPlayer()
    elif Value == "GodMode":
        Action.GodMode()
    # 武器変更（10種類）
    elif Value == "Weapon1":
        Action.WeaponChange("1")
    elif Value == "Weapon2":
        Action.WeaponChange("2")
    elif Value == "Weapon3":
        Action.WeaponChange("3")
    elif Value == "Weapon4":
        Action.WeaponChange("4")
    elif Value == "Weapon5":
        Action.WeaponChange("5")
    elif Value == "Weapon6":
        Action.WeaponChange("6")
    elif Value == "Weapon7":
        Action.WeaponChange("7")
    elif Value == "Weapon8":
        Action.WeaponChange("8")
    elif Value == "Weapon9":
        Action.WeaponChange("9")
    elif Value == "Weapon0":
        Action.WeaponChange("0")
    else:
        logging.error("対象アクション無し")

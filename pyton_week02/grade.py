print("หาค่าเกรดเฉลี่ย")
a = int(input('กรุณากรอกคะแนน : '))
if a < 0 or a > 100:
    print("กรุณาใส่ 0-100")
elif a >= 80 :
    print("เกรด 4")
elif a >= 75 :
    print("เกรด 3.5")
elif a >= 70 :
    print('เกรด 3')
elif a >= 65 :
    print("เกรด 2.5")
elif a >= 60 :
    print("เกรด 2")
elif a >= 55 :
    print("เกรด 1.5")
elif a >= 50 :
    print("เกรด 1")
elif a < 50 :
    print("สอบไม่ผ่าน")

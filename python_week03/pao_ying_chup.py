import random
print('เป้า ยิ้ง ฉุบ')

while True :
    print('1 = ค้อน , 2 = กระดาษ , 3 = กรรไกร')
    print(f'1 ชนะ 3 \n2 ชนะ 1 \n3 ชนะ 2')
    user = int(input('ป้อนตัวเลข : '))
    com = int(random.choice ([1,2,3]))
    print(f'คอมพิวเตอร์ : {com}')

    if user not in [1,2,3] :
        print("ใส่เฉพาะ 1 2 3 เท่านั้น !!!")
    elif user == com :
        print('you draw\n')
    elif  (user == 1 and com == 3) or \
        (user == 2 and com == 1) or \
        (user == 3 and com == 2) :
        print('you win\n')
    else :
        print('com win\n')
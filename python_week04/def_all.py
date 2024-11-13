def area_square(): 
    print("โปรแกรมคำนวณหาพื้นที่ 4 เหลี่ยมจัตุรัส")
    area = float(input("ใส่ด้าน : " ))
    square = area * area
    print(f'ค่าของพื้นที่ของสี่เหลี่ยมจัตุรัส = {square}') 
    return square

def area_side(): 
    print("โปรแกรมคำนวณหาพื้นที่ 4 เหลี่ยมพื้นผ้า")
    weight = float(input("ใส่ความกว้าง : " ))
    lenght = float(input("ใส่ความยาว : "))
    side = weight * lenght
    print(f'ค่าของพื้นที่ของสี่เหลี่ยมผืนผ้า = {side}') 
    return side

def area_circle(): 
    print("โปรแกรมคำนวณหาพื้นที่วงกลม")
    r = float(input("ใส่รัสมีของวงกลม : " ))
    circle = 3.14 * (r**2)
    print(f'ค่าของพื้นที่ของวงกลม = {circle}') 
    return circle

def pyc():
    import random
    print('เป้า ยิ้ง ฉุบ')
    print('1 = ค้อน , 2 = กระดาษ , 3 = กรรไกร , 4 = ออกจากเกม')

    while True :
        
        user = int(input('ป้อนตัวเลข : '))
        com = int(random.choice ([1,2,3]))
        print(f'คอมพิวเตอร์ : {com}')

        if user not in [1,2,3,4] :
            print("ใส่เฉพาะ 1 2 3 4 เท่านั้น !!!")
        elif user == com :
            print('เสมอ')
        elif  (user == 1 and com == 3) or \
            (user == 2 and com == 1) or \
            (user == 3 and com == 2) :
            print('คุณชนะ')
        elif user == 4:
            print('ออกจากเกม\n')
            break
        else :
            print('คอมชนะ')
        '''
        play_again = input("ต้องการเล่นอีกครั้งหรือไม่? (y/n): ")
        if play_again != 'y':
            print('ออกจากเกม\n')
            break
'''
def all():
    
    while True:
        print('เลือกโปรแกรมที่จะเล่น')
        print('1. เป้า ยิ้ง ฉุบ')
        print('2. หาพื้นที่')
        print('3. ออกจากโปรแกรม...')
        
        choice = int(input("กรุณาเลือก : "))

        if choice == 1:
            pyc()

        elif choice == 2:
            while True:
                print('\nโปรแกรมใช้คำนวนหาพื้นที่')
                print("1. พื้นที่สี่เหลี่ยมจัตุรัส")
                print("2. พื้นที่สี่เหลี่ยมผืนผ้า")
                print("3. พื้นที่วงกลม")
                print("4. กลับสู่หน้าหลัก")
                
                area = int(input('เลือกพื้นที่ที่ต้องการจะหา : '))
                if area == 1:
                    area_square()

                elif area == 2:
                    area_side()

                elif area == 3:
                    area_circle()

                elif area == 4:
                    print('ออก\n')
                    break

                else :
                    print('เลือกหมายเลขให้ถูกต้อง\n')

        elif choice == 3:
            print('tank you')
            break
        
        else :
            print('ใส่ให้ถูกต้องอย่ากวนตีนไอ้สัส!!!\n')
all()
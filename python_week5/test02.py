import test01

while True:
    print('\nโปรแกรมที่ต้องการใช้')
    print("1 = %3 , 2 = รวมค่า")
    a = int(input('เลือก : '))
    if a == 1:
        while True:
            print('\nโปรแกรม %3')
            print('พิมพ์ 0 เพื่อต้องการออก')
            a = 1
            b = int(input('ใส่ค่าปลาย : '))    
            c = test01.loop(a,b)
            if b == 0:
                break
            print(f'{c}\n')

    elif a == 2 :
        b = 0
        c = 0
        while True:
            print('\nโปรแกรมรวมค่า')
            print('พิมพ์ 0 เพื่อต้องการออก')
            a = int(input('ใส่เลข : '))
            if a == 0:
                print(f'ผลรวมของค่าบวก = {b}')
                print(f'ผลรวมของค่าลบ = {c}')
                break
            b,c = test01.sum(a,b,c)
            print(b,c)
    
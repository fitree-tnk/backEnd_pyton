def sum_def(num):
    total = sum(num)
    average = sum(num) / len(num)
    max_val = max(num)
    min_val = min(num)
    
    
    return (average, total, max_val, min_val) #(ค่าเฉลี่ย, ผลบวกทั้งหมด, ค่ามากที่สุด, ค่าน้อยที่สุด)

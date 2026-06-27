def even():
    testdatasaet = [2, "skip", 4, 0, 6, "ignore", -1, 10, 12]
    count = 0 
    for i in testdatasaet:
        if isinstance(i,str):
            continue
        if i < 0:
            break
        if i == 0:
            pass
        if i%2 == 0:
            count += 1
    print(count)    

even()        

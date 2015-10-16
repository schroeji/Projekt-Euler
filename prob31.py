count = 1 # 1*2P
for p100 in range(0,3):
    if(p100 * 100 == 200):
        count = count + 1
        break
    
    for p50 in range(0,5):
        print(p50)
        if(p100 * 100 + p50 * 50  > 200):
                break
        elif(p100 * 100 + p50 * 50 == 200):
            count = count + 1
            break
        
        for p20 in range(0,11):
            if(p100 * 100 + p50 * 50 + p20 * 20 > 200):
                break
            elif(p100 * 100 + p50 * 50 + p20 * 20 == 200):
                count = count + 1
                break
            
            for p10 in range(0,21):
                if(p100 * 100 + p50 * 50 +  p20 * 20 + p10 * 10 > 200):
                    break
                elif(p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 == 200):
                    count = count + 1
                    break
                
                for p5 in range(0,41):
                    if(p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 > 200):
                        break
                    elif(p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 == 200):
                        count = count + 1
                        break
                    
                    for p2 in range(0,101):
                        if(p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2  > 200):
                            break
                        elif(p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2 == 200):
                            count = count + 1
                            break
                        
                        for p1 in range(0,201):
                            if (p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2 + p1 > 200 ):
                                break
                            elif (p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2 + p1 == 200 ):
                                count = count +1
                               
print(count)
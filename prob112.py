def is_bouncy(x):
    x = str(x)
    dire = "uk"
    for i in range(0,len(x)):
        try:
            if( int(x[i:i+2][0]) < int(x[i:i+2][1]) ) :
                if(dire == "dec"):
                    return True
                elif(dire == "uk"):
                    dire = "inc"
            elif( int(x[i:i+2][0]) > int(x[i:i+2][1]) ):
                if(dire == "inc"):
                    return True
                elif(dire == "uk"):
                    dire = "dec"
        except: 
            pass
    return False

i = 100
bouncy = 0

while(True):
    bouncy = bouncy + 1 if is_bouncy(i) else bouncy
    #if (float(bouncy) / i == 0.9):
     #   print(i)
    if (float(bouncy) / i == 0.99):
        print(i)
        break
    i += 1
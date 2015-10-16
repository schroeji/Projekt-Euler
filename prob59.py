f = open('prob59file', 'r')
inp = f.readline();
asd = inp.split(",")
for i in range(97,123):
   for j in range(97,123):
       for k in range(97,123):
           string = ""
           c = 0
           ascii_sum = 0
           for a in asd:
               if (c % 3 == 0):
                   string += chr(int(a) ^ i)
               elif (c % 3 == 1):
                   string += chr(int(a) ^ j)
               elif (c % 3 == 2):
                   string += chr(int(a) ^ k)
               ascii_sum += ord(string[-1])
               c += 1
           if(string.find("and") > 0 and string.find("is") > 0 and string.find("are") > 0):
              print string
              print ascii_sum
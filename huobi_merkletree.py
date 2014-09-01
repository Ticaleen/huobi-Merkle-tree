import hashlib
import ConfigParser

'''
火币Merkle树验证实例
'''

while True:
    content = int(raw_input("1为算自己，2为算左右树,3为自动全匹配\n"))
    config = ConfigParser.ConfigParser()
    config.readfp(open("test.ini"))                
    if content==1:
        zh = config.get("1","zh")
        sjs= config.get("1","sjs")
        sl= config.get("1","sl")
            
        print  hashlib.sha256(hashlib.sha256(hashlib.sha256(zh).hexdigest()[:50]+sjs).hexdigest()+'|'+sl).hexdigest()
    
    elif content==2:
        zuo = config.get("2","zuo")
        you= config.get("2","you")
        
        print hashlib.sha256(zuo+'|'+you).hexdigest()
        
    elif content==3:
        dicttemp={}
        listtemp=[]
        counttemp=0
        f = open("test2.txt")           
        line = f.readline()            
        while line:
            if line=="":
                break
            line.split(" ")
            dicttemp[line.split(" ")[0]]=line.split(" ")[1]
            listtemp.append(line.split(" ")[0])
            counttemp=counttemp+1
            line = f.readline()
        f.close()
            
        num = len(listtemp)
        temp=listtemp[num-1]
        while True:
            if num<1:
                break
            if not dicttemp.has_key(temp):
                print "卧槽，错了\n"
                break
            else:            
                if int(dicttemp[listtemp[num-1]][0])==1:
                    left=listtemp[num-1]
                    right=listtemp[num-2]
                else:
                    right=listtemp[num-1]
                    left=listtemp[num-2]   
                
                temp=hashlib.sha256(left+'|'+right).hexdigest()
                num=num-2
        print temp
            
    else:
        print("别瞎B输\n")

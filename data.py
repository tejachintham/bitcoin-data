import requests
f=0
ghf=0
var = 1
while var == 1 :
    try:
        myvar = open("hf.csv", 'r')
        lst = myvar.readlines()
        myvar.close
        M=len(lst)
        fd=lst[M-1:]
        firs = fd[0]
        g=firs.split(",")
        dfs=g[1]
        FID=dfs.split("T")
        FIDT=FID[0]
        fia=FIDT.split("-")
        da=fia[2]
        D=FID[1].split("Z")
        FI=FIDT+" "+D[0]
        sg=D[0].split(":")
        sg[1]=int(sg[1])+1
        if(int(sg[1])>59):            
            sg[1]=00
            sg[0]=int(sg[0])+1
        if(int(sg[0])>23):
            sg[0]=00
            da=int(da)+1
        if(fia[1]=="01"):
            if(int(da)>31):    
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="02"):
            
            if(int(da)>28):
                
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="03"):
            
            if(int(da)>31):
                
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="04"):
            
            if(int(da)>30):
                
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="05"):
            
            if(int(da)>31):
                
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="06"):
            
            if(int(da)>30):
                
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="07"):
            
            if(int(da)>31):
                
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="08"):
            
            if(int(da)>31):
                
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="09"):
            
            if(int(da)>30):
                
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="10"):
            
            if(int(da)>31):
                
                fia[1]=int(fia[1])+1
        if(fia[1]=="11"):
            
            if(int(da)>30):
                
                fia[1]=int(fia[1])+1
                da=1
        if(fia[1]=="12"):
            
            if(int(da)>31):
        
                fia[1]=1
                da=1
                fia[0]=int(fia[0])+1        
        url="https://www.bitmex.com/api/v1/trade/bucketed?binSize=1m&partial=false&symbol=XBTUSD&columns=open%2Chigh%2Clow%2Cclose%2Cvolume&count=500&reverse=false&startTime="+str(fia[0])+"-"+str(fia[1])+"-"+str(da)+"%200"+str(sg[0])+"%3A"+str(sg[1])+"&_format=csv"  
        print(url)
        rcomp = requests.get(url)
        data = rcomp.text
        dat=data[57:]
        if(f<1):
            dat=dat.lstrip()
            f=f+1
        with open("hf.csv", "a") as myfile:
            if(ghf==dat):
                break
            myfile.write(dat)
            ghf=dat
        
    except:
        print("This is an error message!")
        break

            

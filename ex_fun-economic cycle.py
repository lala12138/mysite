import math

def main():
    list_am=[]
    list_bm=[]
    listnum=fileopen()
    m=input("Enter the cycle number: ")
    m=m.split(',')
    m=[int(a) for a in m]
    A=parameter(listnum,m)
    forcast(A,m,listnum)

def fileopen():
    infile=open("G:/python/program/economic cycle/finvest_hp.csv",'r')
    list1=[line.rstrip() for line in infile]
    list2=[eval(a) for a in list1]
    infile.close()
    return list2

def datadeal(listnum,m,k):
    sum_am=0
    sum_bm=0
    for a in range(len(listnum)):
        sum_am += listnum[a]*math.cos(2*math.pi*m[k]*(a+1)/len(listnum))
    am=sum_am/len(listnum)
    for b in range(len(listnum)):
        sum_bm += listnum[b]*math.sin(2*math.pi*m[k]*(b+1)/len(listnum))
    bm=sum_bm/len(listnum)
    return am,bm

def parameter(listnum,m):
    A=sum(listnum)/len(listnum)
    print("A0:",A)
    outfileA=open("G:/python/program/economic cycle/finvest_hp_parameterA.txt",'w')
    outfileA.write(str(A))
    outfileam=open("G:/python/program/economic cycle/finvest_hp_parameteram.txt",'w')
    outfilebm=open("G:/python/program/economic cycle/finvest_hp_parameterbm.txt",'w')
    for k in range(len(m)):
        am,bm=datadeal(listnum,m,k)
        print("m:{0},am:{1:.4f},bm:{2:.4f}".format(m[k],am,bm))
        outfileam.write(str(am)+'\n')
        outfilebm.write(str(bm)+'\n')
    outfileam.close()
    outfilebm.close()
    outfileA.close()
    return A

def forcast(A,m,listnum):
    X=A
    infileam=open("G:/python/program/economic cycle/finvest_hp_parameteram.txt",'r')
    infilebm=open("G:/python/program/economic cycle/finvest_hp_parameterbm.txt",'r')
    listam=[line.rstrip() for line in infileam]
    listam=[eval(a) for a in listam]
    listbm=[line.rstrip() for line in infilebm]
    listbm=[eval(b) for b in listbm]
    infileam.close()
    infilebm.close()
    outfileforcast=open("G:/python/program/economic cycle/finvest_hp_forcast.txt",'w')
    for i in range(len(listnum)-1,len(listnum)+5):
        for j in range(len(m)):
            X += listam[j]*math.cos(2*math.pi*m[j]*i/len(listnum))-listbm[j]*math.sin(2*math.pi*m[j]*i/len(listnum))
        outfileforcast.write(str(X)+'\n')
        print("forcast{0}:{1:.4f}".format(i,X))
    outfileforcast.close()
    
main()

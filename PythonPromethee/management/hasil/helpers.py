import os,django
import pandas as pd
from orm.models import Pekerja,Pko, Disiplin, Kesehatan, Petadua, Psikotes
import math

pj = Pekerja.objects.all()

def ListNilaiPko(pj):
    if len(pj)>0:
        cols = ['nilai']
        
        kel ={
            
            cols[0] : [int(a.Pkos.nilai) for a in pj],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]
def ListNilaiDisiplin(pj):
    if len(pj)>0:
        cols = ['nilai']
        
        kel ={
            
            cols[0] : [int(a.Disiplins.nilai) for a in pj],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]
def ListNilaiKesehatan(pj):
    if len(pj)>0:
        cols = ['nilai']
        
        kel ={
            
            cols[0] : [int(a.Kesehatans.nilai) for a in pj],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]
def ListNilaiPsikotes(pj):
    if len(pj)>0:
        cols = ['nilai']
        
        kel ={
            
            cols[0] : [int(a.Psikotess.nilai) for a in pj],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]
def ListNilaiPetadua(pj):
    if len(pj)>0:
        cols = ['nilai']
        
        kel ={
            
            cols[0] : [int(a.Petaduas.nilai) for a in pj],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

df = pd.concat([ListNilaiPko(pj),ListNilaiDisiplin(pj),ListNilaiKesehatan(pj),ListNilaiPsikotes(pj),ListNilaiPetadua(pj)], axis=1)
df.columns=['Pko','Disiplin','Kesehatan','Psikotes','pt2']


# Mencari nilai Preferensi (h(d))
def prefhasil():
    p1 = len(df)
    p2 = len(df)
    p3 = len(df.loc[0])
    arr = []
    hasil = []
    for i in range(p1):
        arr1 = []
        hasil1 = []
        for j in range(p2):
            arr2 = []
            hasil2= []
            for k in range(p3):
                z = df.loc[i][k]-df.loc[j][k]
                m = 0
                if (z <= 0):
                    m = 0
                else:
                    m = 1
                hasil2.append(z)
                arr2.append(m)
            arr1.append(arr2)
            hasil1.append(hasil2)
        arr.append(arr1)
        hasil.append(hasil1)
    return hasil

# Nilai Preferensi (h(d)=0)
def prefarr():
    p1 = len(df)
    p2 = len(df)
    p3 = len(df.loc[0])
    arr = []
    hasil = []
    for i in range(p1):
        arr1 = []
        hasil1 = []
        for j in range(p2):
            arr2 = []
            hasil2= []
            for k in range(p3):
                z = df.loc[i][k]-df.loc[j][k]
                m = 0
                if (z <= 0):
                    m = 0
                else:
                    m = 1
                hasil2.append(z)
                arr2.append(m)
            arr1.append(arr2)
            hasil1.append(hasil2)
        arr.append(arr1)
        hasil.append(hasil1)
    return arr

# Mengihitung Index Preferensi 
def akhirn():
    hasil = prefhasil()
    arr = prefarr()
    akhir = []
    for i in range(len(hasil)):
        akhir1 = []
        for j in range(len(arr[i])):
            bla = sum(arr[i][j])/len(arr[i][j])
            akhir1.append(bla)
        akhir.append(akhir1)
    return akhir

def indexpref():
    akhir = akhirn()
    tmp = []
    for i in range(len(akhir)):
        tmp1 = []
        for j in range(len(akhir[i])):
            tmp1.append(akhir[i][j])
        tmp.append(tmp1)
    return tmp

# Menghitung nilai Leaving Flow
def lflow():
    lf=[]
    akhir = akhirn()
    for i in range(len(akhir)):
        jwb = 1/(len(akhir) - 1) * sum(akhir[i])
        lf.append(jwb)
    return lf

# Mengihitung nilai Entry Flow
def efl():
    tmp = indexpref()
    ef = []
    for i in range(len(tmp)):
        jwb = 1/(len(tmp) - 1) * sum(tmp[i])
        ef.append(jwb)
    return ef

# Menghitung nilai Net Flow 
def nef():
    lf=lflow()
    ef=efl()
    nf = []    
    for i in range(len(ef)):
        jwb = lf[i]-ef[i]
        nf.append(jwb)
        nflow=pd.DataFrame(data=nf,columns=['net flow'])
    return nflow

# Membuat Data Frame dari Leaving FLow, Entry Flow, dan Net flow
entrflow= pd.DataFrame(data=efl(),columns=['Entry Flow'])    
leavingflow= pd.DataFrame(data=lflow(),columns=['leaving flow'])

# Menggabungkan dataframe Leaving flow, Entry Flow, dan Net Flow menjadi satu Data Frame 
rangking=pd.concat([entrflow,leavingflow,nef()],axis=1)
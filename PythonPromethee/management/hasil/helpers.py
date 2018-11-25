import os,django
import pandas as pd
from orm.models import Pekerja,Pko, Disiplin, Kesehatan, Petadua, Psikotes
import math

pj = Pekerja.objects.all()

def ListNilaiPekerja(pj):
    if len(pj)>0:
        cols = ['nama']
        
        kel ={
            
            cols[0] : [str(a.nama) for a in pj],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]
    
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

def gbdf(pj):
    df = pd.concat([ListNilaiPko(pj),ListNilaiDisiplin(pj),ListNilaiKesehatan(pj),
                ListNilaiPsikotes(pj),ListNilaiPetadua(pj)], axis=1)
    df.columns=['Pko','Disiplin','Kesehatan','Psikotes','Peta Dua ']
    return df

def prefhasil(pj):
    df = gbdf(pj)
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
        dfhsl= pd.DataFrame(hasil)
    return dfhsl
    
def prefarr(pj):
    df=gbdf(pj)
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

# Mencari index prefensi
def akhirn(pj):
    hasil = prefhasil(pj)
    arr = prefarr(pj)
    akhir = []
    for i in range(len(hasil)):
        akhir1 = []
        for j in range(len(arr[i])):
            bla = sum(arr[i][j])/len(arr[i][j])
            akhir1.append(bla)
        akhir.append(akhir1)
    return akhir

# Hasil Akhir index prefensi
def indexpref(pj):
    akhir = akhirn(pj)
    tmp = []
    for i in range(len(akhir)):
        tmp1 = []
        for j in range(len(akhir[i])):
            tmp1.append(akhir[j][i])
        tmp.append(tmp1)
    indpref= pd.DataFrame(data=tmp)
    return indpref


def lflow(pj):
    lf=[]
    akhir = akhirn(pj)
    for i in range(len(akhir)):
        jwb = 1/(len(akhir) - 1) * sum(akhir[i])
        lf.append(jwb)
    return lf
def efl(pj):
    tmp = indexpref(pj)
    ef = []
    for i in range(len(tmp)):
        jwb = 1/(len(tmp) - 1) * sum(tmp[i])
        ef.append(jwb)
    return ef

def nef(pj):
    lf=lflow(pj)
    ef=efl(pj)
    nf = []    
    for i in range(len(ef)):
        jwb = lf[i]-ef[i]
        nf.append(jwb)
        nflow=pd.DataFrame(data=nf,columns=['net flow'])
    return nflow

def rangking(pj):
    entrflow= pd.DataFrame(data=efl(pj),columns=['Entry Flow'])    
    leavingflow= pd.DataFrame(data=lflow(pj),columns=['leaving flow'])        

    rangking=pd.concat([ListNilaiPekerja(pj),leavingflow,entrflow,nef(pj)],axis=1)
    return rangking

# Nilai Preferensi F1 (PKO)
def krtpko(pj):
    kriteria1 = []
    arr = prefarr(pj)
    for i in range(len(arr)):
        kriteria11 = []
        for j in range(len(arr[i])):
            kriteria11.append(arr[i][j][0])
        kriteria1.append(kriteria11)
    krpko = pd.DataFrame(kriteria1)
    return krpko

                
# Nilai Preferensi F2 (Disiplin)
def krtdsp(pj):
    kriteria2 = [] 
    arr = prefarr(pj)
    for i in range(len(arr)):
        kriteria22 = []
        for j in range(len(arr[i])):
            kriteria22.append(arr[i][j][1])
        kriteria2.append(kriteria22)
        krdsp = pd.DataFrame(kriteria2)
    return krdsp
    
# Nilai Preferensi F3 (Kesehatan) 
def krtkes(pj):
    kriteria3 = []
    arr = prefarr(pj)
    for i in range(len(arr)):
        kriteria33 = []
        for j in range(len(arr[i])):
            kriteria33.append(arr[i][j][2])
        kriteria3.append(kriteria33)
        krkes = pd.DataFrame(kriteria3)
    return krkes

# Nilai Preferensi F4 (Psikotes) 
def krtpsk(pj):
    kriteria4 = []
    arr = prefarr(pj)
    for i in range(len(arr)):
        kriteria44 = []
        for j in range(len(arr[i])):
            kriteria44.append(arr[i][j][3])
        kriteria4.append(kriteria44)
        krpsk = pd.DataFrame(kriteria4)
    return krpsk
      
# Nilai Preferensi F5 (Peta Dua) 
def krtpt2(pj):
    kriteria5 = []
    arr = prefarr(pj)
    for i in range(len(arr)):
        kriteria55 = []
        for j in range(len(arr[i])):
            kriteria55.append(arr[i][j][4])
        kriteria5.append(kriteria55)
        krpt2 = pd.DataFrame(kriteria5)
    return krpt2
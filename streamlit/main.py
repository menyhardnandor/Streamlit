import streamlit as st


#Csupa nagybetű
#Szavak száma
#leggyakoribb szó
#leggyakoribb betű
#betűk száma
g = st.text_input("Szöveg")
szam = 0
a = g.split(" ")

for i in a:
    if i == "":
        continue
    else: szam += 1

s = {}

for szo in a:
    if szo in s:
        s[szo] += 1
    else: s[szo] = 1


t = {}
for szoo in g:
        if szoo in t:
            t[szoo] +=1
        else: t[szoo] = 1



st.title("Leggyakoribb betű:")
try:st.write(max(t, key=t.get))
except: st.write("")

st.title("Leggyakoribb szó:")
try: st.write(max(s))
except: st.write("")

szama= 0
betuk = g.strip()

for d in betuk:
     szama += 1



st.title("betűk száma: ")
st.write(szama)

st.write(g.upper())
st.title("Szavak száma")

st.write(szam)
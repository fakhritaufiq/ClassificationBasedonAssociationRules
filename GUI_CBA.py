#!/usr/bin/env python
# coding: utf-8

# In[127]:


from sklearn.model_selection import train_test_split
import os
import pandas as pd
from pyarc import CBA, TransactionDB
from pyarc.algorithms import (
    top_rules,
    createCARs,
    M1Algorithm,
    M2Algorithm
)
df = pd.read_csv("Iris.csv")
x=df
x_train, x_test = train_test_split(x, test_size = 0.2)
train=(x_train)
test=(x_test)
data_train = train
data_test = test
txns_train = TransactionDB.from_DataFrame(data_train)
txns_test = TransactionDB.from_DataFrame(data_test)
cba = CBA(support=0.0, confidence=0.5, algorithm="m1")
cba.fit(txns_train)
accuracy = cba.rule_model_accuracy(txns_test) 


# In[140]:


import tkinter
import os
import pandas as pd
df = pd.read_csv("Iris.csv")

main = tkinter.Tk()

hasil_prediksi = cba.predict(txns_test)
dtrain=train.count()
dtest=test.count()

def data():
    global col
    col = list(df)

    for i in range(len(col)):
        box1.insert(i+1, col[i])

def data_train():
    box1.insert(END, "Jumlah data train: ")
    box1.insert(END, dtrain)
        
def data_testing():
    box1.insert(END, "Jumlah data test: ")
    box1.insert(END, dtest)
    
def accur():
    box1.insert(END, "Akurasi: ")
    box1.insert(END, accuracy*100)
    
def predict():
    global hasil
    hasil = list(hasil_prediksi)
    box1.insert(END, "Prediksi: ")
    for i in range(len(hasil)):
        box1.insert(i+1, hasil[i])
        
def clear():
    box1.delete(0, END)

label = tkinter.Label(main, text="Klasifikasi CBA")
tombol1 = tkinter.Button(main, text="1. Data", command = data)
tombol2 = tkinter.Button(main, text="2. Data Training", command = data_train)
tombol3 = tkinter.Button(main, text="2. Data Testing", command = data_testing)
tombol4 = tkinter.Button(main, text="3. Akurasi", command = accur)
tombol5 = tkinter.Button(main, text="4. Prediksi", command = predict)
clear = tkinter.Button(main, text="Clear", command = clear)

box1 = Listbox(main, selectmode='multiple', width=21)

label.pack()
tombol1.pack()
tombol2.pack()
tombol3.pack()
tombol4.pack()
tombol5.pack()
clear.pack()
box1.pack(side=BOTTOM)
main_window.mainloop()


# In[ ]:





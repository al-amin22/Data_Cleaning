# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:09:41 2022

@author: ASUS
"""

#import numpy as np # linear algebra
#import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import seaborn as sns
#import matplotlib.pyplot as plt
#matplotlib inline

import pandas as pd
#import dataset
dataku_asli = pd.read_excel("D:/Artificial Intelegent/amazon 1.xlsx")
dataku = pd.read_excel("D:/Artificial Intelegent/amazon 1.xlsx")
#cekk tipe data
tipe_data = dataku.dtypes
#informasi mengenai data
#dataku.info()
#mendeskripsikan semua data 
deskripsi_data = dataku.describe(include="all")

#Preprocessing
## mengubah tulisan capital pada kolom phone_name dan brand
#dengan tujuan kita tidak mempunyai duplikat dengan huruf kapital dan huruf kecil
dataku.loc[:,["phone_name","Brand"]] = dataku.loc[:,["phone_name","Brand"]].apply(lambda x : x.str.upper())

# ada beberapa merek yang diperbarui maka untuk itu kita harus memperbaikinya dengan cara mengdrop kata diperbarui tersebut
dataku[dataku.phone_name.str.contains("RENEWED").fillna(True)]

# Mengdrop kata "renewed" pada kolom phone_name
dataku["phone_name"] = dataku['phone_name'].str.replace('(RENEWED)',"")
#dataku["phone_name"] = dataku["phone_name"].apply(lambda x: x.replace("(RENEWED) ",""))
dataku[dataku.phone_name.str.contains("RENEWED").fillna(True)]


# Mengdrop kata "Renewed" pada Kolom Brand
dataku["Brand"] = dataku["Brand"].str.replace("(RENEWED) ", "")
dataku["Brand"] = dataku["Brand"].str.replace("(RENEWED)", "")

dataku[dataku.Brand.str.contains("RENEWED").fillna(False)]


# mengganti nama brand berdasarkan informasi dari nama_hp
dataku.loc[dataku.Brand=="","Brand"] = dataku[dataku.Brand==""].phone_name.str.split(" ").str[0]
dataku.Brand.value_counts()
# menghapus kata yang double untuk memudah analisis nantinya
# misini merupakan kata ynag perlu dihapus

dataku["Brand"]=dataku["Brand"].str.replace("TECNO SPARK","TECNO")
dataku["Brand"]=dataku["Brand"].str.replace("REALME C","REALME")
dataku["Brand"]=dataku["Brand"].str.replace("SHIVANSH LYF","SHIVANSH")


### cek dataku [ada kolom phone name]
dataku.phone_name

#menghapus kolom "Unnamed: 1"
dataku.drop(labels="Unnamed: 1",axis=1,inplace=True)

#menampilkan data 3 teratas
data_3_teratas = dataku.head(3)


#3.2. Preprocessing untuk kolom ratting_out_of_five dan rated_people
# menghubungkan kolom ratting dan branfda pada varibael dataku
dataku['ratting_out_of_five']=dataku.groupby('Brand')['ratting_out_of_five'].apply(lambda x:x.fillna(x.mean()))


# menghapus data yang bernilai null pada kolom "ratting_out_of_five","Rated_people"
dataku.dropna(axis=0,subset=["ratting_out_of_five","Rated_people"],inplace=True)


# menghapus koma dan mengubah tipe data menjadi int
dataku.loc[:,"Rated_people"]=dataku.loc[:,"Rated_people"].apply(lambda x: x.replace(",",""))
dataku = dataku[dataku["Rated_people"] != "Save ₹1500"]
dataku["Rated_people"]=dataku["Rated_people"].astype("int")


#3.3. Preprocessing untuk offered_price, real_price and percent off¶
dataku.info()

# menghapus koma dan merubah tipe data pada kolom offed_price_in_ruppe
dataku.loc[:,"Offered_price_in_rupee"]=dataku.loc[:,"Offered_price_in_rupee"].str.replace(",","")
dataku.loc[:,"Offered_price_in_rupee"]=dataku.loc[:,"Offered_price_in_rupee"].astype("float")

dataku.info()

# ada nilai harga yang hilnag atau harga yang kosong pada kolom Offered_price_in_rupee","real_rice_in_rupee","Percent_off
# kita harus melakukan penghapusan terhadap hal tersebut

dataku.dropna(axis=0,subset=["Offered_price_in_rupee","real_rice_in_rupee","Percent_off"],inplace=True)


# skrang kita tidak mempunyai nilai yang kosong lagi
dataku.info()

deskripsi_data_2 = dataku.describe(include='all')


'''
# visualisasi unntuk Brands dan Ratings
brand_rating=dataku.groupby("Brand").aggregate({"ratting_out_of_five":"mean"}).sort_values(by="ratting_out_of_five",ascending=False).reset_index()
plt.figure(figsize=(15,4))
plt.ylim(0,5)
plt.subplot(1,2,1)
sns.barplot(data=brand_rating.head(5),x="Brand",y="ratting_out_of_five")
plt.title("Brand name vs Mean Rating")

plt.subplot(1,2,2)
plt.ylim(0,5)
sns.barplot(data=brand_rating.tail(5),x="Brand",y="ratting_out_of_five",)
plt.title("Brand name vs Mean Rating")
'''

'''#diagram lingkaran
brand_rating=dataku.groupby("Brand").aggregate({"Rated_people":"sum"}).sort_values(by="Rated_people",ascending=False).reset_index()

plt.figure(figsize=(10,10))
plt.pie(data=brand_rating,labels="Brand",x="Rated_people",autopct="%1.2f%%");
plt.title("persentase total dari ratings dalama brands")
'''

'''#diagram batang
plt.figure(figsize=(15,10))

plt.subplot(2,1,1)
plt.title("Nama Brand vs Total Ratings (Highest)")
highest=brand_rating.head(5)
lowest=brand_rating.tail(5)

sns.barplot(data=pd.concat([highest,lowest]),x="Brand",y="Rated_people")
plt.subplot(2,1,2)
plt.title("Brand name vs Total Number of Ratings (Lowest)")
sns.barplot(data=lowest,x="Brand",y="Rated_people")
'''


'''
brand_rating=dataku.groupby("Brand").aggregate({"ratting_out_of_five":"mean","Rated_people":"sum"}).sort_values(by="ratting_out_of_five",ascending=False).reset_index()

more_rated_brands=brand_rating.loc[brand_rating.Rated_people>100,:]

plt.figure(figsize=(15,4))
plt.ylim(0,5)
plt.subplot(1,2,1)
plt.title("Top 5 ratings")
sns.barplot(data=more_rated_brands.head(5),x="Brand",y="ratting_out_of_five")
plt.subplot(1,2,2)
plt.title("Least 5 ratings")
plt.ylim(0,5)
sns.barplot(data=more_rated_brands.tail(5),x="Brand",y="ratting_out_of_five",)
'''
'''
#Ratings vs Price
numeric_columns= dataku.select_dtypes(include=np.number).columns.tolist()

plt.figure(figsize=(8,6))
sns.heatmap(dataku[numeric_columns].corr(),annot=True)
'''
'''#Brands vs Price and Total Products Offered By Brands
dataku.head()

plt.figure(figsize=(20,7))
sns.swarmplot(data=dataku,x="Brand",y="Offered_price_in_rupee",size=5);
plt.title("Brands vs Distribution of Phone Prices")
plt.ylabel("Price")

# Count number of phones offered by Brands
occurences_of_brands=pd.DataFrame(dataku["Brand"].value_counts()).rename(columns={"Brand":"Count"})

# calculate mean prices of phone by brands and discount percents
brand_price=dataku.groupby("Brand").aggregate({"Offered_price_in_rupee":"mean","Percent_off":"mean"}).sort_values(by="Offered_price_in_rupee",ascending=False)

# merge number of phones with mean prices and discounts
brand_price=brand_price.join(occurences_of_brands,on="Brand").reset_index()

# get brands offering at least 3 phones to the market
brand_price=brand_price.loc[brand_price["Count"]>2,:]
# 

# sort by mean price
brand_price.sort_values(by="Offered_price_in_rupee",ascending=False)

sns.barplot(data=brand_price.head(5),x="Brand",y="Offered_price_in_rupee")
plt.ylabel("Price")
plt.title("Top 5 Expensive Products vs Mean Prices ")


# sort by number of products offered
brand_price= brand_price.sort_values(by="Count",ascending=False)

plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.barplot(data=brand_price.head(5),x="Brand",y="Count")

plt.subplot(1,2,2)
plt.pie(data=brand_price,x="Count",labels="Brand",autopct="%1.2f%%",radius=1.5);'''


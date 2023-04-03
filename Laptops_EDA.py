#Importing Required Libraries
import streamlit as slt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from PIL import Image

#Setting Page Configuration
icon = Image.open("pageicon.png")
slt.set_page_config(page_title = "Laptops - EDA",page_icon=icon,layout="wide")

#Designing SideBar
names = ['Praneeth Vasa']
slt.sidebar.title("Project Team Members")
for i in names:
    slt.sidebar.write(i)
slt.sidebar.title("Under the Guidence of - ")
slt.sidebar.write(" Dr. B Rama Krishna")

#Designing Main Page
icon1 = Image.open("logo.png")
slt.image(icon1,use_column_width = True)
slt.title("Exploratory Data Analysis On Laptops DataSet")
uploaded_file = slt.file_uploader("Upload a Laptops Dataset (.csv)")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    slt.write("Preview : ")
    slt.dataframe(data)
    slt.title("Laptops Specifications DataSet")
    #Displaying Queries In Checkbox
    if slt.checkbox("Display the Dimension and Shape of Laptop DataFrame"):
        slt.write(f"Number of dimensions : {data.ndim}")
        slt.write(f"Shape : {data.shape}")
    if slt.checkbox("List the Features/Attributes of Laptop DataSet?"):
        slt.write(pd.DataFrame(data.columns, columns=["Features/Attributes"]))
    if slt.checkbox("Display the Data type of each column in Laptop DataFrame"):
        #slt.dataframe(data.dtypes)
        slt.write(pd.DataFrame(data.dtypes,columns=['Data Type']))
    if slt.checkbox("Display the count of non-null values of each column in Dataframe"):
        #slt.dataframe(data.count())
        slt.write(pd.DataFrame(data.count(),columns=['count']))
    if slt.checkbox("Fill the Null values with Zero, if exists and Display the count of Non-NULL values"):
        data.fillna(0,inplace = True)
        slt.write("NULL values are repalced with 0, Therefore dataset doesn't contains NULL values")
        #slt.dataframe(data.count())
        slt.write(pd.DataFrame(data.count(),columns=['count']))
    if slt.checkbox("How many Laptops are in the DataSet?"):
        slt.write(f"{len(data)} Laptops")
    if slt.checkbox("What is the most Expensive Laptop in DataSet? and Give it's Specifications"):
        slt.write(data.loc[data['price'].idxmax()])
    if slt.checkbox("What is the Least Expensive Laptop in DataSet? and Give it's Specifications"):
        slt.write(data.loc[data['price'].idxmin()])
    if slt.checkbox("What Would be the Average Price of Laptop?"):
        slt.write(f"₹{int(data['price'].mean())} Rupees")
    if slt.checkbox("Display the Basic statistics of Laptop Prices"):
        slt.write(data.price.describe())
    if slt.checkbox("What is the Highest Rated Laptop?"):
        slt.write(data.loc[data.rating.idxmax()])
    if slt.checkbox("Classify the Number of laptops Based On Operating System?"):
        slt.write(data.os.value_counts())
    if slt.checkbox("How many laptops have intel i7 processer in Laptop DataSet?"):
        slt.write(f"{len(data[data['processor'].str.contains('i7')])} Laptops having Inter i7 processor")
    if slt.checkbox("Plot the Correlation between Price and Rating of Laptops"):
        fig,x = plt.subplots()
        plt.scatter(data['price'], data['rating'])
        plt.title('Correlation between Price and Rating')
        plt.xlabel('Price')
        plt.ylabel('Rating')
        slt.pyplot(fig)
    if slt.checkbox("Show the Distribution of Laptop Prices"):
        fig,x = plt.subplots()
        plt.hist(data['price'])
        plt.title('Distribution of Laptop Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        slt.pyplot(fig)
    if slt.checkbox("List the Top rated laptops of price in between 30k and 40k"):
        d = (data.price >= 30000) & (data.price <=40000)
        data1 = data.loc[d].sort_values(by='rating',ascending=False).head(10)
        slt.write("Top 10 High rated laptops between 30k and 40k")
        #slt.write(data1.loc[data1.rating.idxmax()])
        slt.write(data1)
    if slt.checkbox("What is the distribution of laptop prices based on their operating system?"):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='os', y='price', data=data, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        ax.set_title('Distribution of Laptop Prices based on Operating System')
        ax.set_xlabel('Operating System')
        ax.set_ylabel('Price')
        slt.pyplot(fig)
    if slt.checkbox("What is the average price of laptops for each operating system?"):
        avg_prices = data.groupby('os')['price'].mean().reset_index()
        slt.write("Average prices of laptops for each operating system:")
        fig, ax = plt.subplots()
        sns.barplot(x='os', y='price', data=avg_prices, ax=ax)
        ax.set_xlabel("Operating System")
        ax.set_ylabel("Average Price")
        ax.set_title("Average Laptop Prices by Operating System")
        plt.xticks(rotation=45, ha='right')
        slt.pyplot(fig)
    if slt.checkbox("suggest 5 best laptops in the branding of Lenovo based on rating"):
        lenovo_data = data[data['name'].str.contains('Lenovo')]
        top_5_laptops = lenovo_data.sort_values(by='rating', ascending=False).head(5)
        slt.write("Top 5 Lenovo laptops based on rating:")
        slt.write(top_5_laptops[['name', 'processor', 'rating', 'price']])
    if slt.checkbox("Compare the Prices of i3 Processor Laptops of Brands HP and DELL"):
        #hp_i3 = data[data['name'].str.contains('HP') and data['processor'].str.contains('i3')]
        #dell_i3 = data[data['name'].str.contains('DELL') and data['processor'].str.contains('i3')]
        fig, ax = plt.subplots()
        d = data[data['name'].str.contains('HP') | data['name'].str.contains("DELL")]
        sns.boxplot(x='name', y="price", data=d)
        slt.pyplot(fig)
        
        
        
        
        
        
    






    



    

    
    
    
    





    


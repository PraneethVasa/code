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
        sns.boxplot(x='os', y='price', data=data, ax=ax)
        ax.set_title('Distribution of Laptop Prices based on Operating System')
        ax.set_xlabel('Operating System')
        ax.set_ylabel('Price (INR)')
        slt.pyplot(fig)
        
        
        
        
        
    






    



    

    
    
    
    





    


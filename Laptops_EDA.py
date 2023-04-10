#Importing Required Libraries
import streamlit as slt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

#Setting Page Configuration
slt.set_page_config(page_title = "Laptops - EDA",page_icon="icon.png",layout="wide")
slt.caption("PraneethVasa")
mt = True
mt = False
if mt:
    l = Image.open("mn.png")
    slt.image(l,use_column_width = True)
    slt.title("Sorry, the app (Laptops_EDA) is currently under maintenance. Please try again Later😶‍🌫️")
else:
    #Designing SideBar
    #names = ['Praneeth Vasa']
    names = ['21A21A6162 - Vasa Purna Praneeth','21A21A6138 - m. ankanmma rao','21A21A6135 - V.Dinesh','21A21A6141- N.Murali','21A21A6129- k.Reshi Charan','21A21A6124- K.Gopi','21A21A6130- K.Jahnavi','21A21A6161 - V.Divyanjali']
    slt.sidebar.title("Project Team Members")
    for i in names:
        slt.sidebar.write(i)
    slt.sidebar.title("Under the Guidence of - ")
    slt.sidebar.write(" Dr. B Rama Krishna")

    #Designing Main Page
    slt.image("logo.png",use_column_width = True)
    slt.title("Exploratory Data Analysis On Laptops DataSet")
    uploaded_file = slt.file_uploader("Upload a Laptops Dataset (.csv)")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        slt.write("Preview : ")
        slt.dataframe(data)
        slt.title("Laptops Specifications DataSet")
        #Displaying Queries In Checkbox
        #Q1
        if slt.checkbox("Display the Dimension and Shape of Laptop DataFrame"):
            slt.write(f"Number of dimensions : {data.ndim}")
            slt.write(f"Shape : {data.shape}")
    
        #Q2
        if slt.checkbox("List the Features/Attributes of Laptop DataSet?"):
            slt.write(pd.DataFrame(data.columns, columns=["Features/Attributes"]))
        #Q3
        if slt.checkbox("Display the Data type of each column in Laptop DataFrame"):
            slt.write(pd.DataFrame(data.dtypes,columns=['Data Type']))
        
        #Q4
        if slt.checkbox("Display the count of non-null values of each column in Dataframe"):
            slt.write(pd.DataFrame(data.count(),columns=['count']))
        
        #Q5
        if slt.checkbox("How many Laptops are in the DataSet?"):
            slt.write(f"{len(data)} Laptops")
        
        #Q6
        if slt.checkbox("Display the Basic statistics of Laptop Prices"):
            slt.write(data.price.describe())
        
        #Q7
        if slt.checkbox("What Would be the Average Price of Laptop?"):
            slt.write(f"₹{int(data['price'].mean())} Rupees")
        #Q8
        if slt.checkbox("What is the most Expensive Laptop in DataSet? and Give it's Specifications"):
            slt.write(data.loc[data['price'].idxmax()])
        #Q9
        if slt.checkbox("What is the Least Expensive Laptop in DataSet? and Give it's Specifications"):
            slt.write(data.loc[data['price'].idxmin()])
    
        #Q10
        if slt.checkbox("What is the Highest Rated Laptop?"):
            slt.write(data.loc[data.rating.idxmax()])
        #Q11
        if slt.checkbox("Classify the Number of laptops Based On Operating System?"):
            slt.write(data.os.value_counts())
        #Q12
        if slt.checkbox("How many laptops have intel i7 processer in Laptop DataSet?"):
            slt.write(f"{len(data[data['processor'].str.contains('i7')])} Laptops having Inter i7 processor")
        #Q13
        if slt.checkbox("List the Top rated laptops of price in between 30k and 40k"):
            d = (data.price >= 30000) & (data.price <=40000)
            data1 = data.loc[d].sort_values(by='rating',ascending=False).head(10)
            slt.write("Top 10 High rated laptops between 30k and 40k")
            slt.write(data1)
        #Q14
        if slt.checkbox("suggest 5 best laptops in the branding of Lenovo based on rating"):
            lenovo_data = data[data['name'].str.contains('Lenovo')]
            top_5_laptops = lenovo_data.sort_values(by='rating', ascending=False).head(5)
            slt.write("Top 5 Lenovo laptops based on rating:")
            slt.write(top_5_laptops[['name', 'processor', 'rating', 'price']])
        slt.title("VISUALIZATION")
        #Q15
        if slt.checkbox("Plot the Correlation between Price and Rating of Laptops"):
            fig,x = plt.subplots()
            plt.scatter(data['price'], data['rating'])
            plt.title('Correlation between Price and Rating')
            plt.xlabel('Price')
            plt.ylabel('Rating')
            slt.pyplot(fig)
        #Q16
        if slt.checkbox("Show the Distribution of Laptop Prices"):
            fig,x = plt.subplots()
            plt.hist(data['price'])
            plt.title('Distribution of Laptop Ratings')
            plt.xlabel('Rating')
            plt.ylabel('Frequency')
            slt.pyplot(fig)
        #Q17
        if slt.checkbox("What is the distribution of laptop prices based on their operating system?"):
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x='os', y='price', data=data, ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            ax.set_title('Distribution of Laptop Prices based on Operating System')
            ax.set_xlabel('Operating System')
            ax.set_ylabel('Price')
            slt.pyplot(fig)
        #Q18
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
    
        #Q19
        if slt.checkbox("Compare the Prices of i3 Processor Laptops of Brands HP and DELL"):
            fig, ax = plt.subplots()
            d = data[data['name'].str.contains('HP') | data['name'].str.contains("DELL")]
            d1 = d[d['processor'].str.contains('i3')]
            sns.barplot(x="price", y="name", data=d1)
            plt.xticks(rotation=50, ha='right')
            slt.pyplot(fig)
        data1 = data.copy(deep = True)
        data1 = data1.drop(['name'],axis=1)
        if slt.checkbox("Plot Graphs by runtime Input"):
            ty = slt.selectbox("select Type ",['Distribution','Correlation'])
            x_l = slt.selectbox("On X - AXIS " ,list(data1.columns))
            if ty != 'Distribution':
                y_l = slt.selectbox("On Y - AXIS ",list(data1.columns))
            if slt.button("Plot Graph",key='fd'):
                fig,ax = plt.subplots()
                if ty == 'Distribution':
                    plt.title(f"The {ty} of {x_l}")
                    sns.histplot(x = x_l,data = data1,kde = True,ax=ax)
                    plt.xticks(rotation = 'vertical')
                    slt.pyplot(fig)
                else:
                    plt.title(f"The {ty} of {x_l} and {y_l}")
                    sns.scatterplot(x = x_l,y = y_l,data = data1,ax=ax)
                    plt.xticks(rotation = 'vertical')
                    slt.pyplot(fig)
        slt.title("LAPTOP FINDER")
        if slt.checkbox("Confused about which laptop to buy? Just feed in your requirements to our Laptop Finder and you will get best recommendations according to your specifications"):
             brand = slt.selectbox("Select Preferred Brand",['Lenovo','HP','DELL','APPLE','RedmiBook','SAMSUNG','MSI','realme Book','ASUS','acer','Infinix'])
             x1 = data[data['name'].str.contains(brand)]
             p = x1.processor.unique()
             processor = slt.selectbox("Select Preferred Processor",p)
             x1 = x1[x1['processor'] == processor]
             r = x1.ram.unique()
             ram = slt.selectbox("Select Preferred RAM",r)
             x1 = x1[x1['ram'] == ram]
             s = x1.storage.unique()
             storage = slt.selectbox("Select Preferred Storage",s)
             x1 = x1[x1['storage'] == storage]
             d = x1.display_size.unique()
             display = slt.selectbox("select Preferred Display Size",d)
             x1 = x1[x1['display_size'] == display]
             price = slt.number_input("Enter Your Budget : ",value=45000,step=5000)
             x1 = x1[x1['price'] <= price]
             x1 = x1.sort_values(by='rating', ascending=False)
             x1 = x1[['name','os','ram','storage','display_size','price','rating']]
             if slt.button("Find Laptops",key='1'):
                if len(x1) == 0:
                    slt.warning(f"The {brand} Laptops having {processor} are bit Much Expensive.  -- TRY TO INCREASE YOUR BUDGET(₹ price) for the Above Requirments")
                else:
                    slt.write("Here are the Best Matches for the Above Specifications")
                    slt.write(x1)

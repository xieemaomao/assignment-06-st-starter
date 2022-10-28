# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# show the title
st.title('Titanic APP by Miaomiao Hou')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
df
# create a figure with three subplots, size should be (15, 5)
plt.style.use('seaborn')
st.subheader('The Box Plot For Ticket Price with Different Classes')
fig, ax = plt.subplots(1, 3, figsize = (15,5))
# show the box plot for ticket price with different classes
df[df['Pclass'] == 1]['Fare'].plot.box(ax = ax[0])
df[df['Pclass'] == 2]['Fare'].plot.box(ax = ax[1])
df[df['Pclass'] == 3]['Fare'].plot.box(ax = ax[2])

# you need to set the x labels and y labels
ax[0].set_ylabel('Fare')
ax[0].set_xlabel('PClass1')
ax[1].set_xlabel('PClass2')
ax[2].set_xlabel('PClass3')

# a sample diagram is shown below
st.pyplot(fig)


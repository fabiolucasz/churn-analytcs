import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt
import seaborn as sns

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

print(base_path)

df = pd.read_csv(os.path.join(base_path, 'data', 'customer_churn_business_dataset.csv'))

country_filter = st.sidebar.selectbox(
    'Select your country',
    options = df['country'].unique(),
)

df = df[df["country"] == country_filter]
df = pd.DataFrame(df)

st.title('Customer Churn Analytics')

#quantidade de linhas e colunas
st.sidebar.write(df.shape)

#st.write(df.describe())

fig, ax = plt.subplots(figsize=(6,4))
sns.countplot(x="churn", data=df)
ax.set_title("Churn Distribution")
ax.set_xlabel("Churn (0 = No, 1 = Yes)")
ax.set_ylabel("Customer Count")
st.pyplot(fig)


fig, ax = plt.subplots(figsize=(7,4))
sns.countplot(x="contract_type", hue="churn", data=df)
plt.title("Contract Type vs Churn")
st.pyplot(fig)




fig, ax = plt.subplots(figsize=(7,4))
sns.countplot(x="customer_segment", hue="churn", data=df)
plt.title("Customer Segment vs Churn")
st.pyplot(fig)



# # Churns by country
# st.title('Churn by country')

# get_countries = df['country'].unique()
# country_list = []
# for country in get_countries:
#     country_churn = df[df['country'] == country]['churn'].sum()
#     items = [country, country_churn]
#     country_list.append(items)

# df_country_churn = pd.DataFrame(country_list, columns=['country', 'churn']).sort_values(by='churn', ascending=False)
# st.write(df_country_churn)

# # Churns by city 
# # Add the country that match the city on dataframe
# st.title('Churn by city')

# get_cities = df['city'].unique()
# city_list = []
# for city in get_cities:
#     city_churn = df[df['city'] == city]['churn'].sum()
#     items = [city, city_churn]
#     city_list.append(items)

# df_city = pd.DataFrame(city_list, columns=['city', 'churn']).sort_values(by='churn', ascending=False)
# st.write(df_city)


# st.title('Churn by channel')
# #signup channel unique items
# get_channels = df['signup_channel'].unique()
# print(get_channels)
# channel_list = []

# for channel in get_channels:
#     channel_churn = df[df['signup_channel'] == channel]
#     channel_churn_percent = len(channel_churn) / len(df['signup_channel']) * 100
#     channel_items = [channel, channel_churn_percent]
#     channel_list.append(channel_items)

# df_channels = pd.DataFrame(channel_list, columns=['channel', 'churn_percent']).sort_values(by='churn_percent', ascending=False)
# st.write(df_channels)

# st.title('Churn by contract type')
# #signup channel unique items
# get_contract_types = df['contract_type'].unique()
# print(get_contract_types)
# contract_type_list = []

# for contract_type in get_contract_types:
#     contract_type_churn = df[df['contract_type'] == contract_type]
#     contract_type_churn_percent = len(contract_type_churn) / len(df['contract_type']) * 100
#     contract_type_items = [contract_type, contract_type_churn_percent]
#     contract_type_list.append(contract_type_items)

# df_contract_type = pd.DataFrame(contract_type_list, columns=['contract_type', 'churn_percent']).sort_values(by='churn_percent', ascending=False)
# st.write(df_contract_type)
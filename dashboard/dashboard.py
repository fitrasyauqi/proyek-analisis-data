# Import semua library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Load dataset
day_df = pd.read_csv("day.csv")

# Mengubah key menjadi values keterangan
day_df['mnth'] = day_df['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['weathersit'] = day_df['weathersit'].map({
    1: 'Clear etc',
    2: 'Mist etc',
    3: 'Light Snow etc',
    4: 'Heavy Rain etc'
})

# Membuat Sidebar
with st.sidebar:
    st.title('Bike Sharing Dashboard')
    st.text('by Mohd Alfitra Syauqi')
    st.image("https://png.pngtree.com/png-clipart/20221020/ourmid/pngtree-young-man-riding-a-bicycle-png-image_6352227.png")

# Membuat Judul
st.title('Analisis Dataset Bike Sharing 🚲')
st.markdown("---")

# Menampilkan Visualisasi pertanyaan 1
st.subheader('Jumlah Sewa Sepeda berdasarkan Cuaca')
plt.figure(figsize=(8, 5))
sns.barplot(
    y="cnt",
    x="weathersit",
    color="cyan",
    data=day_df
)
plt.title("Jumlah sewa sepeda berdasarkan cuaca")
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(plt.gcf())

col1, col2, col3 = st.columns(3)
 
with col1:
    mist_count = round(day_df[day_df['weathersit'] == 'Mist etc']['cnt'].mean())
    st.metric("Kondisi Cuaca Mist dll", value=mist_count)

with col2:
    clear_count = round(day_df[day_df['weathersit'] == 'Clear etc']['cnt'].mean())
    st.metric("Kondisi Cuaca Clear dll", value=clear_count)

with col3:
    light_snow_count = round(day_df[day_df['weathersit'] == 'Light Snow etc']['cnt'].mean())
    st.metric("Kondisi Cuaca Light Snow dll", value=light_snow_count)

st.markdown("---")

# Menampilkan Visualisasi pertanyaan 2
st.subheader('Jumlah Registered User berdasarkan Hari')
plt.figure(figsize=(8, 5))
sns.barplot(
    y="registered",
    x="weekday",
    color="cyan",
    data=day_df
)
plt.title("Jumlah registered user berdasarkan hari")
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(plt.gcf())

st.markdown("---")

# Menampilkan Visualisasi pertanyaan 3
st.subheader('Tren Sewa Sepeda berdasarkan Tahun')
day_df['mnth'] = pd.Categorical(day_df['mnth'], categories=
    ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    ordered=True)

monthly_counts = day_df.groupby(by=["mnth","yr"]).agg({
    "cnt": "sum"
}).reset_index()

fig, ax = plt.subplots()
sns.lineplot(
    data=monthly_counts,
    x="mnth",
    y="cnt",
    hue="yr",
    palette="mako_r",
    marker="o",
    ax=ax
)
plt.title("Tren penyewaan sepeda berdasarkan tahun dengan kondisi tiap bulan")
plt.xlabel(None)
plt.ylabel(None)
plt.legend(title="Tahun", loc="upper left")
st.pyplot(fig)

col1, col2 = st.columns(2)
 
with col1:
    total_rent_2011 = day_df[day_df['yr'] == 0]['cnt'].sum()
    st.metric("Total Sewa Sepeda Tahun 2011", value=total_rent_2011)

with col2:
    total_rent_2012 = day_df[day_df['yr'] == 1]['cnt'].sum()
    st.metric("Total Sewa Sepeda Tahun 2012", value=total_rent_2012)

# Membuat caption copyright
st.caption('Copyright (c) Mohd Alfitra Syauqi 2024')
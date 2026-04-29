import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Analisis Review Pelanggan")

# Load data hasil olahan
df = pd.read_csv('dashboard/main_data.csv')

# Jika belum ada kolom month (opsional)
if 'month' not in df.columns:
    df['month'] = df.iloc[:,0]

# Visualisasi 1: Tren Rating
st.subheader("Tren Rata-rata Rating per Bulan")
st.line_chart(df.set_index('month'))

# Load raw data untuk analisis tambahan
df_raw = pd.read_csv('data/order_reviews_dataset.csv')
df_raw['review_creation_date'] = pd.to_datetime(df_raw['review_creation_date'])

# Panjang komentar
df_raw['comment_length'] = df_raw['review_comment_message'].fillna('').str.len()

low = df_raw[df_raw['review_score'] <= 2]
high = df_raw[df_raw['review_score'] >= 4]

# Visualisasi 2
st.subheader("Perbandingan Panjang Komentar")

fig, ax = plt.subplots()
ax.boxplot([low['comment_length'], high['comment_length']],
           labels=['Rating Rendah', 'Rating Tinggi'])

st.pyplot(fig)
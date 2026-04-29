import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Analisis Review Pelanggan")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv('data/order_reviews_dataset.csv')
df['review_creation_date'] = pd.to_datetime(df['review_creation_date'])
df['comment_length'] = df['review_comment_message'].fillna('').str.len()

# =========================
# INTERAKTIF (WAJIB)
# =========================
st.sidebar.header("Filter")

year = st.sidebar.selectbox(
    "Pilih Tahun",
    sorted(df['review_creation_date'].dt.year.unique())
)

df_filtered = df[df['review_creation_date'].dt.year == year].copy()

# =========================
# PERTANYAAN 1
# =========================
st.subheader("Tren Rata-rata Rating per Bulan")

df_filtered['month'] = df_filtered['review_creation_date'].dt.to_period('M')
monthly = df_filtered.groupby('month')['review_score'].mean()

st.line_chart(monthly)

st.caption("Menjawab: Tren perubahan rating pelanggan per bulan")

# =========================
# PERTANYAAN 2
# =========================
st.subheader("Perbandingan Panjang Komentar (Rating Rendah vs Tinggi)")

low = df_filtered[df_filtered['review_score'] <= 2]
high = df_filtered[df_filtered['review_score'] >= 4]

fig, ax = plt.subplots()
ax.boxplot([low['comment_length'], high['comment_length']],
           labels=['Rating Rendah', 'Rating Tinggi'])

st.pyplot(fig)

st.caption("Menjawab: Karakteristik komentar berdasarkan rating")

# =========================
# INSIGHT
# =========================
st.markdown("""
### Insight:
- Rating pelanggan dapat berubah tergantung periode waktu
- Pelanggan dengan rating rendah cenderung memberikan komentar lebih panjang
""")
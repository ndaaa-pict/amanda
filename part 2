import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(
    page_title="Dashboard Analisis Penjualan",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Analisis Penjualan")

# ==========================
# LOAD DATA
# ==========================
df = pd.read_csv("data_penjualan.csv")

st.subheader("Dataset")

st.dataframe(df,use_container_width=True)

# ==========================
# PERHITUNGAN
# ==========================

df["Keuntungan"] = df["Penjualan"] - df["Biaya"]
df["Margin (%)"] = round(df["Keuntungan"]/df["Penjualan"]*100,2)

st.subheader("Hasil Perhitungan")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Penjualan",
    f"{df['Penjualan'].sum():,.0f}"
)

col2.metric(
    "Total Biaya",
    f"{df['Biaya'].sum():,.0f}"
)

col3.metric(
    "Total Keuntungan",
    f"{df['Keuntungan'].sum():,.0f}"
)

col4.metric(
    "Margin Rata-rata",
    f"{df['Margin (%)'].mean():.2f}%"
)

# ==========================
# GRAFIK GARIS
# ==========================

st.subheader("Grafik Tren Penjualan")

fig = px.line(
    df,
    x="Bulan",
    y="Penjualan",
    markers=True,
    title="Tren Penjualan"
)

st.plotly_chart(fig,use_container_width=True)

# ==========================
# GRAFIK BATANG
# ==========================

st.subheader("Grafik Batang Keuntungan")

fig2 = px.bar(
    df,
    x="Bulan",
    y="Keuntungan",
    color="Keuntungan",
    text_auto=True
)

st.plotly_chart(fig2,use_container_width=True)

# ==========================
# PIE CHART
# ==========================

st.subheader("Komposisi Penjualan vs Biaya")

pie = pd.DataFrame({
    "Kategori":["Penjualan","Biaya"],
    "Nilai":[
        df["Penjualan"].sum(),
        df["Biaya"].sum()
    ]
})

fig3 = px.pie(
    pie,
    names="Kategori",
    values="Nilai",
    hole=0.4
)

st.plotly_chart(fig3,use_container_width=True)

# ==========================
# MODEL ANALISIS
# Weighted Score
# ==========================

st.subheader("Model Weighted Scoring")

bobot_penjualan = st.slider(
    "Bobot Penjualan",
    0.0,
    1.0,
    0.6
)

bobot_margin = 1-bobot_penjualan

score = (
    (df["Penjualan"]/df["Penjualan"].max())*bobot_penjualan
    +
    (df["Margin (%)"]/df["Margin (%)"].max())*bobot_margin
)

df["Score"] = round(score*100,2)

st.dataframe(
    df[[
        "Bulan",
        "Penjualan",
        "Margin (%)",
        "Score"
    ]]
)

# ==========================
# REGRESI LINEAR
# ==========================

st.subheader("Prediksi Penjualan")

X = np.arange(len(df)).reshape(-1,1)

y = df["Penjualan"]

model = LinearRegression()

model.fit(X,y)

bulan_prediksi = st.slider(
    "Prediksi Bulan ke",
    13,
    24,
    15
)

pred = model.predict([[bulan_prediksi-1]])

st.success(
    f"Prediksi Penjualan Bulan ke-{bulan_prediksi} : {pred[0]:.2f}"
)

# ==========================
# VISUAL PREDIKSI
# ==========================

future = np.arange(24).reshape(-1,1)

hasil = model.predict(future)

pred_df = pd.DataFrame({
    "Periode":range(1,25),
    "Prediksi":hasil
})

fig4 = px.line(
    pred_df,
    x="Periode",
    y="Prediksi",
    markers=True,
    title="Prediksi Penjualan"
)

st.plotly_chart(fig4,use_container_width=True)

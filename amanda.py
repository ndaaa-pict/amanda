import streamlit as st

st.set_page_config(
    page_title="Aplikasi Streamlit",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Aplikasi Streamlit Sederhana")

st.write("Masukkan data di bawah ini.")

nama = st.text_input("Nama")

umur = st.number_input(
    "Umur",
    min_value=0,
    max_value=120,
    value=20
)

hobi = st.selectbox(
    "Pilih Hobi",
    ["Membaca", "Olahraga", "Musik", "Coding"]
)

if st.button("Tampilkan"):
    st.success("Data berhasil diproses!")
    st.write("### Hasil")
    st.write(f"**Nama:** {nama}")
    st.write(f"**Umur:** {umur} tahun")
    st.write(f"**Hobi:** {hobi}")

    if umur >= 17:
        st.info("Status: Dewasa")
    else:
        st.warning("Status: Belum Dewasa")

import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================
# KONFIGURASI HALAMAN
# ==============================
st.set_page_config(
    page_title="Portfolio Amanda Kurnianingrum",
    page_icon="🎓",
    layout="wide"
)

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:

    st.title("🎓 Portfolio")

    try:
        st.image("profile.jpg", width=180)
    except:
        st.info("Tambahkan file profile.jpg")

    st.markdown("## Amanda Kurnianingrum")
    st.write("Mahasiswa Baru 2026")
    st.write("Teknologi Rekayasa Perangkat Lunak")
    st.write("Universitas Gadjah Mada")

    st.markdown("---")

    menu = st.radio(
        "Menu",
        [
            "Profil",
            "Skill",
            "Proyek",
            "Grafik",
            "Kontak"
        ]
    )

# ==============================
# PROFIL
# ==============================

if menu == "Profil":

    st.title("👩‍💻 Amanda Kurnianingrum")

    st.subheader("Mahasiswa Baru 2026")

    st.write("""
Saya merupakan mahasiswa Program Studi **Teknologi Rekayasa Perangkat Lunak**
Universitas Gadjah Mada.

Saya memiliki minat dalam bidang:

- Software Engineering
- Artificial Intelligence
- Data Science
- Web Development
- Mobile Development
- UI/UX Design

Saya berkomitmen untuk terus belajar, mengembangkan keterampilan,
dan membangun solusi teknologi yang bermanfaat.
""")

    col1,col2,col3 = st.columns(3)

    col1.metric("Angkatan","2026")
    col2.metric("Semester","1")
    col3.metric("Target IPK","> 3.75")

# ==============================
# SKILL
# ==============================

elif menu == "Skill":

    st.title("💻 Keahlian")

    st.subheader("Hard Skill")

    skill = {
        "Python":85,
        "HTML":80,
        "CSS":75,
        "JavaScript":70,
        "Java":65,
        "SQL":75,
        "Git":70
    }

    for k,v in skill.items():
        st.write(k)
        st.progress(v)

    st.subheader("Soft Skill")

    soft = pd.DataFrame({
        "Skill":[
            "Komunikasi",
            "Problem Solving",
            "Kerja Tim",
            "Leadership",
            "Public Speaking"
        ],
        "Nilai":[85,90,88,75,80]
    })

    st.dataframe(soft,use_container_width=True)

# ==============================
# PROYEK
# ==============================

elif menu == "Proyek":

    st.title("📂 Proyek")

    data = pd.DataFrame({

        "Nama Proyek":[
            "Website Portfolio",
            "Dashboard Streamlit",
            "Aplikasi To Do List",
            "Analisis Data Penjualan"
        ],

        "Teknologi":[
            "HTML CSS JS",
            "Python Streamlit",
            "Python SQLite",
            "Pandas Plotly"
        ],

        "Status":[
            "Selesai",
            "Selesai",
            "Pengembangan",
            "Selesai"
        ]

    })

    st.dataframe(data,use_container_width=True)

# ==============================
# GRAFIK
# ==============================

elif menu == "Grafik":

    st.title("📊 Visualisasi Skill")

    df = pd.DataFrame({

        "Skill":[
            "Python",
            "HTML",
            "CSS",
            "JavaScript",
            "Java",
            "SQL",
            "Git"
        ],

        "Nilai":[
            85,
            80,
            75,
            70,
            65,
            75,
            70
        ]

    })

    fig = px.bar(
        df,
        x="Skill",
        y="Nilai",
        color="Nilai",
        text="Nilai",
        title="Kemampuan Hard Skill"
    )

    st.plotly_chart(fig,use_container_width=True)

    fig2 = px.pie(
        values=[40,25,20,15],
        names=[
            "Web Development",
            "AI",
            "Data Science",
            "UI/UX"
        ],
        hole=0.5,
        title="Bidang yang Diminati"
    )

    st.plotly_chart(fig2,use_container_width=True)

# ==============================
# KONTAK
# ==============================

elif menu == "Kontak":

    st.title("📞 Kontak")

    st.info("📧 Email : amanda@email.com")

    st.info("💻 GitHub : github.com/amandakurnianingrum")

    st.info("💼 LinkedIn : linkedin.com/in/amandakurnianingrum")

    st.success("Terima kasih telah mengunjungi portfolio saya.")

import streamlit as st

# --- CONFIG ---
st.set_page_config(
    page_title="Ana Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR (buat navigasi simpel) ---
with st.sidebar:
    st.title("Ana Widiyawati")
    st.subheader("Data Enthusiast • Planogram")
    
    st.markdown("---")
    st.markdown("**Quick Links**")
    if st.button("About", use_container_width=True):
        st.session_state.section = "about"
    if st.button("Skills", use_container_width=True):
        st.session_state.section = "skills"
    if st.button("Projects", use_container_width=True):
        st.session_state.section = "projects"
    if st.button("Contact", use_container_width=True):
        st.session_state.section = "contact"
    
    st.markdown("---")
    st.markdown("**Connect**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/ana-widiyawati/)")
    st.markdown("[GitHub](https://github.com/anawidiyawa-create)")

    # Default section kalau belum klik apa-apa
if "section" not in st.session_state:
    st.session_state.section = "about"

# --- MAIN CONTENT ---
st.title("Halo! Saya Ana Widiyawati 👋")

if st.session_state.section == "about":
    st.header("About Me")
    st.markdown("""
    Saya adalah seorang profesional yang termotivasi dan berorientasi pada detail, sedang melakukan transisi ke bidang Data Analytics melalui bootcamp 6 bulan yang berfokus pada Python, SQL, Excel, dan Power BI. Memiliki latar belakang di Business Development, Marketing, dan Commercial Analytics di Blibli dan Traveloka, berpengalaman dalam membaca data, melacak KPI, serta mengubah informasi menjadi insight yang mendukung pertumbuhan bisnis. Senang mempelajari hal-hal baru dan menggunakan data untuk memahami tantangan, meningkatkan proses, serta membantu tim dalam membuat keputusan yang lebih baik.
    
    Fun facts:
    - Kopi hitam tanpa gula adalah bahan bakar utama ☕
    - Suka debug code sambil denger lo-fi
    - Pernah bikin bot yang malah bikin rugi sendiri 😂
    """)
    
    # Download CV tanpa gambar
    cv_data = """Ini isi CV kamu dalam text (atau link Google Drive/Dropbox kalau mau)"""
    st.download_button(
        label="📄 Download CV (PDF)",
        data=cv_data.encode('utf-8'),
        file_name="https://drive.google.com/file/d/1lZ6ESN9P_aCtgIta6SGz4oHFeFHfrAUr/view?usp=sharing",  
    )

elif st.session_state.section == "skills":
    st.header("Skills & Tools")
    
    cols = st.columns(3)
    with cols[0]:
        st.subheader("Core")
        st.markdown("- Python\n- Pandas & NumPy\n- Streamlit\n- SQL")
    
    with cols[1]:
        st.subheader("Data/ML")
        st.markdown("- Scikit-learn\n- Matplotlib / Seaborn\n- Basic Stats\n- Git & GitHub")
    

elif st.session_state.section == "projects":
    st.header("Projects Unggulan")
    
    st.subheader("RFM Customer Analytics Dashboard")
    st.markdown("""
    - Tech: Power BI + Python
    - Tentang: Customer Segmentation & Revenue Growth Strategy RFM Analysis on Superstore Dataset (2014–2017)
    - Impact: Mengidentifikasi segmen pelanggan utama, menentukan prioritas untuk retensi dan akuisisi, serta memberikan rekomendasi berbasis data guna meningkatkan kontribusi revenue.
    → [Demo](https://www.canva.com/design/DAG6EsCgLKs/3yOh8LwsAQdR9EIpENTYsA/view?utm_content=DAG6EsCgLKs&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h70a1091381) | [Source](https://github.com/anawidiyawa-create/RFM)
    """)


elif st.session_state.section == "contact":
    st.header("Hubungi Saya")
    st.markdown(""" Email: anawidiyawati@gmail.com """)
    st.markdown (""" LinkedIn: linkedin.com/in/ana-widiyawati""")
    st.markdown (""" GitHub: github.com/anawidiyawa-create """)
    
    st.markdown("### Kirim Pesan Cepat")
    with st.form("contact_form"):
        name = st.text_input("Nama")
        email = st.text_input("Email")
        message = st.text_area("Pesan kamu")
        submitted = st.form_submit_button("Kirim")
        
        if submitted:
            st.info("Ini simulasi aja ya — nanti bisa connect ke email via st.experimental_get_query_params atau pakai formspree/Google Form external.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit • Last updated Feb 2026")
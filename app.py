import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="G-HEats App", page_icon="🥗", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    html, body, [class*="css"]  { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #F4FBF6; }
    .header-title { font-size: 1.5rem; font-weight: 700; color: #113214; margin-bottom: 10px; }
    .card { background: white; border-radius: 16px; padding: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.04); margin-bottom: 15px; border: 1px solid #E8F5E9; }
    .menu-row { display: flex; align-items: center; background: white; border-radius: 16px; padding: 12px; margin-bottom: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); }
    .menu-img { width: 80px; height: 80px; border-radius: 12px; object-fit: cover; margin-right: 15px; }
</style>
""", unsafe_allow_html=True)

# --- TAB NAVIGASI ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🍲 Menu", "🍱 Katering", "🎁 Reward"])

with tab1:
    st.markdown("<div class='header-title'>Halo, Fitri! 👋</div>", unsafe_allow_html=True)
    st.write("Target Harian: 1800 kcal")
    st.progress(0.7)

with tab2:
    st.markdown("<div class='header-title'>Pemesanan Menu</div>", unsafe_allow_html=True)
    
    menus = [
        {"nama": "Geprek Oat Rendah Natrium", "kal": "450 kcal"},
        {"nama": "Bakso Ikan Nila Kuah Bening", "kal": "380 kcal"},
        {"nama": "Nasi Goreng Merah Organik", "kal": "400 kcal"}
    ]
    
    for menu in menus:
        st.markdown(f"**{menu['nama']}** - {menu['kal']}")
        # INI TOMBOL YANG BISA DIKLIK:
        if st.button(f"Pesan {menu['nama']}", key=menu['nama']):
            st.success(f"Berhasil memesan {menu['nama']}!")

with tab3:
    st.markdown("<div class='header-title'>Katering Sehat</div>", unsafe_allow_html=True)
    if st.button("Langganan Paket Hemat 7 Hari"):
        st.balloons()
        st.success("Paket 7 Hari telah dipilih!")

with tab4:
    st.markdown("<div class='header-title'>Komunitas & Reward</div>", unsafe_allow_html=True)
    st.write("Poin Anda: 2150 Poin")
    if st.button("Tukar Voucher Diskon"):
        st.warning("Poin berhasil ditukar!")

import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="G-HEats App", page_icon="🥗", layout="centered")

# --- CUSTOM CSS UNTUK TAMPILAN MODERN ---
st.markdown("""
<style>
    .stApp { background-color: #F8FAF9; }
    .header-box { padding: 10px; border-bottom: 2px solid #E8F5E9; margin-bottom: 20px; }
    .menu-card { background: white; padding: 15px; border-radius: 15px; border: 1px solid #E0E0E0; margin-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2E7D32; color: white; }
</style>
""", unsafe_allow_html=True)

# --- DATA MENU ---
MENU_DATA = [
    {"nama": "Geprek Oat", "kal": "450 kcal", "img": "🍗"},
    {"nama": "Bakso Nila", "kal": "380 kcal", "img": "🍲"},
    {"nama": "Nasi Goreng", "kal": "400 kcal", "img": "🍛"}
]

# --- FUNGSI TAMPILAN ---
def render_header():
    st.markdown("<div class='header-box'><h3>Halo, Fitri! 👋</h3><p>Target Harian: 1800 kcal</p></div>", unsafe_allow_html=True)
    st.progress(0.7)

def main():
    render_header()
    
    # Navigasi Tab
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🍲 Menu", "🍱 Katering", "🎁 Reward"])

    with tab1:
        st.subheader("Sajian Hari Ini")
        st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500")
        st.write("Tetap semangat menjaga pola makan sehat!")

    with tab2:
        st.subheader("Pemesanan Menu")
        for i, item in enumerate(MENU_DATA):
            with st.container():
                st.markdown(f"""
                <div class='menu-card'>
                    <div style='font-size:30px;'>{item['img']}</div>
                    <b>{item['nama']}</b><br>{item['kal']}
                </div>
                """, unsafe_allow_html=True)
                # Key unik untuk setiap tombol agar tidak error
                if st.button(f"Pesan {item['nama']}", key=f"btn_menu_{i}"):
                    st.success(f"Berhasil memesan {item['nama']}!")

    with tab3:
        st.subheader("Katering Sehat")
        st.write("Pilih paket langganan mingguan atau bulanan.")
        if st.button("Pilih Paket 7 Hari", key="btn_katering"):
            st.balloons()

    with tab4:
        st.subheader("Reward")
        st.metric("Poin Anda", "2150 Poin")
        if st.button("Tukar Voucher", key="btn_reward"):
            st.warning("Voucher diklaim!")

if __name__ == "__main__":
    main()

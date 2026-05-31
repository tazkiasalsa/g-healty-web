import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="G-HEats App", page_icon="🥗", layout="centered")

# --- CSS UNTUK TAMPILAN MODERN ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #F8FAF9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2E7D32; color: white; border: none; }
    .card { background: white; padding: 15px; border-radius: 15px; border: 1px solid #E0E0E0; margin-bottom: 15px; }
    .header-text { font-size: 20px; font-weight: bold; color: #1B5E20; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# --- FUNGSI TAMPILAN ---
def main():
    st.markdown("<div class='header-text'>Halo, Fitri! 👋</div>", unsafe_allow_html=True)
    
    # Progress Bar Kalori
    st.write("Target Harian: 1800 kcal")
    st.progress(70) 

    # Tab Navigasi
    tabs = st.tabs(["🏠 Home", "🍲 Menu", "🍱 Katering", "🎁 Reward"])

    with tabs[0]: # HOME
        st.subheader("Sajian Hari Ini")
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400", use_column_width=True)
            st.write("**Salmon Panggang**")
        with col2:
            st.image("https://images.unsplash.com/photo-1628557044797-f21a177c37ec?w=400", use_column_width=True)
            st.write("**Smoothie Detox**")

    with tabs[1]: # MENU
        st.subheader("Pemesanan Menu")
        menu_items = [
            ("Geprek Oat Rendah Natrium", "450 kcal"),
            ("Bakso Ikan Nila", "380 kcal"),
            ("Nasi Goreng Merah", "400 kcal")
        ]
        for nama, kal in menu_items:
            with st.container():
                st.markdown(f"<div class='card'><b>{nama}</b><br>{kal}</div>", unsafe_allow_html=True)
                if st.button(f"Pesan {nama}", key=f"menu_{nama}"):
                    st.success(f"Berhasil menambahkan {nama}!")

    with tabs[2]: # KATERING
        st.subheader("Katering Sehat")
        st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800", use_column_width=True)
        if st.button("Langganan Paket 7 Hari"):
            st.balloons()
            st.success("Paket mingguan berhasil dipilih!")

    with tabs[3]: # REWARD
        st.subheader("Reward")
        st.metric("Poin Anda", "2150 Poin")
        if st.button("Tukar Voucher"):
            st.warning("Voucher berhasil diklaim!")

if __name__ == "__main__":
    main()

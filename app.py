import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="G-HEats", page_icon="🥗", layout="centered")

# --- CUSTOM CSS (Mirip UI App Mobile) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #F8FAF9; }
    .stApp { max-width: 450px; margin: 0 auto; }
    .header { font-weight: 700; color: #1B5E20; font-size: 1.5rem; margin-bottom: 5px; }
    .card { background: white; border-radius: 16px; padding: 16px; border: 1px solid #E8F5E9; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 15px; }
    .btn-green { background-color: #2E7D32 !important; color: white !important; border-radius: 20px !important; }
</style>
""", unsafe_allow_html=True)

# --- FUNGSI HEADER ---
def render_header(nama):
    st.markdown(f"<div class='header'>Halo, {nama}! 👋</div>", unsafe_allow_html=True)
    st.write("Target Harian: 1800 kcal")
    st.progress(70) # 70% progress

# --- MAIN APP ---
def main():
    render_header("Fitri")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🍲 Menu", "🍱 Katering", "🎁 Reward"])

    # TAB HOME
    with tab1:
        st.subheader("Sajian Hari Ini")
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400", use_column_width=True)
            st.write("**Salmon Panggang** (410 kcal)")
        with c2:
            st.image("https://images.unsplash.com/photo-1628557044797-f21a177c37ec?w=400", use_column_width=True)
            st.write("**Smoothie Bowl** (250 kcal)")

    # TAB MENU
    with tab2:
        st.subheader("Pemesanan & Langganan")
        menus = [("Geprek Oat", "450 kcal"), ("Bakso Ikan Nila", "380 kcal"), ("Nasi Goreng Merah", "400 kcal")]
        for i, (nama, kal) in enumerate(menus):
            with st.container():
                st.markdown(f"<div class='card'><b>{nama}</b><br>{kal}</div>", unsafe_allow_html=True)
                if st.button(f"Pesan {nama}", key=f"menu_{i}"):
                    st.success(f"Berhasil menambahkan {nama}!")

    # TAB KATERING
    with tab3:
        st.subheader("Katering Sehat")
        st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800", use_column_width=True)
        if st.button("Berlangganan Paket Hemat", key="kat_1"):
            st.balloons()
            st.success("Paket berhasil dipilih!")

    # TAB REWARD
    with tab4:
        st.subheader("Komunitas & Reward")
        st.metric("G-HEats Point", "2150 Poin")
        if st.button("Tukar Voucher", key="rew_1"):
            st.warning("Voucher berhasil diklaim!")

if __name__ == "__main__":
    main()

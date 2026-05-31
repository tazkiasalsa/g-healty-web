import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="G-HEats - Garut Healthy Eats", page_icon="🥗", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
    /* 1. KODE UNTUK MENYEMBUNYIKAN LOGO GITHUB & BAWAAN STREAMLIT */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .viewerBadge_container__1QSob {display: none;}
    
    /* 2. KODE DESAIN TAMPILAN G-HEATS (Sama seperti sebelumnya) */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #F4F7F5;
    }
    .main-title { color: #1E4620; font-weight: 700; font-size: 2.8rem; margin-bottom: 5px; }
    .subtitle { color: #556B2F; font-size: 1.1rem; margin-bottom: 25px; }
    .card { background-color: #ffffff; padding: 20px; border-radius: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px; border-left: 5px solid #2E7D32; }
    .menu-card { background-color: #ffffff; border-radius: 16px; box-shadow: 0 4px 10px rgba(0,0,0,0.04); overflow: hidden; margin-bottom: 25px; transition: transform 0.2s; border: 1px solid #eee; }
    .menu-card:hover { transform: translateY(-5px); }
    .menu-desc { padding: 15px; }
    .badge-cal { background-color: #E8F5E9; color: #2E7D32; padding: 4px 10px; border-radius: 8px; font-weight: 600; font-size: 0.85rem; }
    .badge-price { color: #1976D2; font-weight: 700; font-size: 1.1rem; }
</style>
""", unsafe_allow_html=True)
# Session State digunakan agar data tidak hilang saat tombol ditekan (halaman direfresh)
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'target_kalori' not in st.session_state:
    st.session_state.target_kalori = 1500 # Default target
if 'total_kalori' not in st.session_state:
    st.session_state.total_kalori = 0
if 'total_protein' not in st.session_state:
    st.session_state.total_protein = 0
if 'total_karbo' not in st.session_state:
    st.session_state.total_karbo = 0
if 'total_lemak' not in st.session_state:
    st.session_state.total_lemak = 0
if 'total_harga' not in st.session_state:
    st.session_state.total_harga = 0

# --- FUNGSI TAMBAH KE KERANJANG ---
def add_to_cart(item):
    st.session_state.cart.append(item['nama'])
    st.session_state.total_kalori += item['kalori_num']
    st.session_state.total_harga += item['harga_num']
    st.session_state.total_protein += item['protein']
    st.session_state.total_karbo += item['karbo']
    st.session_state.total_lemak += item['lemak']

def reset_cart():
    st.session_state.cart = []
    st.session_state.total_kalori = 0
    st.session_state.total_harga = 0
    st.session_state.total_protein = 0
    st.session_state.total_karbo = 0
    st.session_state.total_lemak = 0

# --- DATA MENU ---
menus = [
    {"nama": "Salmon Mentai Shirataki", "kalori_num": 380, "harga_num": 45000, "protein": 30, "karbo": 25, "lemak": 15, "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500", "cat": "Main"},
    {"nama": "Ayam Geprek Oat Garut", "kalori_num": 410, "harga_num": 28000, "protein": 35, "karbo": 30, "lemak": 12, "img": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=500", "cat": "Main"},
    {"nama": "Nila Bakar Madu Cikajang", "kalori_num": 320, "harga_num": 32000, "protein": 28, "karbo": 20, "lemak": 10, "img": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=500", "cat": "Main"},
    {"nama": "Sate Lilit Ayam Quinoa", "kalori_num": 290, "harga_num": 30000, "protein": 25, "karbo": 22, "lemak": 9, "img": "https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?w=500", "cat": "Main"},
    {"nama": "Soto Ayam Bening Beras Merah", "kalori_num": 280, "harga_num": 25000, "protein": 22, "karbo": 35, "lemak": 5, "img": "https://images.unsplash.com/photo-1547592165-e1d17f57655c?w=500", "cat": "Snack"},
    {"nama": "Chia Seed Pudding Mangga", "kalori_num": 150, "harga_num": 18000, "protein": 5, "karbo": 20, "lemak": 6, "img": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=500", "cat": "Snack"},
]

# --- SIDEBAR & NAVIGASI ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=150", width=80)
    st.markdown("### Halo, Fit-User! 👋")
    
    st.markdown("""
    <div style='background-color: #E3F2FD; padding: 15px; border-radius: 12px; border-left: 4px solid #1E88E5;'>
        <p style='margin:0; font-size:0.9rem; color:#1565C0;'>G-HEats Rewards Balance</p>
        <h3 style='margin:0; color:#0D47A1;'>✨ 2,150 Poin</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    menu_nav = st.radio("Navigasi Aplikasi", ["Katalog Menu Sehat", "Smart Nutrition Tracker", "Konsultasi Gizi & Komunitas"])
    
    # Keranjang Belanja di Sidebar
    st.write("---")
    st.markdown("### 🛒 Keranjang Hari Ini")
    if len(st.session_state.cart) > 0:
        for p in st.session_state.cart:
            st.markdown(f"- {p}")
        st.markdown(f"**Total: Rp {st.session_state.total_harga:,}**")
        if st.button("Kosongkan Keranjang", type="secondary"):
            reset_cart()
            st.rerun()
    else:
        st.info("Keranjang masih kosong.")

# --- HALAMAN 1: KATALOG MENU ---
if menu_nav == "Katalog Menu Sehat":
    st.markdown("<h1 class='main-title'>Garut Healthy Eats 🥗</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Mengubah makanan 'berdosa' menjadi menu sehat premium tanpa hambar.</p>", unsafe_allow_html=True)
    
    kategori = st.tabs(["Semua Menu", "Main Course (Rendah Kalori)", "Clean Comfort & Snacks"])
    
    def render_menu(filtered_menus):
        cols = st.columns(3)
        for idx, item in enumerate(filtered_menus):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="menu-card">
                    <img src="{item['img']}" style="width:100%; height:200px; object-fit:cover;">
                    <div class="menu-desc">
                        <h4 style="margin:0 0 8px 0; color:#1E4620;">{item['nama']}</h4>
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                            <span class="badge-cal">🔥 {item['kalori_num']} kkal</span>
                            <span class="badge-price">Rp {item['harga_num']:,}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Tombol "Pesan" yang memicu fungsi add_to_cart
                if st.button(f"Pesan Sekarang", key=f"btn_{item['nama']}_{idx}"):
                    add_to_cart(item)
                    st.toast(f"✅ {item['nama']} ditambahkan ke keranjang Tracker!")

    with kategori[0]: render_menu(menus)
    with kategori[1]: render_menu([m for m in menus if m['cat'] == 'Main'])
    with kategori[2]: render_menu([m for m in menus if m['cat'] == 'Snack'])

# --- HALAMAN 2: SMART NUTRITION TRACKER ---
elif menu_nav == "Smart Nutrition Tracker":
    st.markdown("<h2 style='color:#1E4620;'>📊 Smart Nutrition Tracker</h2>", unsafe_allow_html=True)
    
    # Kalkulator Target Kalori Harian
    with st.expander("⚙️ Atur Ulang Target Kalori (Kalkulator)"):
        c1, c2 = st.columns(2)
        berat = c1.number_input("Berat Badan (kg)", value=65)
        tinggi = c2.number_input("Tinggi Badan (cm)", value=165)
        if st.button("Hitung Target Defisit Kalori"):
            # Rumus kasar sederhana untuk demonstrasi
            target_baru = int((berat * 10) + (tinggi * 6.25) - 500) 
            st.session_state.target_kalori = target_baru
            st.success(f"Target kalori harian disetel ke {target_baru} kkal untuk defisit.")

    st.write("### Progres Konsumsi Hari Ini")
    
    # Menghitung persentase progres
    persentase = st.session_state.total_kalori / st.session_state.target_kalori
    if persentase > 1.0: persentase = 1.0 # Maksimal bar 100%
    
    st.progress(persentase)
    st.markdown(f"<p style='font-size:1.2rem; font-weight:600; color:#2E7D32;'>✨ {int(persentase*100)}% Terpenuhi ({st.session_state.total_kalori} / {st.session_state.target_kalori} kkal)</p>", unsafe_allow_html=True)
    
    # Grafik Makronutrisi Dinamis dari Keranjang
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("**Total Makronutrisi dari pesananmu:**")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="🥩 Protein", value=f"{st.session_state.total_protein}g")
    col2.metric(label="🍚 Karbohidrat", value=f"{st.session_state.total_karbo}g")
    col3.metric(label="🥑 Lemak Baik", value=f"{st.session_state.total_lemak}g")
    st.markdown("</div>", unsafe_allow_html=True)

# --- HALAMAN 3: KONSULTASI & KOMUNITAS ---
elif menu_nav == "Konsultasi Gizi & Komunitas":
    st.markdown("<h2 style='color:#1E4620;'>💬 Konsultasi Gizi Gratis & Healthy Squad</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card" style="border-left: 5px solid #1E88E5;">
        <h4 style="margin:0 0 5px 0; color:#1565C0;">💬 Chat dengan Ahli Gizi Kami</h4>
        <p style="margin:0; font-size:0.9rem; color:#555;">Konsultasikan berat badan idealmu langsung dengan Ahli Gizi G-HEats!</p>
    </div>
    """, unsafe_allow_html=True)
    
    user_msg = st.text_input("Ketik pertanyaan Anda...")
    if st.button("Kirim"):
        if user_msg: st.success("Pesan terkirim! Ahli gizi akan membalas segera.")
            
    st.write("---")
    st.markdown("### 👥 Komunitas 'Healthy Squad'")
    st.text_area("Live Feed", value="Mhs_Uniga99: Ayam Geprek Oat enak parah!\nDietGarut_Fit: Besok jalan pagi di Kerkof yuk teman-teman!", height=100, disabled=True)

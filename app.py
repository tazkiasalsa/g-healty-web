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
    html, body, [class*="css"]  {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #F4FBF6;
    }
    .header-title { font-size: 1.5rem; font-weight: 700; color: #113214; margin-bottom: 10px; }
    .card { background: white; border-radius: 16px; padding: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.04); margin-bottom: 15px; border: 1px solid #E8F5E9; }
    .card-img-top { border-radius: 12px; width: 100%; height: 140px; object-fit: cover; margin-bottom: 10px; }
    .tag-green { background: #E8F5E9; color: #2E7D32; padding: 4px 8px; border-radius: 6px; font-size: 0.75rem; font-weight: 600; display: inline-block;}
    .menu-row { display: flex; align-items: center; background: white; border-radius: 16px; padding: 12px; margin-bottom: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); border: 1px solid #eee; }
    .menu-img { width: 80px; height: 80px; border-radius: 12px; object-fit: cover; margin-right: 15px; }
    .menu-info h4 { margin: 0 0 5px 0; font-size: 1rem; color: #1E4620; }
    .menu-info p { margin: 0; font-size: 0.85rem; color: #666; }
    .point-card { background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%); padding: 20px; border-radius: 16px; text-align: center; margin-bottom: 20px;}
    .doctor-card { display: flex; align-items: center; background: white; padding: 15px; border-radius: 16px; border: 1px solid #4CAF50; }
</style>
""", unsafe_allow_html=True)

# --- TAB NAVIGASI ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🍲 Menu", "🍱 Katering", "🎁 Reward"])

with tab1:
    st.markdown("<div class='header-title'>Halo, Fitri! 👋</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="text-align:center; border-top: 4px solid #4CAF50;">
        <h2 style="color:#2E7D32; margin:0; font-size: 2.5rem;">70%</h2>
        <p style="margin:0; color:#555; font-weight:600;">Target Harian: 1800 kcal</p>
        <p style="font-size:0.8rem; color:#888;">🟢 Terpenuhi 1260 kcal</p>
    </div>
    """, unsafe_allow_html=True)
    st.progress(0.7)
    
    st.markdown("### Sajian Hari Ini")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <img src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500" class="card-img-top">
            <h5 style="margin:0;">Salmon Panggang</h5>
            <span class="tag-green">410 kcal</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <img src="https://images.unsplash.com/photo-1628557044797-f21a177c37ec?w=500" class="card-img-top">
            <h5 style="margin:0;">Smoothie Detox</h5>
            <span class="tag-green">250 kcal</span>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='header-title'>Pemesanan Menu</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color:#2E7D32; color:white; padding:20px; border-radius:16px; margin-bottom:20px;">
        <h2 style="margin:0;">Ubah Jajanan<br>Favoritmu!</h2>
        <p style="margin:0; opacity:0.8;">Lebih sehat, lebih nikmat.</p>
    </div>
    """, unsafe_allow_html=True)
    
    menus = [
        {
            "img": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=200", 
            "nama": "Geprek Oat Rendah Natrium", 
            "kal": "450 kcal"
        },
        {
            "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=200", 
            "nama": "Bakso Ikan Nila Kuah Bening", 
            "kal": "380 kcal"
        },
        {
            "img": "https://images.unsplash.com/photo-1603048297172-c92544798d5e?w=200", 
            "nama": "Nasi Goreng Merah Organik", 
            "kal": "400 kcal"
        }
    ]
    
    # Kode yang rawan error sudah dirombak total di bawah ini:
    for menu in menus:
        html_content = '<div class="menu-row">'
        html_content += '<img src="' + menu["img"] + '" class="menu-img">'
        html_content += '<div class="menu-info" style="flex:1;">'
        html_content += '<h4>' + menu["nama"] + '</h4>'
        html_content += '<p>Mulai dari <strong style="color:#2E7D32;">' + menu["kal"] + '</strong></p>'
        html_content += '<div style="margin-top:5px;"><span class="tag-green">✅ Gizi Lengkap</span></div>'
        html_content += '</div></div>'
        
        st.markdown(html_content, unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='header-title'>Katering Sehat</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="padding:0; overflow:hidden;">
        <img src="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800" style="width:100%; height:200px; object-fit:cover;">
        <div style="padding: 15px;">
            <h3 style="margin:0 0 5px 0;">Salmon Mentai Shirataki</h3>
            <span class="tag-green">380 kcal</span>
            <p style="font-size:0.9rem; color:#666; margin-top:10px;">Menu premium dengan bahan lokal Garut, saus mentai rendah kalori yang aman untuk diet.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Paket Katering")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='card' style='text-align:center;'><h4>Paket Hemat<br>7 Hari</h4><button style='background:#4CAF50; color:white; border:none; padding:8px 15px; border-radius:20px; width:100%; margin-top:10px;'>Pilih</button></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card' style='text-align:center;'><h4>Paket Full<br>30 Hari</h4><button style='background:#4CAF50; color:white; border:none; padding:8px 15px; border-radius:20px; width:100%; margin-top:10px;'>Pilih</button></div>", unsafe_allow_html=True)

with tab4:
    st.markdown("<div class='header-title'>Komunitas & Reward</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="point-card">
        <p style="margin:0; color:#2E7D32; font-weight:600;">G-HEats Point Balance</p>
        <h1 style="margin:0; color:#1B5E20; font-size:2.8rem;">🌱 2150 Poin</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Konsultasi Gizi Gratis")
    st.markdown("""
    <div class="doctor-card">
        <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=200" style="width:60px; height:60px; border-radius:30px; object-fit:cover; margin-right:15px;">
        <div style="flex:1;">
            <h4 style="margin:0;">Dr. Sarah 🩺</h4>
            <p style="margin:0; font-size:0.85rem; color:#666;">Ahli Gizi, Garut</p>
        </div>
        <button style="background:#2E7D32; color:white; border:none; padding:8px 15px; border-radius:20px; cursor:pointer;">Chat</button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Tukar Poinmu!")
    rc1, rc2 = st.columns(2)
    with rc1:
        st.markdown("<div class='card' style='text-align:center;'>🏷️<br><b>Voucher Diskon</b></div>", unsafe_allow_html=True)
    with rc2:
        st.markdown("<div class='card' style='text-align:center;'>🥦<br><b>Produk Organik</b></div>", unsafe_allow_html=True)

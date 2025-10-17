
# ======================================================
# 🎯 TEKA-TEKI FAMILY ATOK HASSAN
# Dibuat khas untuk dimainkan bersama keluarga!
# Jalankan guna: streamlit run keluarga_ceria.py
# ======================================================

import streamlit as st

# Tajuk utama
st.set_page_config(page_title="Teka-Teki Family Atok Hassan", page_icon="🎉")
st.title("🎉 TEKA-TEKI FAMILY ATOK HASSAN 🎉")
st.write("Mari kita tengok siapa paling cepat dan tepat dalam menjawab teka-teki lucu hari ini! 😄")

# Soalan teka-teki
soalan = [
    {"soalan": "Buah apa yang takut? 🍌", "jawapan": "buah takut"},
    {"soalan": "Dalam banyak-banyak ikan, ikan apa yang pemalu? 🐟", "jawapan": "ikan malu"},
    {"soalan": "Kasut apa yang boleh makan? 👟", "jawapan": "kasut tart"},
    {"soalan": "Benda apa bila basah makin ringan? 💧", "jawapan": "tuala"},
    {"soalan": "Apa beza ayam dengan surat? 🐔📩", "jawapan": "ayam ada sayap surat ada stem"},
    {"soalan": "Buah apa selalu marah? 🍊", "jawapan": "buah naga"},
    {"soalan": "Kereta apa paling malas? 🚗", "jawapan": "kereta malas"},
    {"soalan": "Nasi apa yang menari? 🍚", "jawapan": "nasi lemak bergoyang"},
    {"soalan": "Sayur apa yang pandai menyanyi? 🥬", "jawapan": "kobis mariah carey"},
    {"soalan": "Burung apa pandai kira? 🐦", "jawapan": "burung kalkulator"},
]

# Simpan markah semua pemain
if "rekod" not in st.session_state:
    st.session_state.rekod = {}

# Input nama pemain
nama = st.text_input("Masukkan nama anda 👤")

if nama:
    skor = 0
    st.write(f"Hai **{nama}**, selamat menjawab teka-teki! 🤩")

    for i, s in enumerate(soalan, 1):
        jawapan_pengguna = st.text_input(f"{i}. {s['soalan']}", key=f"{nama}_{i}")
        if jawapan_pengguna:
            if jawapan_pengguna.strip().lower() == s["jawapan"]:
                st.success("✅ Betul!")
                skor += 1
            else:
                st.error("❌ Salah...")

    if st.button("Hantar Markah"):
        st.session_state.rekod[nama] = skor
        st.success(f"Markah anda: **{skor} / {len(soalan)}** 🎯")

# Paparan markah semua pemain
if st.session_state.rekod:
    st.subheader("🏆 Papan Markah Keluarga 🏆")
    for pemain, markah in st.session_state.rekod.items():
        st.write(f"👤 {pemain} — {markah} / {len(soalan)}")

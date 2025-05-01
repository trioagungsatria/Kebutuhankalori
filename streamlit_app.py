import streamlit as st

st.set_page_config(page_title="Rekomendasi Makanan", page_icon="🍧", layout="centered")

# Sidebar untuk navigasi antar slide
page = st.sidebar.selectbox("Pilih Halaman", ["Rekomendasi Makanan", "Tentang Aplikasi"])

# Slide: Rekomendasi Makanan (kode asli kamu)

if page == "Rekomendasi Makanan":
    # Judul aplikasi
    st.title("Rekomendasi Makanan Berdasarkan Aktivitas & Usia")

    # Input pengguna
    age = st.number_input("Masukkan umur Anda (tahun)", min_value=1, max_value=100)
    gender = st.selectbox("Pilih jenis kelamin", ["Pria", "Wanita"])
    activity_level = st.selectbox("Tingkat aktivitas fisik Anda", ["Rendah", "Sedang", "Tinggi"])

    # Fungsi untuk menentukan makanan berdasarkan input
    def get_food_recommendations(age, gender, activity_level):
        recommended = {}
        to_avoid = {}

        if age < 18:
            recommended.update({
                "Susu rendah lemak": 250,
                "Sayuran hijau": 100,
                "Protein hewani dan nabati": 150
            })
            to_avoid.update({
                "Makanan cepat saji": 200,
                "Minuman bersoda": 330,
                "Makanan tinggi gula": 100
            })
        elif 18 <= age <= 50:
            recommended.update({
                "Karbohidrat kompleks (nasi merah, oatmeal)": 200,
                "Sayuran & buah segar": 300,
                "Protein (telur, ayam, tahu)": 200
            })
            to_avoid.update({
                "Gorengan": 150,
                "Makanan olahan": 180,
                "Terlalu banyak kafein": 200
            })
        else:  # usia di atas 50
            recommended.update({
                "Makanan tinggi kalsium": 250,
                "Ikan berlemak (salmon, sarden)": 150,
                "Sayur berserat tinggi": 200
            })
            to_avoid.update({
                "Makanan asin": 150,
                "Daging merah berlebihan": 200,
                "Gula tinggi": 100
            })

        if activity_level == "Tinggi":
            recommended.update({
                "Karbohidrat sehat (ubi, roti gandum)": 250,
                "Pisang": 120,
                "Air mineral yang cukup": 2000
            })
        elif activity_level == "Rendah":
            to_avoid.update({
                "Camilan manis": 100,
                "Minuman manis": 250,
                "Lemak jenuh": 70
            })

        return recommended, to_avoid

    # Tampilkan rekomendasi saat tombol ditekanif st.button("Tampilkan Rekomendasi"):
if st.button("Tampilkan Rekomendasi"):
    good_foods, avoid_foods = get_food_recommendations(age, gender, activity_level)

    # Makanan yang direkomendasikan
    st.subheader(f"✅ Makanan yang Direkomendasikan (Total: {len(good_foods)} jenis):")
    total_recommended_grams = 0
    recommended_text = ""
    for food, gram in good_foods.items():
        recommended_text += f"- {food}: <b>{gram} gram</b><br>"
        total_recommended_grams += gram
    recommended_text += f"<br><b>Total konsumsi yang disarankan: {total_recommended_grams} gram/ml</b>"

    st.markdown(
        f"""
        <div style="background-color: #b30000; padding: 15px; border-radius: 10px; color: white;">
            {recommended_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Makanan yang dihindari
    st.subheader(f"🚫 Makanan yang Sebaiknya Dihindari (Total: {len(avoid_foods)} jenis):")
    total_avoid_grams = 0
    avoid_text = ""
    for food, gram in avoid_foods.items():
        avoid_text += f"- {food}: <b>{gram} gram</b><br>"
        total_avoid_grams += gram
    avoid_text += f"<br><b>Total konsumsi yang perlu dibatasi: {total_avoid_grams} gram/ml</b>"

    st.markdown(
        f"""
        <div style="background-color: #cc0000; padding: 15px; border-radius: 10px; color: white;">
            {avoid_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    )


# Slide: Tentang Aplikasi
elif page == "Tentang Aplikasi":
    st.title("Tentang Aplikasi")
    st.markdown("""
    Aplikasi **Rekomendasi Makanan Berdasarkan Aktivitas & Usia** dibuat untuk memberikan panduan sederhana mengenai pola makan sehat berdasarkan kondisi individu.
    
    - Menggunakan data usia dan aktivitas untuk menentukan saran gizi
    - Rekomendasi bersifat umum dan bukan pengganti nasihat medis
    
    💡 Dibuat dengan Streamlit oleh [Tim Anda]
    """)
    



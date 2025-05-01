import streamlit as st

st.set_page_config(page_title="Rekomendasi Makanan", page_icon="🍧", layout="centered")

page = st.sidebar.selectbox("Pilih Halaman", ["Rekomendasi Makanan", "Tentang Aplikasi"])

# Fungsi rekomendasi
def get_food_recommendations(age, gender, activity_level, weight):
    recommended = {}
    to_avoid = {}

    adjustment_factor = weight / 60.0  # patokan berat badan 60 kg

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
    else:
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

    # Penyesuaian berat badan
    for food in recommended:
        recommended[food] = int(recommended[food] * adjustment_factor)

    for food in to_avoid:
        adjusted = to_avoid[food] * adjustment_factor
        max_limit = to_avoid[food] * 1.3
        to_avoid[food] = int(min(adjusted, max_limit))

    return recommended, to_avoid

# Halaman utama
if page == "Rekomendasi Makanan":
    st.title("Rekomendasi Makanan Berdasarkan Aktivitas & Usia")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color: rgba(0, 102, 204, 0.25); padding: 8px 12px; border-radius: 8px; color: black;">
            <b>Umur Anda (tahun)</b>
        </div>
        """, unsafe_allow_html=True)
        age = st.number_input("", min_value=1, max_value=100, key="age_input")

        st.markdown("""
        <div style="background-color: rgba(0, 102, 204, 0.25); padding: 8px 12px; border-radius: 8px; color: black;">
            <b>Berat Badan Anda (kg)</b>
        </div>
        """, unsafe_allow_html=True)
        weight = st.number_input("", min_value=1.0, max_value=200.0, step=0.1, key="weight_input")

    with col2:
        st.markdown("""
        <div style="background-color: rgba(0, 102, 204, 0.25); padding: 8px 12px; border-radius: 8px; color: black;">
            <b>Pilih jenis kelamin</b>
        </div>
        """, unsafe_allow_html=True)
        gender = st.selectbox("", ["Pria", "Wanita"], key="gender_input")

        st.markdown("""
        <div style="background-color: rgba(0, 102, 204, 0.25); padding: 8px 12px; border-radius: 8px; color: black;">
            <b>Tingkat aktivitas fisik Anda</b>
        </div>
        """, unsafe_allow_html=True)
        activity_level = st.selectbox("", ["Rendah", "Sedang", "Tinggi"], key="activity_input")

    if st.button("Tampilkan Rekomendasi"):
        good_foods, avoid_foods = get_food_recommendations(age, gender, activity_level, weight)

        # Rekomendasi makanan
        st.subheader(f"✅ Makanan yang Direkomendasikan (Total: {len(good_foods)} jenis):")
        total_recommended_grams = 0
        recommended_text = ""
        for food, gram in good_foods.items():
            recommended_text += f"- {food}: <b>{gram} gram</b><br>"
            total_recommended_grams += gram
        recommended_text += f"<br><b>Total konsumsi yang disarankan: {total_recommended_grams} gram/ml</b>"

        st.markdown(
            f"""
            <div style="background-color: rgba(200, 0, 0, 0.4); padding: 15px; border-radius: 10px; color: white;">
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
            <div style="background-color: rgba(180, 0, 0, 0.4); padding: 15px; border-radius: 10px; color: white;">
                {avoid_text}
            </div>
            """,
            unsafe_allow_html=True
        )

# Halaman tentang
elif page == "Tentang Aplikasi":
    st.title("Tentang Aplikasi")
    st.markdown("""
    Aplikasi **Rekomendasi Makanan Berdasarkan Aktivitas & Usia** dibuat untuk memberikan panduan sederhana mengenai pola makan sehat berdasarkan kondisi individu.

    - Berdasarkan data umur, berat badan, dan aktivitas fisik
    - Rekomendasi bersifat umum dan bukan pengganti nasihat medis profesional

    💡 Dibuat dengan Streamlit oleh [Tim Anda]
    """)






    



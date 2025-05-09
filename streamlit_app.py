import streamlit as st

st.set_page_config(page_title="Rekomendasi Makanan", page_icon="🍧", layout="centered")

# Sidebar Navigasi
page = st.sidebar.selectbox("Pilih Halaman", ["Rekomendasi Makanan", "Tentang Aplikasi"])

# Fungsi rekomendasi makanan
def get_food_recommendations(age, gender, activity_level, weight):
    recommended = {}
    to_avoid = {}

    adjustment_factor = weight / 60.0

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

    for food in recommended:
        recommended[food] = int(recommended[food] * adjustment_factor)
    for food in to_avoid:
        adjusted = to_avoid[food] * adjustment_factor
        to_avoid[food] = int(min(adjusted, to_avoid[food] * 1.3))

    return recommended, to_avoid

# Fungsi menampilkan efek baik dan risiko
def generate_effects(recommended_foods, avoided_foods):
    efek_baik = []
    risiko = []

    if "Sayuran hijau" in recommended_foods or "Sayuran & buah segar" in recommended_foods:
        efek_baik.append("Meningkatkan sistem imun dan pencernaan")
    if "Protein" in "".join(recommended_foods.keys()):
        efek_baik.append("Mendukung pertumbuhan dan perbaikan sel")
    if "Karbohidrat kompleks" in recommended_foods or "Karbohidrat sehat (ubi, roti gandum)" in recommended_foods:
        efek_baik.append("Memberi energi lebih stabil sepanjang hari")
    if "Ikan berlemak (salmon, sarden)" in recommended_foods:
        efek_baik.append("Menjaga kesehatan jantung dan otak")

    if "Gorengan" in avoided_foods or "Makanan cepat saji" in avoided_foods:
        risiko.append("Risiko kolesterol tinggi dan gangguan jantung")
    if "Minuman bersoda" in avoided_foods or "Minuman manis" in avoided_foods:
        risiko.append("Meningkatkan risiko diabetes dan obesitas")
    if "Gula tinggi" in avoided_foods or "Makanan tinggi gula" in avoided_foods:
        risiko.append("Gangguan metabolisme dan resistensi insulin")
    if "Makanan asin" in avoided_foods:
        risiko.append("Peningkatan tekanan darah dan gangguan ginjal")

    return efek_baik, risiko

# Halaman Rekomendasi
if page == "Rekomendasi Makanan":
    st.markdown(
        """
        <div style="background-color: rgba(0, 102, 204, 0.7); padding:20px; border-radius:10px; color:white; text-align:center;">
            <h2>Rekomendasi Makanan Berdasarkan Aktivitas & Usia</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Masukkan Data Anda")

    with st.container():
        st.markdown("#### 🧓 Umur Anda")
        age = st.number_input("Masukkan umur Anda (tahun)", min_value=1, max_value=100, key="age")
        st.markdown("#### ⚖️ Berat Badan Anda")
        weight = st.number_input("Masukkan berat badan Anda (kg)", min_value=1.0, max_value=200.0, step=0.1, key="weight")
        st.markdown("#### 🚻 Jenis Kelamin")
        gender = st.selectbox("Pilih jenis kelamin", ["Pria", "Wanita"], key="gender")
        st.markdown("#### 🏃‍♂️ Tingkat Aktivitas Fisik")
        activity_level = st.selectbox("Tingkat aktivitas fisik Anda", ["Rendah", "Sedang", "Tinggi"], key="activity")

    if st.button("Tampilkan Rekomendasi"):
        good_foods, avoid_foods = get_food_recommendations(age, gender, activity_level, weight)
        efek_baik, risiko = generate_effects(good_foods, avoid_foods)

        # Rekomendasi
        st.subheader("✔❤ Makanan yang Direkomendasikan:")
        total_recommended_grams = sum(good_foods.values())
        recommended_html = "".join([f"- {food}: <b>{gram} gram</b><br>" for food, gram in good_foods.items()])
        recommended_html += f"<br><b>Total konsumsi yang disarankan: {total_recommended_grams} gram/ml</b>"

        st.markdown(
            f"""
            <div style="background-color: rgba(255, 0, 0, 0.3); padding: 15px; border-radius: 10px; color: white;">
                {recommended_html}
            </div>
            """, unsafe_allow_html=True
        )

        # Hindari
        st.subheader("❌💔 Makanan yang Sebaiknya Dihindari:")
        total_avoid_grams = sum(avoid_foods.values())
        avoid_html = "".join([f"- {food}: <b>{gram} gram</b><br>" for food, gram in avoid_foods.items()])
        avoid_html += f"<br><b>Total konsumsi yang perlu dibatasi: {total_avoid_grams} gram/ml</b>"

        st.markdown(
            f"""
            <div style="background-color: rgba(180, 0, 0, 0.4); padding: 15px; border-radius: 10px; color: white;">
                {avoid_html}
            </div>
            """, unsafe_allow_html=True
        )

        # Efek Baik
        if efek_baik:
            st.subheader("🌿 Efek Baik Jika Mengonsumsi Makanan yang Direkomendasikan:")
            st.markdown(
                f"""
                <div style="background-color: rgba(0, 153, 76, 0.4); padding: 15px; border-radius: 10px; color: white;">
                    {"<br>".join(["- " + item for item in efek_baik])}
                </div>
                """,
                unsafe_allow_html=True
            )

        # Risiko
        if risiko:
            st.subheader("⚠️ Risiko Jika Tidak Menghindari Makanan Tersebut:")
            st.markdown(
                f"""
                <div style="background-color: rgba(0, 153, 76, 0.4); padding: 15px; border-radius: 10px; color: white;">
                    {"<br>".join(["- " + item for item in risiko])}
                </div>
                """,
                unsafe_allow_html=True
            )

# Halaman Tentang
elif page == "Tentang Aplikasi":
    st.title("Tentang Aplikasi")
    st.markdown("""
    Aplikasi **Rekomendasi Makanan Berdasarkan Aktivitas & Usia** dibuat untuk memberikan panduan sederhana mengenai pola makan sehat berdasarkan kondisi individu.

    - Berdasarkan data umur, berat badan, dan aktivitas fisik
    - Rekomendasi bersifat umum dan bukan pengganti nasihat medis profesional

    💡 Dibuat dengan Streamlit oleh [Tim Anda]
    """)

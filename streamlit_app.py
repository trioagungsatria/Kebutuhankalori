import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Rekomendasi Makanan", page_icon="🍧", layout="centered")

# Sidebar Navigasi
page = st.sidebar.selectbox("Pilih Halaman", [
    "Rekomendasi Makanan",
    "Efek Konsumsi Makanan",
    "Tentang Aplikasi"
])

# Fungsi rekomendasi makanan
def get_food_recommendations(age, gender, activity_level, weight):
    recommended = {}
    to_avoid = {}

    adjustment_factor = weight / 60.0  # berat badan standar

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
        to_avoid[food] = int(min(adjusted, to_avoid[food] * 1.3))

    return recommended, to_avoid

# Halaman Rekomendasi
if page == "Rekomendasi Makanan":
    st.title("Rekomendasi Makanan Berdasarkan Aktivitas & Usia")

    st.markdown("### Masukkan Data Anda")

    # Kolom Input dengan Background Biru
    with st.container():
        st.markdown('<div style="background-color: rgba(0, 102, 204, 0.7); padding:30px; border-radius:10px;">', unsafe_allow_html=True)

        age = st.number_input("Masukkan umur Anda (tahun)", min_value=1, max_value=100, key="age")
        weight = st.number_input("Masukkan berat badan Anda (kg)", min_value=1.0, max_value=200.0, step=0.1, key="weight")
        gender = st.selectbox("Pilih jenis kelamin", ["Pria", "Wanita"], key="gender")
        activity_level = st.selectbox("Tingkat aktivitas fisik Anda", ["Rendah", "Sedang", "Tinggi"], key="activity")

        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Tampilkan Rekomendasi"):
        good_foods, avoid_foods = get_food_recommendations(age, gender, activity_level, weight)

        st.session_state.good_foods = good_foods
        st.session_state.avoid_foods = avoid_foods

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

        st.subheader("❌💔 Makanan yang Sebaiknya Dihindari:")
        total_avoid_grams = sum(avoid_foods.values())
        avoid_html = "".join([f"- {food}: <b>{gram} gram</b><br>" for food, gram in avoid_foods.items()])
        avoid_html += f"<br><b>Total konsumsi yang perlu dibatasi: {total_avoid_grams} gram/ml</b>"

        st.markdown(
            f"""
            <div style="background-color: rgba(180, 0, 0, 0.4); padding: 15px; border-radius: 10px; color: white;">
                {avoid_html}
            </div>
            """,
            unsafe_allow_html=True
        )

# Halaman Efek Konsumsi
elif page == "Efek Konsumsi Makanan":
    st.title("Efek Konsumsi Makanan Tidak Direkomendasikan")

    avoid_foods = st.session_state.get("avoid_foods", {})

    if avoid_foods:
        st.markdown("### Dampak Menghindari vs. Mengonsumsi")

        efek_baik = {
            "Makanan cepat saji": "Menurunkan risiko obesitas",
            "Minuman bersoda": "Menjaga kestabilan gula darah",
            "Makanan tinggi gula": "Mencegah diabetes",
            "Gorengan": "Menurunkan kolesterol",
            "Makanan olahan": "Mengurangi risiko kanker",
            "Terlalu banyak kafein": "Tidur lebih nyenyak",
            "Makanan asin": "Tekanan darah lebih stabil",
            "Daging merah berlebihan": "Menurunkan risiko jantung",
            "Gula tinggi": "Mencegah resistensi insulin",
            "Camilan manis": "Menjaga berat badan ideal",
            "Minuman manis": "Mencegah lonjakan gula darah",
            "Lemak jenuh": "Menjaga pembuluh darah"
        }

        # Efek visual
        efek_list = []
        for food in avoid_foods:
            efek = efek_baik.get(food, "Menjaga kesehatan secara umum")
            efek_list.append((food, efek))

        for makanan, efek in efek_list:
            st.markdown(f"**{makanan}**\n- 📈 Jika dikonsumsi: Risiko meningkat\n- 📉 Jika dihindari: {efek}")

        # Chart sederhana
        st.markdown("### Visualisasi Risiko Konsumsi")
        labels = [food for food in avoid_foods.keys()]
        values = [avoid_foods[food] for food in avoid_foods.keys()]

        fig, ax = plt.subplots()
        ax.barh(labels, values, color="crimson")
        ax.set_xlabel("Potensi Risiko (gram/ml berlebih)")
        ax.set_title("Tingkat Risiko dari Makanan Tidak Direkomendasikan")
        st.pyplot(fig)
    else:
        st.info("Silakan kunjungi halaman 'Rekomendasi Makanan' terlebih dahulu.")

# Halaman Tentang
elif page == "Tentang Aplikasi":
    st.title("Tentang Aplikasi")
    st.markdown("""
    Aplikasi **Rekomendasi Makanan Berdasarkan Aktivitas & Usia** dibuat untuk memberikan panduan sederhana mengenai pola makan sehat berdasarkan kondisi individu.

    - Berdasarkan data umur, berat badan, dan aktivitas fisik
    - Rekomendasi bersifat umum dan bukan pengganti nasihat medis profesional

    💡 Dibuat dengan Streamlit oleh [Tim Anda]
    """)















    



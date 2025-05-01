import streamlit as st

st.set_page_config(page_title="Rekomendasi Makanan", page_icon="🍧", layout="centered")

page = st.sidebar.selectbox("Pilih Halaman", ["Rekomendasi Makanan", "Tentang Aplikasi"])

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
        }







    



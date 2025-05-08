import streamlit as st
import altair as alt
import pandas as pd

def main():
    # Konfigurasi halaman Streamlit
    st.set_page_config(page_title="Aplikasi Rekomendasi Makanan", layout="wide")
    st.title("🍽️ Aplikasi Rekomendasi Makanan Sehat")
    
    # Sidebar untuk navigasi antar halaman
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Pilih Halaman:", ("Rekomendasi Makanan", "Efek Konsumsi Makanan"))
    
    if page == "Rekomendasi Makanan":
        halaman_rekomendasi()
    elif page == "Efek Konsumsi Makanan":
        halaman_efek()

def halaman_rekomendasi():
    st.header("Rekomendasi Makanan Berdasarkan Profil Pengguna")
    st.write("""
        Masukkan data diri untuk mendapatkan rekomendasi makanan yang sesuai 
        dengan usia, berat badan, jenis kelamin, dan tingkat aktivitas Anda. 
        Aplikasi ini akan menampilkan daftar makanan yang direkomendasikan 
        serta yang sebaiknya dihindari.
    """)
    
    # Form input data pengguna
    usia = st.number_input("Umur (tahun)", min_value=1, max_value=120, value=25)
    berat = st.number_input("Berat Badan (kg)", min_value=10, max_value=200, value=70)
    jenis_kelamin = st.selectbox("Jenis Kelamin", ("Laki-laki", "Perempuan"))
    aktivitas = st.selectbox("Tingkat Aktivitas", ("Rendah", "Sedang", "Tinggi"))
    
    if st.button("Lihat Rekomendasi"):
        # Klasifikasi kategori berat badan berdasarkan gender
        if jenis_kelamin == "Laki-laki":
            if berat < 60:
                kategori_bb = "Underweight"
            elif berat > 75:
                kategori_bb = "Overweight"
            else:
                kategori_bb = "Normal"
        else:  # Perempuan
            if berat < 50:
                kategori_bb = "Underweight"
            elif berat > 65:
                kategori_bb = "Overweight"
            else:
                kategori_bb = "Normal"
        
        # Daftar awal makanan rekomendasi dan yang tidak direkomendasikan
        rekomendasi = ["Sayuran hijau", "Buah-buahan", "Protein tanpa lemak", "Air putih"]
        tidak_rekomendasi = ["Makanan cepat saji", "Minuman bersoda", "Gorengan", "Makanan tinggi gula"]
        
        # Tambahkan rekomendasi khusus berdasarkan kategori berat badan
        if kategori_bb == "Underweight":
            rekomendasi += ["Kacang-kacangan", "Buah kering", "Susu tinggi kalori", "Ikan berlemak"]
        elif kategori_bb == "Overweight":
            rekomendasi += ["Sayuran berserat tinggi", "Oatmeal", "Kacang hijau", "Ikan panggang"]
        else:  # Normal
            rekomendasi += ["Nasi merah", "Ayam tanpa kulit", "Telur rebus", "Yogurt"]
        
        # Tambahkan rekomendasi khusus berdasarkan tingkat aktivitas
        if aktivitas == "Tinggi":
            rekomendasi += ["Karbohidrat kompleks (roti gandum, ubi)", "Protein untuk pemulihan otot (dada ayam, ikan)"]
        elif aktivitas == "Rendah":
            rekomendasi += ["Sayuran rendah karbohidrat", "Lemak sehat (alpukat, kacang-kacangan)"]
        else:  # Sedang
            rekomendasi += ["Karbohidrat sehat (beras merah, buah)", "Protein sedang (ikan, tahu)"]
        
        # Hapus duplikat pada daftar rekomendasi
        rekomendasi = list(dict.fromkeys(rekomendasi))
        
        # Tampilkan daftar makanan rekomendasi
        st.subheader("Makanan yang Direkomendasikan")
        for makanan in rekomendasi:
            st.write("- " + makanan)
        
        # Tampilkan daftar makanan yang tidak direkomendasikan
        st.subheader("Makanan yang Tidak Direkomendasikan")
        for makanan in tidak_rekomendasi:
            st.write("- " + makanan)
        
        # Grafik komposisi makronutrien harian (horizontal bar)
        st.subheader("Grafik Komposisi Makronutrien Harian (Estimasi)")
        if aktivitas == "Rendah":
            persen = {"Karbohidrat": 45, "Protein": 30, "Lemak": 25}
        elif aktivitas == "Sedang":
            persen = {"Karbohidrat": 50, "Protein": 30, "Lemak": 20}
        else:  # Tinggi
            persen = {"Karbohidrat": 60, "Protein": 25, "Lemak": 15}
        
        df_makro = pd.DataFrame({
            "Nutrisi": list(persen.keys()),
            "Persen": list(persen.values())
        })
        bar_chart = alt.Chart(df_makro).mark_bar(color='teal').encode(
            x=alt.X('Persen:Q', title='Persentase (%)'),
            y=alt.Y('Nutrisi:N', sort='-x', title='Jenis Nutrisi')
        ).properties(width=600)
        st.altair_chart(bar_chart, use_container_width=True)

def halaman_efek():
    st.header("Efek Konsumsi Makanan")
    st.write("""
        Halaman ini menjelaskan **efek positif** dari menghindari makanan yang tidak direkomendasikan
        serta **efek negatif** jika makanan-makanan tersebut dikonsumsi secara rutin.
    """)
    
    # Efek positif dari menghindari makanan buruk
    st.subheader("Efek Baik Menghindari Makanan Tidak Direkomendasikan")
    st.write("""
    - Menurunkan risiko penyakit jantung karena asupan lemak jenuh dan kolesterol berkurang.
    - Menjaga berat badan ideal sehingga terhindar dari obesitas.
    - Mengontrol kadar gula darah lebih baik dan menurunkan risiko diabetes.
    - Meningkatkan kesehatan pencernaan karena lebih banyak asupan serat.
    """)
    
    # Efek buruk jika makanan tidak direkomendasikan dikonsumsi
    st.subheader("Efek Buruk Jika Makanan Tidak Direkomendasikan Dikonsumsi")
    st.write("""
    - Meningkatkan risiko kenaikan berat badan dan obesitas.
    - Meningkatkan risiko penyakit jantung karena kolesterol dan lemak jenuh tinggi.
    - Meningkatkan risiko diabetes tipe 2 akibat konsumsi gula berlebihan.
    - Menyebabkan kerusakan gigi dan masalah kesehatan mulut karena makanan manis.
    """)
    
    # Visualisasi risiko penyakit (diagram batang horizontal)
    data_risiko = pd.DataFrame({
        'Penyakit': ['Jantung', 'Diabetes', 'Obesitas', 'Karies Gigi'],
        'Risiko': [8, 9, 7, 6]
    })
    bar_chart2 = alt.Chart(data_risiko).mark_bar(color='salmon').encode(
        x=alt.X('Risiko:Q', title='Level Risiko (1-10)'),
        y=alt.Y('Penyakit:N', sort='-x', title='Jenis Penyakit')
    ).properties(
        title='Estimasi Risiko Penyakit Jika Makanan Tidak Direkomendasikan Dikonsumsi',
        width=600
    )
    st.altair_chart(bar_chart2, use_container_width=True)

if __name__ == "__main__":
    main()
















    



import streamlit as st
import pandas as pd
from sqlalchemy import text

# Set page configuration
st.set_page_config(
    page_title="Kel.3 FP3 Manajemen Data v1.0.0",
    page_icon="📊",
    layout="wide"
)

st.markdown('aKelompok 3_FP3 - Aplikasi Manajemen Data v1.0.0')

image_url = "https://www.its.ac.id/wp-content/uploads/2020/07/Logo-ITS-1-300x185.png"
st.sidebar.image(image_url, caption='Kelompok 3', width=100)

list_doctor = ['', 'Dra. Lucia Aridinanti, M.Si.', 'Ir. Sri Pingit Wulandari, M.Si.', 'Prof. Dr. Wahyu Wibowo, S.Si, M.Si.', 'Dra. Sri Mumpuni Retnaningsih, M.T.', 'Iis Dewi Ratih, S.Si, M.Si.', 'Zakiatul Wildani, S.Si, M.Sc.', 'Mike Prastuti, S.Si, M.Si.', 'Muhammad Alifian Nuriman, S.Stat, M.Stat.', 'Dra. Destri Susilaningrum, M.Si.', 'Dr. Brodjol Sutijo Suprih Ulama, M.Si.', 'Dwi Endah Kusrini, S.Si, M.Si.', 'Mukti Ratna Dewi, S.Si, M.Sc.', 'Muhammad Reza Habibi, S.Si, M.Si.', 'Fausania Hibatullah, S.Stat, M.Stat.']
list_jenis_kelamin = ['', 'Laki-laki', 'Perempuan']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://dzakkirabbani99:EFm9ODoGAx2w@ep-floral-pine-60585995.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS mbdf3 (id serial, dosen_wali varchar, nama_mahasiswa varchar, jenis_kelamin char(25), \
                                                       mata_kuliah_favorit text, no_whatsapp varchar, alamat_domisili text);')
    session.execute(query)

st.header('Database Mahasiswa Kelas 3B Statistika Bisnis ITS Angkatan 2022')

st.sidebar.header("Select Menu")

page = st.sidebar.selectbox("Select by", ["View Data", "Search Data", "Edit Data (password is required)"])

if page == "View Data":
    data = conn.query('SELECT * FROM mbdf3 ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

# untuk fitur search
# ...

if page == "Search Data":
    st.sidebar.subheader("Search Data")

    # Dropdown menu for selecting search criteria
    search_criteria = st.sidebar.selectbox("Select Search Criteria", ['Dosen Wali', 'Nama Mahasiswa', 'Jenis Kelamin', 'Jam Tidur'])

    # Input widgets for search criteria based on user's choice
    if search_criteria == 'Dosen Wali':
        search_value = st.sidebar.selectbox("Search by Dosen Wali", ['', *list_doctor[1:]])
        condition = f"dosen_wali = :search_value"
        query_params = {"search_value": search_value}
    elif search_criteria == 'Nama Mahasiswa':
        search_value = st.sidebar.text_input("Search by Nama Mahasiswa", "")
        condition = f"nama_mahasiswa ILIKE :search_value"
        query_params = {"search_value": f"%{search_value}%"}
    elif search_criteria == 'Jenis Kelamin':
        search_value = st.sidebar.selectbox("Search by Jenis Kelamin", ['', 'Laki-laki', 'Perempuan'])
        condition = f"jenis_kelamin = :search_value"
        query_params = {"search_value": search_value}
    elif search_criteria == 'Jam Tidur':
        search_value = st.sidebar.time_input("Search by Jam Tidur", None)
        condition = f"jam_tidur = :search_value"
        query_params = {"search_value": search_value}
    else:
        condition = ""
        query_params = {}

    # Build the SQL query based on the chosen search criteria
    query = f'SELECT * FROM mbdf3'
    if condition:
        query += f' WHERE {condition}'
    query += ' ORDER By id;'

    # Execute the SQL query
    data = conn.query(query, params=query_params, ttl="0").set_index('id')

    # Display the result
    st.dataframe(data)

# untuk memberikan fitur password #

# ...

if page == "Edit Data (password is required)":

    # Password input for authentication
    password = st.text_input("Enter password {'pass: datamilikkelas3b_dsbfvokasiits'}", "", type="password")

    # Check if the password is correct
    correct_password = "datamilikkelas3b_dsbfvokasiits"  # Replace with your actual password

    # Flag to track if the user has successfully signed in
    signed_in = False

    # Flag to track if the password check failed
    incorrect_password = False

    # Button to trigger password check
    if st.button("Sign in"):
        if password == correct_password:
            signed_in = True  # Set the flag to True after successful login
            incorrect_password = False  # Reset the incorrect_password flag

            data = conn.query('SELECT * FROM mbdf3 ORDER By id;', ttl="0")
            for _, result in data.iterrows():        
                id = result['id']
                dosen_wali_lama = result["dosen_wali"]
                nama_mahasiswa_lama = result["nama_mahasiswa"]
                jenis_kelamin_lama = result["jenis_kelamin"]
                mata_kuliah_favorit_lama = result["mata_kuliah_favorit"]
                no_whatsapp_lama = result["no_whatsapp"]
                alamat_domisili_lama = result["alamat_domisili"]
                jam_tidur_lama = result["jam_tidur"]

                with st.expander(f'a.n. {nama_mahasiswa_lama}'):
                    with st.form(f'data-{id}'):
                        dosen_wali_baru = st.selectbox("dosen_wali", list_doctor, list_doctor.index(dosen_wali_lama))
                        nama_mahasiswa_baru = st.text_input("nama_mahasiswa", nama_mahasiswa_lama)
                        jenis_kelamin_baru = st.selectbox("jenis_kelamin", list_jenis_kelamin, list_jenis_kelamin.index(jenis_kelamin_lama))
                        mata_kuliah_favorit_baru = st.multiselect("mata_kuliah_favorit", ['Manajemen Basis Data', 'Teknik Pengambilan Sampel', 'Rancangan Percobaan', 'Pengantar Teknik Sistem dan Industri', 'Statistika Ofisial', 'Bahasa Indonesia', 'Industri dan Lembaga Keuangan'], eval(mata_kuliah_favorit_lama))
                        no_whatsapp_baru = st.text_input("no_whatsapp", no_whatsapp_lama)
                        alamat_domisili_baru = st.text_input("alamat_domisili", alamat_domisili_lama)
                        jam_tidur_baru = st.time_input("jam_tidur", jam_tidur_lama)

                        col1, col2 = st.columns([1, 6])

                        with col1:
                            if st.form_submit_button('UPDATE'):
                                with conn.session as session:
                                    query = text('UPDATE mbdf3 \
                                                  SET dosen_wali=:1, nama_mahasiswa=:2, jenis_kelamin=:3, mata_kuliah_favorit=:4, \
                                                  no_whatsapp=:5, alamat_domisili=:6, jam_tidur=:7 \
                                                  WHERE id=:8;')
                                    session.execute(query, {'1':dosen_wali_baru, '2':nama_mahasiswa_baru, '3':jenis_kelamin_baru, '4':str(mata_kuliah_favorit_baru), 
                                                            '5':no_whatsapp_baru, '6':alamat_domisili_baru, '7':jam_tidur_baru, '8':id})
                                    session.commit()
                                    st.experimental_rerun()

                        with col2:
                            if st.form_submit_button('DELETE'):
                                query = text(f'DELETE FROM mbdf3 WHERE id=:1;')
                                session.execute(query, {'1':id})
                                session.commit()
                                st.experimental_rerun()
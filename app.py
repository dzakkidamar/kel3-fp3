import streamlit as st
import pandas as pd
from sqlalchemy import text

list_doctor = ['', 'Dra. Lucia Aridinanti, M.Si.', 'Ir. Sri Pingit Wulandari, M.Si.', 'Prof. Dr. Wahyu Wibowo, S.Si, M.Si.', 'Dra. Sri Mumpuni Retnaningsih, M.T.', 'Iis Dewi Ratih, S.Si, M.Si.', 'Zakiatul Wildani, S.Si, M.Sc.', 'Mike Prastuti, S.Si, M.Si.', 'Muhammad Alifian Nuriman, S.Stat, M.Stat.', 'Dra. Destri Susilaningrum, M.Si.', 'Dr. Brodjol Sutijo Suprih Ulama, M.Si.', 'Dwi Endah Kusrini, S.Si, M.Si.', 'Mukti Ratna Dewi, S.Si, M.Sc.', 'Muhammad Reza Habibi, S.Si, M.Si.', 'Fausania Hibatullah, S.Stat, M.Stat.']
list_jenis_kelamin = ['', 'Laki-laki', 'Perempuan']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://dzakkirabbani99:ledw08gzCjma@ep-jolly-rice-21648614.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS mbdf3 (id serial, dosen_wali varchar, nama_mahasiswa varchar, jenis_kelamin char(25), \
                                                       mata_kuliah_favorit text, no_whatsapp varchar, alamat_domisili text);')
    session.execute(query)

st.header('Data Base Mahasiswa Kelas 3B Statistika Bisnis ITS Angkatan 2022')
page = st.sidebar.selectbox("Pilih Menu", ["View Data", "Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM mbdf3 ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO mbdf3 (dosen_wali, nama_mahasiswa, jenis_kelamin, mata_kuliah_favorit, no_whatsapp, alamat_domisili, jam_tidur) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'[]', '5':'', '6':'', '7':None})
            session.commit()

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
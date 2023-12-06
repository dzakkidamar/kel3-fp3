drop table if exists mbdf3;
create table mbdf3 (
	id serial,
	dosen_wali text,
	nama_mahasiswa text,
	jenis_kelamin text,
	mata_kuliah_favorit text,
	no_whatsapp text,
	alamat_domisili text,
	jam_tidur time
);

insert into mbdf3 (dosen_wali, nama_mahasiswa, jenis_kelamin, mata_kuliah_favorit, no_whatsapp, alamat_domisili, jam_tidur) 
values
	('Dr. Brodjol Sutijo Suprih Ulama, M.Si.', 'Azzam Pahlawan Ramadhan', 'Laki-laki', '["Manajemen Basis Data", "Teknik Pengambilan Sampel"]', 62895382638129, 'Asrama 1 SDM IPTEK', '23:45'),
	('Ir. Sri Pingit Wulandari, M.Si.', 'Dzakki Damar Rabbani', 'Laki-laki', '["Manajemen Basis Data", "Teknik Pengambilan Sampel"]', 6282177772050, 'Asrama 2 SDM IPTEK', '00:00'),
	('Dwi Endah Kusrini, S.Si, M.Si.', 'Farhan Bramhatchi', 'Laki-laki', '["Manajemen Basis Data", "Teknik Pengambilan Sampel"]', 6283853937043, 'Jl. Ngagel Rejo 3B/1', '01:15'),
	('Muhammad Reza Habibi, S.Si, M.Si.', 'Fauzi Dwi Aryasatyawan', 'Laki-laki', '["Manajemen Basis Data", "Teknik Pengambilan Sampel"]', 6285706013518, 'Jl.Ploso 1 no 28 surabaya', '23:15'),
	('Prof. Dr. Wahyu Wibowo, S.Si, M.Si.', 'Alesandro Yoel', 'Laki-laki', '["Manajemen Basis Data", "Teknik Pengambilan Sampel"]', 6288801739760, 'Gubeng Klingsingan I No.21', '22:50')
	;
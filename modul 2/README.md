# Analisis Listing Airbnb di Bangkok

## Latar Belakang

Bangkok sebagai destinasi wisata menyediakan berbagai jenis akomodasi melalui Airbnb, seperti kamar pribadi, rumah, apartemen, dan hotel yang dikelola oleh host.

## Permasalahan

Host menghadapi tantangan dalam menetapkan harga sewa yang optimal untuk menarik tamu dan meningkatkan pendapatan.

## Tujuan Analisis

Tujuan dari analisis ini adalah untuk mengidentifikasi faktor-faktor yang mempengaruhi harga sewa di Airbnb Bangkok. Analisis ini juga bertujuan untuk memberikan rekomendasi strategis kepada host dalam menetapkan harga sewa yang optimal dan meningkatkan daya tarik listing mereka kepada calon tamu, sehingga dapat memaksimalkan pendapatan.

## Metodologi

Analisis ini dilakukan dengan menggunakan teknik analisis statistik untuk mengevaluasi faktor-faktor yang mempengaruhi harga sewa dan visualisasi data untuk mendukung hasil analisis.

## Batasan Analisis
- **Cakupan Data**: Analisis ini hanya menggunakan data dari platform Airbnb untuk tahun 2022 terkait listing di Bangkok dan mungkin tidak mencakup semua listing atau aspek terbaru di kota tersebut.
- **Faktor Eksternal**: Beberapa faktor eksternal seperti perubahan musim, cuaca, tanggal tertentu, area wisata, atau peristiwa khusus di Bangkok tidak dipertimbangkan dalam analisis ini.
- **Keterbatasan Data**: Data ulasan atau informasi listing mungkin tidak lengkap atau memiliki bias. Airbnb tidak menyediakan informasi tentang fasilitas dan ulasan mungkin tidak sepenuhnya merepresentasikan pengalaman tamu, seperti rating berbintang.
- **Pembersihan Data**: Setelah pembersihan data, harga rata-rata dan maksimum mengalami perubahan. **Entire home/apt** yang sebelumnya tertinggi kini menjadi tertinggi kedua setelah **Hotel Room**.
- **Hasil Analisis**: Temuan ini mungkin tidak berlaku untuk semua jenis akomodasi atau lokasi di Bangkok di luar sampel yang dianalisis, seperti rumah mewah atau listing dengan harga sangat tinggi.

Batasan-batasan ini harus dipertimbangkan saat menafsirkan hasil analisis dan rekomendasi yang diberikan.


## Hasil Analisis

- **Akomodasi Jangka Pendek**: Sebagian besar tamu di Bangkok lebih memilih menginap dalam jangka pendek. Hal ini menunjukkan pentingnya bagi host untuk menyesuaikan penawaran mereka dengan preferensi ini, misalnya dengan menawarkan diskon atau paket khusus untuk pemesanan jangka pendek.

- **Jenis Akomodasi**: Tamu cenderung memilih untuk menyewa seluruh rumah atau apartemen dibandingkan dengan jenis akomodasi lainnya. Ini menunjukkan bahwa akomodasi yang menawarkan privasi dan kenyamanan lebih tinggi, seperti **Entire home/apt**, memiliki daya tarik yang kuat.

- **Rentang Harga Berdasarkan Jenis Kamar**:
  - **Entire Home/Apt**: Memiliki harga yang mahal, mencerminkan akomodasi yang menawarkan privasi dan fasilitas lengkap. Ideal untuk tamu yang menginginkan pengalaman menginap yang lebih nyaman dan eksklusif. Rentang harga: 990 - 1999.
  - **Shared Room**: Memiliki harga termurah dibandingkan dengan jenis akomodasi lainnya. Ini cocok untuk tamu yang mencari opsi akomodasi yang lebih ekonomis. Rentang harga: 380 - 550.
  - **Private Room**: Memiliki harga yang berada di tengah-tengah. Akomodasi ini menawarkan privasi lebih dibandingkan dengan **Shared Room**, tetapi dengan fasilitas yang lebih terbatas dibandingkan **Entire Home/Apt**. Rentang harga: 750 - 1500.
  - **Hotel Room**: Menunjukkan variasi harga yang lebih luas, dari harga yang terjangkau hingga yang lebih mahal. Ini mencerminkan berbagai tingkat kualitas dan layanan yang tersedia. Rentang harga: 900 - 2222.

- **Korelasi Ulasan dan Harga**: Analisis menunjukkan bahwa jumlah ulasan yang lebih tinggi berkorelasi dengan harga sewa yang lebih tinggi. Ini mungkin disebabkan oleh reputasi dan kepercayaan yang lebih besar terhadap listing dengan ulasan yang banyak.

- **Hubungan Jumlah Listing dan Harga**: Terdapat korelasi positif antara jumlah listing yang dimiliki oleh host dan harga sewa. Host dengan lebih banyak listing dapat menetapkan harga yang lebih tinggi, kemungkinan karena reputasi dan pengalaman yang lebih baik.

- **Pengaruh Lokasi**: Listing yang berada dekat dengan pusat kota cenderung memiliki harga yang lebih tinggi dibandingkan dengan listing di lokasi yang lebih jauh. Ini menunjukkan bahwa lokasi strategis memberikan nilai tambah signifikan terhadap harga sewa.

- **Distribusi Listing Berdasarkan Distrik**:
  - **Distrik Khlong Toei**: Memiliki jumlah listing terbanyak, menunjukkan permintaan tinggi di area ini.
  - **Distrik Vadhana**: Memiliki jumlah host terbanyak, menandakan konsentrasi yang lebih besar dari penyedia akomodasi di area ini.
  - **Distrik Pathum Wan**: Menunjukkan harga rata-rata listing tertinggi, yang menunjukkan bahwa area ini mungkin memiliki daya tarik premium atau lebih banyak fasilitas.

Bagian ini memberikan rincian tentang hasil analisis yang dilakukan, menjelaskan pola-pola dan hubungan yang ditemukan antara berbagai faktor yang mempengaruhi harga sewa di Airbnb Bangkok.


## Kesimpulan

- Mayoritas tamu memilih menginap jangka pendek dan menyewa **Entire home/apt**.
- Semakin banyak ulasan dan listing yang dimiliki host, semakin tinggi harga sewa yang dapat ditetapkan.
- Listing yang dekat dengan pusat kota atau berada di distrik populer cenderung memiliki harga lebih tinggi.

## Rekomendasi

- Tawarkan diskon untuk pemesanan jangka pendek.
- Tingkatkan fasilitas dan kenyamanan **Entire home/apt**.
- Tetapkan harga kompetitif sesuai jenis kamar.
- Dorong tamu untuk meninggalkan ulasan positif.
- Manfaatkan lokasi strategis untuk menetapkan harga lebih tinggi.
- Tambah listing di distrik dengan permintaan tinggi.

Dengan mengikuti rekomendasi ini, host dapat menarik lebih banyak tamu dan memaksimalkan pendapatan dari listing Airbnb mereka.

## Dokumentasi

1. [Jupyter Notebook](https://github.com/fikigayo/Capstone-Project/blob/68e3a67b1624c90493cb7c9eb045036721d5d773/modul%202/Data%20Analisis%20Airbnb%20Listing%20Bangkok.ipynb)
2. [Tableau Story](https://public.tableau.com/app/profile/fiki.putra/viz/CapstoneProjectModul2AirbnbListingBangkok/Story)
3. [Video Penjelasan](https://drive.google.com/file/d/1jB3NNPaLY5MhmAId9cqluiut22nsVrfJ/view?usp=drive_link)

## Rencana Pengembangan Lanjutan

Untuk pengembangan selanjutnya, analisis dapat diperluas dengan menggunakan teknik analisis yang lebih mendalam, seperti machine learning, untuk memprediksi harga sewa dengan lebih akurat.

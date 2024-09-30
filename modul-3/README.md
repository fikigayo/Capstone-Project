# Customer Lifetime Value

## Background

Customer Lifetime Value (CLV) mengukur nilai seorang pelanggan bagi perusahaan, membantu meningkatkan keuntungan dan mengurangi biaya untuk menarik atau mempertahankan pelanggan. Dalam industri asuransi, memahami CLV penting karena mempertahankan pelanggan lebih murah dibandingkan memperoleh yang baru. Dengan model machine learning, perusahaan dapat memprediksi CLV berdasarkan karakteristik pelanggan, meningkatkan efisiensi dan fokus pada pelanggan bernilai.
![image](https://github.com/user-attachments/assets/c07f2a28-1b66-4e55-9f94-4d030908e999)


### Problem Statement
Salah satu tantangan utama perusahaan asuransi adalah memprediksi Customer Lifetime Value (CLV) secara efisien. Penghitungan manual sering lambat dan kurang relevan, mengakibatkan anggaran terbuang pada pelanggan yang tidak menguntungkan. Dengan prediksi CLV berbasis machine learning, perusahaan dapat lebih selektif dalam memilih pelanggan bernilai tinggi, menghemat biaya, dan meningkatkan layanan.
![image](https://github.com/user-attachments/assets/275f1f17-31ce-4779-a0d3-7cdc16304ca4)


---

## Cara Install

### Prasyarat
Sebelum menginstal proyek ini, pastikan kamu memiliki:
- Python 3.x
- Jupyter Notebook

### Langkah Install

1. **Clone repository**:  
   ```bash
   git clone https://github.com/fikigayo/Capstone-Project.git
   cd Capstone-Project/modul-3

2. Buat environment baru (opsional, tapi direkomendasikan):
   ```bash
   python -m venv clv-analysis-env
   ```
   Aktifkan Environment:
   - Linux atau Mac
     ```bash
      source clv-analysis-env/bin/activate
     ```
   - Windows
      ```bash
      clv-analysis-env/Scripts/activate
      ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Instal Jupyter Notebook (jika belum ada):
   ```bash
   pip install notebook

5. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook clv_analysis.ipynb

6. Setelah selesai, non-aktifkan environment
   ```bash
   deactivate


## Cara Menggunakan Pickle
Anda dapat memprediksi CLV menggunakan Pickle dengan mengikuti langkah-langkah berikut:

1. Jalankan Jupyter Notebook dengan perintah berikut:
   ```bash
   jupyter notebook predict_clv_from_pickle.ipynb

2. Setelah notebook terbuka, jalankan program dan masukkan data yang diminta. Program akan memprediksi nilai CLV berdasarkan data yang Anda input.
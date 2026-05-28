# 📊 Olist E-Commerce Dashboard

Dashboard interaktif ini dibuat menggunakan Streamlit untuk menganalisis performa penjualan pada dataset Olist E-Commerce.

---

## Setup Environment - VS Code

### 1. Buka Project di VS Code

- Buka Visual Studio Code
- Pilih **File → Open Folder**
- Buka folder project Aji Hidayat_AIC299B6Y0015_Submission_Analisis Data

---

### 2. Membuka Terminal

Pada VS Code pilih:

```bash
Terminal → New Terminal
```
### 3. Membuat Virtual Environment

```bash
python -m venv venv
```


### 4. Mengaktifkan Virtual Environment

```bash
venv\Scripts\activate
```

### 5. Install Library

Install library 

```bash
pip install pandas
pip install matplotlib
pip install seaborn
pip install plotly
pip install streamlit
```
## Run Streamlit App

### 1. Menjalankan Dashboard

Gunakan perintah berikut untuk menjalankan dashboard:

```bash
streamlit run Dashboard.py
```

Perintah tersebut digunakan untuk menjalankan file `Dashboard.py` menggunakan Streamlit.

---

Dashboard akan berjalan secara lokal pada perangkat pengguna menggunakan Streamlit server.


## Dashboard Features

Dashboard memiliki beberapa fitur interaktif untuk membantu proses analisis data penjualan Olist, yaitu:

### 📅 Filter Rentang Tanggal

Pengguna dapat memilih rentang tanggal tertentu untuk melihat data transaksi berdasarkan periode waktu yang diinginkan.

Filter ini membantu pengguna menganalisis tren penjualan pada waktu tertentu.

---

### 🛍️ Filter Kategori Produk

Pengguna dapat memilih satu atau beberapa kategori produk untuk menampilkan data sesuai kategori yang dipilih.

Contohnya:
- electronics
- furniture
- toys
- fashion

Visualisasi dan KPI akan otomatis berubah mengikuti kategori produk yang dipilih.

---

### 🏙️ Filter Kota Customer

Pengguna dapat memilih kota customer tertentu untuk melihat distribusi transaksi berdasarkan lokasi customer.

Dashboard akan menampilkan data sesuai kota yang dipilih pengguna.

---

### 📈 KPI (Key Performance Indicator)

Dashboard menampilkan beberapa indikator utama, yaitu:

- **Total Orders** → jumlah total transaksi/order
- **Total Revenue** → total pendapatan dari seluruh transaksi
- **Average Product Price** → rata-rata harga produk

KPI akan berubah secara otomatis sesuai filter yang digunakan.

---

### 📊 Top 10 Product Categories by Revenue

Visualisasi bar chart digunakan untuk menampilkan 10 kategori produk dengan revenue tertinggi.

Grafik ini membantu mengetahui kategori produk paling profitable pada platform Olist.

---

### 📉 Monthly Orders Trend

Visualisasi line chart digunakan untuk melihat tren jumlah order setiap bulan.

Grafik ini membantu pengguna memahami kenaikan atau penurunan transaksi dari waktu ke waktu.

---

### 🥧 Customer Distribution by City

Visualisasi pie chart digunakan untuk melihat distribusi customer berdasarkan kota.

Grafik ini membantu mengetahui kota dengan jumlah customer terbanyak.

---

### 📥 Download Filtered Data

Pengguna dapat mengunduh data hasil filter ke dalam format CSV menggunakan tombol download yang tersedia pada dashboard.

---

### 🗂️ Show Raw Data

Dashboard menyediakan fitur untuk menampilkan raw data hasil filter dalam bentuk tabel dataframe.

Fitur ini membantu pengguna melakukan eksplorasi data secara langsung.

---

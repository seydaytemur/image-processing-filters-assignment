# Görüntü İşleme Filtreleri (Image Processing Filters)

Bu proje, çeşitli görüntü işleme filtrelerinin (yumuşatma, kenar belirleme, lineer olmayan işlemler vb.) Python ile temel seviyede uygulanmasını ve test edilmesini içermektedir. Geliştirilen fonksiyonlar `scikit-image` kütüphanesindeki örnek görüntüler (camera, coins, rice vb.) üzerinde test edilmiştir.

## İçerik ve Filtreler

Proje dâhilinde iki temel Python dosyası bulunmaktadır:
1. **`filters_utils.py`**: Filtreleme algoritmalarının fonksiyon olarak tanımlandığı yardımcı modül. Ortak bir dolgu (padding) mekanizması ile birlikte aşağıdaki filtreleri içerir:
   - Ortalama (Mean) Filtresi
   - Gaussian Filtresi
   - Medyan Filtresi (Özellikle Tuz-Biber gürültüsü için)
   - Minimum ve Maksimum Filtreleri
   - K-En Yakın Komşu (K-NN) Filtresi
   - Sobel ve Prewitt Kenar Belirleme Filtreleri
2. **`homework_solution.py`**: Görüntüleri yükleyen, çeşitli gürültüler ekleyen, filtreleri uygulayan ve sonuç grafiklerini `sonuclar` klasörüne çıkaran ana çalıştırılabilir programdır.

## Kurulum ve Çalıştırma

### Gereksinimler
Projenin sorunsuz çalışması için ortamınızda aşağıdaki paketlerin kurulu olduğundan emin olunuz:
- `numpy`
- `scipy`
- `matplotlib`
- `scikit-image`

Gerekli paketleri pip üzerinden şu şekilde kurabilirsiniz:
```bash
pip install numpy scipy matplotlib scikit-image
```

### Projeyi Çalıştırma
Proje dizininde terminali/komut satırını açarak aşağıdaki komutu çalıştırınız:
```bash
python homework_solution.py
```

İşlem tamamlandıktan sonra, filtreleme sonuçlarını (orijinal ile karşılaştırmalı olarak) içeren yüksek çözünürlüklü görseller **`sonuclar`** dizini içerisine kaydedilecektir. Çıktıların Git üzerinden takibi aktiftir, dilerseniz GitHub üzerinden doğrudan görselleri inceleyebilirsiniz.

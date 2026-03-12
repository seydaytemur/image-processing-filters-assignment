import matplotlib.pyplot as plt
from skimage import data, util
import filters_utils as fu
import os

# Sonuçlar klasörünü oluştur
if not os.path.exists('sonuclar'):
    os.makedirs('sonuclar')

def save_and_show(images, titles, filename):
    n = len(images)
    plt.figure(figsize=(n * 4, 6)) # Boyutu artırıldı
    for i in range(n):
        plt.subplot(1, n, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i], fontsize=12, pad=10) # Font boyutu ve boşluk eklendi
        plt.axis('off')
    plt.tight_layout()
    plt.savefig(f'sonuclar/{filename}.png', dpi=100)
    plt.close()

def run_homework():
    print("Filtreleme işlemleri başlatılıyor...")

    # 1. Verileri yükle 
    try:
        original_rice = data.rice()
    except AttributeError:
        original_rice = data.moon() # Rice yoksa moon kullan
        
    original_img = data.camera()
    original_coins = data.coins()

    # --- ÖRNEK 1: Yumuşatma ve Gürültü Azaltma (Rice & Camera) ---
    # Tuz-Biber gürültüsü ekle
    noisy_rice = util.random_noise(original_rice, mode='s&p', amount=0.05)
    
    # Filtreleri uygula
    avg_rice = fu.average_filter(noisy_rice, size=3)
    gauss_rice = fu.gaussian_filter(noisy_rice, sigma=1)
    median_rice = fu.median_filter(noisy_rice, size=3)
    
    save_and_show(
        [original_rice, noisy_rice, avg_rice, gauss_rice, median_rice],
        ["Orijinal", "Gürültülü", "Ortalama (3x3)", "Gaussian", "Medyan (3x3)"],
        "yumusatma_sonuclari"
    )
    print("- Yumuşatma ve gürültü azaltma sonuçları kaydedildi.")

    # --- ÖRNEK 2: Kenar Belirleme (Coins) ---
    sobel_coins = fu.sobel_filter(original_coins)
    prewitt_coins = fu.prewitt_filter(original_coins)
    
    save_and_show(
        [original_coins, sobel_coins, prewitt_coins],
        ["Orijinal", "Sobel Kenar", "Prewitt Kenar"],
        "kenar_belirleme_sonuclari"
    )
    print("- Kenar belirleme sonuçları kaydedildi.")

    # --- ÖRNEK 3: Non-Lineer Operatörler (Min, Max, KNN) ---
    min_img = fu.min_filter(original_img, size=3)
    max_img = fu.max_filter(original_img, size=3)
    knn_img = fu.knn_filter(original_img, size=3, k=5)
    
    save_and_show(
        [original_img, min_img, max_img, knn_img],
        ["Orijinal", "Min Filtresi", "Max Filtresi", "KNN (k=5)"],
        "non_lineer_islem_sonuclari"
    )
    print("- Lineer olmayan işlem sonuçları kaydedildi.")

    print("\nTüm işlemler başarıyla tamamlandı. 'sonuclar' klasörüne göz atabilirsiniz.")

if __name__ == "__main__":
    run_homework()

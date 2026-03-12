import numpy as np
from scipy import ndimage

def apply_padding(image, pad_size, mode='constant', value=0):
    """Görüntüye belirtilen modda dolgu ekler."""
    if mode == 'constant':
        return np.pad(image, pad_size, mode='constant', constant_values=value)
    return np.pad(image, pad_size, mode=mode)

def average_filter(image, size=3):
    """Ortalama (Mean) filtresi uygular."""
    kernel = np.ones((size, size)) / (size * size)
    return ndimage.convolve(image, kernel)

def gaussian_filter(image, sigma=1):
    """Gaussian filtresi uygular."""
    return ndimage.gaussian_filter(image, sigma=sigma)

def sobel_filter(image):
    """Sobel kenar belirleme filtresi uygular."""
    dx = ndimage.sobel(image, axis=0)
    dy = ndimage.sobel(image, axis=1)
    return np.hypot(dx, dy)

def prewitt_filter(image):
    """Prewitt kenar belirleme filtresi uygular."""
    dx = ndimage.prewitt(image, axis=0)
    dy = ndimage.prewitt(image, axis=1)
    return np.hypot(dx, dy)

def median_filter(image, size=3):
    """Medyan filtresi uygular (Tuz-biber gürültüsü için ideal)."""
    return ndimage.median_filter(image, size=size)

def min_filter(image, size=3):
    """Minimum filtresi uygular."""
    return ndimage.minimum_filter(image, size=size)

def max_filter(image, size=3):
    """Maksimum filtresi uygular."""
    return ndimage.maximum_filter(image, size=size)

def knn_filter(image, size=3, k=5):
    """Basitleştirilmiş K-En Yakın Komşu (K-NN) filtresi.
    Merkezi piksele değerce en yakın k komşunun ortalamasını alır.
    """
    pad_val = size // 2
    padded_img = apply_padding(image, pad_val, mode='reflect')
    output = np.zeros_like(image, dtype=float)
    
    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            window = padded_img[i:i+size, j:j+size].flatten()
            center_pixel = window[len(window)//2]
            # Merkeze olan mutlak farkları hesapla
            distances = np.abs(window - center_pixel)
            # En yakın k indeksi bul
            idx = np.argsort(distances)[:k]
            output[i, j] = np.mean(window[idx])
            
    return output

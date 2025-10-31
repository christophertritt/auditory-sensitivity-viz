# Masking analysis module
from typing import List, Dict, Tuple
import numpy as np

class MaskingAnalysis:
    """Analysis functions for masking effects of urban noise on fish hearing"""
    @staticmethod
    def calculate_masking_index(threshold_db: float, urban_noise_db: float) -> float:
        return urban_noise_db - threshold_db

    @staticmethod
    def calculate_masking_percentage(frequencies: np.ndarray, thresholds: np.ndarray, urban_noise_levels: np.ndarray) -> Tuple[float, int, int]:
        masked = urban_noise_levels > thresholds
        n_masked = np.sum(masked)
        n_total = len(frequencies)
        percentage = (n_masked / n_total) * 100
        return percentage, int(n_masked), n_total

    @staticmethod
    def identify_vulnerable_bands(frequencies: np.ndarray, thresholds: np.ndarray, urban_noise_levels: np.ndarray, masking_threshold_db: float = 0) -> List[Dict]:
        masking_index = urban_noise_levels - thresholds
        vulnerable_bands = []
        in_vulnerable_band = False
        band_start = None
        band_masking_indices = []
        for i, (freq, mi) in enumerate(zip(frequencies, masking_index)):
            if mi > masking_threshold_db:
                if not in_vulnerable_band:
                    band_start = freq
                    in_vulnerable_band = True
                band_masking_indices.append(mi)
            else:
                if in_vulnerable_band:
                    band_end = frequencies[i-1] if i > 0 else freq
                    vulnerable_bands.append({
                        'start_freq': float(band_start),
                        'end_freq': float(band_end),
                        'max_masking': float(np.max(band_masking_indices)),
                        'avg_masking': float(np.mean(band_masking_indices))
                    })
                    in_vulnerable_band = False
                    band_masking_indices = []
        if in_vulnerable_band:
            vulnerable_bands.append({
                'start_freq': float(band_start),
                'end_freq': float(frequencies[-1]),
                'max_masking': float(np.max(band_masking_indices)),
                'avg_masking': float(np.mean(band_masking_indices))
            })
        return vulnerable_bands

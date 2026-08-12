# VISTA-Visual Image Smoothing Testing Application
<div align="center">

# 🖼️ VISTA
### Visual Image Smoothing & Testing Application
**K-Nearest Neighbors (KNN) vs Mean Filter Performance**[cite: 1]

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)]()
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)]()
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)]()

*An interactive desktop environment designed for the quantitative evaluation of spatial noise reduction algorithms on grayscale imagery.*[cite: 1]

</div>

---

## 📸 Platform Overview

Standard linear convolution often compromises critical structural details, blurring sharp image edges when attempting to reduce noise. **VISTA** provides an intuitive, side-by-side diagnostic environment to directly compare a standard **Mean (Average) Filter** against an edge-preserving **K-Nearest Neighbors (KNN) Filter**[cite: 1]. Users can load custom images, inject uniform noise distributions, apply both spatial filters simultaneously, and quantitatively evaluate their restoration performance using Mean Squared Error (MSE) metrics[cite: 1].

<div align="center">
  <table>
    <tr>
      <td align="center"><b>💻 Tkinter Interface</b><br><img src="p1.png" width="300" alt="UI Screenshot 1"/></td>
      <td align="center"><b>🌫️ Noise Injection</b><br><img src="p2.png" width="300" alt="Noise Screenshot 2"/></td>
      <td align="center"><b>📊 MSE Comparison</b><br><img src="p3.png" width="300" alt="MSE Screenshot 3"/></td>
    </tr>
  </table>
</div>

---
  
## ✨ Key Features

* **Custom Noise Injection:** Dynamically introduces uniform random noise to the source image based on user-defined minimum and maximum amplitude boundaries[cite: 1].
* **Algorithm Implementation:** Features optimized custom implementations of a spatial Mean Filter (utilizing edge padding) and a KNN Filter (utilizing reflect padding)[cite: 1].
* **Quantitative Metrics:** Calculates the Mean Squared Error (MSE) to mathematically evaluate the fidelity of the reconstructed images against the original baseline[cite: 1]. The MSE is calculated mathematically as:
$$MSE = \frac{1}{n} \sum (Y - \hat{Y})^2$$
* **Interactive GUI:** Built with `tkinter`, granting users real-time control to adjust noise ranges, kernel window sizes, and $K$ parameters dynamically prior to execution[cite: 1].
* **Visual Results:** Leverages `matplotlib` to render a high-contrast 1x4 subplot grid, displaying the Original, Noisy, Average, and KNN-filtered images side-by-side with overlaid diagnostic MSE scores[cite: 1].

---

## 🛠️ Architecture Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend UI** | `tkinter` | Provides the interactive application window, file dialogs, and real-time parameter input fields[cite: 1]. |
| **Matrix Math** | `numpy` | Powers the core array operations, image padding logic, and mathematical filter transformations[cite: 1]. |
| **Image I/O** | `PIL` (Pillow) | Handles the ingestion of image files and converts them into standardized 32-bit float grayscale arrays[cite: 1]. |
| **Visualization** | `matplotlib.pyplot` | Renders the subplot comparison grid and dynamically overlays the statistical MSE text[cite: 1]. |

---

## 📂 Project Structure

```text
VISTA-filter-bench/
│
├── main.py                # Main application script containing UI routing and VISTA filter logic[cite: 1]
├── requirements.txt       # Python environment dependencies (numpy, Pillow, matplotlib)
└── README.md              # Project documentation and theoretical background

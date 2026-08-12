import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_image():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.tif;*.bmp")])
    if not path: return None
    img = np.array(Image.open(path).convert("L"), dtype=np.float32)
    return img

def add_noise(img, low, high):
    return np.clip(img + np.random.uniform(low, high, img.shape), 0, 255)

def mean_filter(img, win):
    pad = win//2
    padded = np.pad(img, pad, 'edge')
    out = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i,j] = np.mean(padded[i:i+win, j:j+win])
    return out

def knn_filter(img, win, k):
    pad = win//2
    padded = np.pad(img, pad, 'reflect')
    out = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            w = padded[i:i+win, j:j+win].flatten()
            c = w[len(w)//2]
            mask = np.argsort(np.abs(w-c))[:k+1]  # include center
            out[i,j] = np.mean(w[mask])
    return out

def mse(a,b): return np.mean((a-b)**2)

def run_process():
    global img
    if img is None:
        messagebox.showerror("Error", "Load an image first!")
        return
    try:
        low, high = float(ent_noise_min.get()), float(ent_noise_max.get())
        win, k = int(ent_win.get()), int(ent_k.get())
    except:
        messagebox.showerror("Error","Invalid parameters!")
        return

    noisy = add_noise(img, low, high)
    avg = mean_filter(noisy, win)
    knn = knn_filter(noisy, win, k)
    m1, m2 = mse(img, avg), mse(img, knn)

    # Update the small UI labels
    mse_avg_label.config(text=f"MSE (Average) = {m1:.2f}")
    mse_knn_label.config(text=f"MSE (KNN)     = {m2:.2f}")

    # Also show them under the corresponding matplotlib subplots
    fig, axs = plt.subplots(1,4,figsize=(12,4))
    titles = ["Original","Noisy","Average","KNN"]
    for a,im,t in zip(axs,[img,noisy,avg,knn],titles):
        a.imshow(im,cmap='gray',vmin=0,vmax=255)
        a.set_title(t)
        a.axis('off')

    # put MSE text under the Average and KNN subplots
    axs[2].text(0.5, -0.12, f"MSE = {m1:.2f}", transform=axs[2].transAxes, ha='center', fontsize=10)
    axs[3].text(0.5, -0.12, f"MSE = {m2:.2f}", transform=axs[3].transAxes, ha='center', fontsize=10)

    fig.tight_layout()
    plt.show()

# ---- GUI ----
root = tk.Tk(); root.title("KNN vs Average Filter")

tk.Button(root, text="Load Image", command=lambda: globals().update(img=load_image())).grid(row=0,column=0, sticky='w', padx=4, pady=4)
tk.Label(root, text="Noise min,max:").grid(row=1,column=0, sticky='w')
ent_noise_min, ent_noise_max = tk.Entry(root,width=6), tk.Entry(root,width=6)
ent_noise_min.insert(0,"-30"); ent_noise_max.insert(0,"30")
ent_noise_min.grid(row=1,column=1); ent_noise_max.grid(row=1,column=2)

tk.Label(root,text="Window:").grid(row=2,column=0, sticky='w')
ent_win=tk.Entry(root,width=6); ent_win.insert(0,"5"); ent_win.grid(row=2,column=1)

tk.Label(root,text="K:").grid(row=2,column=2, sticky='w')
ent_k=tk.Entry(root,width=6); ent_k.insert(0,"8"); ent_k.grid(row=2,column=3)

tk.Button(root,text="Run",command=run_process).grid(row=3,column=0,columnspan=4, pady=(6,4))

# MSE labels placed in the UI (under the Run button)
mse_avg_label = tk.Label(root, text="MSE (Average) = -", anchor='w')
mse_avg_label.grid(row=4, column=0, columnspan=2, sticky='w', padx=4, pady=(2,4))

mse_knn_label = tk.Label(root, text="MSE (KNN)     = -", anchor='w')
mse_knn_label.grid(row=4, column=2, columnspan=2, sticky='w', padx=4, pady=(2,4))

img=None
root.mainloop()

# 🔐 Face Lock & Folder Guard System with Real-Time Facial Authentication

This project is a biometric security system that authenticates users using **facial recognition**, built with **Deep Learning (Siamese Neural Networks)**. It provides:
- Access control to folders
- Real-time system monitoring
- Lockdown on unauthorized usage

The core idea is to apply **One-Shot Learning** using **Siamese Neural Networks**, inspired by the paper [Siamese Neural Networks for One-shot Image Recognition (Koch et al.)](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf).

---

## 📁 Project Features

### ✅ Folder Guard
- Protects specific folders using facial identity verification.
- Triggers a facial authentication check **when the folder is opened**.
- Blocks unauthorized access and can log or shut down access on failure.

### 🔁 Idle Face Lock
- Periodically verifies the active user during idle periods.
- Auto-locks or shuts the system if unauthorized access is detected.

### 🚫 OS Constraints
- Direct face lock integration at **system boot or login** is restricted due to OS-level limitations.
- Folder protection begins **after folder is opened**, as click events don't trigger processes natively at the OS level.

---

## 🧠 Tech Stack

- **Python**
- **OpenCV** (Real-time webcam integration)
- **TensorFlow / Keras** (Siamese Neural Network)
- **NumPy**, **OS**, **Threading**
- **Facial Image Dataset** (Custom or pre-labeled)

---

## 📘 Research Background

The Siamese Neural Network used in this project is based on:

> Koch, G., Zemel, R., & Salakhutdinov, R. (2015). *Siamese Neural Networks for One-shot Image Recognition*. ICML.

### Key Techniques:
- One-shot learning with pairwise image comparisons.
- Distance-based verification (using L1 distance + sigmoid).
- Affine transformations for data augmentation.
- CNN backbone for embedding facial features.

---

## 📊 Use Cases

- 🔒 Secure folders with biometric checks (e.g. confidential data, reports, projects).
- 🛡️ Monitor unauthorized use in shared or public workstations.
- 💻 Protect developer machines and personal vaults.
- 🏫 Perfect for labs, startups, student developers, or home setups.

---

## 🚀 Getting Started

1. Clone the repository.
2. Train your Siamese model or load the pretrained model.
3. Run the authentication service.

```bash
pip install -r requirements.txt
python run_face_guard.py

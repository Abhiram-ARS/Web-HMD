# Web-HMD : Website Hashing for Modification Detection

A Python Flask-based web application that allows users to generate and compare cryptographic hashes of websites to detect content modifications.

## 🛡️ Overview

**Website Hashing for Modification Detection** is a lightweight and practical tool developed to help users detect unauthorized or unexpected changes to web pages. This tool is especially useful for web developers, cybersecurity professionals, and educators who want to ensure the integrity of a website over time.

The application uses **Python (Flask)** for backend processing and a simple **HTML** frontend for user interaction.

---

## 🔍 Features

* ✅ **Website Hash Generator** – Generate SHA-256 hashes of website content.
* 🔁 **Hash Comparator** – Compare two hash values to detect content changes.
* 🌐 **Support for Local & Online Pages** – Works with both hosted websites and local HTML files.
* 🧠 **Simple and Intuitive UI** – Clean frontend with clear input fields and result display.

---

## 📂 Project Structure

```
App/
│
├── Backend/
│   └── API.py         
│   └── Hash.py
│   └── Launcher.py
│   └── Main.py
│   └── WebCommunication.py
│
├── Frontend/
│   └── WebHMD.html 
│
└── RunWebHMD.py                # Main application
└── requirements.txt
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

* Python 3.7+
* Flask

### 🧪 Installation

```bash
git clone https://github.com/Abhiram-ARS/Web-HMD/tree/96a25508f441528e8df1f10ebd6b0442a39b957e/App
pip install -r requirements.txt
```

### ▶️ Running the App

```bash
python RunWebHMD.py
```

---

## 🧰 Example Use Cases

* Detecting **unauthorized changes** on a hosted website.
* Checking for **tampering or defacement** of public-facing pages.
* Monitoring content updates for **compliance or record-keeping**.

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/fd0425b2-b7c8-4e4d-abf4-662855b8ab10)


---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---


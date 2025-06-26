# Immigration Lawyer Access and Transparency Project

**Created by:** Gael Alejandro Fonseca
**Faculty Mentor:** Dr. Doina Bein

---

## 🔍 Project Summary

This social justice data science project focuses on extracting, analyzing, and visualizing the accessibility of pro bono immigration lawyers listed in the Department of Justice's EOIR (Executive Office for Immigration Review) PDF directory.

The goal is to provide public transparency, identify disparities in access by state and organization type, and deliver an interactive tool that helps individuals locate immigration legal aid while highlighting patterns in nonprofit distribution.

---

## 📁 What This Project Includes

* 🧠 **PDF OCR Pipeline** — Extracts lawyer data from the EOIR government PDF using `pdf2image` and `pytesseract`.
* 🧹 **Data Cleaning** — Normalizes names, state codes, and organizations.
* 💾 **MySQL Database** — Stores structured data for analysis and access.
* 📊 **Visualizations** — Created using `matplotlib`, including:

  * Pro bono lawyers per state
  * Organization type distribution
* 🌐 **Flask API + Web Interface** — Enables users to search for lawyers by state.

---

## 🧪 Tools Used

* Python 3.12
* pandas, matplotlib, pytesseract, pdf2image
* MySQL
* Flask (API and webpage rendering)
* Render (for deployment)

---

## 🗂️ Directory Structure

```
LawyerDataScience/
├── api/                  # Flask API and web interface
├── data/                 # EOIR source files and cleaned CSV
├── db/                   # MySQL insert scripts
├── eda/                  # Visualizations and analysis code
├── web/                  # Static charts, HTML templates
├── README.md
└── render.yaml           # Render deployment file
```

---

## 🚀 Try It Out

Visit the live site at: [https://justice-lens.onrender.com](https://justice-lens.onrender.com) *(replace with actual URL)*

Features:

* Search for lawyers by 2-letter state code
* See charts showing gaps and distribution

---

## 📈 Key Findings

* Some states (like CA, NY) have dozens of pro bono lawyers, while others have <5.
* Majority of orgs are categorized as Legal Aid, Clinics, or Centers.
* "Other" orgs were excluded to emphasize transparency in recognizable org types.

---

## ✊ Social Justice Impact

* Improves public access to legal aid for immigrants
* Identifies underserved states for future funding or support
* Helps reduce information asymmetry and legal vulnerability

---

## 🧠 Lessons Learned

* OCR on government PDFs is inconsistent — cleaning is crucial.
* Tailwind/React stack caused setup delays; Flask and HTML worked more reliably.
* Flask + visual storytelling is a powerful combo for fast, mission-driven projects.

---

## 📬 Contact

Gael Alejandro Fonseca
\[Add GitHub or email link here]

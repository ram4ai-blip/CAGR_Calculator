# CAGR_Calculator
A simple CAGR calculator with Streamlit
# 📈 CAGR Calculator

A simple, interactive **Compound Annual Growth Rate (CAGR) Calculator** built with Python and Streamlit.

---

## What It Does

Enter a beginning value, ending value, and number of years — the app instantly calculates:

- **CAGR** — the annualized rate of return
- **Total Growth %** — overall percentage gain
- **Absolute Gain** — profit in ₹
- **Interactive Chart** — portfolio growth curve over time
- **Year-by-year Breakdown** — value, annual gain, and growth % for each year

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI |
| Plotly | Interactive chart |
| Pandas | Data table |

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/cagr-calculator.git
cd cagr-calculator
```

**2. Install dependencies**
```bash
pip install streamlit plotly pandas
```

**3. Run the app**
```bash
python -m streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## Formula

$$CAGR = \left(\frac{\text{Ending Value}}{\text{Beginning Value}}\right)^{\frac{1}{n}} - 1$$

Where **n** is the number of years.

---

## Screenshot

<img width="695" height="853" alt="image" src="https://github.com/user-attachments/assets/f67ba76a-f79d-4e38-b6f4-6be562c11737" />

<img width="651" height="315" alt="image" src="https://github.com/user-attachments/assets/ab31a7ec-7ee3-446d-82ce-8f3366a4ea44" />



---

## License

MIT License — free to use and modify.

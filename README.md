# 📊 Excel Data Insights Dashboard

An interactive **Streamlit** dashboard for analyzing and visualizing Excel-based sales data. Simply upload your `.xlsx` file to explore key business insights through charts and summaries.

## 🚀 Features

- Upload and preview Excel data
- Summary statistics and missing value analysis
- Correlation matrix heatmap
- Interactive charts:
  - Sales by Region (Bar Chart)
  - Top 10 Products by Sales (Horizontal Bar)
  - Order Priority Distribution (Pie Chart)
  - Profit by Category & Sub-Category (Bar Chart)

## 🧠 Technologies Used

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/)

## 📦 Installation

```bash
git clone https://github.com/yourusername/excel-insights-dashboard.git
cd excel-insights-dashboard
pip install -r requirements.txt
````

Or manually install the dependencies:

```bash
pip install streamlit pandas plotly seaborn matplotlib openpyxl
```

## ▶️ How to Run

```bash
streamlit run app.py
```

Then open the app in your browser and upload your Excel file (`.xlsx`).

## 📁 Example

Upload an Excel file with columns like:

* Order Date
* Sales
* Profit
* Region
* Product Category
* Order Priority

## 📌 Screenshots

> *Add screenshots here if desired for better presentation.*

## 📝 License

MIT License. Feel free to use and modify.

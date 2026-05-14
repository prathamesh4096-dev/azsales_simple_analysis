# Amazon Sales Report Analysis

## Overview
This project performs data cleaning and exploratory data analysis (EDA) on an Amazon sales dataset using Python, Pandas, and Matplotlib.

The script:
- Loads and inspects the dataset
- Cleans and standardizes the data
- Removes unnecessary columns and invalid records
- Corrects inconsistent state names
- Generates visualizations for:
  - Sales per state
  - Quantity sold by category

---

## Technologies Used

- Python 3
- Pandas
- Matplotlib

---

## Project Structure

```text
.
├── amazon_sales_report.csv
├── Amazon_Sales_Report_Cleaned.csv
├── amazon_sales_analysis.py
└── README.md
```

---

## Features

### Data Cleaning
- Removes unnecessary columns
- Trims whitespace from column names
- Removes duplicate rows
- Removes rows with missing values
- Standardizes:
  - State names
  - Category names

### Data Transformation
- Corrects inconsistent state names using mapping replacements
- Converts category and state names to uppercase

### Data Visualization
- Bar chart:
  - Total sales by state
- Pie chart:
  - Quantity sold by category

---

## Dataset

The dataset used is:

```text
amazon_sales_report.csv
```

Expected columns include:

- `ship-state`
- `Category`
- `Amount`
- `Qty`

Additional unused columns are removed during preprocessing.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/amazon-sales-analysis.git
cd amazon-sales-analysis
```

Install required libraries:

```bash
pip install pandas matplotlib
```

---

## Running the Script

Run the Python file:

```bash
python amazon_sales_analysis.py
```

The script will:
1. Load the dataset
2. Clean the data
3. Save a cleaned CSV file
4. Display visualizations

---

## Data Cleaning Details

### Removed Columns

```python
[
    'Unnamed: 22',
    'Style',
    'SKU',
    'ASIN',
    'ship-postal-code',
    'fulfilled-by',
    'ship-country',
    'currency',
    'index',
    'promotion-ids',
    'ship-city'
]
```

### State Name Corrections

| Incorrect Value | Corrected Value |
|---|---|
| RAJSHTHAN | RAJASTHAN |
| ORISSA | ODISHA |
| NEW DELHI | DELHI |
| PB | PUNJAB |
| AR | ARUNACHAL PRADESH |

---

## Visualizations

### Sales by State
Displays total sales amount grouped by shipping state using a bar chart.

### Quantity by Category
Displays product quantity distribution across categories using a pie chart.

---

## Sample Outputs

### Cleaned Dataset
```text
Amazon_Sales_Report_Cleaned.csv
```

### Charts
- Bar Chart: Sales per State
- Pie Chart: Quantity by Category

---

## Future Improvements

Possible enhancements:
- Add monthly sales trend analysis
- Use Seaborn or Plotly for advanced visualizations
- Add dashboard support using Streamlit
- Perform customer segmentation analysis
- Add sales forecasting models

---

## Author

**Prathamesh**

---

## License

This project is open-source and available under the MIT License.

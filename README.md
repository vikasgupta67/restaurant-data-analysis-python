# 🍽️ Restaurant Data Analysis | Python EDA & Marketing Insights

![Python](https://img.shields.io/badge/Python-Pandas-blue)
![Dataset](https://img.shields.io/badge/Data-9551%20Restaurants-green)

## 📌 Business Problem
Build an intelligent B2C recommendation portal. Before building it, understand:
Which cities have most restaurants? Do customers prefer online delivery? Which cuisines are most popular?

## 📊 Dataset
- `data.xlsx` - 9551 rows, 19 columns (Restaurant, City, Cuisines, Cost, Rating, Votes, etc.)
- `Country-Code.xlsx` - 15 rows, 2 columns
- After merge: 9551 rows, 20 columns

## 🛠️ Tools Used
Python, Pandas, NumPy, Matplotlib, Seaborn, Tableau (planned)

## 🔍 EDA Process
1.  Loaded & merged datasets on Country Code (Left Join)
2.  Checked info, describe, missing values, duplicates
3.  Geographical, Franchise, Booking, Delivery & Cuisine analysis

## 🔑 Key Findings
1.  **Geography:** New Delhi dominates with 5,473 restaurants (57%), followed by Gurgaon 1,118 & Noida 1,080. Recommendation system will be biased to Delhi - need balancing.
2.  **Franchise:** Barbeque Nation present in 22 cities (highest), Pizza Hut 12, KFC 8 - Strong national presence.
3.  **Table Booking:** Only 1,158 (12.1%) restaurants allow table booking. Huge gap - 87.9% market untapped.
4.  **Online Delivery:** Only 25.66% offer delivery. 74% restaurants losing online customers.
5.  **Votes:** Non-delivery restaurants got 980,731 votes vs Delivery 517,914 - Delivery alone does not guarantee engagement.
6.  **Cuisines:** North Indian, Chinese, Fast Food are top. Max 8 cuisines per restaurant, Min 1.

## 💡 Business Recommendations
- Focus onboarding on Non-Delivery restaurants in Delhi/NCR - biggest opportunity.
- Promote Table Booking feature to 87% restaurants - new revenue stream.
- For Recommendation Portal: Standardize cuisine names (strip spaces) before model training.

## 📁 Files
- `restaurant_analysis.py` - Complete Python code
- `requirements.txt` - Libraries needed
- `Marketing_project_writeup.pdf` - Detailed 8-page report


## 🚀 How to Run
`bash`
- `pip install -r requirements.txt`
- `python restaurant_analysis.py`

## 👤 Author
Vikas Gupta | BBA @ IGNOU | Data Analytics @ Simplilearn
Skills: SQL, Python, Excel, Power BI, Tableau
Seeking: Remote Data Analyst Intern

# 🛍️ Product Recommendation System

A Python and Pandas based product recommendation system that recommends products based on category, budget, rating, reviews, and price.

## ✨ Features

- Select from different product categories
- View the available price range
- Filter products according to budget
- Recommend the highest-rated product
- Recommend the product with the most reviews
- Recommend the lowest-priced product
- Handle invalid numeric inputs
- Choose another category or exit

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Pandas | Data handling and filtering |
| CSV | Product dataset |


## ⚙️ How It Works

1. Select a product category.
2. Enter your budget.
3. Choose a recommendation method.
4. Get a recommended product based on your choice.

## 🚀 Getting Started

**Requirements:** Python 3.x, pandas

```bash
pip install pandas
```

Ensure `products.csv` is in the same folder as the script, then run:


```bash
python "Product Recommendation System.py"
```

## 🕹️ Sample Usage 

```
Available Categories
1 Books
2 Electronics
3 Stationery

Enter your choice: 2
Price range: ₹699 - ₹2999
Enter your budget: ₹2000

---Product Recommender---
How would you like to choose your product?
1. Highest Rating
2. Most reviews
3. Lowest price
4. Exit

Enter your choice: 1

Your Best Seller Recommendation
Product:  Wireless Headphones
Price: ₹ 1999
Rating: ★ 4.6
Reviews:  2300
Budget: ₹ 2000
```

## 📁 Project Structure

```text
Product Recommendation System/
├── Product Recommendation System.py
├── products.csv
└── README.md
```

## 📋 Dataset Format

`products.csv` should include these columns:

| column   | description          |
|----------|------------------------|
| category | product category        |
| name     | product name              |
| price    | price in ₹                |
| rating   | average rating              |
| reviews  | number of reviews            |

🔮 Future Improvements
Add a larger dataset
Add more recommendation criteria
Add a graphical user interface
Explore more advanced recommendation techniques
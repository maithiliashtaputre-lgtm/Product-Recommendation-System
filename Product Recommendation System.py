# Load product dataset
import pandas as pd
data = pd.read_csv("products.csv")

# Category selection
while True:
    categories = data["category"].unique()
    print("Available Categories")
    for number, category in enumerate(categories, start= 1):
        print(number, category)

# Filter products based on category and budget of the user
    while True:
        try: 
            category_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number: ")
            continue

        if category_choice < 1 or category_choice > len(categories):
            print("Invalid choice. Please select again.")
        else:
            selected_category = categories[category_choice - 1]
            category_data = data[data["category"]== selected_category]
            min_price = category_data["price"].min()
            max_price = category_data["price"].max()
            print("Price range: ₹", min_price, "- ₹", max_price)
            budget = int(input("Enter your budget: ₹"))
            break


    filtered_data = data[(data["price"]<=budget)&(data["category"]==selected_category)]

    if filtered_data.empty:
        print("There is no item available within this budget")

# Product Recommendation menu
    else:
        while True:
            print("\n---Product Recommender---")
            print("How would you like to choose your product?")
            print("1. Highest Rating")
            print("2. Most reviews")
            print("3. Lowest price")
            print("4. Exit")

            recommendation_choice = int(input("Enter your choice: "))

            if recommendation_choice == 1:
                sorted_data = filtered_data.sort_values("rating", ascending = False)

            elif recommendation_choice == 2:
                sorted_data = filtered_data.sort_values("reviews", ascending = False)

            elif recommendation_choice == 3:
                sorted_data = filtered_data.sort_values("price", ascending = True)

            elif recommendation_choice == 4:
                break
            if recommendation_choice in (1, 2, 3):
                best_product = sorted_data.head(1).iloc[0]
                print("Your Best Seller Recommendation")
                print("Product: ", best_product["name"])
                print("Price: ₹", best_product["price"])
                print("Rating: ★", best_product["rating"])
                print("Reviews: ", best_product["reviews"])
                print("Budget: ₹", budget)

            elif recommendation_choice != 4:
                print("Invalid choice")
               
# Continue or exit
        print("Would you like to continue?")
        print("1. Choose another category")
        print("2. Exit")

        continuation_choice = int(input("Enter your choice: "))
        if continuation_choice == 2:
            print("Thank you! Please Visit Again!")
            break
        elif continuation_choice != 1:
            print("Invalid choice")


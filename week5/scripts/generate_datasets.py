import os
import random
import datetime
import pandas as pd
import numpy as np

def create_superstore_data():
    random.seed(42)
    np.random.seed(42)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)

    regions_data = [
        {"RegionID": "REG-01", "RegionName": "East", "RegionalManager": "Sarah Jenkins", "TerritoryCode": "US-E"},
        {"RegionID": "REG-02", "RegionName": "West", "RegionalManager": "Marcus Vance", "TerritoryCode": "US-W"},
        {"RegionID": "REG-03", "RegionName": "Central", "RegionalManager": "Elena Rostova", "TerritoryCode": "US-C"},
        {"RegionID": "REG-04", "RegionName": "South", "RegionalManager": "David Kim", "TerritoryCode": "US-S"}
    ]
    dim_region = pd.DataFrame(regions_data)

    customers = []
    segments = ["Consumer", "Corporate", "Home Office"]
    segment_weights = [0.52, 0.30, 0.18]
    cities_by_region = {
        "East": [("New York", "New York", "10001"), ("Philadelphia", "Pennsylvania", "19104"), ("Boston", "Massachusetts", "02108")],
        "West": [("Los Angeles", "California", "90001"), ("Seattle", "Washington", "98101"), ("San Francisco", "California", "94102")],
        "Central": [("Chicago", "Illinois", "60601"), ("Dallas", "Texas", "75201"), ("Detroit", "Michigan", "48201")],
        "South": [("Atlanta", "Georgia", "30301"), ("Miami", "Florida", "33101"), ("Charlotte", "North Carolina", "28202")]
    }

    first_names = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]

    for i in range(1, 201):
        cust_id = f"CUST-{1000 + i}"
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        segment = random.choices(segments, weights=segment_weights)[0]
        region_record = random.choice(regions_data)
        city_info = random.choice(cities_by_region[region_record["RegionName"]])
        customers.append({
            "CustomerID": cust_id,
            "CustomerName": name,
            "Segment": segment,
            "Country": "United States",
            "City": city_info[0],
            "State": city_info[1],
            "PostalCode": city_info[2]
        })
    dim_customer = pd.DataFrame(customers)

    products_data = [
        ("PROD-TEC-001", "Apple MacBook Pro 16", "Technology", "Laptops", 1800.0, 2499.0),
        ("PROD-TEC-002", "Dell XPS 15 Laptop", "Technology", "Laptops", 1350.0, 1899.0),
        ("PROD-TEC-003", "HP Spectre x360", "Technology", "Laptops", 1000.0, 1399.0),
        ("PROD-TEC-004", "iPhone 15 Pro Max", "Technology", "Phones", 850.0, 1199.0),
        ("PROD-TEC-005", "Samsung Galaxy S24 Ultra", "Technology", "Phones", 820.0, 1149.0),
        ("PROD-TEC-006", "Sony WH-1000XM5 Headphones", "Technology", "Accessories", 220.0, 399.0),
        ("PROD-TEC-007", "Logitech MX Master 3S Mouse", "Technology", "Accessories", 55.0, 99.0),
        ("PROD-TEC-008", "LG UltraFine 27-inch 4K Monitor", "Technology", "Accessories", 380.0, 599.0),
        ("PROD-TEC-009", "Cisco Business PoE Switch", "Technology", "Networking", 310.0, 480.0),
        ("PROD-FUR-001", "Herman Miller Aeron Chair", "Furniture", "Chairs", 780.0, 1250.0),
        ("PROD-FUR-002", "Steelcase Gesture Ergonomic Chair", "Furniture", "Chairs", 720.0, 1120.0),
        ("PROD-FUR-003", "Solid Oak Executive Conference Table", "Furniture", "Tables", 950.0, 1450.0),
        ("PROD-FUR-004", "Motorized Adjustable Standing Desk", "Furniture", "Tables", 420.0, 680.0),
        ("PROD-FUR-005", "4-Tier Modular Wood Bookcase", "Furniture", "Bookcases", 180.0, 310.0),
        ("PROD-FUR-006", "Commercial Steel 3-Drawer Filing Cabinet", "Furniture", "Furnishings", 130.0, 220.0),
        ("PROD-FUR-007", "LED Dimmable Modern Desk Lamp", "Furniture", "Furnishings", 35.0, 75.0),
        ("PROD-OFF-001", "Multi-Purpose Copy Paper 20lb (Case)", "Office Supplies", "Paper", 24.0, 48.0),
        ("PROD-OFF-002", "Heavy-Duty View 3-Ring Binders (12pk)", "Office Supplies", "Binders", 18.0, 36.0),
        ("PROD-OFF-003", "Pilot G2 Gel Roller Pens (Pack of 24)", "Office Supplies", "Pens", 14.0, 28.0),
        ("PROD-OFF-004", "Fellowes Powershred Cross-Cut Shredder", "Office Supplies", "Appliances", 110.0, 195.0),
        ("PROD-OFF-005", "Scotch Heavy Duty Packaging Tape (6pk)", "Office Supplies", "Storage", 16.0, 32.0),
        ("PROD-OFF-006", "Neenah Classic Crest Linen Envelopes (500pk)", "Office Supplies", "Envelopes", 22.0, 45.0),
        ("PROD-OFF-007", "Avery Self-Adhesive Shipping Labels (1000pk)", "Office Supplies", "Labels", 12.0, 26.0),
        ("PROD-OFF-008", "Quartet Magnetic Glass Dry-Erase Board", "Office Supplies", "Art", 95.0, 175.0)
    ]
    dim_product = pd.DataFrame(products_data, columns=["ProductID", "ProductName", "Category", "SubCategory", "UnitCost", "UnitPrice"])

    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append({
            "Date": current_date.strftime("%Y-%m-%d"),
            "Year": current_date.year,
            "Quarter": f"Q{(current_date.month - 1) // 3 + 1}",
            "MonthNumber": current_date.month,
            "MonthName": current_date.strftime("%B"),
            "MonthYear": current_date.strftime("%b %Y"),
            "Day": current_date.day,
            "Weekday": current_date.strftime("%A"),
            "IsWeekend": "Yes" if current_date.weekday() >= 5 else "No"
        })
        current_date += datetime.timedelta(days=1)
    dim_date = pd.DataFrame(date_list)

    transactions = []
    total_days = (end_date - start_date).days
    order_id_counter = 1001

    discount_options = [0.0, 0.05, 0.10, 0.15, 0.20]
    discount_weights = [0.55, 0.20, 0.12, 0.08, 0.05]

    for order_seq in range(1, 3501):
        order_day_offset = int(np.random.beta(2, 1.5) * total_days)
        order_dt = start_date + datetime.timedelta(days=min(order_day_offset, total_days))
        ship_delay = random.choices([1, 2, 3, 4, 5, 6, 7], weights=[0.10, 0.35, 0.25, 0.15, 0.08, 0.05, 0.02])[0]
        ship_dt = order_dt + datetime.timedelta(days=ship_delay)

        order_id = f"ORD-{order_dt.year}-{order_id_counter}"
        order_id_counter += 1

        customer_row = dim_customer.sample(1).iloc[0]
        region_row = dim_region.sample(1).iloc[0]

        items_in_order = random.choices([1, 2, 3, 4], weights=[0.60, 0.25, 0.10, 0.05])[0]
        chosen_products = dim_product.sample(items_in_order)

        for _, prod in chosen_products.iterrows():
            quantity = random.choices([1, 2, 3, 4, 5, 6, 8, 10], weights=[0.40, 0.25, 0.15, 0.08, 0.05, 0.03, 0.02, 0.02])[0]
            discount = random.choices(discount_options, weights=discount_weights)[0]
            
            gross_amount = round(prod["UnitPrice"] * quantity, 2)
            sales = round(gross_amount * (1.0 - discount), 2)
            cost = round(prod["UnitCost"] * quantity, 2)
            profit = round(sales - cost, 2)

            transactions.append({
                "OrderID": order_id,
                "OrderDate": order_dt.strftime("%Y-%m-%d"),
                "ShipDate": ship_dt.strftime("%Y-%m-%d"),
                "CustomerID": customer_row["CustomerID"],
                "ProductID": prod["ProductID"],
                "RegionID": region_row["RegionID"],
                "Sales": sales,
                "Cost": cost,
                "Profit": profit,
                "Quantity": quantity,
                "Discount": discount
            })

    fact_sales = pd.DataFrame(transactions)

    raw_records = []
    for idx, row in fact_sales.iterrows():
        cust = dim_customer.loc[dim_customer["CustomerID"] == row["CustomerID"]].iloc[0]
        prod = dim_product.loc[dim_product["ProductID"] == row["ProductID"]].iloc[0]
        reg = dim_region.loc[dim_region["RegionID"] == row["RegionID"]].iloc[0]

        date_val = row["OrderDate"]
        if idx % 17 == 0:
            dt_obj = datetime.datetime.strptime(date_val, "%Y-%m-%d")
            date_val = dt_obj.strftime("%d/%m/%Y")
        elif idx % 29 == 0:
            dt_obj = datetime.datetime.strptime(date_val, "%Y-%m-%d")
            date_val = dt_obj.strftime("%Y/%m/%d")

        seg = cust["Segment"]
        if idx % 23 == 0:
            seg = seg.lower()
        elif idx % 47 == 0:
            seg = f"  {seg}  "

        cat = prod["Category"]
        if idx % 31 == 0:
            cat = f" {cat} "

        postal = cust["PostalCode"]
        if idx % 41 == 0:
            postal = None

        raw_records.append({
            "order_id_num": row["OrderID"],
            "Order_Date": date_val,
            "Ship_Date": row["ShipDate"],
            "Customer_ID": row["CustomerID"],
            "Customer_Name": cust["CustomerName"],
            "Customer_Segment": seg,
            "Postal_Code": postal,
            "City": cust["City"],
            "State": cust["State"],
            "Region_ID": reg["RegionID"],
            "Region_Name": reg["RegionName"],
            "Product_ID": prod["ProductID"],
            "Product_Name": prod["ProductName"],
            "Product_Category": cat,
            "Sub_Category": prod["SubCategory"],
            "Sales_Amount": row["Sales"],
            "Unit_Cost": row["Cost"],
            "Net_Profit": row["Profit"],
            "Item_Quantity": row["Quantity"],
            "Discount_Rate": row["Discount"],
            "Internal_Audit_Code": f"AUD-{random.randint(10000, 99999)}",
            "Temp_System_Flag": "ACTIVE"
        })

    raw_df = pd.DataFrame(raw_records)
    duplicates = raw_df.sample(25, random_state=42)
    raw_df_with_dups = pd.concat([raw_df, duplicates], ignore_index=True)

    fact_sales.to_csv(os.path.join(data_dir, "FactSales.csv"), index=False)
    dim_customer.to_csv(os.path.join(data_dir, "DimCustomer.csv"), index=False)
    dim_product.to_csv(os.path.join(data_dir, "DimProduct.csv"), index=False)
    dim_region.to_csv(os.path.join(data_dir, "DimRegion.csv"), index=False)
    dim_date.to_csv(os.path.join(data_dir, "DimDate.csv"), index=False)
    raw_df_with_dups.to_csv(os.path.join(data_dir, "raw_superstore_data.csv"), index=False)

    excel_path = os.path.join(data_dir, "Superstore_Retail_MultiTable.xlsx")
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        fact_sales.to_excel(writer, sheet_name="FactSales", index=False)
        dim_customer.to_excel(writer, sheet_name="DimCustomer", index=False)
        dim_product.to_excel(writer, sheet_name="DimProduct", index=False)
        dim_region.to_excel(writer, sheet_name="DimRegion", index=False)
        dim_date.to_excel(writer, sheet_name="DimDate", index=False)

    print(f"Datasets generated successfully:")
    print(f"FactSales: {len(fact_sales)} rows")
    print(f"DimCustomer: {len(dim_customer)} rows")
    print(f"DimProduct: {len(dim_product)} rows")
    print(f"DimRegion: {len(dim_region)} rows")
    print(f"DimDate: {len(dim_date)} rows")
    print(f"raw_superstore_data: {len(raw_df_with_dups)} rows")

if __name__ == "__main__":
    create_superstore_data()

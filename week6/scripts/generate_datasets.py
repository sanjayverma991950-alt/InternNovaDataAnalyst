import os
import random
import datetime
import pandas as pd
import numpy as np

def build_capstone_dataset():
    random.seed(101)
    np.random.seed(101)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    channels_data = [
        {"ChannelID": "CH-01", "ChannelName": "Organic Search", "CampaignType": "SEO & Inbound", "AverageCAC": 12.50},
        {"ChannelID": "CH-02", "ChannelName": "Paid Search", "CampaignType": "Google Ads / SEM", "AverageCAC": 48.00},
        {"ChannelID": "CH-03", "ChannelName": "Social Media", "CampaignType": "Meta / TikTok", "AverageCAC": 32.00},
        {"ChannelID": "CH-04", "ChannelName": "Email Newsletter", "CampaignType": "Retention Marketing", "AverageCAC": 8.00},
        {"ChannelID": "CH-05", "ChannelName": "Affiliate Referral", "CampaignType": "Partner Network", "AverageCAC": 24.00}
    ]
    dim_channel = pd.DataFrame(channels_data)

    categories_spec = [
        ("PROD-101", "Ultra Wireless ANC Headphones", "Electronics", "Audio", 65.0, 149.0),
        ("PROD-102", "Smart Fitness Tracker 4K", "Electronics", "Wearables", 42.0, 99.0),
        ("PROD-103", "Mechanical Gaming Keyboard RGB", "Electronics", "Accessories", 38.0, 89.0),
        ("PROD-104", "Pro Studio Condenser Mic", "Electronics", "Audio", 55.0, 129.0),
        ("PROD-105", "USB-C Multi-Port Hub Pro", "Electronics", "Accessories", 18.0, 49.0),
        ("PROD-201", "Ergonomic Lumbar Office Chair", "Furniture", "Seating", 110.0, 249.0),
        ("PROD-202", "Motorized Dual-Motor Standing Desk", "Furniture", "Desks", 220.0, 489.0),
        ("PROD-203", "Solid Bamboo Desk Riser", "Furniture", "Accessories", 24.0, 65.0),
        ("PROD-204", "Acoustic Noise-Dampening Panel 6pk", "Furniture", "Decor", 30.0, 79.0),
        ("PROD-301", "Performance Thermal Travel Mug", "Lifestyle", "Drinkware", 12.0, 34.0),
        ("PROD-302", "Water-Resistant Commuter Backpack", "Lifestyle", "Bags", 28.0, 79.0),
        ("PROD-303", "Compact Desk Air Purifier HEPA", "Lifestyle", "Appliances", 36.0, 95.0),
        ("PROD-304", "UV-C Sanitizing Desk Organizer", "Lifestyle", "Appliances", 20.0, 55.0),
        ("PROD-401", "Recycled Hardcover Notebook 3pk", "Supplies", "Stationery", 6.0, 18.0),
        ("PROD-402", "Heavy-Duty Cable Sleeve Kit", "Supplies", "Organization", 8.0, 22.0),
        ("PROD-403", "Precision Aluminum Stylus Pen", "Supplies", "Accessories", 11.0, 29.0)
    ]
    dim_product = pd.DataFrame(categories_spec, columns=["ProductID", "ProductName", "Category", "SubCategory", "UnitCost", "UnitPrice"])

    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Sam", "Chris", "Pat", "Riley", "Casey", "Jesse", "Cameron", "Dakota", "Reese", "Skyler", "Rowan", "Avery", "Logan", "Peyton", "Finley", "Hayden"]
    last_names = ["Bennett", "Foster", "Hayes", "Sullivan", "Powell", "Jenkins", "Perry", "Russell", "Coleman", "Simmons", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Bryant", "Alexander", "Griffin", "Diaz"]

    cities = [
        ("New York", "NY", "East"), ("Los Angeles", "CA", "West"), ("Chicago", "IL", "Central"),
        ("Houston", "TX", "South"), ("Phoenix", "AZ", "West"), ("Philadelphia", "PA", "East"),
        ("Seattle", "WA", "West"), ("Miami", "FL", "South"), ("Denver", "CO", "Central"), ("Atlanta", "GA", "South")
    ]

    segments = ["Champions", "Loyal Customers", "Potential Loyalists", "At Risk", "Hibernating"]
    segment_weights = [0.18, 0.32, 0.25, 0.15, 0.10]
    tiers = ["Platinum", "Gold", "Silver", "Standard"]
    tier_weights = [0.12, 0.28, 0.35, 0.25]

    customers = []
    for c_idx in range(1, 351):
        cid = f"CUST-{2000 + c_idx}"
        cname = f"{random.choice(first_names)} {random.choice(last_names)}"
        city_info = random.choice(cities)
        seg = random.choices(segments, weights=segment_weights)[0]
        tier = random.choices(tiers, weights=tier_weights)[0]
        acq_offset = random.randint(10, 700)
        acq_date = datetime.date(2023, 1, 1) - datetime.timedelta(days=acq_offset)
        customers.append({
            "CustomerID": cid,
            "CustomerName": cname,
            "Segment": seg,
            "LoyaltyTier": tier,
            "City": city_info[0],
            "State": city_info[1],
            "Region": city_info[2],
            "AcquisitionDate": acq_date.strftime("%Y-%m-%d")
        })
    dim_customer = pd.DataFrame(customers)

    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    date_records = []
    curr = start_date
    while curr <= end_date:
        date_records.append({
            "Date": curr.strftime("%Y-%m-%d"),
            "Year": curr.year,
            "Quarter": f"Q{(curr.month - 1) // 3 + 1}",
            "MonthNumber": curr.month,
            "MonthName": curr.strftime("%B"),
            "MonthYear": curr.strftime("%b %Y"),
            "Weekday": curr.strftime("%A"),
            "IsWeekend": "Yes" if curr.weekday() >= 5 else "No"
        })
        curr += datetime.timedelta(days=1)
    dim_date = pd.DataFrame(date_records)

    payment_methods = ["Credit Card", "PayPal", "Debit Card", "Apple Pay", "Buy Now Pay Later"]
    pay_weights = [0.44, 0.26, 0.14, 0.10, 0.06]

    total_span_days = (end_date - start_date).days
    transactions = []
    raw_rows = []

    tx_counter = 10001
    for order_i in range(1, 4501):
        day_shift = int(np.random.beta(1.8, 1.4) * total_span_days)
        tx_date = start_date + datetime.timedelta(days=min(day_shift, total_span_days))
        
        cust = dim_customer.sample(1).iloc[0]
        chan = dim_channel.sample(1).iloc[0]
        pay_m = random.choices(payment_methods, weights=pay_weights)[0]

        basket_count = random.choices([1, 2, 3], weights=[0.68, 0.24, 0.08])[0]
        basket_products = dim_product.sample(basket_count)

        for _, prod in basket_products.iterrows():
            tx_id = f"TXN-{tx_date.year}-{tx_counter}"
            tx_counter += 1

            qty = random.choices([1, 2, 3, 4, 5], weights=[0.55, 0.25, 0.12, 0.05, 0.03])[0]
            disc_rate = random.choices([0.0, 0.05, 0.10, 0.15, 0.25], weights=[0.48, 0.24, 0.16, 0.08, 0.04])[0]

            gross = round(prod["UnitPrice"] * qty, 2)
            discount_val = round(gross * disc_rate, 2)
            net = round(gross - discount_val, 2)
            tax_val = round(net * 0.07, 2)
            final_sales = round(net + tax_val, 2)
            cost_val = round(prod["UnitCost"] * qty, 2)
            profit_val = round(net - cost_val, 2)

            deliv_days = random.choices([1, 2, 3, 4, 5, 7, 9], weights=[0.15, 0.38, 0.24, 0.12, 0.06, 0.03, 0.02])[0]
            is_returned = random.choices(["No", "Yes"], weights=[0.94, 0.06])[0]

            transactions.append({
                "TransactionID": tx_id,
                "OrderDate": tx_date.strftime("%Y-%m-%d"),
                "CustomerID": cust["CustomerID"],
                "ProductID": prod["ProductID"],
                "ChannelID": chan["ChannelID"],
                "SalesAmount": final_sales,
                "CostAmount": cost_val,
                "ProfitAmount": profit_val,
                "DiscountAmount": discount_val,
                "TaxAmount": tax_val,
                "Quantity": qty,
                "PaymentMethod": pay_m,
                "DeliveryDays": deliv_days,
                "ReturnStatus": is_returned
            })

            raw_date = tx_date.strftime("%Y-%m-%d")
            if order_i % 19 == 0:
                raw_date = tx_date.strftime("%d/%m/%Y")
            elif order_i % 31 == 0:
                raw_date = tx_date.strftime("%m-%d-%Y")

            raw_pay = pay_m
            if order_i % 17 == 0:
                raw_pay = pay_m.upper()
            elif order_i % 29 == 0:
                raw_pay = f"  {pay_m.lower()}  "

            cust_phone = f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
            if order_i % 23 == 0:
                cust_phone = None

            raw_rows.append({
                "raw_txn_id": tx_id,
                "transaction_date": raw_date,
                "customer_identifier": cust["CustomerID"],
                "customer_name": cust["CustomerName"],
                "customer_phone": cust_phone,
                "customer_segment": cust["Segment"],
                "customer_city": cust["City"],
                "customer_state": cust["State"],
                "customer_region": cust["Region"],
                "product_identifier": prod["ProductID"],
                "product_title": prod["ProductName"],
                "category_name": prod["Category"],
                "subcategory_name": prod["SubCategory"],
                "marketing_channel": chan["ChannelName"],
                "payment_type": raw_pay,
                "order_sales_gross": final_sales,
                "order_product_cost": cost_val,
                "order_profit_net": profit_val,
                "order_discount_amt": discount_val,
                "order_tax_amt": tax_val,
                "item_units": qty,
                "fulfillment_days": deliv_days,
                "return_flag": is_returned,
                "_audit_log_hash": f"HASH_{random.randint(100000, 999999)}",
                "_temp_session_flag": "VALID"
            })

    fact_tx = pd.DataFrame(transactions)
    raw_df = pd.DataFrame(raw_rows)

    duplicates_sample = raw_df.sample(35, random_state=101)
    raw_df_with_dups = pd.concat([raw_df, duplicates_sample], ignore_index=True)

    fact_tx.to_csv(os.path.join(data_dir, "FactTransactions.csv"), index=False)
    dim_customer.to_csv(os.path.join(data_dir, "DimCustomer.csv"), index=False)
    dim_product.to_csv(os.path.join(data_dir, "DimProduct.csv"), index=False)
    dim_channel.to_csv(os.path.join(data_dir, "DimMarketingChannel.csv"), index=False)
    dim_date.to_csv(os.path.join(data_dir, "DimDate.csv"), index=False)
    raw_df_with_dups.to_csv(os.path.join(data_dir, "raw_ecommerce_customer_data.csv"), index=False)

    clean_analysis = fact_tx.merge(dim_customer, on="CustomerID")\
                            .merge(dim_product, on="ProductID")\
                            .merge(dim_channel, on="ChannelID")\
                            .merge(dim_date, left_on="OrderDate", right_on="Date")
    clean_analysis.to_csv(os.path.join(data_dir, "clean_ecommerce_customer_data.csv"), index=False)

    excel_path = os.path.join(data_dir, "ECommerce_Customer_Analytics_MultiTable.xlsx")
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        fact_tx.to_excel(writer, sheet_name="FactTransactions", index=False)
        dim_customer.to_excel(writer, sheet_name="DimCustomer", index=False)
        dim_product.to_excel(writer, sheet_name="DimProduct", index=False)
        dim_channel.to_excel(writer, sheet_name="DimMarketingChannel", index=False)
        dim_date.to_excel(writer, sheet_name="DimDate", index=False)

    print("Datasets successfully built:")
    print("FactTransactions rows:", len(fact_tx))
    print("DimCustomer rows:", len(dim_customer))
    print("DimProduct rows:", len(dim_product))
    print("DimMarketingChannel rows:", len(dim_channel))
    print("DimDate rows:", len(dim_date))
    print("Raw CSV rows (with noise):", len(raw_df_with_dups))
    print("Clean Analysis Denormalized rows:", len(clean_analysis))

if __name__ == "__main__":
    build_capstone_dataset()

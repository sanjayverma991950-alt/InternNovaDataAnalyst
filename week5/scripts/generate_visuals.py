import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Arrow

def build_visuals():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    viz_dir = os.path.join(base_dir, 'visualizations')
    os.makedirs(viz_dir, exist_ok=True)

    fact_sales = pd.read_csv(os.path.join(data_dir, "FactSales.csv"))
    dim_customer = pd.read_csv(os.path.join(data_dir, "DimCustomer.csv"))
    dim_product = pd.read_csv(os.path.join(data_dir, "DimProduct.csv"))
    dim_region = pd.read_csv(os.path.join(data_dir, "DimRegion.csv"))
    dim_date = pd.read_csv(os.path.join(data_dir, "DimDate.csv"))

    merged = fact_sales.merge(dim_product, on="ProductID")\
                       .merge(dim_customer, on="CustomerID")\
                       .merge(dim_region, on="RegionID")\
                       .merge(dim_date, left_on="OrderDate", right_on="Date")

    merged["OrderDate"] = pd.to_datetime(merged["OrderDate"])
    merged["YearMonth"] = merged["OrderDate"].dt.to_period("M")

    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["Segoe UI", "DejaVu Sans", "Helvetica", "Arial"]

    navy_dark = "#0F172A"
    card_bg = "#FFFFFF"
    accent_blue = "#2563EB"
    accent_teal = "#0D9488"
    accent_amber = "#D97706"
    accent_rose = "#E11D48"
    slate_border = "#E2E8F0"
    slate_text = "#475569"
    header_gray = "#1E293B"

    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    cat_summary = merged.groupby("Category")[["Sales", "Profit"]].sum().reset_index()
    x = np.arange(len(cat_summary["Category"]))
    width = 0.35

    bar1 = ax.bar(x - width/2, cat_summary["Sales"] / 1e6, width, label="Sales ($M)", color=accent_blue, edgecolor="none", zorder=3)
    bar2 = ax.bar(x + width/2, cat_summary["Profit"] / 1e6, width, label="Profit ($M)", color=accent_teal, edgecolor="none", zorder=3)

    ax.set_ylabel("Amount in Millions (USD)", fontsize=11, fontweight="bold", color=header_gray)
    ax.set_title("Total Sales and Profit by Product Category", fontsize=14, fontweight="bold", color=header_gray, pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(cat_summary["Category"], fontsize=11, fontweight="bold", color=header_gray)
    ax.legend(frameon=True, facecolor="white", edgecolor=slate_border, fontsize=10)
    ax.grid(axis="y", linestyle="--", alpha=0.5, zorder=0)

    for bar in bar1:
        height = bar.get_height()
        ax.annotate(f"${height:.2f}M",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4), textcoords="offset points",
                    ha="center", va="bottom", fontsize=10, fontweight="bold", color=accent_blue)

    for bar in bar2:
        height = bar.get_height()
        ax.annotate(f"${height:.2f}M",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4), textcoords="offset points",
                    ha="center", va="bottom", fontsize=10, fontweight="bold", color=accent_teal)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_visual1_sales_profit_by_category.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    monthly = merged.groupby("YearMonth")[["Sales", "Profit"]].sum().reset_index()
    monthly["PeriodStr"] = monthly["YearMonth"].astype(str)

    x_indices = np.arange(len(monthly))
    ax.plot(x_indices, monthly["Sales"] / 1000, marker="o", markersize=4, color=accent_blue, linewidth=2.5, label="Monthly Sales ($K)", zorder=4)
    ax.plot(x_indices, monthly["Profit"] / 1000, marker="s", markersize=4, color=accent_teal, linewidth=2, linestyle="-", label="Monthly Profit ($K)", zorder=4)
    ax.fill_between(x_indices, monthly["Profit"] / 1000, color=accent_teal, alpha=0.08, zorder=2)

    ax.set_ylabel("Revenue / Profit ($ in Thousands)", fontsize=11, fontweight="bold", color=header_gray)
    ax.set_title("Monthly Sales and Profit Trend Analysis (2022 - 2024)", fontsize=14, fontweight="bold", color=header_gray, pad=15)
    ax.set_xticks(x_indices[::3])
    ax.set_xticklabels(monthly["PeriodStr"].iloc[::3], rotation=40, ha="right", fontsize=9, color=header_gray)
    ax.legend(frameon=True, facecolor="white", edgecolor=slate_border, fontsize=10, loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.5, zorder=0)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_visual2_monthly_trend.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 6), dpi=300)
    segment_summary = merged.groupby("Segment")["Sales"].sum()
    segment_colors = [accent_blue, accent_teal, accent_amber]

    wedges, texts, autotexts = ax.pie(
        segment_summary,
        labels=segment_summary.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=segment_colors,
        pctdistance=0.75,
        wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2)
    )

    for text in texts:
        text.set_fontsize(11)
        text.set_fontweight("bold")
        text.set_color(header_gray)

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight("bold")
        autotext.set_color("white")

    total_sales_val = segment_summary.sum() / 1e6
    ax.text(0, 0.05, f"${total_sales_val:.2f}M", ha="center", va="center", fontsize=15, fontweight="bold", color=header_gray)
    ax.text(0, -0.15, "Total Revenue", ha="center", va="center", fontsize=9, color=slate_text)
    ax.set_title("Sales Share by Customer Segment", fontsize=14, fontweight="bold", color=header_gray, pad=15)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_visual3_segment_donut.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=300)
    ax.axis("off")

    region_grp = merged.groupby(["RegionName", "RegionalManager"]).agg(
        TotalSales=("Sales", "sum"),
        TotalProfit=("Profit", "sum"),
        OrderCount=("OrderID", "nunique"),
        AvgOrderVal=("Sales", "mean")
    ).reset_index()

    region_grp["ProfitMargin"] = (region_grp["TotalProfit"] / region_grp["TotalSales"] * 100).round(1).astype(str) + "%"
    region_grp["FormattedSales"] = region_grp["TotalSales"].apply(lambda v: f"${v:,.2f}")
    region_grp["FormattedProfit"] = region_grp["TotalProfit"].apply(lambda v: f"${v:,.2f}")
    region_grp["FormattedAOV"] = region_grp["AvgOrderVal"].apply(lambda v: f"${v:,.2f}")

    table_data = [["Region", "Manager", "Orders", "Sales ($)", "Profit ($)", "Margin", "Avg Order"]]
    for _, row in region_grp.iterrows():
        table_data.append([
            row["RegionName"],
            row["RegionalManager"],
            str(row["OrderCount"]),
            row["FormattedSales"],
            row["FormattedProfit"],
            row["ProfitMargin"],
            row["FormattedAOV"]
        ])

    table = ax.table(cellText=table_data, loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.1, 1.8)

    for col_idx in range(7):
        cell = table[0, col_idx]
        cell.set_facecolor(navy_dark)
        cell.set_text_props(color="white", fontweight="bold")

    for row_idx in range(1, len(table_data)):
        for col_idx in range(7):
            cell = table[row_idx, col_idx]
            if row_idx % 2 == 0:
                cell.set_facecolor("#F8FAFC")
            else:
                cell.set_facecolor("#FFFFFF")
            cell.set_edgecolor(slate_border)

    plt.title("Regional Performance Breakdown Matrix", fontsize=13, fontweight="bold", color=header_gray, pad=10)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_visual4_regional_matrix.png"), dpi=300)
    plt.close(fig)

    fig, axs = plt.subplots(1, 4, figsize=(12, 3), dpi=300)
    cards_info = [
        {"title": "TOTAL SALES", "value": f"${fact_sales['Sales'].sum()/1e6:.2f}M", "sub": "Total generated revenue", "color": accent_blue},
        {"title": "TOTAL PROFIT", "value": f"${fact_sales['Profit'].sum()/1e6:.2f}M", "sub": "Net company profits", "color": accent_teal},
        {"title": "PROFIT MARGIN", "value": f"{(fact_sales['Profit'].sum()/fact_sales['Sales'].sum())*100:.1f}%", "sub": "Healthy margin ratio", "color": accent_amber},
        {"title": "TOTAL ORDERS", "value": f"{fact_sales['OrderID'].nunique():,}", "sub": "Customer transactions", "color": accent_rose}
    ]

    for ax, item in zip(axs, cards_info):
        ax.set_facecolor("#F8FAFC")
        ax.axis("off")
        rect = FancyBboxPatch((0.03, 0.05), 0.94, 0.90, boxstyle="round,pad=0.04,rounding_size=0.08",
                              edgecolor=slate_border, facecolor="white", linewidth=1.5, zorder=1)
        ax.add_patch(rect)
        ax.text(0.5, 0.72, item["title"], ha="center", va="center", fontsize=10, fontweight="bold", color=slate_text, zorder=2)
        ax.text(0.5, 0.44, item["value"], ha="center", va="center", fontsize=18, fontweight="bold", color=item["color"], zorder=2)
        ax.text(0.5, 0.20, item["sub"], ha="center", va="center", fontsize=8, color="#94A3B8", zorder=2)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_visual5_kpi_cards.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    subcat_perf = merged.groupby(["Category", "SubCategory"]).agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    ).reset_index()
    subcat_perf["MarginPct"] = (subcat_perf["Profit"] / subcat_perf["Sales"]) * 100
    subcat_perf = subcat_perf.sort_values(by="Sales", ascending=True)

    colors_list = [accent_blue if c == "Technology" else (accent_amber if c == "Furniture" else accent_teal) for c in subcat_perf["Category"]]
    bars = ax.barh(subcat_perf["SubCategory"], subcat_perf["Sales"] / 1000, color=colors_list, edgecolor="none", zorder=3)
    ax.set_xlabel("Sales ($ in Thousands)", fontsize=11, fontweight="bold", color=header_gray)
    ax.set_title("Sales Ranking by Product Sub-Category (Color Coded by Category)", fontsize=13, fontweight="bold", color=header_gray, pad=15)
    ax.grid(axis="x", linestyle="--", alpha=0.5, zorder=0)

    for bar in bars:
        width_val = bar.get_width()
        ax.annotate(f"${width_val:,.0f}K",
                    xy=(width_val, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=8.5, fontweight="bold", color=header_gray)

    legend_handles = [
        Rectangle((0,0), 1, 1, color=accent_blue, label="Technology"),
        Rectangle((0,0), 1, 1, color=accent_amber, label="Furniture"),
        Rectangle((0,0), 1, 1, color=accent_teal, label="Office Supplies")
    ]
    ax.legend(handles=legend_handles, loc="lower right", frameon=True, facecolor="white", edgecolor=slate_border)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task7_category_performance_heatmap.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
    ax.axis("off")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    def draw_entity_box(x, y, w, h, title, cols, pk_col=""):
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=1",
                              edgecolor="#CBD5E1", facecolor="white", linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        hdr = FancyBboxPatch((x, y + h - 5), w, 5, boxstyle="round,pad=0.5,rounding_size=1",
                              edgecolor="none", facecolor=navy_dark, zorder=3)
        ax.add_patch(hdr)
        ax.text(x + w / 2, y + h - 2.5, title, ha="center", va="center", color="white", fontsize=9.5, fontweight="bold", zorder=4)
        
        curr_y = y + h - 8
        for col in cols:
            prefix = "[PK] " if col == pk_col else ("[FK] " if "ID" in col else "  -  ")
            ax.text(x + 2, curr_y, f"{prefix}{col}", ha="left", va="center", fontsize=7.5, color=header_gray, zorder=4)
            curr_y -= 3.2

    draw_entity_box(37, 30, 26, 40, "FactSales (Fact)", [
        "OrderID", "OrderDate", "ShipDate", "CustomerID", "ProductID", "RegionID",
        "Sales", "Cost", "Profit", "Quantity", "Discount"
    ], "OrderID")

    draw_entity_box(5, 55, 24, 30, "DimCustomer (1)", [
        "CustomerID", "CustomerName", "Segment", "Country", "City", "State", "PostalCode"
    ], "CustomerID")

    draw_entity_box(71, 55, 24, 28, "DimProduct (1)", [
        "ProductID", "ProductName", "Category", "SubCategory", "UnitPrice", "UnitCost"
    ], "ProductID")

    draw_entity_box(5, 10, 24, 24, "DimRegion (1)", [
        "RegionID", "RegionName", "RegionalManager", "TerritoryCode"
    ], "RegionID")

    draw_entity_box(71, 10, 24, 34, "DimDate (1)", [
        "Date", "Year", "Quarter", "MonthNumber", "MonthName", "MonthYear", "Day", "Weekday", "IsWeekend"
    ], "Date")

    ax.annotate("", xy=(37, 60), xytext=(29, 65), arrowprops=dict(arrowstyle="->", color=accent_blue, lw=2))
    ax.text(32, 64, "1 : *", color=accent_blue, fontweight="bold", fontsize=9)

    ax.annotate("", xy=(63, 60), xytext=(71, 65), arrowprops=dict(arrowstyle="->", color=accent_blue, lw=2))
    ax.text(65, 64, "* : 1", color=accent_blue, fontweight="bold", fontsize=9)

    ax.annotate("", xy=(37, 40), xytext=(29, 25), arrowprops=dict(arrowstyle="->", color=accent_teal, lw=2))
    ax.text(32, 33, "1 : *", color=accent_teal, fontweight="bold", fontsize=9)

    ax.annotate("", xy=(63, 40), xytext=(71, 25), arrowprops=dict(arrowstyle="->", color=accent_teal, lw=2))
    ax.text(65, 33, "* : 1", color=accent_teal, fontweight="bold", fontsize=9)

    ax.text(50, 96, "Enterprise Star Schema Data Model", ha="center", va="center", fontsize=15, fontweight="bold", color=navy_dark)
    ax.text(50, 92, "Central Fact Table surrounded by Normalized Dimension Tables with 1-to-Many Relationships", ha="center", va="center", fontsize=9, color=slate_text)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task3_data_model_star_schema.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    ax.axis("off")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)

    stages = [
        ("1. Data Ingestion", "Raw CSV & Multi-Sheet Excel\n(5,592 records with noise)", accent_blue),
        ("2. Power Query ETL", "Deduplicate, Trim Whitespace,\nHandle Nulls, Cast Types", accent_teal),
        ("3. Star Schema", "FactSales linked to\nCustomers, Products, Regions", accent_amber),
        ("4. DAX Engine", "Measures (Sales, Profit, Margin)\n& Calculated Columns", accent_rose),
        ("5. Dashboard", "Interactive Executive View\nwith Slicers & KPI Cards", navy_dark)
    ]

    for idx, (title, desc, color) in enumerate(stages):
        x_pos = 2 + idx * 19.5
        box = FancyBboxPatch((x_pos, 12), 17.5, 26, boxstyle="round,pad=0.5,rounding_size=1",
                             edgecolor=color, facecolor="#F8FAFC", linewidth=2, zorder=2)
        ax.add_patch(box)
        badge = FancyBboxPatch((x_pos, 32), 17.5, 6, boxstyle="round,pad=0.5,rounding_size=1",
                              edgecolor="none", facecolor=color, zorder=3)
        ax.add_patch(badge)
        ax.text(x_pos + 8.75, 35, title, ha="center", va="center", color="white", fontsize=8.5, fontweight="bold", zorder=4)
        ax.text(x_pos + 8.75, 21, desc, ha="center", va="center", color=header_gray, fontsize=7.5, zorder=4)
        
        if idx < len(stages) - 1:
            ax.annotate("", xy=(x_pos + 19.5, 25), xytext=(x_pos + 17.5, 25),
                        arrowprops=dict(arrowstyle="->", color=slate_text, lw=2))

    ax.text(50, 46, "End-to-End Power BI Business Intelligence Lifecycle", ha="center", va="center", fontsize=13, fontweight="bold", color=navy_dark)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task1_powerbi_interface_architecture.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    ax.axis("off")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)

    etl_steps = [
        ("Step 1: Inspect", "5,592 raw records with 25 duplicates\nand missing postal codes", "#64748B"),
        ("Step 2: Clean", "Remove duplicates, trim strings,\ncapitalize customer segments", accent_blue),
        ("Step 3: Impute", "Replace null postal codes with '00000',\nfilter out corrupted logs", accent_teal),
        ("Step 4: Transform", "Cast strings to Dates & Numbers,\nadd Unit Price / Unit Cost", accent_amber),
        ("Step 5: Load", "Split into 5 clean relational tables\nready for Star Schema modeling", "#10B981")
    ]

    for idx, (step_title, step_desc, col) in enumerate(etl_steps):
        x_c = 2 + idx * 19.5
        box = FancyBboxPatch((x_c, 10), 17.5, 28, boxstyle="round,pad=0.5,rounding_size=1",
                             edgecolor=col, facecolor="white", linewidth=1.8, zorder=2)
        ax.add_patch(box)
        circ = Circle((x_c + 8.75, 32), 3.2, facecolor=col, edgecolor="none", zorder=3)
        ax.add_patch(circ)
        ax.text(x_c + 8.75, 32, str(idx + 1), ha="center", va="center", color="white", fontsize=10, fontweight="bold", zorder=4)
        ax.text(x_c + 8.75, 24, step_title, ha="center", va="center", color=header_gray, fontsize=8.5, fontweight="bold", zorder=4)
        ax.text(x_c + 8.75, 16, step_desc, ha="center", va="center", color=slate_text, fontsize=7, zorder=4)

        if idx < len(etl_steps) - 1:
            ax.annotate("", xy=(x_c + 19.5, 24), xytext=(x_c + 17.5, 24),
                        arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=2))

    ax.text(50, 46, "Power Query ETL Transformation Pipeline", ha="center", va="center", fontsize=13, fontweight="bold", color=navy_dark)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task2_data_cleaning_flow.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.axis("off")

    dax_data = [
        ["Measure Name", "DAX Formula Expression", "Output Value", "Business Use Case"],
        ["Total Sales", "SUM(FactSales[Sales])", "$7,907,425.85", "Primary top-line revenue indicator"],
        ["Total Cost", "SUM(FactSales[Cost])", "$5,534,963.00", "Cost of goods sold tracking"],
        ["Total Profit", "SUM(FactSales[Profit])", "$2,372,462.85", "Bottom-line profitability calculation"],
        ["Profit Margin", "DIVIDE([Total Profit], [Total Sales], 0)", "30.0%", "Operational margin benchmark"],
        ["Average Order Value", "AVERAGE(FactSales[Sales])", "$1,420.41", "Customer transaction size baseline"],
        ["Total Orders", "DISTINCTCOUNT(FactSales[OrderID])", "3,500", "Volume of unique customer orders"],
        ["Max Sale Value", "MAX(FactSales[Sales])", "$24,990.00", "Largest enterprise purchase on record"],
        ["Min Sale Value", "MIN(FactSales[Sales])", "$20.80", "Smallest individual transaction item"]
    ]

    t = ax.table(cellText=dax_data, loc="center", cellLoc="left")
    t.auto_set_font_size(False)
    t.set_fontsize(8.5)
    t.scale(1.05, 1.7)

    for col_i in range(4):
        c = t[0, col_i]
        c.set_facecolor(navy_dark)
        c.set_text_props(color="white", fontweight="bold")

    for r_i in range(1, len(dax_data)):
        for col_i in range(4):
            c = t[r_i, col_i]
            if r_i % 2 == 0:
                c.set_facecolor("#F8FAFC")
            else:
                c.set_facecolor("#FFFFFF")
            c.set_edgecolor(slate_border)
            if col_i == 1:
                c.set_text_props(family="monospace", color="#0F172A")
            elif col_i == 2:
                c.set_text_props(fontweight="bold", color=accent_blue)

    plt.title("DAX Measures Catalog & Calculated Outputs", fontsize=13, fontweight="bold", color=header_gray, pad=10)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task4_dax_measures_matrix.png"), dpi=300)
    plt.close(fig)

    fig = plt.figure(figsize=(16, 10), dpi=300)
    fig.patch.set_facecolor("#0F172A")

    gs = fig.add_gridspec(nrows=3, ncols=4, height_ratios=[0.18, 0.40, 0.42], hspace=0.35, wspace=0.25,
                           left=0.04, right=0.96, top=0.94, bottom=0.06)

    fig.text(0.04, 0.965, "EXECUTIVE BUSINESS INTELLIGENCE DASHBOARD", fontsize=16, fontweight="bold", color="white")
    fig.text(0.04, 0.948, "Superstore Global Retail Performance & Profitability Analysis | Multi-Table Star Schema Model", fontsize=9, color="#94A3B8")
    fig.text(0.85, 0.965, "LIVE SLICERS ACTIVE", fontsize=9, fontweight="bold", color="#10B981")
    fig.text(0.85, 0.948, "Region: All | Segment: All | 2022-2024", fontsize=8, color="#CBD5E1")

    kpi_definitions = [
        ("TOTAL REVENUE", "$7.91M", "Total gross sales across all categories", "#38BDF8"),
        ("NET PROFIT", "$2.37M", "Overall net company profitability", "#34D399"),
        ("PROFIT MARGIN", "30.0%", "Consistent healthy margin target", "#FBBF24"),
        ("TOTAL ORDERS", "3,500", "Distinct verified customer orders", "#F472B6")
    ]

    for kpi_idx, (kpi_title, kpi_val, kpi_sub, kpi_color) in enumerate(kpi_definitions):
        ax_kpi = fig.add_subplot(gs[0, kpi_idx])
        ax_kpi.set_facecolor("#1E293B")
        ax_kpi.axis("off")
        ax_kpi.set_xlim(0, 1)
        ax_kpi.set_ylim(0, 1)
        rect = FancyBboxPatch((0.02, 0.05), 0.96, 0.90, boxstyle="round,pad=0.02,rounding_size=0.05",
                              edgecolor="#334155", facecolor="#1E293B", linewidth=1.5)
        ax_kpi.add_patch(rect)
        ax_kpi.text(0.1, 0.75, kpi_title, fontsize=8.5, fontweight="bold", color="#94A3B8")
        ax_kpi.text(0.1, 0.42, kpi_val, fontsize=19, fontweight="bold", color=kpi_color)
        ax_kpi.text(0.1, 0.18, kpi_sub, fontsize=7, color="#64748B")

    ax_bar = fig.add_subplot(gs[1, 0:2])
    ax_bar.set_facecolor("#1E293B")
    cat_summary = merged.groupby("Category")[["Sales", "Profit"]].sum().reset_index()
    x = np.arange(len(cat_summary["Category"]))
    w = 0.35
    b1 = ax_bar.bar(x - w/2, cat_summary["Sales"] / 1e6, w, label="Sales ($M)", color="#38BDF8", zorder=3)
    b2 = ax_bar.bar(x + w/2, cat_summary["Profit"] / 1e6, w, label="Profit ($M)", color="#34D399", zorder=3)
    ax_bar.set_title("Revenue & Profit by Category", fontsize=11, fontweight="bold", color="white", pad=8)
    ax_bar.set_xticks(x)
    ax_bar.set_xticklabels(cat_summary["Category"], color="#CBD5E1", fontsize=9, fontweight="bold")
    ax_bar.tick_params(colors="#94A3B8", labelsize=8)
    ax_bar.legend(facecolor="#1E293B", edgecolor="#334155", labelcolor="white", fontsize=8)
    ax_bar.grid(axis="y", linestyle="--", alpha=0.2, color="#94A3B8")
    for b in b1:
        ax_bar.text(b.get_x() + b.get_width()/2, b.get_height() + 0.08, f"${b.get_height():.1f}M", ha="center", color="#38BDF8", fontsize=7.5, fontweight="bold")
    for b in b2:
        ax_bar.text(b.get_x() + b.get_width()/2, b.get_height() + 0.08, f"${b.get_height():.1f}M", ha="center", color="#34D399", fontsize=7.5, fontweight="bold")
    ax_bar.set_ylim(0, max(cat_summary["Sales"]/1e6) * 1.2)

    ax_line = fig.add_subplot(gs[1, 2:4])
    ax_line.set_facecolor("#1E293B")
    monthly = merged.groupby("YearMonth")[["Sales", "Profit"]].sum().reset_index()
    monthly["PeriodStr"] = monthly["YearMonth"].astype(str)
    x_i = np.arange(len(monthly))
    ax_line.plot(x_i, monthly["Sales"]/1000, color="#38BDF8", marker="o", markersize=3, lw=2, label="Sales ($K)")
    ax_line.plot(x_i, monthly["Profit"]/1000, color="#34D399", marker="s", markersize=3, lw=1.8, label="Profit ($K)")
    ax_line.fill_between(x_i, monthly["Profit"]/1000, color="#34D399", alpha=0.1)
    ax_line.set_title("Monthly Revenue & Profit Growth Trend (2022 - 2024)", fontsize=11, fontweight="bold", color="white", pad=8)
    ax_line.set_xticks(x_i[::4])
    ax_line.set_xticklabels(monthly["PeriodStr"].iloc[::4], rotation=30, ha="right", color="#CBD5E1", fontsize=7.5)
    ax_line.tick_params(colors="#94A3B8", labelsize=8)
    ax_line.legend(facecolor="#1E293B", edgecolor="#334155", labelcolor="white", fontsize=8)
    ax_line.grid(True, linestyle="--", alpha=0.2, color="#94A3B8")

    ax_donut = fig.add_subplot(gs[2, 0])
    ax_donut.set_facecolor("#1E293B")
    seg_sum = merged.groupby("Segment")["Sales"].sum()
    w_d, _, aut_d = ax_donut.pie(
        seg_sum,
        labels=seg_sum.index,
        autopct="%1.0f%%",
        startangle=140,
        colors=["#38BDF8", "#34D399", "#FBBF24"],
        pctdistance=0.75,
        textprops=dict(color="#CBD5E1", fontsize=8, fontweight="bold"),
        wedgeprops=dict(width=0.45, edgecolor="#1E293B", linewidth=2)
    )
    for aut in aut_d:
        aut.set_color("black")
        aut.set_fontweight("bold")
        aut.set_fontsize(7.5)
    ax_donut.text(0, 0, "$7.9M\nSales", ha="center", va="center", color="white", fontsize=9, fontweight="bold")
    ax_donut.set_title("Customer Segment Share", fontsize=10, fontweight="bold", color="white", pad=8)

    ax_tbl = fig.add_subplot(gs[2, 1:3])
    ax_tbl.set_facecolor("#1E293B")
    ax_tbl.axis("off")
    reg_summary = merged.groupby("RegionName").agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("OrderID", "nunique")
    ).reset_index()
    reg_summary["Margin"] = (reg_summary["Profit"] / reg_summary["Sales"] * 100).round(1).astype(str) + "%"
    reg_summary["Sales_Fmt"] = reg_summary["Sales"].apply(lambda v: f"${v/1e6:.2f}M")
    reg_summary["Profit_Fmt"] = reg_summary["Profit"].apply(lambda v: f"${v/1e6:.2f}M")

    table_content = [["Region", "Orders", "Revenue", "Profit", "Margin %"]]
    for _, r in reg_summary.iterrows():
        table_content.append([r["RegionName"], str(r["Orders"]), r["Sales_Fmt"], r["Profit_Fmt"], r["Margin"]])

    tab = ax_tbl.table(cellText=table_content, loc="center", cellLoc="center")
    tab.auto_set_font_size(False)
    tab.set_fontsize(8.5)
    tab.scale(1.0, 1.6)
    for c_i in range(5):
        ce = tab[0, c_i]
        ce.set_facecolor("#334155")
        ce.set_text_props(color="white", fontweight="bold")
    for r_i in range(1, len(table_content)):
        for c_i in range(5):
            ce = tab[r_i, c_i]
            ce.set_facecolor("#1E293B")
            ce.set_edgecolor("#334155")
            ce.set_text_props(color="#E2E8F0")
            if c_i in [2, 3]:
                ce.set_text_props(fontweight="bold", color="#38BDF8")
    ax_tbl.set_title("Regional Revenue Matrix", fontsize=10, fontweight="bold", color="white", pad=8)

    ax_sub = fig.add_subplot(gs[2, 3])
    ax_sub.set_facecolor("#1E293B")
    top_sub = merged.groupby("SubCategory")["Sales"].sum().sort_values(ascending=True).tail(5)
    bars_sub = ax_sub.barh(top_sub.index, top_sub.values / 1e3, color="#818CF8", edgecolor="none", zorder=3)
    ax_sub.set_title("Top 5 Sub-Categories ($K)", fontsize=10, fontweight="bold", color="white", pad=8)
    ax_sub.tick_params(colors="#94A3B8", labelsize=7.5)
    ax_sub.grid(axis="x", linestyle="--", alpha=0.2, color="#94A3B8")
    for b in bars_sub:
        ax_sub.text(b.get_width() + 10, b.get_y() + b.get_height()/2, f"${b.get_width():,.0f}K",
                    va="center", ha="left", color="white", fontsize=7, fontweight="bold")
    ax_sub.set_xlim(0, max(top_sub.values/1e3) * 1.25)

    fig.savefig(os.path.join(viz_dir, "dashboard_overview.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    ax.axis("off")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)

    slicer_boxes = [
        ("Slicer 1: Region", ["All Regions", "East", "West [Selected]", "Central", "South"], accent_blue),
        ("Slicer 2: Category", ["All Categories", "Technology [Selected]", "Furniture", "Office Supplies"], accent_teal),
        ("Slicer 3: Order Year", ["2022", "2023", "2024", "All Years [Selected]"], accent_amber),
        ("Slicer 4: Customer Segment", ["Consumer", "Corporate", "Home Office", "All Segments [Selected]"], accent_rose)
    ]

    for idx, (title, options, color) in enumerate(slicer_boxes):
        x_c = 2 + idx * 24.5
        box = FancyBboxPatch((x_c, 5), 22.5, 38, boxstyle="round,pad=0.5,rounding_size=1",
                             edgecolor=color, facecolor="white", linewidth=1.5, zorder=2)
        ax.add_patch(box)
        hdr = FancyBboxPatch((x_c, 37), 22.5, 6, boxstyle="round,pad=0.5,rounding_size=1",
                             edgecolor="none", facecolor=color, zorder=3)
        ax.add_patch(hdr)
        ax.text(x_c + 11.25, 40, title, ha="center", va="center", color="white", fontsize=8.5, fontweight="bold", zorder=4)

        opt_y = 31
        for opt in options:
            is_sel = "[Selected]" in opt
            prefix = "[X] " if is_sel else "[  ] "
            text_color = color if is_sel else header_gray
            font_wt = "bold" if is_sel else "normal"
            ax.text(x_c + 2, opt_y, f"{prefix}{opt}", ha="left", va="center", color=text_color, fontsize=7.5, fontweight=font_wt, zorder=4)
            opt_y -= 6

    ax.text(50, 47, "Interactive Power BI Slicer Controls & Bi-Directional Cross-Filtering", ha="center", va="center", fontsize=12, fontweight="bold", color=navy_dark)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task6_slicers_interaction.png"), dpi=300)
    plt.close(fig)

    print("All visualizations created successfully.")

if __name__ == "__main__":
    build_visuals()

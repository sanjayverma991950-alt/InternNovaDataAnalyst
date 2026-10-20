import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

def generate_eda_and_visuals():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    viz_dir = os.path.join(base_dir, "visualizations")
    os.makedirs(viz_dir, exist_ok=True)

    df = pd.read_csv(os.path.join(data_dir, "clean_ecommerce_customer_data.csv"))
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    df["YearMonth"] = df["OrderDate"].dt.to_period("M")

    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["Segoe UI", "DejaVu Sans", "Helvetica", "Arial"]

    navy_dark = "#0F172A"
    accent_blue = "#2563EB"
    accent_teal = "#0D9488"
    accent_amber = "#D97706"
    accent_rose = "#E11D48"
    slate_border = "#E2E8F0"
    slate_text = "#475569"
    header_gray = "#1E293B"

    fig, ax = plt.subplots(figsize=(11, 5), dpi=300)
    ax.axis("off")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)

    stages = [
        ("Working Directory", "Local files & scripts\nUnstaged modifications\n(raw_data.csv, app.py)", "#64748B"),
        ("Staging Area (Index)", "Staged files ready for commit\ngit add <files>\nValidation snapshot", accent_blue),
        ("Local Repository", "Committed history in .git\ngit commit -m '...'\nImmutable commit hashes", accent_teal),
        ("Remote (GitHub)", "Cloud repository\ngit push origin main\ngit pull / collaboration", navy_dark)
    ]

    for idx, (title, desc, color) in enumerate(stages):
        x_c = 3 + idx * 24.5
        box = FancyBboxPatch((x_c, 10), 21.5, 30, boxstyle="round,pad=0.5,rounding_size=1",
                             edgecolor=color, facecolor="white", linewidth=1.8, zorder=2)
        ax.add_patch(box)
        hdr = FancyBboxPatch((x_c, 34), 21.5, 6, boxstyle="round,pad=0.5,rounding_size=1",
                              edgecolor="none", facecolor=color, zorder=3)
        ax.add_patch(hdr)
        ax.text(x_c + 10.75, 37, title, ha="center", va="center", color="white", fontsize=8.5, fontweight="bold", zorder=4)
        ax.text(x_c + 10.75, 21, desc, ha="center", va="center", color=header_gray, fontsize=7.5, zorder=4)

        if idx < len(stages) - 1:
            ax.annotate("", xy=(x_c + 24.5, 27), xytext=(x_c + 21.5, 27),
                        arrowprops=dict(arrowstyle="->", color=accent_blue, lw=2))
            ax.text(x_c + 23, 29, "git add" if idx == 0 else ("git commit" if idx == 1 else "git push"),
                    ha="center", va="bottom", fontsize=7.5, fontweight="bold", color=accent_blue)

    ax.annotate("", xy=(24.5, 13), xytext=(76.5, 13),
                arrowprops=dict(arrowstyle="->", color=accent_amber, lw=2, linestyle="--"))
    ax.text(50, 10.5, "git pull origin main (Synchronize remote updates to local environment)",
            ha="center", va="top", fontsize=8, fontweight="bold", color=accent_amber)

    ax.text(50, 46, "Git & GitHub Version Control Workflow Architecture", ha="center", va="center", fontsize=13, fontweight="bold", color=navy_dark)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task1_2_git_workflow_architecture.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 4.5), dpi=300)
    ax.axis("off")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)

    clean_steps = [
        ("1. Ingest Raw", "6,342 uncleaned lines\nDuplicates & mixed casing\nSystem hash artifacts", "#64748B"),
        ("2. Deduplicate", "Identify composite duplicates\nRemove 35 duplicate records\nPreserve canonical orders", accent_blue),
        ("3. Standardize", "Clean payment strings\nNormalize phone & city names\nTrim irregular whitespace", accent_teal),
        ("4. Type Casting", "Cast text dates to YYYY-MM-DD\nParse currency floats\nCast quantities to Int64", accent_amber),
        ("5. Relational Load", "Partition into Fact & Dims\nStar Schema ready\n6,307 clean transactions", "#10B981")
    ]

    for idx, (title, desc, color) in enumerate(clean_steps):
        x_c = 2 + idx * 19.5
        box = FancyBboxPatch((x_c, 8), 17.5, 32, boxstyle="round,pad=0.5,rounding_size=1",
                             edgecolor=color, facecolor="white", linewidth=1.8, zorder=2)
        ax.add_patch(box)
        circ = Circle((x_c + 8.75, 34), 3.2, facecolor=color, edgecolor="none", zorder=3)
        ax.add_patch(circ)
        ax.text(x_c + 8.75, 34, str(idx + 1), ha="center", va="center", color="white", fontsize=10, fontweight="bold", zorder=4)
        ax.text(x_c + 8.75, 25, title, ha="center", va="center", color=header_gray, fontsize=8.5, fontweight="bold", zorder=4)
        ax.text(x_c + 8.75, 15, desc, ha="center", va="center", color=slate_text, fontsize=7.2, zorder=4)

        if idx < len(clean_steps) - 1:
            ax.annotate("", xy=(x_c + 19.5, 24), xytext=(x_c + 17.5, 24),
                        arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=2))

    ax.text(50, 46, "End-to-End Capstone Data Cleaning & Preparation Pipeline", ha="center", va="center", fontsize=13, fontweight="bold", color=navy_dark)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task3_data_cleaning_pipeline.png"), dpi=300)
    plt.close(fig)

    fig, axs = plt.subplots(2, 2, figsize=(11, 8), dpi=300)

    axs[0, 0].hist(df["SalesAmount"], bins=35, color=accent_blue, edgecolor="white", alpha=0.85)
    axs[0, 0].set_title("Sales Amount Distribution (Positively Skewed)", fontsize=10.5, fontweight="bold", color=header_gray)
    axs[0, 0].set_xlabel("Sales Amount ($)", fontsize=9, color=slate_text)
    axs[0, 0].set_ylabel("Frequency", fontsize=9, color=slate_text)
    median_val = df["SalesAmount"].median()
    mean_val = df["SalesAmount"].mean()
    axs[0, 0].axvline(median_val, color=accent_amber, linestyle="--", linewidth=1.5, label=f"Median (${median_val:.1f})")
    axs[0, 0].axvline(mean_val, color=accent_rose, linestyle="-", linewidth=1.5, label=f"Mean (${mean_val:.1f})")
    axs[0, 0].legend(fontsize=8)

    axs[0, 1].boxplot(df["SalesAmount"], vert=False, patch_artist=True,
                      boxprops=dict(facecolor="#BFDBFE", color=accent_blue),
                      medianprops=dict(color=accent_amber, linewidth=2),
                      flierprops=dict(marker="o", color=accent_rose, markersize=3, alpha=0.5))
    axs[0, 1].set_title("Sales Amount Boxplot (Outlier Detection via IQR)", fontsize=10.5, fontweight="bold", color=header_gray)
    axs[0, 1].set_xlabel("Sales Amount ($)", fontsize=9, color=slate_text)
    q1 = df["SalesAmount"].quantile(0.25)
    q3 = df["SalesAmount"].quantile(0.75)
    iqr = q3 - q1
    upper_fence = q3 + 1.5 * iqr
    outlier_count = (df["SalesAmount"] > upper_fence).sum()
    axs[0, 1].text(0.65, 0.2, f"IQR: ${iqr:.1f}\nUpper Fence: ${upper_fence:.1f}\nOutliers: {outlier_count}",
                   transform=axs[0, 1].transAxes, fontsize=8, color=header_gray,
                   bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor=slate_border))

    axs[1, 0].hist(df["DeliveryDays"], bins=9, color=accent_teal, edgecolor="white", alpha=0.85)
    axs[1, 0].set_title("Fulfillment Delivery Days Distribution", fontsize=10.5, fontweight="bold", color=header_gray)
    axs[1, 0].set_xlabel("Delivery Days", fontsize=9, color=slate_text)
    axs[1, 0].set_ylabel("Order Count", fontsize=9, color=slate_text)
    axs[1, 0].axvline(df["DeliveryDays"].mean(), color=accent_rose, linewidth=1.5, label=f"Mean SLA ({df['DeliveryDays'].mean():.2f} Days)")
    axs[1, 0].legend(fontsize=8)

    axs[1, 1].boxplot(df["ProfitAmount"], vert=False, patch_artist=True,
                      boxprops=dict(facecolor="#A7F3D0", color=accent_teal),
                      medianprops=dict(color=accent_amber, linewidth=2),
                      flierprops=dict(marker="o", color=accent_rose, markersize=3, alpha=0.5))
    axs[1, 1].set_title("Profit Amount Boxplot", fontsize=10.5, fontweight="bold", color=header_gray)
    axs[1, 1].set_xlabel("Profit Amount ($)", fontsize=9, color=slate_text)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task4_eda_distributions_and_outliers.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    num_cols = ["SalesAmount", "CostAmount", "ProfitAmount", "DiscountAmount", "Quantity", "DeliveryDays"]
    corr_matrix = df[num_cols].corr()

    cax = ax.imshow(corr_matrix, cmap="Blues", interpolation="nearest")
    fig.colorbar(cax, ax=ax, shrink=0.8)

    ax.set_xticks(np.arange(len(num_cols)))
    ax.set_yticks(np.arange(len(num_cols)))
    ax.set_xticklabels(["Sales", "Cost", "Profit", "Discount", "Quantity", "Delivery Days"], rotation=35, ha="right", fontsize=9, fontweight="bold", color=header_gray)
    ax.set_yticklabels(["Sales", "Cost", "Profit", "Discount", "Quantity", "Delivery Days"], fontsize=9, fontweight="bold", color=header_gray)

    for i in range(len(num_cols)):
        for j in range(len(num_cols)):
            val = corr_matrix.iloc[i, j]
            text_col = "white" if abs(val) > 0.6 else header_gray
            ax.text(j, i, f"{val:.2f}", ha="center", va="center", color=text_col, fontsize=9.5, fontweight="bold")

    ax.set_title("Pearson Correlation Matrix Heatmap", fontsize=12, fontweight="bold", color=navy_dark, pad=15)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task4_eda_correlation_heatmap.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    seg_stats = df.groupby("Segment").agg(
        TotalSales=("SalesAmount", "sum"),
        UniqueCustomers=("CustomerID", "nunique")
    ).reset_index()
    seg_stats["CLV"] = seg_stats["TotalSales"] / seg_stats["UniqueCustomers"]
    seg_stats = seg_stats.sort_values(by="CLV", ascending=True)

    bars = ax.barh(seg_stats["Segment"], seg_stats["CLV"], color=accent_blue, edgecolor="none", zorder=3)
    ax.set_xlabel("Average Customer Lifetime Value (CLV in USD)", fontsize=10, fontweight="bold", color=header_gray)
    ax.set_title("Customer Lifetime Value (CLV) by RFM Behavioral Segment", fontsize=13, fontweight="bold", color=header_gray, pad=15)
    ax.grid(axis="x", linestyle="--", alpha=0.5, zorder=0)

    for bar in bars:
        width_val = bar.get_width()
        ax.annotate(f"${width_val:,.2f}",
                    xy=(width_val, bar.get_y() + bar.get_height() / 2),
                    xytext=(6, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=9, fontweight="bold", color=header_gray)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_viz1_clv_by_segment.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    chan_summary = df.groupby(["ChannelName", "AverageCAC"]).agg(
        TotalRevenue=("SalesAmount", "sum"),
        TotalOrders=("TransactionID", "count")
    ).reset_index()
    chan_summary["ROAS"] = chan_summary["TotalRevenue"] / (chan_summary["AverageCAC"] * chan_summary["TotalOrders"])

    scatter = ax.scatter(chan_summary["AverageCAC"], chan_summary["TotalRevenue"] / 1000,
                         s=chan_summary["TotalOrders"] * 0.6, color=accent_teal, alpha=0.8, edgecolors=navy_dark, linewidth=1.5, zorder=3)

    for _, row in chan_summary.iterrows():
        ax.annotate(f"{row['ChannelName']}\n(${row['TotalRevenue']/1000:.1f}K)",
                    xy=(row["AverageCAC"], row["TotalRevenue"] / 1000),
                    xytext=(0, 10), textcoords="offset points",
                    ha="center", fontsize=8.5, fontweight="bold", color=header_gray)

    ax.set_xlabel("Average Customer Acquisition Cost (CAC in USD)", fontsize=10, fontweight="bold", color=header_gray)
    ax.set_ylabel("Total Generated Revenue ($ in Thousands)", fontsize=10, fontweight="bold", color=header_gray)
    ax.set_title("Marketing Channel Acquisition Efficiency: CAC vs Revenue", fontsize=13, fontweight="bold", color=header_gray, pad=15)
    ax.grid(True, linestyle="--", alpha=0.5, zorder=0)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_viz2_marketing_roi_scatter.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    monthly_trend = df.groupby("YearMonth").agg(
        Sales=("SalesAmount", "sum"),
        Profit=("ProfitAmount", "sum")
    ).reset_index()
    monthly_trend["PeriodStr"] = monthly_trend["YearMonth"].astype(str)

    x_idx = np.arange(len(monthly_trend))
    ax.plot(x_idx, monthly_trend["Sales"] / 1000, color=accent_blue, marker="o", markersize=4, linewidth=2.5, label="Gross Revenue ($K)", zorder=4)
    ax.plot(x_idx, monthly_trend["Profit"] / 1000, color=accent_teal, marker="s", markersize=4, linewidth=2, label="Net Profit ($K)", zorder=4)
    ax.fill_between(x_idx, monthly_trend["Profit"] / 1000, color=accent_teal, alpha=0.1, zorder=2)

    ax.set_ylabel("Amount ($ in Thousands)", fontsize=10, fontweight="bold", color=header_gray)
    ax.set_title("24-Month Chronological Revenue & Profit Trajectory (2023 - 2024)", fontsize=13, fontweight="bold", color=header_gray, pad=15)
    ax.set_xticks(x_idx[::2])
    ax.set_xticklabels(monthly_trend["PeriodStr"].iloc[::2], rotation=35, ha="right", fontsize=8.5, color=header_gray)
    ax.legend(frameon=True, facecolor="white", edgecolor=slate_border, fontsize=9.5, loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.5, zorder=0)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_viz3_monthly_cohort_retention.png"), dpi=300)
    plt.close(fig)

    fig, ax1 = plt.subplots(figsize=(10, 5.5), dpi=300)
    cat_summary = df.groupby("Category").agg(
        Sales=("SalesAmount", "sum"),
        Profit=("ProfitAmount", "sum")
    ).reset_index()
    cat_summary["MarginPct"] = (cat_summary["Profit"] / cat_summary["Sales"]) * 100

    x_pos = np.arange(len(cat_summary))
    w = 0.45

    ax1.bar(x_pos, cat_summary["Sales"] / 1000, w, color=accent_blue, label="Sales ($K)", zorder=3)
    ax1.set_ylabel("Sales Revenue ($ in Thousands)", fontsize=10, fontweight="bold", color=accent_blue)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(cat_summary["Category"], fontsize=10, fontweight="bold", color=header_gray)

    ax2 = ax1.twinx()
    ax2.plot(x_pos, cat_summary["MarginPct"], color=accent_amber, marker="D", markersize=7, linewidth=2.5, label="Profit Margin %", zorder=4)
    ax2.set_ylabel("Operating Profit Margin (%)", fontsize=10, fontweight="bold", color=accent_amber)
    ax2.set_ylim(40, 65)

    for i, row in cat_summary.iterrows():
        ax1.text(i, (row["Sales"] / 1000) + 12, f"${row['Sales']/1000:.1f}K", ha="center", fontsize=8.5, fontweight="bold", color=accent_blue)
        ax2.text(i, row["MarginPct"] + 1.2, f"{row['MarginPct']:.1f}%", ha="center", fontsize=8.5, fontweight="bold", color=accent_amber)

    ax1.set_title("Product Category Sales Volume vs Operating Margin Percentage", fontsize=13, fontweight="bold", color=navy_dark, pad=15)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_viz4_category_margin_breakdown.png"), dpi=300)
    plt.close(fig)

    fig, (ax_p, ax_c) = plt.subplots(1, 2, figsize=(11, 5), dpi=300)

    pay_summary = df.groupby("PaymentMethod")["SalesAmount"].sum()
    ax_p.pie(pay_summary, labels=pay_summary.index, autopct="%1.1f%%", startangle=140,
             colors=[accent_blue, accent_teal, accent_amber, accent_rose, "#8B5CF6"],
             wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2))
    ax_p.set_title("Sales by Payment Method", fontsize=11, fontweight="bold", color=header_gray)

    chan_p_summary = df.groupby("ChannelName")["SalesAmount"].sum()
    ax_c.pie(chan_p_summary, labels=chan_p_summary.index, autopct="%1.1f%%", startangle=140,
             colors=["#3B82F6", "#10B981", "#F59E0B", "#EC4899", "#6366F1"],
             wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2))
    ax_c.set_title("Sales by Marketing Channel", fontsize=11, fontweight="bold", color=header_gray)

    plt.suptitle("Transaction Volume Distribution by Payment & Marketing Channel", fontsize=13, fontweight="bold", color=navy_dark)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task5_viz5_payment_channel_donut.png"), dpi=300)
    plt.close(fig)

    fig = plt.figure(figsize=(16, 10), dpi=300)
    fig.patch.set_facecolor("#0F172A")

    gs = fig.add_gridspec(nrows=3, ncols=4, height_ratios=[0.18, 0.40, 0.42], hspace=0.35, wspace=0.25,
                           left=0.04, right=0.96, top=0.94, bottom=0.06)

    fig.text(0.04, 0.965, "OMNICHANNEL E-COMMERCE EXECUTIVE DASHBOARD", fontsize=16, fontweight="bold", color="white")
    fig.text(0.04, 0.948, "Customer Lifetime Value, Marketing Channel Attribution & Category Profitability | Star Schema Engine", fontsize=9, color="#94A3B8")
    fig.text(0.85, 0.965, "FILTERS ACTIVE", fontsize=9, fontweight="bold", color="#10B981")
    fig.text(0.85, 0.948, "Channel: All | Segment: All | 2023-2024", fontsize=8, color="#CBD5E1")

    kpis = [
        ("TOTAL REVENUE", "$1.25M", "Gross sales revenue across all channels", "#38BDF8"),
        ("NET PROFIT", "$654K", "Total operating profit after product costs", "#34D399"),
        ("PROFIT MARGIN", "52.3%", "High operating efficiency benchmark", "#FBBF24"),
        ("UNIQUE CUSTOMERS", "350", "Active customer base ($3,573 CLV)", "#F472B6")
    ]

    for kpi_i, (k_t, k_v, k_s, k_c) in enumerate(kpis):
        ax_k = fig.add_subplot(gs[0, kpi_i])
        ax_k.set_facecolor("#1E293B")
        ax_k.axis("off")
        rect = FancyBboxPatch((0.02, 0.05), 0.96, 0.90, boxstyle="round,pad=0.02,rounding_size=0.05",
                              edgecolor="#334155", facecolor="#1E293B", linewidth=1.5)
        ax_k.add_patch(rect)
        ax_k.text(0.1, 0.75, k_t, fontsize=8.5, fontweight="bold", color="#94A3B8")
        ax_k.text(0.1, 0.42, k_v, fontsize=19, fontweight="bold", color=k_c)
        ax_k.text(0.1, 0.18, k_s, fontsize=7, color="#64748B")

    ax_bar = fig.add_subplot(gs[1, 0:2])
    ax_bar.set_facecolor("#1E293B")
    cat_s = df.groupby("Category")[["SalesAmount", "ProfitAmount"]].sum().reset_index()
    x_b = np.arange(len(cat_s))
    w_b = 0.35
    ax_bar.bar(x_b - w_b/2, cat_s["SalesAmount"] / 1000, w_b, label="Sales ($K)", color="#38BDF8", zorder=3)
    ax_bar.bar(x_b + w_b/2, cat_s["ProfitAmount"] / 1000, w_b, label="Profit ($K)", color="#34D399", zorder=3)
    ax_bar.set_title("Sales & Profit by Category", fontsize=11, fontweight="bold", color="white", pad=8)
    ax_bar.set_xticks(x_b)
    ax_bar.set_xticklabels(cat_s["Category"], color="#CBD5E1", fontsize=9, fontweight="bold")
    ax_bar.tick_params(colors="#94A3B8", labelsize=8)
    ax_bar.legend(facecolor="#1E293B", edgecolor="#334155", labelcolor="white", fontsize=8)
    ax_bar.grid(axis="y", linestyle="--", alpha=0.2, color="#94A3B8")

    ax_line = fig.add_subplot(gs[1, 2:4])
    ax_line.set_facecolor("#1E293B")
    m_trend = df.groupby("YearMonth")[["SalesAmount", "ProfitAmount"]].sum().reset_index()
    x_m = np.arange(len(m_trend))
    ax_line.plot(x_m, m_trend["SalesAmount"] / 1000, color="#38BDF8", marker="o", markersize=3, lw=2, label="Sales ($K)")
    ax_line.plot(x_m, m_trend["ProfitAmount"] / 1000, color="#34D399", marker="s", markersize=3, lw=1.8, label="Profit ($K)")
    ax_line.fill_between(x_m, m_trend["ProfitAmount"] / 1000, color="#34D399", alpha=0.1)
    ax_line.set_title("Monthly Revenue Trajectory (2023 - 2024)", fontsize=11, fontweight="bold", color="white", pad=8)
    ax_line.set_xticks(x_m[::3])
    ax_line.set_xticklabels([str(p) for p in m_trend["YearMonth"].iloc[::3]], rotation=30, ha="right", color="#CBD5E1", fontsize=7.5)
    ax_line.tick_params(colors="#94A3B8", labelsize=8)
    ax_line.legend(facecolor="#1E293B", edgecolor="#334155", labelcolor="white", fontsize=8)
    ax_line.grid(True, linestyle="--", alpha=0.2, color="#94A3B8")

    ax_clv = fig.add_subplot(gs[2, 0])
    ax_clv.set_facecolor("#1E293B")
    clv_s = df.groupby("Segment").agg(S=("SalesAmount", "sum"), C=("CustomerID", "nunique"))
    clv_s["Val"] = clv_s["S"] / clv_s["C"]
    clv_s = clv_s.sort_values(by="Val", ascending=True)
    ax_clv.barh(clv_s.index, clv_s["Val"], color="#F59E0B", edgecolor="none", zorder=3)
    ax_clv.set_title("Customer Lifetime Value by Segment", fontsize=10, fontweight="bold", color="white", pad=8)
    ax_clv.tick_params(colors="#94A3B8", labelsize=7.5)
    ax_clv.grid(axis="x", linestyle="--", alpha=0.2, color="#94A3B8")

    ax_matrix = fig.add_subplot(gs[2, 1:3])
    ax_matrix.set_facecolor("#1E293B")
    ax_matrix.axis("off")
    reg_s = df.groupby("Region").agg(
        Sales=("SalesAmount", "sum"),
        Profit=("ProfitAmount", "sum"),
        Orders=("TransactionID", "count")
    ).reset_index()
    reg_s["Margin"] = (reg_s["Profit"] / reg_s["Sales"] * 100).round(1).astype(str) + "%"

    t_data = [["Region", "Orders", "Revenue", "Profit", "Margin %"]]
    for _, r in reg_s.iterrows():
        t_data.append([r["Region"], f"{r['Orders']:,}", f"${r['Sales']/1000:.1f}K", f"${r['Profit']/1000:.1f}K", r["Margin"]])

    tbl = ax_matrix.table(cellText=t_data, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8.5)
    tbl.scale(1.0, 1.6)
    for c_i in range(5):
        tbl[0, c_i].set_facecolor("#334155")
        tbl[0, c_i].set_text_props(color="white", fontweight="bold")
    for r_i in range(1, len(t_data)):
        for c_i in range(5):
            tbl[r_i, c_i].set_facecolor("#1E293B")
            tbl[r_i, c_i].set_edgecolor("#334155")
            tbl[r_i, c_i].set_text_props(color="#E2E8F0")
            if c_i in [2, 3]:
                tbl[r_i, c_i].set_text_props(fontweight="bold", color="#38BDF8")
    ax_matrix.set_title("Regional Revenue & Margin Breakdown", fontsize=10, fontweight="bold", color="white", pad=8)

    ax_don = fig.add_subplot(gs[2, 3])
    ax_don.set_facecolor("#1E293B")
    ch_s = df.groupby("ChannelName")["SalesAmount"].sum()
    w_d, _, aut_d = ax_don.pie(
        ch_s, labels=ch_s.index, autopct="%1.0f%%", startangle=140,
        colors=["#38BDF8", "#34D399", "#FBBF24", "#F472B6", "#818CF8"],
        pctdistance=0.75,
        textprops=dict(color="#CBD5E1", fontsize=7.5, fontweight="bold"),
        wedgeprops=dict(width=0.45, edgecolor="#1E293B", linewidth=2)
    )
    for aut in aut_d:
        aut.set_color("black")
        aut.set_fontweight("bold")
        aut.set_fontsize(7)
    ax_don.text(0, 0, "$1.25M\nSales", ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
    ax_don.set_title("Marketing Channel Share", fontsize=10, fontweight="bold", color="white", pad=8)

    fig.savefig(os.path.join(viz_dir, "task6_powerbi_capstone_dashboard.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
    ax.axis("off")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    def draw_box(x, y, w, h, title, cols, pk=""):
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=1",
                              edgecolor="#CBD5E1", facecolor="white", linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        hdr = FancyBboxPatch((x, y + h - 5), w, 5, boxstyle="round,pad=0.5,rounding_size=1",
                              edgecolor="none", facecolor=navy_dark, zorder=3)
        ax.add_patch(hdr)
        ax.text(x + w / 2, y + h - 2.5, title, ha="center", va="center", color="white", fontsize=9.5, fontweight="bold", zorder=4)

        curr_y = y + h - 8
        for col in cols:
            prefix = "[PK] " if col == pk else ("[FK] " if "ID" in col else "  -  ")
            ax.text(x + 2, curr_y, f"{prefix}{col}", ha="left", va="center", fontsize=7.5, color=header_gray, zorder=4)
            curr_y -= 3.2

    draw_box(37, 28, 26, 44, "FactTransactions (Fact)", [
        "TransactionID", "OrderDate", "CustomerID", "ProductID", "ChannelID",
        "SalesAmount", "CostAmount", "ProfitAmount", "DiscountAmount", "TaxAmount",
        "Quantity", "PaymentMethod", "DeliveryDays", "ReturnStatus"
    ], "TransactionID")

    draw_box(5, 55, 24, 32, "DimCustomer (1)", [
        "CustomerID", "CustomerName", "Segment", "LoyaltyTier", "City", "State", "Region", "AcquisitionDate"
    ], "CustomerID")

    draw_box(71, 55, 24, 28, "DimProduct (1)", [
        "ProductID", "ProductName", "Category", "SubCategory", "UnitPrice", "UnitCost"
    ], "ProductID")

    draw_box(5, 10, 24, 25, "DimMarketingChannel (1)", [
        "ChannelID", "ChannelName", "CampaignType", "AverageCAC"
    ], "ChannelID")

    draw_box(71, 10, 24, 32, "DimDate (1)", [
        "Date", "Year", "Quarter", "MonthNumber", "MonthName", "MonthYear", "Weekday", "IsWeekend"
    ], "Date")

    ax.annotate("", xy=(37, 60), xytext=(29, 65), arrowprops=dict(arrowstyle="->", color=accent_blue, lw=2))
    ax.text(32, 64, "1 : *", color=accent_blue, fontweight="bold", fontsize=9)

    ax.annotate("", xy=(63, 60), xytext=(71, 65), arrowprops=dict(arrowstyle="->", color=accent_blue, lw=2))
    ax.text(65, 64, "* : 1", color=accent_blue, fontweight="bold", fontsize=9)

    ax.annotate("", xy=(37, 40), xytext=(29, 25), arrowprops=dict(arrowstyle="->", color=accent_teal, lw=2))
    ax.text(32, 33, "1 : *", color=accent_teal, fontweight="bold", fontsize=9)

    ax.annotate("", xy=(63, 40), xytext=(71, 25), arrowprops=dict(arrowstyle="->", color=accent_teal, lw=2))
    ax.text(65, 33, "* : 1", color=accent_teal, fontweight="bold", fontsize=9)

    ax.text(50, 96, "Capstone Power BI Star Schema Data Model", ha="center", va="center", fontsize=15, fontweight="bold", color=navy_dark)
    ax.text(50, 92, "Central FactTransactions Table connected to Normalized Customer, Product, Channel & Calendar Dimensions", ha="center", va="center", fontsize=9, color=slate_text)

    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task6_powerbi_star_schema.png"), dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.axis("off")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)

    recs_boxes = [
        ("Rec 1: Loyalty Retention", "Target 'At Risk' ($172K sales)\nwith automated email workflows\nProjected: +$45K retention", accent_blue),
        ("Rec 2: Channel Reallocation", "Shift 25% ad spend from Paid Search\nto Organic & Email Newsletter\nProjected: +18% net ROAS", accent_teal),
        ("Rec 3: Furniture Upselling", "Bundle Seating & Desks\nwith high-margin accessories\nProjected: +$60K gross profit", accent_amber),
        ("Rec 4: Express Fulfillment", "Incentivize 1-2 day delivery\nDirect correlation to low returns\nProjected: -1.8% return rate", accent_rose)
    ]

    for idx, (title, desc, color) in enumerate(recs_boxes):
        x_c = 2 + idx * 24.5
        box = FancyBboxPatch((x_c, 8), 22.5, 32, boxstyle="round,pad=0.5,rounding_size=1",
                             edgecolor=color, facecolor="white", linewidth=1.8, zorder=2)
        ax.add_patch(box)
        hdr = FancyBboxPatch((x_c, 34), 22.5, 6, boxstyle="round,pad=0.5,rounding_size=1",
                              edgecolor="none", facecolor=color, zorder=3)
        ax.add_patch(hdr)
        ax.text(x_c + 11.25, 37, title, ha="center", va="center", color="white", fontsize=8.5, fontweight="bold", zorder=4)
        ax.text(x_c + 11.25, 20, desc, ha="center", va="center", color=header_gray, fontsize=7.5, zorder=4)

    ax.text(50, 46, "Strategic Business Decision & Impact Framework", ha="center", va="center", fontsize=13, fontweight="bold", color=navy_dark)
    plt.tight_layout()
    fig.savefig(os.path.join(viz_dir, "task7_business_recommendations_matrix.png"), dpi=300)
    plt.close(fig)

    print("All EDA charts, dashboard mockups, and diagrams generated successfully.")

if __name__ == "__main__":
    generate_eda_and_visuals()

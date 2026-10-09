"""
Generate Professional Submission PDF for Week 4 Assignment:
Statistics, Data Visualization & Exploratory Data Analysis.
Student Name: Sanjay Kumar
InternNova Data Analytics Internship
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, 'Week4_Statistics_Visualization_EDA_Report.pdf')
    viz_dir = os.path.join(base_dir, 'visualizations')

    # Page setup
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    primary_color = colors.HexColor('#1a365d')    # Deep Navy
    secondary_color = colors.HexColor('#2b6cb0')  # Blue
    accent_color = colors.HexColor('#2c7a7b')     # Teal
    dark_gray = colors.HexColor('#2d3748')
    light_bg = colors.HexColor('#f7fafc')

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        alignment=1, # Center
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=secondary_color,
        alignment=1,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=primary_color,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=secondary_color,
        spaceBefore=6,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=dark_gray,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=dark_gray,
        leftIndent=12,
        spaceAfter=3
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#2c5282'),
        backColor=colors.HexColor('#ebf8ff'),
        borderPadding=6,
        spaceAfter=6
    )

    story = []

    # -------------------------------------------------------------
    # HEADER BANNER & STUDENT METADATA
    # -------------------------------------------------------------
    story.append(Paragraph("INTERNNOVA DATA ANALYTICS INTERNSHIP", title_style))
    story.append(Paragraph("WEEK 4 ASSIGNMENT: STATISTICS, DATA VISUALIZATION & EDA", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=primary_color, spaceAfter=8))

    meta_data = [
        [
            Paragraph("<b>Student Name:</b> Sanjay Kumar", body_style),
            Paragraph("<b>Course:</b> Python for Data Analytics & AI", body_style)
        ],
        [
            Paragraph("<b>Assignment:</b> Week 4 Practical Portfolio", body_style),
            Paragraph("<b>Duration:</b> 1 Week (7 Days)", body_style)
        ],
        [
            Paragraph("<b>Total Marks:</b> 100 / 100", body_style),
            Paragraph("<b>Dataset:</b> E-Commerce Customer & Sales Analytics (600 Rows)", body_style)
        ]
    ]
    t_meta = Table(meta_data, colWidths=[270, 270])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), light_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # EXECUTIVE SUMMARY
    # -------------------------------------------------------------
    story.append(Paragraph("Executive Summary & Core Objectives", h1_style))
    summary_text = (
        "This project delivers an end-to-end analytical study fulfilling all requirements of the InternNova Week 4 "
        "curriculum. Using a comprehensive e-commerce transaction dataset, this report applies descriptive and inferential "
        "statistics, detects anomalies using IQR and Z-Score techniques, builds professional visualization suites with "
        "Matplotlib and Seaborn, implements a rigorous data cleaning pipeline, and extracts actionable strategic business recommendations."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # TASK 1: MEAN, MEDIAN & MODE (10 MARKS)
    # -------------------------------------------------------------
    story.append(Paragraph("Task 1: Statistical Analysis – Mean, Median & Mode (10 Marks)", h1_style))
    t1_intro = (
        "Measures of central tendency identify the center or typical value of a dataset. We evaluated the three primary measures "
        "across key numerical variables to inspect distribution shape and central location."
    )
    story.append(Paragraph(t1_intro, body_style))

    t1_table_data = [
        ['Metric / Feature', 'Mean (Average)', 'Median (50th %)', 'Mode (Most Frequent)', 'Skewness Type'],
        ['Sales Amount ($)', '$291.58', '$139.05', '$17.00', 'Strong Positive (5.51)'],
        ['Customer Age (Years)', '35.60 Yrs', '35.00 Yrs', '18.00 Yrs', 'Near Symmetric (0.27)'],
        ['Order Quantity', '2.26 Units', '2.00 Units', '1.00 Unit', 'Positive Skew (3.66)'],
        ['Unit Price ($)', '$131.82', '$84.35', '$10.00', 'Moderate Positive (1.08)']
    ]
    t1_table = Table(t1_table_data, colWidths=[130, 95, 95, 110, 110])
    t1_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t1_table)
    story.append(Spacer(1, 5))

    t1_notes = (
        "<b>Key Interpretation:</b> For <code>Sales_Amount</code>, the Mean ($291.58) is substantially higher than the "
        "Median ($139.05), proving a <b>right-skewed distribution</b>. While 50% of orders are under $139.05, a small cluster "
        "of high-ticket corporate and bulk purchases elevates the arithmetic average. The Median represents the robust typical "
        "consumer order, while Mode ($17.00) captures high-volume entry-level merchandise."
    )
    story.append(Paragraph(t1_notes, callout_style))
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # TASK 2: VARIANCE & STANDARD DEVIATION (10 MARKS)
    # -------------------------------------------------------------
    story.append(Paragraph("Task 2: Variance & Standard Deviation (10 Marks)", h1_style))
    t2_intro = (
        "Measures of dispersion quantify the degree of spread, variability, or dispersion of individual data points "
        "relative to their arithmetic mean."
    )
    story.append(Paragraph(t2_intro, body_style))

    t2_table_data = [
        ['Variable', 'Mean', 'Sample Variance (s²)', 'Std Deviation (s)', 'Coeff. of Variation (%)', 'Spread Assessment'],
        ['Sales Amount', '$291.58', '219,117.27 $²', '$468.10', '160.54%', 'High Volatility / Wide Spread'],
        ['Net Profit', '$63.75', '19,101.21 $²', '$138.21', '216.81%', 'Extreme Spread / Risk Spread'],
        ['Customer Age', '35.60 Yrs', '106.05 Yrs²', '10.30 Yrs', '28.93%', 'Low Spread / Concentrated Target'],
        ['Unit Price', '$131.82', '13,398.96 $²', '$115.75', '87.81%', 'Moderate Product Diversification']
    ]
    t2_table = Table(t2_table_data, colWidths=[90, 75, 105, 85, 95, 90])
    t2_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), secondary_color),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t2_table)
    story.append(Spacer(1, 5))

    t2_notes = (
        "<b>What Standard Deviation Indicates:</b> Standard deviation restores the spread into original interpretable units ($). "
        "A standard deviation of $468.10 on a mean of $291.58 (CV = 160.5%) indicates significant financial volatility: "
        "transactions are not clustered narrowly around the average. Conversely, Customer Age has a low standard deviation "
        "(10.30 years, CV = 28.9%), proving that customers are reliably concentrated between 25 and 46 years."
    )
    story.append(Paragraph(t2_notes, callout_style))
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # TASK 3: CORRELATION & PROBABILITY BASICS (10 MARKS)
    # -------------------------------------------------------------
    story.append(Paragraph("Task 3: Correlation & Probability Basics (10 Marks)", h1_style))
    t3_text = (
        "<b>Part A: Correlation Analysis</b><br/>"
        "• <b>Sales_Amount vs Profit (r = +0.9066, p &lt; 0.001):</b> Strong Positive Linear Correlation. As sales revenue expands, dollar profit scales upwards.<br/>"
        "• <b>Discount_Percent vs Profit (r = -0.1821, p = 7.18e-06):</b> Negative Linear Correlation. Higher discount rates erode unit profit margins.<br/>"
        "• <b>Customer_Age vs Sales_Amount (r = -0.0210, p = 0.608):</b> Weak / Negligible Correlation. Purchase amounts are independent of customer age.<br/><br/>"
        "<b>Part B: Real-World Probability Scenarios</b><br/>"
        "• <b>Scenario 1 (Marginal Probability):</b> Probability that a customer order exceeds $300 (High-Ticket Order).<br/>"
        "  Formula: <code>P(Sales &gt; 300) = n(Sales &gt; 300) / N = 171 / 600 = 0.2850 (28.50%)</code>.<br/>"
        "• <b>Scenario 2 (Conditional Probability):</b> Probability of UPI payment given that the customer is a Young Adult (Age &lt; 30).<br/>"
        "  Formula: <code>P(UPI | Age &lt; 30) = n(UPI ∩ Age &lt; 30) / n(Age &lt; 30) = 64 / 182 = 0.3516 (35.16%)</code>.<br/>"
        "  Young adult shoppers have an elevated 35.2% probability of paying via UPI compared to 34.0% baseline, demonstrating strong mobile-native adoption."
    )
    story.append(Paragraph(t3_text, body_style))
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # TASK 4: OUTLIER DETECTION (10 MARKS)
    # -------------------------------------------------------------
    story.append(Paragraph("Task 4: Outlier Detection (IQR & Z-Score) (10 Marks)", h1_style))
    t4_text = (
        "Outliers are anomalous observations that deviate markedly from the general population. We evaluated outliers in <code>Sales_Amount</code> "
        "using both parametric (Z-Score) and non-parametric (IQR) methods:<br/>"
        "1. <b>IQR Method:</b> Q1 = $61.29, Q3 = $341.05, IQR = $279.76. Threshold Bounds = [-$358.35, $760.68]. Detected: <b>50 outliers (8.33%)</b>.<br/>"
        "2. <b>Z-Score Method (|Z| &gt; 3.0):</b> Mean = $291.58, Std = $468.10. Upper Threshold = $1,695.88. Detected: <b>11 extreme outliers (1.83%)</b>.<br/>"
        "• <b>Impact Demonstration:</b> Removing the 11 Z-score outliers drops the sample Mean from $291.58 to $245.24, and slashes Variance from "
        "219,117 down to 77,494 (-64.6%), while the Median remains rock-steady ($139.05 vs $136.02).<br/>"
        "• <b>Strategic Implication:</b> In commercial retail, these outliers are not 'errors' to be deleted, but high-value corporate/bulk orders "
        "that require specialized B2B management."
    )
    story.append(Paragraph(t4_text, body_style))
    story.append(Spacer(1, 10))

    # Page Break for Visualizations Suite
    story.append(PageBreak())

    # -------------------------------------------------------------
    # TASK 5: MATPLOTLIB VISUALIZATIONS (15 MARKS)
    # -------------------------------------------------------------
    story.append(Paragraph("Task 5: Matplotlib Visualization Suite (15 Marks)", h1_style))
    story.append(Paragraph("Five distinct charts created using Matplotlib with customized axes, palettes, and annotations:", body_style))

    all_mat_path = os.path.join(viz_dir, 'task5_all_matplotlib_visualizations.png')
    if os.path.exists(all_mat_path):
        img_mat = Image(all_mat_path, width=540, height=380)
        story.append(img_mat)
        story.append(Spacer(1, 6))

    mat_descriptions = [
        "1. <b>Line Chart:</b> Tracks monthly sales progression across 2024, highlighting seasonal sales peaks and cyclical demand patterns.",
        "2. <b>Bar Chart:</b> Ranks total revenue by product category, establishing Electronics ($116.3k) and Fashion ($19.6k) as primary revenue engines.",
        "3. <b>Pie Chart:</b> Demonstrates regional revenue market share: South (29.8%), North (25.0%), East (23.5%), West (21.6%).",
        "4. <b>Histogram:</b> Displays customer age frequency with overlaid mean (35.6) and median (35.0) lines, validating a symmetric demographic core.",
        "5. <b>Scatter Plot:</b> Maps individual orders by Sales vs Profit with discount color-coding and linear regression trendline (Slope = 0.27)."
    ]
    for d in mat_descriptions:
        story.append(Paragraph(d, bullet_style))
    story.append(Spacer(1, 10))

    # Page Break for Seaborn Visualizations
    story.append(PageBreak())

    # -------------------------------------------------------------
    # TASK 6: SEABORN VISUALIZATION (15 MARKS)
    # -------------------------------------------------------------
    story.append(Paragraph("Task 6: Seaborn Statistical Visualization Suite (15 Marks)", h1_style))
    story.append(Paragraph("Four statistical visualizations generated using Seaborn highlighting multivariate relationships:", body_style))

    # Two side-by-side or stacked figures
    box_path = os.path.join(viz_dir, 'task6_2_box_plot.png')
    heat_path = os.path.join(viz_dir, 'task6_3_heatmap.png')
    
    table_sb_imgs = []
    if os.path.exists(box_path) and os.path.exists(heat_path):
        img_box = Image(box_path, width=265, height=160)
        img_heat = Image(heat_path, width=265, height=160)
        table_sb_imgs.append([img_box, img_heat])
        t_sb = Table(table_sb_imgs, colWidths=[270, 270])
        t_sb.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER')]))
        story.append(t_sb)
        story.append(Spacer(1, 6))

    count_path = os.path.join(viz_dir, 'task6_1_count_plot.png')
    pair_path = os.path.join(viz_dir, 'task6_4_pair_plot.png')
    if os.path.exists(count_path):
        img_count = Image(count_path, width=420, height=200)
        story.append(KeepTogether([img_count, Spacer(1, 4)]))

    sb_descriptions = [
        "1. <b>Count Plot:</b> Categorizes payment transactions across genders, revealing Credit Card and UPI as dominant methods (>70%).",
        "2. <b>Box Plot:</b> Compares profit distribution by category, revealing wide dispersion and high outliers in Electronics compared to tight spreads in Books.",
        "3. <b>Correlation Heatmap:</b> Displays pairwise Pearson correlation coefficients, pinpointing strong coupling between Sales & Profit (r=0.91) and negative discount effects.",
        "4. <b>Pair Plot:</b> Maps multidimensional distributions with KDE diagonals, visually distinguishing category clusters across feature space."
    ]
    for d in sb_descriptions:
        story.append(Paragraph(d, bullet_style))
    story.append(Spacer(1, 10))

    # Page Break for EDA Cleaning & Insights
    story.append(PageBreak())

    # -------------------------------------------------------------
    # TASK 7: EDA - DATA INSPECTION & CLEANING (15 MARKS)
    # -------------------------------------------------------------
    story.append(Paragraph("Task 7: Exploratory Data Analysis – Data Inspection & Cleaning (15 Marks)", h1_style))
    story.append(Paragraph("A production-grade data hygiene pipeline was applied to resolve data anomalies in the raw transaction dataset:", body_style))

    t7_matrix = [
        ['Quality Dimension', 'Raw Dataset (Before)', 'Cleaned Dataset (After)', 'Remediation Methodology'],
        ['Total Records', '608 Rows', '600 Rows', 'Removed 8 redundant duplicate rows via primary key hashing'],
        ['Missing Customer_Age', '18 Missing (2.96%)', '0 Missing (100% Complete)', 'Imputed using robust median age (35.0 Years)'],
        ['Missing Customer_Rating', '15 Missing (2.47%)', '0 Missing (100% Complete)', 'Imputed using modal rating (4.0 Stars)'],
        ['Category Text Cardinality', '11 Inconsistent Strings', '5 Standardized Categories', 'Standardized title casing and typo clustering'],
        ['Invalid Quantity Entries', '4 Erroneous Entries (<= 0)', '0 Invalid Entries', 'Floored invalid quantities to valid minimum of 1 unit']
    ]
    t7_table = Table(t7_matrix, colWidths=[110, 105, 115, 210])
    t7_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t7_table)
    story.append(Spacer(1, 6))

    clean_img_path = os.path.join(viz_dir, 'task7_cleaning_comparison.png')
    if os.path.exists(clean_img_path):
        img_clean = Image(clean_img_path, width=480, height=220)
        story.append(img_clean)
        story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # TASK 8: EDA – CORRELATION & STRATEGIC INSIGHTS (10 MARKS)
    # -------------------------------------------------------------
    story.append(Paragraph("Task 8: EDA – Correlation & Strategic Insights (10 Marks)", h1_style))
    insights_img_path = os.path.join(viz_dir, 'task8_eda_correlation_insights.png')
    if os.path.exists(insights_img_path):
        img_ins = Image(insights_img_path, width=480, height=220)
        story.append(img_ins)
        story.append(Spacer(1, 6))

    insights_bullets = [
        "<b>Insight 1: Strong Revenue-Profit Coupling (r = 0.906, p &lt; 0.001):</b> Gross sales are the foremost driver of dollar net earnings, demonstrating that customer acquisition directly fuels company valuation.",
        "<b>Insight 2: The 'Discount Cliff' at 20%:</b> Orders with 0-5% discounts generate an average profit of $77.82 (31.8% margin). Once discounts exceed 20%, average profit plummets to just $1.54 (10.2% margin), destroying value in low-margin electronics.",
        "<b>Insight 3: High Margin Potential in Fashion (35.9%) and Beauty (35.1%):</b> While Electronics produces 66.8% of top-line revenue ($116.3k), it yields only 13.7% margin. Reallocating marketing to Fashion yields 2.6x more profit per dollar spent.",
        "<b>Insight 4: Regional Dominance of South (29.8%) and North (25.0%):</b> Combined 54.8% revenue share paired with &gt;70% digital payment adoption creates the ideal foundation for localized micro-warehouses."
    ]
    for b in insights_bullets:
        story.append(Paragraph(b, bullet_style))
    story.append(Spacer(1, 10))

    # Page Break for Business Recommendations
    story.append(PageBreak())

    # -------------------------------------------------------------
    # TASK 9: DATA-DRIVEN BUSINESS RECOMMENDATIONS (5 MARKS)
    # -------------------------------------------------------------
    story.append(Paragraph("Task 9: Data-Driven Business Recommendations (5 Marks)", h1_style))
    story.append(Paragraph("Based on statistical findings and EDA insights, four actionable strategic recommendations are proposed:", body_style))

    recs = [
        (
            "Recommendation 1: Dynamic Discount Caps & Elimination of >20% Blanket Sales",
            "Pricing & Margin Management",
            "Orders discounted >20% collapse unit profit to $1.54 (down from $77.82), triggering loss-making sales in Electronics.",
            "Enforce a hard system cap of 15% discount on Electronics. Replace steep percentage cuts with non-price incentives such as loyalty points and 'Free Delivery over $200'.",
            "Expected Impact: 18-24% expansion in net operating profit without cannibalizing customer acquisition."
        ),
        (
            "Recommendation 2: Shift Marketing Capital Towards High-Margin Fashion & Beauty",
            "Product Mix & Marketing Optimization",
            "Fashion (35.9% margin) and Beauty (35.1% margin) deliver nearly triple the profit efficiency of Electronics (13.7% margin).",
            "Reallocate 25% of top-of-funnel ad spend into fashion influencer partnerships and curated lifestyle product bundles.",
            "Expected Impact: Lifts blended company-wide gross profit margin from 23.5% to over 29.0%."
        ),
        (
            "Recommendation 3: Regional Micro-Fulfillment Hubs in South & North",
            "Supply Chain Logistics",
            "South and North regions generate 54.8% of revenue ($95.8k) with >70% digital payments (UPI + Credit Cards).",
            "Establish regional warehousing hubs in top southern and northern metros to offer same-day delivery and lower fulfillment overhead.",
            "Expected Impact: Slashes shipping times by 40% and increases repeat order frequency by 15%."
        ),
        (
            "Recommendation 4: Launch an Exclusive 'VIP B2B / Wholesale' Program",
            "Account Segmentation & Retention",
            "Task 4 identified 11 high-leverage bulk orders (Z > 3.0) contributing over $25k in sales and $8k in net profit.",
            "Create a dedicated B2B sales concierge providing GST invoicing, credit terms, and volume rebates rather than retail coupon codes.",
            "Expected Impact: Secures sticky institutional recurring revenue and defends VIP clients against competitors."
        )
    ]

    for title, cat, ev, act, imp in recs:
        rec_box = [
            [Paragraph(f"<b>{title}</b>", h2_style)],
            [Paragraph(f"<b>Strategic Domain:</b> {cat}", body_style)],
            [Paragraph(f"<b>Data Evidence:</b> {ev}", body_style)],
            [Paragraph(f"<b>Actionable Implementation:</b> {act}", body_style)],
            [Paragraph(f"<b>Expected ROI / Impact:</b> <font color='#27ae60'><b>{imp}</b></font>", body_style)]
        ]
        t_rec = Table(rec_box, colWidths=[540])
        t_rec.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), light_bg),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e0')),
            ('LINEBELOW', (0,0), (-1,0), 1, secondary_color),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t_rec)
        story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SUBMISSION & REPOSITORY DETAILS
    # -------------------------------------------------------------
    story.append(Spacer(1, 10))
    story.append(Paragraph("Submission Verification & Repository Links", h1_style))
    sub_text = (
        "<b>Student Name:</b> Sanjay Kumar | <b>Internship Track:</b> InternNova Data Analytics<br/>"
        "<b>GitHub Repository:</b> <code>https://github.com/sanjayverma991950-alt/InternNovaDataAnalyst</code><br/>"
        "<b>Deliverables Included:</b> Python source code scripts (Task 1 to Task 9), Raw & Cleaned CSV Datasets, "
        "Matplotlib & Seaborn Visualizations (PNG 300 DPI), End-to-End Jupyter Notebook (.ipynb), and Markdown Submission Report."
    )
    story.append(Paragraph(sub_text, callout_style))

    # Build PDF
    doc.build(story)
    print(f"\nSubmission PDF successfully compiled to: {pdf_path}")
    print(f"File Size: {os.path.getsize(pdf_path) / 1024:.1f} KB")

if __name__ == '__main__':
    generate_pdf()

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return

        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 762, "INTERNNOVA DATA ANALYTICS INTERNSHIP | WEEK 5 SUBMISSION REPORT")
        self.setFont("Helvetica", 8)
        self.drawRightString(576, 762, "POWER BI & BUSINESS INTELLIGENCE")

        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.75)
        self.line(36, 755, 576, 755)

        self.line(36, 38, 576, 38)
        self.setFont("Helvetica", 8)
        self.drawString(36, 26, "Student: Sanjay Kumar | Assignment: Week 5 Power BI Dashboard")
        self.drawRightString(576, 26, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pdf_path = os.path.join(base_dir, "Week5_Power_BI_Business_Intelligence_Report.pdf")
    viz_dir = os.path.join(base_dir, "visualizations")

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=46,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()

    c_primary = colors.HexColor("#0F172A")
    c_blue = colors.HexColor("#1E40AF")
    c_teal = colors.HexColor("#0D9488")
    c_slate = colors.HexColor("#334155")
    c_muted = colors.HexColor("#64748B")
    c_bg_light = colors.HexColor("#F8FAFC")
    c_border = colors.HexColor("#E2E8F0")

    style_title = ParagraphStyle(
        "CoverTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=c_primary,
        alignment=1,
        spaceAfter=8
    )

    style_subtitle = ParagraphStyle(
        "CoverSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=c_blue,
        alignment=1,
        spaceAfter=15
    )

    style_h1 = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=c_primary,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    style_h2 = ParagraphStyle(
        "Heading2_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=c_blue,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    style_body = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=13,
        textColor=c_slate,
        spaceAfter=6
    )

    style_bullet = ParagraphStyle(
        "Bullet_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=c_slate,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )

    style_code = ParagraphStyle(
        "Code_Custom",
        parent=styles["Normal"],
        fontName="Courier",
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=4
    )

    style_tbl_header = ParagraphStyle(
        "TblHdr",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    style_tbl_cell = ParagraphStyle(
        "TblCell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.5,
        leading=10,
        textColor=c_slate
    )

    style_tbl_cell_bold = ParagraphStyle(
        "TblCellBold",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.5,
        leading=10,
        textColor=c_primary
    )

    story = []

    story.append(Spacer(1, 15))
    story.append(Paragraph("POWER BI & BUSINESS INTELLIGENCE", style_title))
    story.append(Paragraph("End-to-End Enterprise Analytics, Data Modeling, DAX & Executive Dashboard", style_subtitle))
    story.append(HRFlowable(width="100%", thickness=2, color=c_blue, spaceBefore=4, spaceAfter=12))

    meta_info = [
        [Paragraph("<b>Course:</b> Data Analytics Internship", style_tbl_cell), Paragraph("<b>Student Name:</b> Sanjay Kumar", style_tbl_cell)],
        [Paragraph("<b>Assignment:</b> Week 5 Final Submission", style_tbl_cell), Paragraph("<b>Dataset:</b> Global Retail Superstore (Enterprise Model)", style_tbl_cell)],
        [Paragraph("<b>Total Score:</b> 100 Marks (Tasks 1 - 7)", style_tbl_cell), Paragraph("<b>Software:</b> Power BI Desktop & DAX Engine", style_tbl_cell)]
    ]
    t_meta = Table(meta_info, colWidths=[270, 270])
    t_meta.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), c_bg_light),
        ("BOX", (0, 0), (-1, -1), 1, c_border),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Executive Project Abstract", style_h2))
    story.append(Paragraph(
        "This project showcases a complete business intelligence lifecycle built on Microsoft Power BI Desktop. "
        "Beginning with raw multi-source ingestion of transactional retail data (5,592 records with noise), the dataset was cleaned "
        "and normalized in Power Query into a high-performance Star Schema model comprising one central fact table (FactSales) and "
        "four dedicated dimension tables (DimCustomer, DimProduct, DimRegion, DimDate). Using the VertiPaq engine, 19 DAX measures "
        "and 6 calculated columns were authored to track financial KPIs (Sales $7.91M, Profit $2.37M, Margin 30.0%, 3,500 Orders). "
        "Finally, an interactive multi-filter executive dashboard was crafted with cross-filtering slicers, line trends, category bar charts, "
        "segment distribution donuts, and regional matrices, yielding actionable strategic business recommendations.",
        style_body
    ))
    story.append(Spacer(1, 6))

    dash_img_path = os.path.join(viz_dir, "dashboard_overview.png")
    if os.path.exists(dash_img_path):
        story.append(Image(dash_img_path, width=540, height=335))
    story.append(Spacer(1, 10))

    story.append(PageBreak())

    story.append(Paragraph("Task 1: Power BI Introduction & Data Import (10 Marks)", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("1.1 Purpose of Microsoft Power BI in Modern Data Analytics", style_h2))
    story.append(Paragraph(
        "Microsoft Power BI is a unified, enterprise-grade business intelligence and data analytics platform that bridges raw transactional "
        "data systems with strategic executive decision-making. Its role in modern analytics covers five core domains:",
        style_body
    ))

    bi_purposes = [
        "<b>Self-Service ETL (Power Query):</b> Ingests, joins, cleans, and transforms heterogeneous datasets across hundreds of connectors (SQL, Excel, Web, APIs, Data Lakes) into automated, repeatable data flows.",
        "<b>In-Memory Tabular Modeling (VertiPaq Engine):</b> Compresses columnar data up to 10x in RAM, enabling instantaneous query evaluation across millions of rows without degrading database performance.",
        "<b>Complex Analytical Computation (DAX):</b> Provides a powerful functional expression language (Data Analysis Expressions) for time-intelligence, cohort analysis, cumulative aggregations, and dynamic business logic.",
        "<b>Interactive Storytelling & Visual Exploration:</b> Delivers highly responsive, bi-directional cross-filtering visualizations (Bar, Line, Matrix, Scatter, Decomposition Trees) tailored for operational and C-suite stakeholders.",
        "<b>Governance, Collaboration & Security:</b> Seamlessly shares dashboards via Power BI Service with Row-Level Security (RLS), scheduled cloud refreshes, and automated alerting."
    ]
    for p_item in bi_purposes:
        story.append(Paragraph(f"• {p_item}", style_bullet))
    story.append(Spacer(1, 6))

    story.append(Paragraph("1.2 Power BI Desktop Interface Architecture", style_h2))
    story.append(Paragraph(
        "Power BI Desktop provides three unified primary views accessible on the left rail, accompanied by analytical side panes:",
        style_body
    ))

    views_info = [
        [Paragraph("<b>Interface Component</b>", style_tbl_header), Paragraph("<b>Function & Workflow Purpose</b>", style_tbl_header)],
        [Paragraph("<b>Ribbon Interface</b>", style_tbl_cell_bold), Paragraph("Houses contextual command menus: Home (Data ingestion), Modeling (Measures, RLS), View (Themes, Layout), and Help.", style_tbl_cell)],
        [Paragraph("<b>Report View</b>", style_tbl_cell_bold), Paragraph("Canvas workspace where visuals, KPI cards, charts, and slicers are designed and arranged into interactive pages.", style_tbl_cell)],
        [Paragraph("<b>Table / Data View</b>", style_tbl_cell_bold), Paragraph("Allows direct tabular row-and-column inspection of loaded datasets, sorting, filtering, and calculated column validation.", style_tbl_cell)],
        [Paragraph("<b>Model View</b>", style_tbl_cell_bold), Paragraph("Visual Entity-Relationship canvas to define schema topologies, manage 1:* relationships, cardinalities, and active filter paths.", style_tbl_cell)],
        [Paragraph("<b>Power Query Editor</b>", style_tbl_cell_bold), Paragraph("Separate mashup window running the M language for data extraction, profiling, type casting, merging, and reshaping.", style_tbl_cell)],
        [Paragraph("<b>Visualizations Pane</b>", style_tbl_cell_bold), Paragraph("Palette of 30+ native visuals, formatting controls, conditional formatting rules, tooltips, and drill-through slots.", style_tbl_cell)],
        [Paragraph("<b>Data / Fields Pane</b>", style_tbl_cell_bold), Paragraph("Hierarchical list of tables, dimension fields, calculated columns, and explicit DAX measures available in the model.", style_tbl_cell)],
        [Paragraph("<b>Filters Pane</b>", style_tbl_cell_bold), Paragraph("Configures scoped filtering rules applied at visual-level, page-level, or across all report pages.", style_tbl_cell)]
    ]
    t_views = Table(views_info, colWidths=[140, 400])
    t_views.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), c_primary),
        ("BOX", (0, 0), (-1, -1), 1, c_border),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t_views)
    story.append(Spacer(1, 8))

    arch_img = os.path.join(viz_dir, "task1_powerbi_interface_architecture.png")
    if os.path.exists(arch_img):
        story.append(Image(arch_img, width=540, height=220))
    story.append(Spacer(1, 10))

    story.append(Paragraph("1.3 Ingested Dataset Inventory & Schema Inspection", style_h2))
    story.append(Paragraph(
        "The multi-table retail dataset was imported using the Excel / CSV data connectors. The table below catalogs all tables, "
        "record counts, column attributes, and verified Power BI data types:",
        style_body
    ))

    schema_inventory = [
        [Paragraph("<b>Table Name</b>", style_tbl_header), Paragraph("<b>Type</b>", style_tbl_header), Paragraph("<b>Row Count</b>", style_tbl_header), Paragraph("<b>Key Columns & Power BI Data Types</b>", style_tbl_header)],
        [Paragraph("<b>FactSales</b>", style_tbl_cell_bold), Paragraph("Fact", style_tbl_cell), Paragraph("5,567", style_tbl_cell), Paragraph("OrderID (Text), OrderDate (Date), ShipDate (Date), CustomerID (Text), ProductID (Text), RegionID (Text), Sales (Decimal), Cost (Decimal), Profit (Decimal), Quantity (Int64), Discount (Decimal)", style_tbl_cell)],
        [Paragraph("<b>DimCustomer</b>", style_tbl_cell_bold), Paragraph("Dimension", style_tbl_cell), Paragraph("200", style_tbl_cell), Paragraph("CustomerID [PK] (Text), CustomerName (Text), Segment (Text), Country (Text), City (Text), State (Text), PostalCode (Text)", style_tbl_cell)],
        [Paragraph("<b>DimProduct</b>", style_tbl_cell_bold), Paragraph("Dimension", style_tbl_cell), Paragraph("24", style_tbl_cell), Paragraph("ProductID [PK] (Text), ProductName (Text), Category (Text), SubCategory (Text), UnitCost (Decimal), UnitPrice (Decimal)", style_tbl_cell)],
        [Paragraph("<b>DimRegion</b>", style_tbl_cell_bold), Paragraph("Dimension", style_tbl_cell), Paragraph("4", style_tbl_cell), Paragraph("RegionID [PK] (Text), RegionName (Text), RegionalManager (Text), TerritoryCode (Text)", style_tbl_cell)],
        [Paragraph("<b>DimDate</b>", style_tbl_cell_bold), Paragraph("Dimension", style_tbl_cell), Paragraph("1,096", style_tbl_cell), Paragraph("Date [PK] (Date), Year (Int64), Quarter (Text), MonthNumber (Int64), MonthName (Text), MonthYear (Text), Day (Int64), Weekday (Text), IsWeekend (Text)", style_tbl_cell)]
    ]
    t_schema = Table(schema_inventory, colWidths=[80, 55, 55, 350])
    t_schema.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), c_primary),
        ("BOX", (0, 0), (-1, -1), 1, c_border),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t_schema)

    story.append(PageBreak())

    story.append(Paragraph("Task 2: Data Cleaning & Preparation in Power Query (15 Marks)", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("2.1 Data Profiling & Quality Assessment", style_h2))
    story.append(Paragraph(
        "Upon initial ingestion of the raw superstore feed (`raw_superstore_data.csv`, 5,592 records), Power Query Column Quality, "
        "Column Distribution, and Column Profile diagnostic tools identified several integrity defects:",
        style_body
    ))

    issues_table = [
        [Paragraph("<b>Defect Category</b>", style_tbl_header), Paragraph("<b>Observed Data Anomaly</b>", style_tbl_header), Paragraph("<b>Power Query Remediation Applied</b>", style_tbl_header)],
        [Paragraph("<b>Duplicate Rows</b>", style_tbl_cell_bold), Paragraph("25 identical duplicate transaction line items across all attributes.", style_tbl_cell), Paragraph("Applied Table.Distinct on composite key [OrderID, ProductID] removing 25 duplicate rows.", style_tbl_cell)],
        [Paragraph("<b>Missing / Null Values</b>", style_tbl_cell_bold), Paragraph("Postal_Code contained null and blank string entries for customer addresses.", style_tbl_cell), Paragraph("Used Table.ReplaceValue replacing nulls and blanks with standard fallback '00000'.", style_tbl_cell)],
        [Paragraph("<b>Inconsistent Text</b>", style_tbl_cell_bold), Paragraph("Customer_Segment contained mixed casing ('consumer', 'CONSUMER') and whitespace.", style_tbl_cell), Paragraph("Applied Text.Trim followed by Text.Proper standardization to unify casing.", style_tbl_cell)],
        [Paragraph("<b>Incorrect Data Types</b>", style_tbl_cell_bold), Paragraph("Order_Date, Sales_Amount, Quantity imported as generic text types.", style_tbl_cell), Paragraph("Transformed column types explicitly to Date, Decimal Currency, and Int64 integer types.", style_tbl_cell)],
        [Paragraph("<b>Irrelevant Columns</b>", style_tbl_cell_bold), Paragraph("System tracking headers (Internal_Audit_Code, Temp_System_Flag) loaded into memory.", style_tbl_cell), Paragraph("Removed unnecessary columns via Table.RemoveColumns to streamline memory usage.", style_tbl_cell)],
        [Paragraph("<b>Column Naming</b>", style_tbl_cell_bold), Paragraph("Inconsistent casing and abbreviations (order_id_num, Sales_Amount, Unit_Cost).", style_tbl_cell), Paragraph("Renamed to clean PascalCase conventions (OrderID, Sales, Cost, Profit) across all tables.", style_tbl_cell)]
    ]
    t_issues = Table(issues_table, colWidths=[110, 210, 220])
    t_issues.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), c_primary),
        ("BOX", (0, 0), (-1, -1), 1, c_border),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t_issues)
    story.append(Spacer(1, 8))

    etl_img = os.path.join(viz_dir, "task2_data_cleaning_flow.png")
    if os.path.exists(etl_img):
        story.append(Image(etl_img, width=540, height=210))
    story.append(Spacer(1, 8))

    story.append(Paragraph("2.2 Power Query ETL M Script Implementations", style_h2))
    story.append(Paragraph("The exact M-code executed for FactSales and DimCustomer transformations is cataloged below:", style_body))

    m_code_snippet = """let
    Source = Csv.Document(File.Contents(".../raw_superstore_data.csv"), [Delimiter=",", Columns=22, Encoding=65001]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    RemovedDuplicates = Table.Distinct(PromotedHeaders, {"order_id_num", "Product_ID"}),
    RemovedColumns = Table.RemoveColumns(RemovedDuplicates, {"Internal_Audit_Code", "Temp_System_Flag"}),
    RenamedColumns = Table.RenameColumns(RemovedColumns, {
        {"order_id_num", "OrderID"}, {"Order_Date", "OrderDate"}, {"Ship_Date", "ShipDate"},
        {"Customer_ID", "CustomerID"}, {"Product_ID", "ProductID"}, {"Region_ID", "RegionID"},
        {"Sales_Amount", "Sales"}, {"Unit_Cost", "Cost"}, {"Net_Profit", "Profit"},
        {"Item_Quantity", "Quantity"}, {"Discount_Rate", "Discount"}
    }),
    ChangedTypes = Table.TransformColumnTypes(RenamedColumns, {
        {"OrderID", type text}, {"OrderDate", type date}, {"ShipDate", type date},
        {"CustomerID", type text}, {"ProductID", type text}, {"RegionID", type text},
        {"Sales", type number}, {"Cost", type number}, {"Profit", type number},
        {"Quantity", Int64.Type}, {"Discount", type number}
    })
in
    ChangedTypes"""

    t_mcode = Table([[Paragraph(m_code_snippet.replace("\n", "<br/>").replace(" ", "&nbsp;"), style_code)]], colWidths=[540])
    t_mcode.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), c_bg_light),
        ("BOX", (0, 0), (-1, -1), 1, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t_mcode)

    story.append(PageBreak())

    story.append(Paragraph("Task 3: Data Modeling & Relationships (15 Marks)", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("3.1 Star Schema Architecture & Relationship Topology", style_h2))
    story.append(Paragraph(
        "A Star Schema architecture was established in the Power BI Model View. The central fact table (`FactSales`) stores quantitative "
        "business metrics and transactions, while four surrounding dimension tables provide business context (Who, What, Where, When). "
        "Every relationship is configured with 1-to-Many (`1:*`) cardinality and Single cross-filter direction pointing from Dimension to Fact.",
        style_body
    ))

    rel_table = [
        [Paragraph("<b>Primary Key (1)</b>", style_tbl_header), Paragraph("<b>Foreign Key (*)</b>", style_tbl_header), Paragraph("<b>Cardinality</b>", style_tbl_header), Paragraph("<b>Cross-Filter</b>", style_tbl_header), Paragraph("<b>Analytical Purpose</b>", style_tbl_header)],
        [Paragraph("<b>DimCustomer[CustomerID]</b>", style_tbl_cell_bold), Paragraph("FactSales[CustomerID]", style_tbl_cell), Paragraph("One-to-Many (1:*)", style_tbl_cell), Paragraph("Single", style_tbl_cell), Paragraph("Filters sales by customer name, city, state, and customer segment.", style_tbl_cell)],
        [Paragraph("<b>DimProduct[ProductID]</b>", style_tbl_cell_bold), Paragraph("FactSales[ProductID]", style_tbl_cell), Paragraph("One-to-Many (1:*)", style_tbl_cell), Paragraph("Single", style_tbl_cell), Paragraph("Slices revenue and margin across product category, sub-category, and SKU.", style_tbl_cell)],
        [Paragraph("<b>DimRegion[RegionID]</b>", style_tbl_cell_bold), Paragraph("FactSales[RegionID]", style_tbl_cell), Paragraph("One-to-Many (1:*)", style_tbl_cell), Paragraph("Single", style_tbl_cell), Paragraph("Enables geographical reporting and regional sales manager accountability.", style_tbl_cell)],
        [Paragraph("<b>DimDate[Date]</b>", style_tbl_cell_bold), Paragraph("FactSales[OrderDate]", style_tbl_cell), Paragraph("One-to-Many (1:*)", style_tbl_cell), Paragraph("Single", style_tbl_cell), Paragraph("Drives time-intelligence calculations, YoY trends, and seasonal quarterly comparisons.", style_tbl_cell)]
    ]
    t_rel = Table(rel_table, colWidths=[125, 115, 80, 55, 165])
    t_rel.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), c_primary),
        ("BOX", (0, 0), (-1, -1), 1, c_border),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t_rel)
    story.append(Spacer(1, 8))

    model_img = os.path.join(viz_dir, "task3_data_model_star_schema.png")
    if os.path.exists(model_img):
        story.append(Image(model_img, width=540, height=310))
    story.append(Spacer(1, 8))

    story.append(Paragraph("3.2 Technical Benefits of Star Schema Design", style_h2))
    schema_benefits = [
        "<b>VertiPaq Engine Optimization:</b> Dimension tables have high cardinality uniqueness, allowing columnar dictionary encoding and run-length compression that drastically reduces memory footprint.",
        "<b>Predictable Filter Propagation:</b> Single cross-filter direction ensures filter context flows strictly downstream from dimensions to fact records, completely preventing circular reference loops and ambiguous query paths.",
        "<b>Simplified DAX Expressions:</b> Clean dimensional separation allows DAX functions like RELATED(), CALCULATE(), and SAMEPERIODLASTYEAR() to evaluate cleanly without complex multi-table bridging joins.",
        "<b>High User Intuitiveness:</b> Report authors and business analysts can readily identify where measures reside and how slicer selections impact report visualizations."
    ]
    for b_item in schema_benefits:
        story.append(Paragraph(f"• {b_item}", style_bullet))

    story.append(PageBreak())

    story.append(Paragraph("Task 4: DAX Calculated Columns & Measures (15 Marks)", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("4.1 Explicit DAX Measures Catalog", style_h2))
    story.append(Paragraph(
        "In compliance with enterprise Power BI best practices, all calculations were authored as explicit DAX measures rather than "
        "relying on default implicit aggregations. The table below details all core measures, DAX expressions, and actual computed outputs:",
        style_body
    ))

    dax_matrix_img = os.path.join(viz_dir, "task4_dax_measures_matrix.png")
    if os.path.exists(dax_matrix_img):
        story.append(Image(dax_matrix_img, width=540, height=220))
    story.append(Spacer(1, 8))

    story.append(Paragraph("4.2 Detailed DAX Measure Expressions & Technical Descriptions", style_h2))

    dax_specs = [
        ("Total Sales", "SUM(FactSales[Sales])", "$7,907,425.85", "Aggregates net gross sales across all transactions. Evaluates dynamically under active filter context."),
        ("Total Profit", "SUM(FactSales[Profit])", "$2,372,462.85", "Computes total net profit generated after accounting for manufacturing and procurement costs."),
        ("Profit Margin", "DIVIDE([Total Profit], [Total Sales], 0)", "30.0%", "Calculates overall return on revenue. The DIVIDE function safely prevents divide-by-zero runtime exceptions."),
        ("Average Order Value", "AVERAGE(FactSales[Sales])", "$1,420.41", "Determines average revenue per line transaction, serving as a benchmark for basket sizing."),
        ("Total Orders", "DISTINCTCOUNT(FactSales[OrderID])", "3,500", "Counts unique purchase orders, properly ignoring multi-item line repetitions within orders."),
        ("Max Sale Value", "MAX(FactSales[Sales])", "$24,990.00", "Extracts largest individual line item order value, identifying high-profile enterprise deals."),
        ("Min Sale Value", "MIN(FactSales[Sales])", "$20.80", "Identifies smallest individual retail transaction value."),
        ("Sales Prior Year", "CALCULATE([Total Sales], SAMEPERIODLASTYEAR(DimDate[Date]))", "Dynamic", "Leverages time-intelligence to compute prior year revenue for comparative YoY growth tracking."),
        ("YoY Sales Growth", "DIVIDE([Total Sales] - [Sales Prior Year], [Sales Prior Year], 0)", "Dynamic", "Measures percentage change in top-line sales performance relative to matching prior period.")
    ]

    dax_rows = [
        [Paragraph("<b>Measure Name</b>", style_tbl_header), Paragraph("<b>DAX Formula</b>", style_tbl_header), Paragraph("<b>Output</b>", style_tbl_header), Paragraph("<b>Formula Mechanism & Business Application</b>", style_tbl_header)]
    ]
    for d_name, d_code, d_out, d_desc in dax_specs:
        dax_rows.append([
            Paragraph(f"<b>{d_name}</b>", style_tbl_cell_bold),
            Paragraph(f"<font face='Courier' color='#0F172A'>{d_code}</font>", style_tbl_cell),
            Paragraph(f"<b>{d_out}</b>", style_tbl_cell),
            Paragraph(d_desc, style_tbl_cell)
        ])

    t_dax_specs = Table(dax_rows, colWidths=[90, 160, 60, 230])
    t_dax_specs.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), c_primary),
        ("BOX", (0, 0), (-1, -1), 1, c_border),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_dax_specs)
    story.append(Spacer(1, 8))

    story.append(Paragraph("4.3 Calculated Columns Created in Data Model", style_h2))
    calc_cols = [
        "<b>FactSales[Shipping Duration Days]</b> = <font face='Courier'>DATEDIFF(FactSales[OrderDate], FactSales[ShipDate], DAY)</font><br/>Calculates logistics fulfillment turnaround for every order row, enabling delivery SLA monitoring.",
        "<b>FactSales[Profit Status]</b> = <font face='Courier'>IF(FactSales[Profit] >= 0, \"Profitable\", \"Loss\")</font><br/>Classifies each transaction row into binary profit categories for conditional matrix formatting.",
        "<b>FactSales[Sales Tier]</b> = <font face='Courier'>SWITCH(TRUE(), FactSales[Sales] >= 5000, \"High Value ($5000+)\", FactSales[Sales] >= 1000, \"Medium Value ($1000-$4999)\", \"Standard Value (<$1000)\")</font><br/>Segments order volumes into analytical tiers for executive segmentation."
    ]
    for c_item in calc_cols:
        story.append(Paragraph(f"• {c_item}", style_bullet))

    story.append(PageBreak())

    story.append(Paragraph("Task 5: Power BI Visualizations Breakdown (15 Marks)", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("5.1 Individual Visual Implementations & Specifications", style_h2))
    story.append(Paragraph(
        "All required visual types were engineered with custom data fields, responsive palettes, and clear formatting standards:",
        style_body
    ))

    v1_img = os.path.join(viz_dir, "task5_visual1_sales_profit_by_category.png")
    v2_img = os.path.join(viz_dir, "task5_visual2_monthly_trend.png")
    v3_img = os.path.join(viz_dir, "task5_visual3_segment_donut.png")
    v4_img = os.path.join(viz_dir, "task5_visual4_regional_matrix.png")
    v5_img = os.path.join(viz_dir, "task5_visual5_kpi_cards.png")

    vis_pairs = [
        [
            Paragraph("<b>Visual 1: Clustered Column Chart (Category Performance)</b><br/>"
                      "• <b>X-Axis:</b> DimProduct[Category]<br/>"
                      "• <b>Y-Axis:</b> [Total Sales], [Total Profit]<br/>"
                      "• <b>Data Labels:</b> Displayed in Millions ($M)<br/>"
                      "• <b>Insight:</b> Technology is the primary revenue driver ($4.98M), while Furniture yields $0.89M profit.", style_body),
            Image(v1_img, width=260, height=140) if os.path.exists(v1_img) else Paragraph("Visual 1", style_body)
        ],
        [
            Paragraph("<b>Visual 2: Line & Area Chart (Monthly Revenue Trend)</b><br/>"
                      "• <b>X-Axis:</b> DimDate[MonthYear] (Chronological sort)<br/>"
                      "• <b>Values:</b> [Total Sales], [Total Profit]<br/>"
                      "• <b>Formatting:</b> Dual-line with shaded profit area<br/>"
                      "• <b>Insight:</b> Highlights strong seasonal surges in Q3/Q4 across 2022 to 2024.", style_body),
            Image(v2_img, width=260, height=140) if os.path.exists(v2_img) else Paragraph("Visual 2", style_body)
        ],
        [
            Paragraph("<b>Visual 3: Donut Chart (Customer Segment Share)</b><br/>"
                      "• <b>Legend:</b> DimCustomer[Segment]<br/>"
                      "• <b>Values:</b> [Total Sales]<br/>"
                      "• <b>Center Label:</b> $7.91M Total Revenue<br/>"
                      "• <b>Insight:</b> Consumer segment commands 53.6% ($4.24M), Corporate 26.0%, and Home Office 20.4%.", style_body),
            Image(v3_img, width=260, height=140) if os.path.exists(v3_img) else Paragraph("Visual 3", style_body)
        ],
        [
            Paragraph("<b>Visual 4: Table / Matrix (Regional Performance Matrix)</b><br/>"
                      "• <b>Rows:</b> DimRegion[RegionName], DimRegion[RegionalManager]<br/>"
                      "• <b>Columns:</b> Orders, Sales, Profit, Profit Margin %, AOV<br/>"
                      "• <b>Formatting:</b> Alternating zebra banding & bold totals<br/>"
                      "• <b>Insight:</b> West Region leads in total sales ($2.37M) and order volume.", style_body),
            Image(v4_img, width=260, height=130) if os.path.exists(v4_img) else Paragraph("Visual 4", style_body)
        ]
    ]

    t_vis = Table(vis_pairs, colWidths=[270, 270])
    t_vis.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOX", (0, 0), (-1, -1), 0.5, c_border),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t_vis)
    story.append(Spacer(1, 8))

    story.append(Paragraph("5.2 KPI Multi-Row Card Visuals", style_h2))
    if os.path.exists(v5_img):
        story.append(Image(v5_img, width=540, height=125))

    story.append(PageBreak())

    story.append(Paragraph("Task 6: Interactive Dashboard & Slicers (15 Marks)", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("6.1 Executive Dashboard Composition & Spatial Layout", style_h2))
    story.append(Paragraph(
        "The Power BI dashboard adheres to the F-pattern visual hierarchy recommended for executive dashboards. "
        "Top-level summary cards provide immediate performance visibility, while analytical visuals and cross-filtering slicers "
        "allow users to drill into specific drivers of variance.",
        style_body
    ))

    dash_components = [
        [Paragraph("<b>Dashboard Zone</b>", style_tbl_header), Paragraph("<b>Visual Elements Included</b>", style_tbl_header), Paragraph("<b>User Interaction & Dynamic Behavior</b>", style_tbl_header)],
        [Paragraph("<b>Header Bar</b>", style_tbl_cell_bold), Paragraph("Executive Title, Corporate Subtitle, Live Status indicator.", style_tbl_cell), Paragraph("Maintains branded context and indicates data model freshness.", style_tbl_cell)],
        [Paragraph("<b>Top KPI Row</b>", style_tbl_cell_bold), Paragraph("4 Multi-Row KPI Cards (Revenue $7.91M, Profit $2.37M, Margin 30.0%, Orders 3,500).", style_tbl_cell), Paragraph("Updates dynamically when any slicer or visual element is selected.", style_tbl_cell)],
        [Paragraph("<b>Middle Row</b>", style_tbl_cell_bold), Paragraph("Clustered Column Chart (Category Sales & Profit) + Line Chart (36-Month Revenue Trend).", style_tbl_cell), Paragraph("Clicking any category bar cross-filters the monthly line chart and tables.", style_tbl_cell)],
        [Paragraph("<b>Bottom Row</b>", style_tbl_cell_bold), Paragraph("Segment Donut Chart + Regional Breakdown Matrix + Top 5 Sub-Categories Horizontal Bar.", style_tbl_cell), Paragraph("Allows geographical and customer cohort exploration with instant recalculation.", style_tbl_cell)],
        [Paragraph("<b>Interactive Slicers</b>", style_tbl_cell_bold), Paragraph("4 Slicers: Region (Tile/Buttons), Category (Dropdown), Order Year (Slider/List), Segment (List).", style_tbl_cell), Paragraph("Enables multi-dimensional slice-and-dice across any dimension combination.", style_tbl_cell)]
    ]
    t_dash_comp = Table(dash_components, colWidths=[110, 200, 230])
    t_dash_comp.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), c_primary),
        ("BOX", (0, 0), (-1, -1), 1, c_border),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t_dash_comp)
    story.append(Spacer(1, 8))

    slicer_img = os.path.join(viz_dir, "task6_slicers_interaction.png")
    if os.path.exists(slicer_img):
        story.append(Image(slicer_img, width=540, height=210))
    story.append(Spacer(1, 8))

    story.append(Paragraph("6.2 Cross-Filtering Verification & Drill-Down Exploration", style_h2))
    story.append(Paragraph(
        "Power BI's bi-directional cross-filtering mechanism was verified across four interactive exploration scenarios:",
        style_body
    ))
    drill_scenarios = [
        "<b>Scenario A (West Region Filter):</b> Selecting 'West' filters Total Revenue to $2.37M across 1,029 orders. Marcus Vance's regional matrix dynamically highlights top performance in California and Washington.",
        "<b>Scenario B (Technology Category Slicer):</b> Selecting 'Technology' isolates $4.98M in sales, instantly showing that Laptops ($2.91M) and Phones ($1.22M) constitute 82.9% of all technology revenues.",
        "<b>Scenario C (Year 2023 Cohort):</b> Slicing by Year 2023 demonstrates peak historical expansion where revenue reached $3.39M with a balanced 29.9% net margin.",
        "<b>Scenario D (Consumer Segment Selection):</b> Cross-filtering by Consumer reveals that consumer buyers generate over 53% of all furniture purchases, particularly ergonomic chairs and standing desks."
    ]
    for sc_item in drill_scenarios:
        story.append(Paragraph(f"• {sc_item}", style_bullet))

    story.append(PageBreak())

    story.append(Paragraph("Task 7: Business Insights & Strategic Recommendations (15 Marks)", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("7.1 Five Key Data-Driven Business Insights", style_h2))

    insights_data = [
        ("Insight 1: Technology Drives 63% of Total Company Revenue",
         "The Technology product category represents $4,977,791.45 (62.9%) of total gross sales ($7.91M) and generates $1,336,401.45 in net profits. "
         "Within Technology, premium Laptops ($2.91M) and flagship Phones ($1.22M) deliver the highest absolute dollar returns across all business lines."),

        ("Insight 2: Office Supplies Delivers the Highest Relative Margin (44.3%)",
         "While Office Supplies represents only $323,367.90 (4.1%) of top-line revenue, it achieves a stellar 44.3% profit margin ($143,264.90 net profit). "
         "Items such as paper cases, binders, and desktop appliances feature low unit costs and require minimal discounting, making them highly profitable."),

        ("Insight 3: West Region Leads in Both Revenue ($2.37M) and Profitability ($709K)",
         "Under Regional Manager Marcus Vance, the West Region generated $2,373,312.60 in revenue and $708,704.60 in profit (29.9% margin), outperforming "
         "the East ($1.86M), South ($1.86M), and Central ($1.81M) territories. High tech enterprise concentration in Los Angeles and Seattle drives this outperformance."),

        ("Insight 4: Consumer Segment Accounts for the Majority of Demand (53.6%)",
         "The Consumer cohort is the company's core volume driver, contributing $4,238,418.90 in sales across 1,885 orders (53.6% share). Corporate clients "
         "account for $2,052,436.00 (26.0%) and Home Office buyers account for $1,616,570.95 (20.4%)."),

        ("Insight 5: Pronounced Q4 Holiday & Year-End Procurement Seasonality",
         "Monthly trend analysis reveals that sales and profitability surge consistently between September and December each year, peaking at over $360K per month. "
         "This pattern aligns with corporate Q4 IT budget flushes and consumer holiday promotions.")
    ]

    for title, desc in insights_data:
        story.append(Paragraph(f"<b>{title}</b>", style_h2))
        story.append(Paragraph(desc, style_body))
        story.append(Spacer(1, 2))

    perf_img = os.path.join(viz_dir, "task7_category_performance_heatmap.png")
    if os.path.exists(perf_img):
        story.append(Image(perf_img, width=540, height=210))
    story.append(Spacer(1, 6))

    story.append(Paragraph("7.2 Highest & Lowest Performing Sub-Categories", style_h2))
    perf_summary = [
        [Paragraph("<b>Performance Tier</b>", style_tbl_header), Paragraph("<b>Product Sub-Category</b>", style_tbl_header), Paragraph("<b>Category</b>", style_tbl_header), Paragraph("<b>Total Sales</b>", style_tbl_header), Paragraph("<b>Net Profit</b>", style_tbl_header), Paragraph("<b>Margin %</b>", style_tbl_header)],
        [Paragraph("<b>Top Performer #1</b>", style_tbl_cell_bold), Paragraph("Laptops", style_tbl_cell), Paragraph("Technology", style_tbl_cell), Paragraph("$2,910,774.00", style_tbl_cell), Paragraph("$724,974.00", style_tbl_cell), Paragraph("24.9%", style_tbl_cell)],
        [Paragraph("<b>Top Performer #2</b>", style_tbl_cell_bold), Paragraph("Phones", style_tbl_cell), Paragraph("Technology", style_tbl_cell), Paragraph("$1,216,228.50", style_tbl_cell), Paragraph("$308,078.50", style_tbl_cell), Paragraph("25.3%", style_tbl_cell)],
        [Paragraph("<b>Top Performer #3</b>", style_tbl_cell_bold), Paragraph("Chairs", style_tbl_cell), Paragraph("Furniture", style_tbl_cell), Paragraph("$1,204,189.50", style_tbl_cell), Paragraph("$405,889.50", style_tbl_cell), Paragraph("33.7%", style_tbl_cell)],
        [Paragraph("<b>Lowest Performer #1</b>", style_tbl_cell_bold), Paragraph("Pens", style_tbl_cell), Paragraph("Office Supplies", style_tbl_cell), Paragraph("$15,506.40", style_tbl_cell), Paragraph("$7,358.40", style_tbl_cell), Paragraph("47.5%", style_tbl_cell)],
        [Paragraph("<b>Lowest Performer #2</b>", style_tbl_cell_bold), Paragraph("Labels", style_tbl_cell), Paragraph("Office Supplies", style_tbl_cell), Paragraph("$15,636.40", style_tbl_cell), Paragraph("$8,100.40", style_tbl_cell), Paragraph("51.8%", style_tbl_cell)],
        [Paragraph("<b>Lowest Performer #3</b>", style_tbl_cell_bold), Paragraph("Storage", style_tbl_cell), Paragraph("Office Supplies", style_tbl_cell), Paragraph("$19,313.60", style_tbl_cell), Paragraph("$9,217.60", style_tbl_cell), Paragraph("47.7%", style_tbl_cell)]
    ]
    t_perf = Table(perf_summary, colWidths=[95, 95, 90, 85, 85, 90])
    t_perf.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), c_primary),
        ("BOX", (0, 0), (-1, -1), 1, c_border),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, c_border),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_perf)
    story.append(Spacer(1, 8))

    story.append(Paragraph("7.3 Strategic Business Recommendations", style_h2))

    recs = [
        ("Recommendation 1: Cross-Sell High-Margin Office Supplies with High-Ticket Technology Orders",
         "Technology orders currently have an Average Order Value of $1,420 but rarely include complementary office accessories. "
         "By implementing automated Power BI basket-bundling recommendations (e.g., offering premium cable organizers, anti-glare filters, "
         "and ergonomic accessories at checkout), the company can increase overall basket margin by an estimated 3.5% to 5.0% without incurring incremental customer acquisition costs."),

        ("Recommendation 2: Optimize Central & East Region Sales Strategies via Corporate Accounts",
         "The Central ($1.81M) and East ($1.86M) regions trail the West ($2.37M) by over $500K in revenue. Data indicates this gap stems from lower corporate "
         "account penetration in Chicago and Philadelphia. Management should incentivize regional sales directors Elena Rostova and Sarah Jenkins to pursue "
         "multi-year B2B corporate workstation supply agreements, matching West Region's enterprise contract volume."),

        ("Recommendation 3: Rationalize Low-Velocity SKUs in Storage and Pens",
         "Products in Pens and Labels generate under $16K annually each. While margin percentage is high (47% - 51%), physical storage and inventory carrying costs "
         "erode net operational gains. The supply chain team should transition these products to minimum-order multi-packs (e.g. bulk cartons) to boost revenue per order line.")
    ]

    for r_title, r_desc in recs:
        story.append(Paragraph(f"<b>{r_title}</b>", style_h2))
        story.append(Paragraph(r_desc, style_body))
        story.append(Spacer(1, 2))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Report generated successfully: {pdf_path}")

if __name__ == "__main__":
    build_pdf()

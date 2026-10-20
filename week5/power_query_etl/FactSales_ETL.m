let
    Source = Csv.Document(File.Contents("C:\Users\sanjay\OneDrive\Pictures\OneDrive\Desktop\InternNovaDataAnalyst\week5\data\raw_superstore_data.csv"), [Delimiter=",", Columns=22, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    RemovedDuplicates = Table.Distinct(PromotedHeaders, {"order_id_num", "Product_ID"}),
    RemovedColumns = Table.RemoveColumns(RemovedDuplicates, {"Internal_Audit_Code", "Temp_System_Flag"}),
    RenamedColumns = Table.RenameColumns(RemovedColumns, {
        {"order_id_num", "OrderID"},
        {"Order_Date", "OrderDate"},
        {"Ship_Date", "ShipDate"},
        {"Customer_ID", "CustomerID"},
        {"Product_ID", "ProductID"},
        {"Region_ID", "RegionID"},
        {"Sales_Amount", "Sales"},
        {"Unit_Cost", "Cost"},
        {"Net_Profit", "Profit"},
        {"Item_Quantity", "Quantity"},
        {"Discount_Rate", "Discount"}
    }),
    SelectedFactColumns = Table.SelectColumns(RenamedColumns, {
        "OrderID", "OrderDate", "ShipDate", "CustomerID", "ProductID", "RegionID", "Sales", "Cost", "Profit", "Quantity", "Discount"
    }),
    ChangedTypes = Table.TransformColumnTypes(SelectedFactColumns, {
        {"OrderID", type text},
        {"OrderDate", type date},
        {"ShipDate", type date},
        {"CustomerID", type text},
        {"ProductID", type text},
        {"RegionID", type text},
        {"Sales", type number},
        {"Cost", type number},
        {"Profit", type number},
        {"Quantity", Int64.Type},
        {"Discount", type number}
    })
in
    ChangedTypes

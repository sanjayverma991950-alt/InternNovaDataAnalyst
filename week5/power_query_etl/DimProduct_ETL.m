let
    Source = Csv.Document(File.Contents("C:\Users\sanjay\OneDrive\Pictures\OneDrive\Desktop\InternNovaDataAnalyst\week5\data\raw_superstore_data.csv"), [Delimiter=",", Columns=22, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    SelectedColumns = Table.SelectColumns(PromotedHeaders, {"Product_ID", "Product_Name", "Product_Category", "Sub_Category", "Sales_Amount", "Item_Quantity", "Discount_Rate", "Unit_Cost"}),
    RemovedDuplicates = Table.Distinct(SelectedColumns, {"Product_ID"}),
    TrimmedCategory = Table.TransformColumns(RemovedDuplicates, {{"Product_Category", Text.Trim, type text}}),
    ChangedTypesInitial = Table.TransformColumnTypes(TrimmedCategory, {
        {"Sales_Amount", type number},
        {"Item_Quantity", Int64.Type},
        {"Discount_Rate", type number},
        {"Unit_Cost", type number}
    }),
    AddedUnitPrice = Table.AddColumn(ChangedTypesInitial, "UnitPrice", each Number.Round([Sales_Amount] / ([Item_Quantity] * (1 - [Discount_Rate])), 2), type number),
    AddedUnitCost = Table.AddColumn(AddedUnitPrice, "UnitCost", each Number.Round([Unit_Cost] / [Item_Quantity], 2), type number),
    RemovedCalcTempCols = Table.RemoveColumns(AddedUnitCost, {"Sales_Amount", "Item_Quantity", "Discount_Rate", "Unit_Cost"}),
    RenamedColumns = Table.RenameColumns(RemovedCalcTempCols, {
        {"Product_ID", "ProductID"},
        {"Product_Name", "ProductName"},
        {"Product_Category", "Category"},
        {"Sub_Category", "SubCategory"}
    }),
    ChangedTypesFinal = Table.TransformColumnTypes(RenamedColumns, {
        {"ProductID", type text},
        {"ProductName", type text},
        {"Category", type text},
        {"SubCategory", type text},
        {"UnitCost", type number},
        {"UnitPrice", type number}
    })
in
    ChangedTypesFinal

let
    Source = Csv.Document(File.Contents("C:\Users\sanjay\OneDrive\Pictures\OneDrive\Desktop\InternNovaDataAnalyst\week6\data\raw_ecommerce_customer_data.csv"), [Delimiter=",", Columns=25, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    SelectedProductCols = Table.SelectColumns(PromotedHeaders, {
        "product_identifier", "product_title", "category_name", "subcategory_name", "order_product_cost", "item_units"
    }),
    RemovedDuplicates = Table.Distinct(SelectedProductCols, {"product_identifier"}),
    ChangedInitTypes = Table.TransformColumnTypes(RemovedDuplicates, {
        {"order_product_cost", type number},
        {"item_units", Int64.Type}
    }),
    AddedUnitCost = Table.AddColumn(ChangedInitTypes, "UnitCost", each Number.Round([order_product_cost] / [item_units], 2), type number),
    RemovedTempCols = Table.RemoveColumns(AddedUnitCost, {"order_product_cost", "item_units"}),
    RenamedColumns = Table.RenameColumns(RemovedTempCols, {
        {"product_identifier", "ProductID"},
        {"product_title", "ProductName"},
        {"category_name", "Category"},
        {"subcategory_name", "SubCategory"}
    }),
    ChangedFinalTypes = Table.TransformColumnTypes(RenamedColumns, {
        {"ProductID", type text},
        {"ProductName", type text},
        {"Category", type text},
        {"SubCategory", type text},
        {"UnitCost", type number}
    })
in
    ChangedFinalTypes

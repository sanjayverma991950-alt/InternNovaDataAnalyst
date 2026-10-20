let
    Source = Csv.Document(File.Contents("C:\Users\sanjay\OneDrive\Pictures\OneDrive\Desktop\InternNovaDataAnalyst\week6\data\raw_ecommerce_customer_data.csv"), [Delimiter=",", Columns=25, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    SelectedCustomerCols = Table.SelectColumns(PromotedHeaders, {
        "customer_identifier", "customer_name", "customer_segment", "customer_city", "customer_state", "customer_region"
    }),
    RemovedDuplicates = Table.Distinct(SelectedCustomerCols, {"customer_identifier"}),
    RenamedColumns = Table.RenameColumns(RemovedDuplicates, {
        {"customer_identifier", "CustomerID"},
        {"customer_name", "CustomerName"},
        {"customer_segment", "Segment"},
        {"customer_city", "City"},
        {"customer_state", "State"},
        {"customer_region", "Region"}
    }),
    ChangedTypes = Table.TransformColumnTypes(RenamedColumns, {
        {"CustomerID", type text},
        {"CustomerName", type text},
        {"Segment", type text},
        {"City", type text},
        {"State", type text},
        {"Region", type text}
    })
in
    ChangedTypes

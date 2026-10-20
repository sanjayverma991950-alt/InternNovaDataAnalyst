let
    Source = Csv.Document(File.Contents("C:\Users\sanjay\OneDrive\Pictures\OneDrive\Desktop\InternNovaDataAnalyst\week5\data\raw_superstore_data.csv"), [Delimiter=",", Columns=22, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    SelectedColumns = Table.SelectColumns(PromotedHeaders, {"Customer_ID", "Customer_Name", "Customer_Segment", "Postal_Code", "City", "State"}),
    RemovedDuplicates = Table.Distinct(SelectedColumns, {"Customer_ID"}),
    TrimmedSegment = Table.TransformColumns(RemovedDuplicates, {{"Customer_Segment", Text.Trim, type text}}),
    CapitalizedSegment = Table.TransformColumns(TrimmedSegment, {{"Customer_Segment", Text.Proper, type text}}),
    ReplacedNullPostal = Table.ReplaceValue(CapitalizedSegment, null, "00000", Replacer.ReplaceValue, {"Postal_Code"}),
    ReplacedEmptyPostal = Table.ReplaceValue(ReplacedNullPostal, "", "00000", Replacer.ReplaceValue, {"Postal_Code"}),
    AddedCountry = Table.AddColumn(ReplacedEmptyPostal, "Country", each "United States", type text),
    RenamedColumns = Table.RenameColumns(AddedCountry, {
        {"Customer_ID", "CustomerID"},
        {"Customer_Name", "CustomerName"},
        {"Customer_Segment", "Segment"},
        {"Postal_Code", "PostalCode"}
    }),
    ReorderedColumns = Table.ReorderColumns(RenamedColumns, {"CustomerID", "CustomerName", "Segment", "Country", "City", "State", "PostalCode"}),
    ChangedTypes = Table.TransformColumnTypes(ReorderedColumns, {
        {"CustomerID", type text},
        {"CustomerName", type text},
        {"Segment", type text},
        {"Country", type text},
        {"City", type text},
        {"State", type text},
        {"PostalCode", type text}
    })
in
    ChangedTypes

let
    Source = Csv.Document(File.Contents("C:\Users\sanjay\OneDrive\Pictures\OneDrive\Desktop\InternNovaDataAnalyst\week5\data\raw_superstore_data.csv"), [Delimiter=",", Columns=22, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    SelectedColumns = Table.SelectColumns(PromotedHeaders, {"Region_ID", "Region_Name"}),
    RemovedDuplicates = Table.Distinct(SelectedColumns, {"Region_ID"}),
    RenamedColumns = Table.RenameColumns(RemovedDuplicates, {
        {"Region_ID", "RegionID"},
        {"Region_Name", "RegionName"}
    }),
    AddedManager = Table.AddColumn(RenamedColumns, "RegionalManager", each 
        if [RegionName] = "East" then "Sarah Jenkins"
        else if [RegionName] = "West" then "Marcus Vance"
        else if [RegionName] = "Central" then "Elena Rostova"
        else "David Kim", type text),
    AddedTerritory = Table.AddColumn(AddedManager, "TerritoryCode", each 
        if [RegionName] = "East" then "US-E"
        else if [RegionName] = "West" then "US-W"
        else if [RegionName] = "Central" then "US-C"
        else "US-S", type text),
    ChangedTypes = Table.TransformColumnTypes(AddedTerritory, {
        {"RegionID", type text},
        {"RegionName", type text},
        {"RegionalManager", type text},
        {"TerritoryCode", type text}
    })
in
    ChangedTypes

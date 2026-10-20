let
    Source = Csv.Document(File.Contents("C:\Users\sanjay\OneDrive\Pictures\OneDrive\Desktop\InternNovaDataAnalyst\week6\data\raw_ecommerce_customer_data.csv"), [Delimiter=",", Columns=25, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    SelectedChannelCols = Table.SelectColumns(PromotedHeaders, {"marketing_channel"}),
    RemovedDuplicates = Table.Distinct(SelectedChannelCols, {"marketing_channel"}),
    RenamedColumns = Table.RenameColumns(RemovedDuplicates, {{"marketing_channel", "ChannelName"}}),
    AddedChannelID = Table.AddIndexColumn(RenamedColumns, "Index", 1, 1, Int64.Type),
    FormattedChannelID = Table.AddColumn(AddedChannelID, "ChannelID", each "CH-" & Text.PadStart(Text.From([Index]), 2, "0"), type text),
    RemovedIndex = Table.RemoveColumns(FormattedChannelID, {"Index"}),
    ReorderedColumns = Table.ReorderColumns(RemovedIndex, {"ChannelID", "ChannelName"}),
    ChangedTypes = Table.TransformColumnTypes(ReorderedColumns, {
        {"ChannelID", type text},
        {"ChannelName", type text}
    })
in
    ChangedTypes

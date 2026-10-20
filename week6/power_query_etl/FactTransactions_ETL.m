let
    Source = Csv.Document(File.Contents("C:\Users\sanjay\OneDrive\Pictures\OneDrive\Desktop\InternNovaDataAnalyst\week6\data\raw_ecommerce_customer_data.csv"), [Delimiter=",", Columns=25, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    RemovedDuplicates = Table.Distinct(PromotedHeaders, {"raw_txn_id"}),
    RemovedSystemCols = Table.RemoveColumns(RemovedDuplicates, {"_audit_log_hash", "_temp_session_flag"}),
    TrimmedPayment = Table.TransformColumns(RemovedSystemCols, {{"payment_type", Text.Trim, type text}}),
    ProperPayment = Table.TransformColumns(TrimmedPayment, {{"payment_type", Text.Proper, type text}}),
    RenamedColumns = Table.RenameColumns(ProperPayment, {
        {"raw_txn_id", "TransactionID"},
        {"transaction_date", "OrderDate"},
        {"customer_identifier", "CustomerID"},
        {"product_identifier", "ProductID"},
        {"order_sales_gross", "SalesAmount"},
        {"order_product_cost", "CostAmount"},
        {"order_profit_net", "ProfitAmount"},
        {"order_discount_amt", "DiscountAmount"},
        {"order_tax_amt", "TaxAmount"},
        {"item_units", "Quantity"},
        {"payment_type", "PaymentMethod"},
        {"fulfillment_days", "DeliveryDays"},
        {"return_flag", "ReturnStatus"}
    }),
    SelectedFactColumns = Table.SelectColumns(RenamedColumns, {
        "TransactionID", "OrderDate", "CustomerID", "ProductID", "SalesAmount",
        "CostAmount", "ProfitAmount", "DiscountAmount", "TaxAmount", "Quantity",
        "PaymentMethod", "DeliveryDays", "ReturnStatus"
    }),
    ChangedTypes = Table.TransformColumnTypes(SelectedFactColumns, {
        {"TransactionID", type text},
        {"OrderDate", type date},
        {"CustomerID", type text},
        {"ProductID", type text},
        {"SalesAmount", type number},
        {"CostAmount", type number},
        {"ProfitAmount", type number},
        {"DiscountAmount", type number},
        {"TaxAmount", type number},
        {"Quantity", Int64.Type},
        {"PaymentMethod", type text},
        {"DeliveryDays", Int64.Type},
        {"ReturnStatus", type text}
    })
in
    ChangedTypes

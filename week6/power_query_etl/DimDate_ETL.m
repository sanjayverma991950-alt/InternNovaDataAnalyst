let
    StartDate = #date(2023, 1, 1),
    EndDate = #date(2024, 12, 31),
    TotalDays = Duration.Days(EndDate - StartDate) + 1,
    DatesList = List.Dates(StartDate, TotalDays, #duration(1, 0, 0, 0)),
    TableConverted = Table.FromList(DatesList, Splitter.SplitByNothing(), {"Date"}, null, ExtraValues.Error),
    DateTypeCast = Table.TransformColumnTypes(TableConverted, {{"Date", type date}}),
    AddedYear = Table.AddColumn(DateTypeCast, "Year", each Date.Year([Date]), Int64.Type),
    AddedQuarter = Table.AddColumn(AddedYear, "Quarter", each "Q" & Text.From(Date.QuarterOfYear([Date])), type text),
    AddedMonthNumber = Table.AddColumn(AddedQuarter, "MonthNumber", each Date.Month([Date]), Int64.Type),
    AddedMonthName = Table.AddColumn(AddedMonthNumber, "MonthName", each Date.MonthName([Date]), type text),
    AddedMonthYear = Table.AddColumn(AddedMonthName, "MonthYear", each Date.ToText([Date], "MMM yyyy"), type text),
    AddedWeekday = Table.AddColumn(AddedMonthYear, "Weekday", each Date.DayOfWeekName([Date]), type text),
    AddedIsWeekend = Table.AddColumn(AddedWeekday, "IsWeekend", each if Date.DayOfWeek([Date], Day.Monday) >= 5 then "Yes" else "No", type text)
in
    AddedIsWeekend

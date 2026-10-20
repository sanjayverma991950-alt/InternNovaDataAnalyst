let
    StartDate = #date(2022, 1, 1),
    EndDate = #date(2024, 12, 31),
    DayCount = Duration.Days(EndDate - StartDate) + 1,
    DateList = List.Dates(StartDate, DayCount, #duration(1, 0, 0, 0)),
    ConvertedToTable = Table.FromList(DateList, Splitter.SplitByNothing(), {"Date"}, null, ExtraValues.Error),
    ChangedDateType = Table.TransformColumnTypes(ConvertedToTable, {{"Date", type date}}),
    AddedYear = Table.AddColumn(ChangedDateType, "Year", each Date.Year([Date]), Int64.Type),
    AddedQuarter = Table.AddColumn(AddedYear, "Quarter", each "Q" & Text.From(Date.QuarterOfYear([Date])), type text),
    AddedMonthNumber = Table.AddColumn(AddedQuarter, "MonthNumber", each Date.Month([Date]), Int64.Type),
    AddedMonthName = Table.AddColumn(AddedMonthNumber, "MonthName", each Date.MonthName([Date]), type text),
    AddedMonthYear = Table.AddColumn(AddedMonthName, "MonthYear", each Date.ToText([Date], "MMM yyyy"), type text),
    AddedDay = Table.AddColumn(AddedMonthYear, "Day", each Date.Day([Date]), Int64.Type),
    AddedWeekday = Table.AddColumn(AddedDay, "Weekday", each Date.DayOfWeekName([Date]), type text),
    AddedIsWeekend = Table.AddColumn(AddedWeekday, "IsWeekend", each if Date.DayOfWeek([Date], Day.Monday) >= 5 then "Yes" else "No", type text)
in
    AddedIsWeekend

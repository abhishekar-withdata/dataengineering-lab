def validate_nulls(df, column):
    return df.filter(df[column].isNull()).count() == 0


def validate_duplicates(df, column):
    return df.groupBy(column).count().filter("count > 1").count() == 0

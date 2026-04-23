def check_nulls(df, column):
    return df.filter(df[column].isNull()).count()

def check_duplicates(df, column):
    return df.groupBy(column).count().filter("count > 1").count()
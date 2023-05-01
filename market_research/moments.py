"""Statistical moments of return DataFrames."""
import functools
from typing import Any, List, Optional, Union

from pyspark.sql import DataFrame, functions as F


def simple_to_log_returns(sDF: DataFrame, col: str) -> DataFrame:
    """Convert simple returns into log returns."""
    return sDF.withColumn(col, F.log10(F.col(col) + F.lit(1.0)))


def log_to_simple_returns(sDF: DataFrame, col: str) -> DataFrame:
    """Convert log returns into simple returns."""
    return sDF.withColumn(col, (F.lit(10.0) ** F.col(col)) - F.lit(1.0))


def transform_columns(sDF: DataFrame, col: List[str], func: Any) -> DataFrame:
    """Transform multiple specified columns."""
    if isinstance(col, str):
        return func(sDF, col)

    return functools.reduce(lambda spark_df, c: func(spark_df, c), col, sDF)


def transform_all_columns(
    sDF: DataFrame, func: Any,
    exclude_columns: Optional[Union[List[str], str]] = None
) -> DataFrame:
    """Transforms all columns, with optional excluded."""
    all_columns: List[str] = sDF.columns

    if exclude_columns is not None:
        if isinstance(exclude_columns, List):
            [all_columns.remove(col) for col in exclude_columns]
        elif isinstance(exclude_columns, str):
            all_columns.remove(exclude_columns)

    return functools.reduce(
        lambda spark_df, c: func(spark_df, c), all_columns, sDF
    )

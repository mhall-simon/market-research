from pyspark.sql import SparkSession


def test_spark(spark_context):
    spark: SparkSession = SparkSession.builder.master("local[1]").getOrCreate()
    spark_context.parallelize([1, 2, 3, 4])
    spark.read.csv("tests/test_files/dummy.csv")

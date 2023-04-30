def test_spark(spark_context):
    test_rdd = spark_context.parallelize([1,2,3,4])
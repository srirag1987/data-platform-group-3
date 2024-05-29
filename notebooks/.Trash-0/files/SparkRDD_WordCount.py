from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("demo").getOrCreate()

text_file = spark.sparkContext.textFile("demo.txt")

counts = (
    text_file.flatMap(lambda line: line.split(" "))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)

counts.collect()
print(counts.collect())
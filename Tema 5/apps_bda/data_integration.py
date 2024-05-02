from pyspark.sql import SparkSession
import pymongo

aws_access_key_id = 'test'
aws_secret_access_key = 'test'

try:
    spark = SparkSession.builder \
    .appName("SPARK S3") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://tema5-localstack-1:4566") \
    .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id) \
    .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key) \
    .config("spark.sql.shuffle.partitions", "4") \
    .config("spark.jars.packages","org.apache.spark:spark-hadoop-cloud_2.13:3.5.1,software.amazon.awssdk:s3:2.25.11") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.driver.extraClassPath", "/opt/spark/jars/s3-2.25.11.jar") \
    .config("spark.executor.extraClassPath", "/opt/spark/jars/s3-2.25.11.jar") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

    
    dfBattleRecord = spark.read.text("/opt/spark-data/text/battle_records.txt")
    
    dfBattleRecord \
    .write \
    .option('fs.s3a.committer.name', 'partitioned') \
    .option('fs.s3a.committer.staging.conflict-mode', 'replace') \
    .option("fs.s3a.fast.upload.buffer", "bytebuffer")\
    .mode('overwrite') \
    .text(path='s3a://new-sample-bucket/battleRecords')
    
    dfJson = spark.read.option("multiline","true").json("/opt/spark-data/json/pokemon_data.json")
    dfJson \
    .write \
    .option('fs.s3a.committer.name', 'partitioned') \
    .option('fs.s3a.committer.staging.conflict-mode', 'replace') \
    .option("fs.s3a.fast.upload.buffer", "bytebuffer")\
    .mode('overwrite') \
    .json(path='s3a://new-sample-bucket/pokemonData')
    
    
    
    mongo_client = pymongo.MongoClient("mongodb://tema5-mongo-1:27017/")
    db = mongo_client["pokemon_events_db"]  

    events_collection = db["events_collection"]

    dataEvents=events_collection.find({},{'_id': False})

    dfMongo=spark.createDataFrame(dataEvents)
    
    dfMongo \
    .write \
    .option('fs.s3a.committer.name', 'partitioned') \
    .option('fs.s3a.committer.staging.conflict-mode', 'replace') \
    .option("fs.s3a.fast.upload.buffer", "bytebuffer")\
    .mode('overwrite') \
    .json(path='s3a://new-sample-bucket/eventsData')
    
    spark.stop()
    
except Exception as e:
    print(e)
    
    

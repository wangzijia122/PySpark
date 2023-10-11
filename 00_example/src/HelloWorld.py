import os
from pyspark import SparkContext, SparkConf

os.environ["HADOOP_CONF_DIR"] = '/usr/local/lib/hadoop/etc/hadoop'
if __name__ == '__main__':
    conf = SparkConf().setAppName("hello_spark_on_k8s")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("INFO")
    rdd = sc.parallelize(["hello spark on k8s"])
    print(rdd.collect())
    sc.stop()


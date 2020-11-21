# SF Crime Statistics with Spark Streaming

**1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?**

When we change the settings, it impacts the value of 
"processedRowsPerSecond", so it means we can process more or less data in each batch and we need to avoid accumulating lag.

In our case since we are sending only one event per second in the Kafka producer (very low throughput), it does not have much impact.


**2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?**

I chose those settings and I was able to get a very good value for processedRowsPerSecond.

- maxOffsetsPerTrigger = 20000  (not to be limited too much by Kafka throughput especially for the first batches when we process the historical data)
- spark.default.parallelism = 8
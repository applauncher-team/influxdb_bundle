# Installing
```
pip install influxdb_bundle
```

# Configuring
In config/config.yml just provide the influxdb server parameters
```
influxdb:
  url: {INFLUXDB_URL}
  org: {INFLUXDB_ORG}
  token: {INFLUXDB_TOKEN}
```

# Using
Just inject the InfluxDBClient and use it!

```python
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import inject

client = inject.instance(InfluxDBClient)
client.buckets_api()
write_api = client.write_api(write_options=SYNCHRONOUS)
write_api.write(
    bucket="my-bucket",
    record=[Point("price").tag("product", product.name).field("price", product.price)]
)

```


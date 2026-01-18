## Question 3:
```sql
SELECT COUNT(*) AS trip_count
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
```

## Question 4:
```sql
SELECT z."Zone" AS pickup_zone,
       SUM(t.total_amount) AS total_revenue
FROM green_taxi_trips t
JOIN taxi_zone_lookup z
  ON t."PULocationID" = z."LocationID"
WHERE t.lpep_pickup_datetime >= '2025-11-18'
  AND t.lpep_pickup_datetime < '2025-11-19'
GROUP BY z."Zone"
ORDER BY total_revenue DESC
LIMIT 1;
```

## Question 5:
```sql
SELECT z_do."Zone" AS dropoff_zone,
       MAX(t.tip_amount) AS largest_tip
FROM green_taxi_trips t
JOIN taxi_zone_lookup z_pu
  ON t."PULocationID" = z_pu."LocationID"
JOIN taxi_zone_lookup z_do
  ON t."DOLocationID" = z_do."LocationID"
WHERE z_pu."Zone" = 'East Harlem North'
  AND t.lpep_pickup_datetime >= '2025-11-01'
  AND t.lpep_pickup_datetime < '2025-12-01'
GROUP BY z_do."Zone"
ORDER BY largest_tip DESC
LIMIT 1;
```


## Ingestion script

Tables:
- green_taxi_trips
- yellow_taxi_trips
- taxi_zone_lookup


```bash
$ docker run -it \
      --network=pg_default \
      taxi_ingest:v001 \
      --pg-user=root \
      --pg-pass=root \
      --pg-host=pgdatabase \
      --pg-port=5432 \
      --pg-db=ny_taxi \
      --target-table=green_taxi_trips
```

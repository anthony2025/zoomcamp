## Question 3:
```sql
SELECT COUNT(*) AS trip_count
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
```

## Ingestion script
```bash
$ docker run -it \
      --network=pg_default \
      taxi_ingest:v001 \
      --pg-user=root \
      --pg-pass=root \
      --pg-host=pgdatabase \
      --pg-port=5432 \
      --pg-db=ny_taxi \
      --target-table=green_taxi_trips \
      --year=2025 \
      --month=11 \
      --chunksize=100000
```

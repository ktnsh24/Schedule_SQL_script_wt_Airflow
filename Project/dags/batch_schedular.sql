USE users_app_data;
DROP TABLE IF EXISTS batch_data_staging;
CREATE TABLE batch_data_staging
    AS SELECT *
        FROM users_details
        WHERE download_date = '{{ prev_ds }}';

INSERT INTO batch_data (event_id,download_date,user_id,app,category,rating,reviews,app_size,installs,app_type,price,content_rating,genres,
            last_updated,current_version,android_version, app_id,user_details)
SELECT event_id,download_date,user_id,app,category,rating,reviews,app_size,installs,app_type,price,content_rating,genres,
       last_updated,current_version,android_version, app_id,user_details
FROM batch_data_staging;

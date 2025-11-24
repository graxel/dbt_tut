{{ config(materialized='view') }}

SELECT
    *
FROM
    {{source('source', 'fact_sales')}} -- dbt_tutorial_dev.source.fact_sales
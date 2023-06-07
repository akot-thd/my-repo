# This file is used for creating development tables and views based on "variables.yaml" file.
# Python script "create_environment.py" parses this file, renders SQL DDL queries and execute in BigQuery.
#
# Requirements: DDL statements must be separated by ";"
#
# Details in Confluence:
# https://hdquotecenter.atlassian.net/wiki/spaces/DW/pages/3763175425/Creating+and+using+a+development+environment+in+BigQuery+for+data+pipelines

-- Example 1
-- create or replace table {{ dev.projects.SSC }}.{{ dev.datasets.SSC_ASSOC }}.table1 as
-- select * from {{ prod.projects.SSC }}.{{ prod.datasets.SSC_ASSOC }}.table1
-- ;

-- Example 2
-- create or replace table {{ dev.env_project_id }}.{{ dev.datasets.Opportunity }}.table2
-- clone {{ prod.env_project_id }}.{{ prod.datasets.Opportunity }}.table2
-- ;


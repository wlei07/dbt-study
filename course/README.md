# Install dbt
* `cp -rf ../../profiles.yml.sample ./profiles.yml`: copy the profiles.yml file, update the private key. 
* `python -m venv venv`: create a python virtual environment.
* `source venv/bin/activate`, or `. venv/bin/activate`: activate the venv.
* `which python`: verify the venv.
* `deactivate`: exit by venv.
* `pip install dbt-snowflake==1.11.0`: install dbt.
* `dbt --version`: verify dbt.
* `dbt init --skip-profile-setup airbnb`: create project.
* `dbt debug`: verify dbt configurations, specifically the snowflake connections with the server
* `dbt run`: to go through models and tests, etc.
* `dbt run --full-refresh`: to rebuild the whole model.
* `dbt seed`: copy seeds to snowflake, seeds are a CSV file in seeds folder defined in the dbt_project.yml
* `dbt ls --resource-type model`
* `dbt compile`: check if all models are connected correctly
* `dbt compile --inline '{# This is a comment #}{% set my_name = "Lei" %}{{ my_name }}'`: ompile the whole project, but also this Jinja code and put result to the screen.
* `dbt compile --inline '{{ select_positive_values("dim_listings_cleansed", "minimum_nights") }}'`: another example of the above
* `dbt show --inline '{{ select_positive_values("dim_listings_cleansed", "minimum_nights") }}'`: execute the query
* `dbt show --inline 'select * from {{ ref("dim_listings_cleansed") }} where {{ no_empty_strings(ref("dim_listings_cleansed")) }}'`: another example of the above
* `dbt source freshness`: check the freshness of the sources defined in the sources.yml: `sources.tables[].config[].freshness`.
* `dbt snapshot`
* `dbt test`
* `dbt test -x`: stop test execution after the first failure so it fails earlier.
* `dbt test -s dim_listings_minimum_nights`: select a single test by name
* `dbt build`: whole package of `dbt seed` -> `dbt run` -> `dbt snapshot` -> tests

# Install Dagster
* `pip install dagster-dbt`: it is dbt integration for dagster, as dependency, it will install dagster core.
* `pip install dagster-webserver`
* `dagster-dbt project scaffold --project-name my_dbt_dagster_project --dbt-project-dir=airbnb`
* `dagster dev --port=3002`

# About Jinja:
* `{# This is a comment #}`
* `{% set my_name = "Lei" %}`: statement: assignments, if statements, macro calls, etc.
* `{{ my_name }}`: expressions

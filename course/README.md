# Install dbt
* `cp -rf ../../profiles.yml.sample ./profiles.yml`: copy the profiles.yml file, update the private key. 
* `python -m venv venv`: create a python virtual environment.
* `source venv/bin/activate`, or `. venv/bin/activate`: activate the venv.
* `which python`: verify the venv.
* `deactivate`: exit by venv.
* `pip install dbt-snowflake==1.11.0rc3`: install dbt.
* `pip install dbt-autofix`: for auto-formatting dbt models.
* `dbt --version`: verify dbt.
* `dbt init --skip-profile-setup airbnb`: create project.
* `dbt debug`: verify dbt configurations, specifically the snowflake connections with the server
* `dbt run`: to go through models and tests, etc.
* `dbt run --full-refresh`: to rebuild the whole model.
* `dbt seed`: copy seeds to snowflake, seeds are a CSV file in seeds folder defined in the dbt_project.yml
* `dbt ls --resource-type model`
* `dbt compile`: check if all models are connected correctly
* `dbt source freshness`: check the freshness of the sources defined in the sources.yml: `sources.tables[].config[].freshness`.
* `dbt snapshot`
* `dbt test`
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

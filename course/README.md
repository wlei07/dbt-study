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
* `dbt ls --resource-type model`: list 

# Install Dagster
* `pip install dagster-dbt`: it is dbt integration for dagster, as dependency, it will install dagster core.
* `pip install dagster-webserver`
* `dagster-dbt project scaffold --project-name my_dbt_dagster_project --dbt-project-dir=airbnb`
* `dagster dev`

# About Jinja:
* `{# This is a comment #}`
* `{% set my_name = "Lei" %}`: statement: assignments, if statements, macro calls, etc.
* `{{ my_name }}`: expressions

# Setup snowflake
Create a snowflake account and a database.
* Choose your Snowflake edition: Standard
* Choose your cloud provider: AWS
* Click the link from email to activate. (keep the link at the bottom of the email)
* Username: admin
* Password: somthing you want
* Startup tutorial: click `Skip for now`
* Convert your public key into snowflake format: `ssh-keygen -f ~/.ssh/id_rsa.pub -e -m PKCS8 | awk 'NR>1 && !/END PUBLIC KEY/' | tr -d '\n'`
* Follow the file [Course Resources](/_course_resources/course-resources.md), replace the public key in the SQL scripts. 

Go to location `course/airbnb`
* `cp -rf ../../profiles.yml.sample ./profiles.yml`: copy the profiles.yml file, update the private key.

# Install dbt and dagster
## Install dbt and dagster by `uv`
In a directory where you have `pyproject.toml` (root project directory):
* first install uv
* `uv sync`: it will install .venv, the virtual python environment.

## Install dbt manually
* `python -m venv venv`: create a python virtual environment.
* `source venv/bin/activate`, or `. venv/bin/activate`: activate the venv.
* `which python`: verify the venv.
* `deactivate`: exit by venv.
* `pip install dbt-snowflake==1.11.0`: install dbt.
* `dbt --version`: verify dbt.

## post dbt install
* `dbt deps`: install packages defined in the packages.yml.
* `dbt seed`: copy seeds to snowflake, seeds are a CSV file in seeds folder defined in the dbt_project.yml
* `dbt build --full-refresh`: whole package of `dbt seed` -> `dbt run` -> `dbt snapshot` -> tests

## Install Dagster manually
* `pip install dagster-dbt`: it is dbt integration for dagster, as dependency, it will install dagster core.
* `pip install dagster-webserver`
* `dagster-dbt project scaffold --project-name my_dbt_dagster_project --dbt-project-dir=airbnb`
* `dagster dev --port=3002`

# Useful dbt commands
* `dbt init --skip-profile-setup airbnb`: create project.
* `dbt debug`: verify dbt configurations, specifically the snowflake connections with the server
* `dbt run`: to go through models and tests, etc.
* `dbt run --full-refresh`: to rebuild the whole model.
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
## dbt documentation
* `dbt docs generate`: generate documentation, taking input form the *.yml files in the models folder.
* `dbt docs serve`: start an HTTP server for the generated documentation.

# About Jinja:
* `{# This is a comment #}`
* `{% set my_name = "Lei" %}`: statement: assignments, if statements, macro calls, etc.
* `{{ my_name }}`: expressions

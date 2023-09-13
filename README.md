## About

This repo contains two [dbt](https://getdbt.com/) quickstart project using Mage. 

The first, `simple_dbt_python_pipeline`, seeds a demo _customers_ dataset from the dbt jaffle shop demo, 
executes a staging model, and performs a Python transformation on the dataset before exporting it to Postgres.

The second pulls the jaffle_shop demo from dbt and creates a profiles.yml file for executing it. Running the pipeline triggers a `dbt build,` 
writing data to the postgres database in our Docker Network. This is a sample workflow for _pulling a dbt project from an external repo_, 
a common pattern in dbt development.

## Prerequisites
1. [Docker](https://docs.docker.com/engine/install/)
2. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

The following command will clone the repo, copy `dev.env` to `.env` and run `docker compose up` to start Mage.

### Mac/Linux

```bash
git clone https://github.com/mage-ai/dbt-quickstart mage-dbt-quickstart \
&& cd mage-dbt-quickstart \
&& cp dev.env .env && rm dev.env \
&& docker compose up
```

### Windows

```bash
git clone https://github.com/mage-ai/dbt-quickstart mage-dbt-quickstart 
cd mage-dbt-quickstart
cp dev.env .env
rm dev.env
docker compose up
```

## Run pipelines

After running the above command, you'll see the Mage overview page. Click the pipelines icon on the left to enter the pipelines overview.

### A Simple dbt Python Pipeline

First, select the `simple_dbt_python_pipeline` by double-clicking— this will take you directly to the editor. You can also single click, 
then select the "code" icon from the side nav.

Select _Run_ + _Execute Pipeline_ to see the pipeline execute. 

You just:
- Seeded a dbt model
- Performed a dbt transformation
- Took the transformed data and performed a Python transformation
- Wrote the data to a Postgres source

To see the output, you can use a querying tool (like DataGrip or psql) to the locally hosted Postgres database and query `public.analytics.cur_customers`.

### A Dynamic dbt Python Pipeline

Next, return to the overview page. Select the `dynamic_dbt_pipeline` by double-clicking— this will take you directly to the editor. You can also single click, 
then select the "code" icon from the side nav.

Select _Run_ + _Execute Pipeline_ to see the pipeline execute. 

You just:
- Pulled a GitHub repo and wrote it to your local Mage directory
- Wrote a demo `profiles.yaml` file that interpolated environment variables from your instance
- Executed `dbt build` to write data to your local postgres database

To see the output, you can use a querying tool (like DataGrip or psql) to the locally hosted Postgres database and check out the `public.analytics` schema.

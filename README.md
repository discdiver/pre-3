# Prefect 3 feature fun

Explore some Prefect 3 features. Part familiarization, part QA, all fun!

## Install

In a brand new virtual enviroment installl the latest released pre-release version of Prefect 3 and all of the integration libraries.

```bash
uv pip install "prefect[aws, azure, bitbucket, dask, databricks, dbt, docker, email, gcp, github, gitlab, kubernetes, ray, slack, snowflake, sqlalchemy]" --pre
```

## Transactions

Prefect's newest feature. Let's explore it!

Create a flow with a task that raises an exception. The flow should be able to handle the exception and rollback any changes made by the task.

Follow the transactions docs to QA them at the same time.

## Deferred Tasks

1. Start a task server. Think for a beat about how to do this. Check out the docs or solution in this repo if you're stuck.
2. Start a task scheduler.
3. Send tasks to the task server from the task scheduler.

## Bonus: Run input

Are you a Pydantic pro (or want to become one)?

Update the run_input example from the Prefect docs to use a Pydantic v2 model.

## Pick an integration library and run an example from its docs

Please file issues for any problems, and if the issue something small with the docs, please submit a PR to fix it! :)

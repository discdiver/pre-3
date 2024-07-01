# Prefect 3 feature fun

Explore some Prefect 3 features. Part familiarization, part QA, all fun!

## Install

Installl  the latest released pre-release version of Prefect 3 and all of integration libraries.

```bash
uv pip install "prefect[aws, azure, bitbucket, dask, databricks, dbt, docker, email, gcp, github, gitlab, kubernetes, ray, slack, snowflake, sqlalchemy]" --pre
```

## Transactions

The newest feature and probably the one we're least familiar with. Let's explore it!

Create a flow with a task that raises an exception. The flow should be able to handle the exception and rollback any changes made by the task.

Follow the transactions docs to QA them at the same time.

## Deferred Tasks

1. Start a task server.
2. Start a task scheduler. There are examples in the docs (and also in this repo).

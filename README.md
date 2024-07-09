# Prefect 3 feature fun

Explore some Prefect 3 features. Part familiarization, part QA, all fun!

## Install

In a brand new virtual enviroment installl the latest released pre-release version of Prefect 3 and all of the integration libraries.

```bash
uv pip install "prefect[aws, azure, bitbucket, dask, databricks, dbt, docker, email, gcp, github, gitlab, kubernetes, ray, slack, snowflake, sqlalchemy]" --pre
```

## Transactions

Prefect's newest feature. Let's explore it!

1. Create a flow with a task that write data to a file. Another task does a data quality check and is hard-coded to fail. Run the code. What happens?
2. Run the same flow, except in a transaction so that it will rollback the write operation.
3. Explore!

## Choose a random Prefect 2 demo/repo and try to run it with Prefect 3

1. Any problems? File an issue!
2. Find something broken in the docs? Open an issue and/or submit a PR!

## Deferred tasks (explored previously on this show)

1. Start a task server. Think for a beat about how to do this. Check out the docs or solution in this repo if you're stuck.
2. Start a task scheduler.
3. Send tasks to the task server from the task scheduler.
4. Where are the tasks in the UI? Or are they in the UI?

## Pick an integration library and run an example from its docs

Please file issues for any problems, and if the issue something small with the docs, please submit a PR to fix it! :)

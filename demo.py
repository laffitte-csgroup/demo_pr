from typing import List

from prefect import task, Flow, Parameter
from prefect.storage import GitHub
from prefect.run_configs import UniversalRun

from prefect_wfs.algorithms.common.string import *

@task
def task_replace(a: List[str], old_value: str, new_value: str):
  return replace(a, old_value, new_value)

@task
def task_split(a: List[str]):
  return split(a)

@task
def task_concat(a: List[str]):
  return concat(a)

@task
def task_print(a: List[str]):
  print(a)

lorem_ipsum = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
a = lorem_ipsum.split(' ')

with Flow("demo_workflow_1") as flow1:
  x = task_replace(a, "bananes", "coconuts")
  x = task_split(x)
  x = task_concat(x)
  task_print(x)

with Flow("demo_workflow_2") as flow2:
  x = task_replace(a, "bananes", "coconuts")
  x = task_concat(x)
  x = task_split(x)
  task_print(x)

for flow in [flow1, flow2]:
    #flow.run()


    flow.storage = GitHub(repo="laffitte-csgroup/demo_pr", path="/demo.py", access_token_secret='GITHUB_ACCESS_TOKEN')
    #flow.run_config = UniversalRun(labels=['sde-scheduling'])
    flow.register(project_name="demo")

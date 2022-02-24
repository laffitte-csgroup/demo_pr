from typing import List

def replace(input: List[str], old_value: str, new_value: str) -> List[str]:
    return [x.replace(old_value, new_value) for x in input]

def split(input: List[str]) -> List[str]:
    intermediate = []
    for element in input:
        n = 3
        intermediate.append([element[i:i+n] for i in range(0, len(element), n) ])
    return [item for sublist in intermediate for item in sublist]

def concat(input: List[str]) -> List[str]:
    # initialize N 
    N = 3
    temp = '{}' * N 
    return [temp.format(*ele) for ele in zip(*[iter(input)] * N)]

from prefect import task, Flow, Parameter
from prefect.storage import Git, GitHub
from prefect.run_configs import UniversalRun, KubernetesRun

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

a = ["bananes", "pommes", "ananas", "poires", "mangues", "kiwis"]

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

    #flow.storage = GitHub(repo="laffitte-csgroup/demo_pr",      path="/demo.py", access_token_secret='GITHUB_ACCESS_TOKEN')
    flow.storage = GitHub(repo="laffitte-csgroup/demo_pr",      path="/demo_s1.py")
    #flow.run_config = KubernetesRun(labels=['sde-scheduling'])


    #flow.run_config = UniversalRun(labels=['sde-scheduling'])

    flow.register(project_name="demo")
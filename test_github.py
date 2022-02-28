from typing import List

from prefect import task, Flow
from prefect.storage import GitHub

from prefect_wfs.algorithms.common.string import *

@task
def task_os():
    import pkg_resources
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
      for i in installed_packages])
    print(installed_packages_list)

    import os

    print(os.system('pwd'))
    print(os.system('ls'))
    print(os.system('env'))

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

with Flow("test_github") as flow:
  task_os()
  x = task_replace(a, "bananes", "coconuts")
  x = task_split(x)
  x = task_concat(x)
  task_print(x)

flow.storage = GitHub(repo="laffitte-csgroup/demo_pr", path="/test_github.py", ref='master', stored_as_script=True)
flow.register(project_name="demo")

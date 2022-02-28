from typing import List
import os
import pkg_resources

from prefect import task, Flow
from prefect.storage import GitHub

@task
def task_os(log_stdout=True):
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
      for i in installed_packages])
    print(installed_packages_list)

    print(os.system('pwd'))
    print(os.system('ls'))
    print(os.system('env'))

with Flow("test_github") as flow:
  task_os()

flow.storage = GitHub(repo="laffitte-csgroup/demo_pr", path="/test_github.py", ref='master', stored_as_script=True)
flow.register(project_name="demo")

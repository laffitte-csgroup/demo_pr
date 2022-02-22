from prefect import task, Flow, Parameter
from prefect.storage import GitHub
from prefect.run_configs import UniversalRun

@task
def hello_world(name):
  logger = prefect.context.get("logger")
  logger.info("Hello "+name)

with Flow("demo_pr_github") as flow:
  name = Parameter('name', default = 'Bob')
  hello_world(name)

flow.storage = GitHub(repo="laffitte-csgroup/demo_pr", path="/demo.py")

flow.run_config = UniversalRun(labels=['sde-scheduling'])

flow.register(project_name="demo_s1")
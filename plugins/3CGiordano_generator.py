import yaml
import os
from jinja2 import Environment, FileSystemLoader

file_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(file_dir))
template = env.get_template("G3Giordano_template_dag_etl.jinja2")

for filename in os.listdir(file_dir):
    if filename.endswith(".yaml"):
        with open(f"{file_dir}/{filename}", "r") as configfile:
            config = yaml.safe_load(configfile)
            with open(f"plugins/{config['dag_id']}.py", "w") as f:
                f.write(template.render(config))

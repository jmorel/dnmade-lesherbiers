from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml

with open('src/content.yaml') as f:
    content = yaml.load(f, Loader=yaml.FullLoader)

env = Environment(
    loader=FileSystemLoader('src/templates/'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('index.html')
rendered = template.render(content)

with open('_build/index.html', 'w') as f:
    f.write(rendered)

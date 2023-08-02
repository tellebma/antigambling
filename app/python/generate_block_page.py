from jinja2 import Template
import json

def generate_template(sites_to_block):
    template_str = """
    [
        {% set current_id = 1 %}
        {% for site in sites_to_block %}
        {
          "id": {{ current_id }},
          "priority": 1,
          "action": { "type": "block" },
          "condition": {"urlFilter": "{{ site }}", "resourceTypes": ["main_frame"] }
        },
        {% set current_id = current_id + 1 %}
        {% endfor %}
    ]
    """
    template = Template(template_str)
    return template.render(sites_to_block=sites_to_block)

# Exemple d'utilisation :
with open("input_sites.json", "r") as file:
    data = json.load(file)
    sites_to_block = data["sites_to_block"]
    
generated_json = generate_template(sites_to_block)

# Écriture du fichier template généré dans un fichier nommé "template.json"
with open("rules.json", "w") as file:
    file.write(generated_json)



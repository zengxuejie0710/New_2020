# Author xuejie zeng
# encoding utf-8
import yaml

def yamltext():
    with open('main.yaml', encoding='utf-8') as f :
        steps = yaml.safe_load(f)
    for step in steps:
        if 'action' in steps.keys():
            action = steps['action']
            if 'click' == action:
                find(step['by'],step['locator'])

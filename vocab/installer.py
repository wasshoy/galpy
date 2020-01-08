import yaml
with open('./config.yaml', mode='r') as f:
    yml = yaml.load(f)
    print(yml)
    print(type(yml))



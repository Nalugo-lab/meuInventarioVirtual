import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

def load_envvars(BASE_DIR):
    try:
        yaml_file=open("./.envvars.yaml", "r")        
    except: 
        yaml_file=open(str(BASE_DIR.parent) + "/.envvars.yaml", "r")
        
        
    return yaml.load(yaml_file, Loader=Loader)
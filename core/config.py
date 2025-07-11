import yaml

class Config:
    def __init__(self):
        with open("config/config.yml", "r") as f:
            self.config = yaml.safe_load(f)

        with open("config/services.yml", "r") as f:
            self.services = yaml.safe_load(f)

    def get(self, section, key):
        return self.config.get(section, {}).get(key)

    def get_service(self, service_name, key):
        return self.services.get("services", {}).get(service_name, {}).get(key)

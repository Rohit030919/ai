class InformationManagement:
    def __init__(self):
        self.knowledge_base = {}

    def add_information(self, topic, details):
        self.knowledge_base[topic] = details

    def get_information(self, topic):
        return self.knowledge_base.get(topic, "Information not found.")

info_system = InformationManagement()
info_system.add_information("Python", "A programming language.")
info_system.add_information("Machine Learning", "A subset of AI where systems learn from data.")

print(info_system.get_information("Python"))
print(info_system.get_information("Data Science"))

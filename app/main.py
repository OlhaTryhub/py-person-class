class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list_obj = [Person(pers["name"], pers["age"]) for pers in people]
    for i in range(len(people)):
        if people[i].get("wife"):
            people_list_obj[i].wife = Person.people[people[i]["wife"]]
        if people[i].get("husband"):
            people_list_obj[i].husband\
                = Person.people[people[i]["husband"]]

    return people_list_obj

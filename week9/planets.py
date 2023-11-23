import week9.humans as humans
import week9.robots as robots


class Planet:

    def __init__(self, name):
        self.name = name

    inhabitants = {
        'humans': [],
        'robots': []
    }

    def add_human(self):
        self.inhabitants['humans'].append(humans.Human())

    def remove_human(self):
        self.inhabitants['humans'].pop()

    def add_robot(self):
        self.inhabitants["robots"].append(robots.Robot())

    def remove_robot(self):
        self.inhabitants["robots"].pop()

    def __str__(self):
        return f'Planet {self.name} has {len(self.inhabitants["humans"])} humans and {len(self.inhabitants["robots"])} robots.'

    def __repr__(self):
        return f'planet(name={self.name}, humans={self.inhabitants["humans"]}, robots={self.inhabitants["robots"]})'


planet = Planet("P")
planet.add_human()
print(planet.inhabitants['humans'][0])
planet.add_robot()
planet.remove_human()
print(planet)

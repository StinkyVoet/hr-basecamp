from abc import ABC
from dataclasses import dataclass
from inspect import unwrap
import re
import string
from sys import stdout
from time import sleep
from tkinter import W
import typing
from random import randrange, uniform
from typing_extensions import Self
from unicodedata import name

class Command():
    @classmethod
    def _inner_classes_list(cls) -> list[str]:
        results = []
        for attrname in dir(cls):
            obj = getattr(cls, attrname)
            if (isinstance(obj, type) and 
            not attrname.startswith("_") and
            not attrname.startswith("Unknown")):
                results.append(attrname.lower())
        return results

    # Exit = Action(exit, "Quit the game")
    # Climb = Action(climb, "Climb the mountain")
    # Eat = Action(eat, "Eat some food")
    # Sleep = Action(sleep, "Sleep to regain energy and health")
    # Stats = Action(showAllStats, "Show all your stats")
    # Help = Action(help, "Show this menu")

    class Exit(): pass
    class Climb(): pass
    class Eat(): pass
    class Stats(): pass
    class Sleep(): pass
    class Help(): pass

    @dataclass
    class Look():
        noun: str

    @dataclass
    class Grab():
        noun: str

    @dataclass
    class Unknown():
        input_str: str

def parse(input_str: str) -> Command:
    lc_input_str = input_str.lower()
    split_input = iter(lc_input_str.split())

    verb = next(split_input)
    noun = next(split_input, "")
    while True:
        next_input = next(split_input, "")
        if next_input == "":
            break
        noun += next_input

    match verb:
        case "exit": return Command.Exit()
        case "climb": return Command.Climb()
        case "eat": return Command.Eat()
        case "sleep": return Command.Sleep()
        case "stats": return Command.Stats()
        case "help": return Command.Help()
        case "look": return Command.Look(noun)
        case "grab": return Command.Grab(noun)
        case _: return Command.Unknown(input_str=input_str.strip())

def get_input() -> Command:
    update_screen("\nWhat is your next action?")
    input_str = input("> ")

    return parse(input_str)

def update_screen(output: str):
    stdout.write("\n")
    for c in output:
        stdout.write(f'{c}')
        stdout.flush()
        if re.match(r"\[a-zA-Z1-9 ]", c):
            sleep(0.03)

    stdout.write("\n")

@dataclass
class Stat:
    label: str
    value: float
    max: typing.Optional[float]=None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            if hasattr(self, 'max'):
                if value >= self.max:
                    self._value = self.max
                    return

            if value < 0:
                self._value = 0
                return
        except (AttributeError, TypeError) as e:
            pass

        self._value = value
        return

    def show(self) -> string:
        cur = int(self.value / 5)

        message = f"%-10s\n[%-20s] {round(self.value, 1)}" % (self.label+":", '='*cur)
        if self.max != None:
            message += f"/{self.max}\n"
        return message

LOC_PLAYER = 0

LOC_BASECAMP = 1
LOC_BASECAMP_CHEST = 2

LOC_OUTSIDE_ABANDONED_CABIN = 3
LOC_ABANDONED_CABIN = 4
LOC_ABANDONED_CABIN_CHEST = 5

@dataclass
class Player:
    stats: dict[Stat]
    location: int = LOC_BASECAMP

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, value):
        self._stats = value
        return True

    @staticmethod
    def new() -> Self:
        return Player(
            stats = {
                "health": Stat("Health", 100, 100),
                "food": Stat("Food", 100, 100),
                #"body_temp": Stat("Body Temp", 37),
                "height": Stat("Climbed distance", 0, 500),
                "energy": Stat("Energy", 100, 100),
            }
        )
    
    def show_stats(self) -> str:
        output = ""
        for stat in self.stats.values():
            output += stat.show()
        return output

@dataclass
class Object:
    name: str
    description: str
    pos: typing.Optional[int] = None

@dataclass
class World:
    objects: dict[Object]

    @staticmethod
    def new() -> Self:
        return World({
            LOC_BASECAMP: Object(
                "Base Camp", 
                "The starting base camp at the foot of the mountain."
            ),
            LOC_PLAYER: Object(
                "Yourself", 
                "yourself",
                LOC_BASECAMP,
            ),
            None: Object(
                "Rope",
                "a rope",
                LOC_BASECAMP,
            ),
            LOC_BASECAMP_CHEST: Object(
                "Chest",
                "chest",
            ),
            LOC_OUTSIDE_ABANDONED_CABIN: Object(
                "Outside",
                "moderately cold area with a few trees scattered about. There is a cabin nearby",
            ),
            LOC_ABANDONED_CABIN: Object(
                "Abandoned Cabin",
                "an old, abandoned cabin",
            ),
            LOC_ABANDONED_CABIN_CHEST: Object(
                "Chest",
                "chest",
            ),

        })

    def update_state(self, command: Command, player: Player) -> str:
        match command:
            case Command.Climb(): return self.do_climb(player)
            case Command.Eat(): return self.do_eat(player)
            case Command.Sleep(): return self.do_sleep(player)
            case Command.Stats(): return player.show_stats()
            case Command.Help(): return help()
            case Command.Exit(): return "Quitting Game..."
            case Command.Look(noun): return self.do_look(noun, player)
            case Command.Grab(noun): return self.do_grab(noun, player)
            case Command.Unknown(input_str): 
                return f"I don't know how to '%s'.\nType 'help' for a list of available actions." % input_str

    def do_climb(self, player: Player) -> str:
        output: string

        if player.stats["energy"].value == 0:
            return "You don't have enough energy to climb."

        climb_dist = randrange(1,15)

        player.stats["height"].value += climb_dist
        output = "You climbed %dm.\n%s\n" % (climb_dist, player.stats["height"].show())

        if player.stats["food"].value > 0:
            hunger = round(climb_dist * uniform(0.8, 3.5), 1)

            player.stats["food"].value -= hunger
            output += "Your food went down by %s.\n%s\n" % (hunger, player.stats["food"].show())

        lost_energy = randrange(20,45)
        player.stats["energy"].value -= lost_energy
        output += "You lost %s energy" % lost_energy

        if randrange(1,7) == 1:
            lost_health = randrange(10,40)
            player.stats["health"].value -= lost_health
            output += "\n\nYou fell while climbing. You lost %d health." % lost_health
        
        return output
    
    def do_eat(self, player: Player) -> str:
        player.stats["food"].value = 100
        print("You ate. Your new food value is:")
        return player.stats["food"].show()
    
    def do_sleep(self, player: Player) -> str:
        if player.stats["energy"].value > 75:
            return "You don't feel tired enough to sleep"

        output: str
        player.stats["energy"].value = 100
        output = "You slept and feel full of energy. "

        if player.stats["health"].value < player.stats["health"].max:
            if player.stats["food"].value >= 75:
                heal_amount = round(player.stats["food"].value / randrange(3, 8), 1)
                player.stats["health"].value += heal_amount
                output += " You healed by %s points." % heal_amount
            else:
                output += " You were too hungry to regain health."

        return output
    
    def do_look(self, noun: str, player: Player) -> str:
        match noun:
            case "around" | "":
                (list_string, _) = self.list_objects_at_location(player)
                return f"You are in {self.objects[player.location].name}.\n{self.objects[player.location].description}\n{list_string}"
            case _:
                return "I don't understand what to see."
    
    def list_objects_at_location(self, player: Player) -> typing.Tuple[str, int]:
        output = ""
        count = 0
        
        for (pos, object) in self.objects.items():
            if pos == LOC_PLAYER:
                continue
            
            if object.pos == None:
                continue
            
            if object.pos == player.location:
                if count == 0:
                    output += "\nYou see:\n"
                count += 1
                output += f"{object.description}"

        return (output, count)

    def do_grab(self, noun: str, player: Player) -> str:
        for (pos, object) in self.objects.items():
            if pos == LOC_PLAYER:
                continue
            
            if object.pos == None:
                continue
            
            if object.pos != player.location:
                continue

            if object.name.lower() == noun:
                object.pos = LOC_PLAYER
                return f"Picked up {object.description}"
            return f"I can't find a {noun} here."

def help() -> str:
    output = "Available commands:\n"

    for command in Command._inner_classes_list():
        output += f" - {command}\n"
    return output

def exit():
    quit("\nok bye... :,(")

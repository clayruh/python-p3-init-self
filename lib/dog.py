#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt", favorite_toy="Any"):
        self.name = name
        self.breed = breed
        self.favorite_toy = favorite_toy

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self
    
    def get_adopted(self, owner_name):
        self.owner = owner_name
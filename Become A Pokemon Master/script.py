class Pokemon:
  #__init__ used as object is created directly from the class to initalise values
    def __init__(self, name, type, level, health, max_health):
      #'self' used to access the attributes and methods of the class itself
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = type
        self.is_knocked_out = False
        #Each Pokemon has certin feautures which they share with all other Pokemon
    

    def lose_health(self, hit_damage):
        self.health -= hit_damage
        #A pokemon's overall health will decrease and save to 'self.health' when damage is taken
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        # If the health of a Pokemon is reduced to 0 or below by a hit, set 'self.health' to 0 and set 'self.knock_out()' to true.
        else:
            print("{self.name} has taken damage, and now has {self.health} health.")
        # Otherwise, state the Pokemon's name an thier new health number.
        
    def gain_health(self, max_health):
        if self.health == 0:
            self.revive()
        self.health += max_health
        self.is_knocked_out = False
        # If a pokemon's health is equal to 0 then add the value of it'smax health to revive the pokemon. Also, set the 'is_knocked_out' value to false as it has been revived.
        if self.health >= self.max_health:
            self.health = self.max_health
        #If the pokemon's health is above the max, re-assign it to the max value
        print("{self.name} has been revived and now has {self.health} health.")




    def attack(self, other_pokemon):
      #I have chosen the 3 most popular types of pokemon. A switch statement may have allowed me to include other but I am not sure how to appropriately write the statement with the condidtion.
      if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Normal") or (self.type == "Normal" and other_pokemon.type == "Fire"):
      #Following a similar structure to "Rock, Paper Scissors", If the pokemon has the advantage in type, then they inflict their max amount of damage which is equal to their level
        print("{self.name} has dealt {other_pokemon.name} {self.level} damage.")
      else:
        half_damge = self.level / 2
        print("{self.name} hes dealt {half_damage} damage to {other_pokemon.name}")

      #All other combinations deal a damage that is equal to half of their current level type


class Trainer:
  def __init__ (self, name, pokemons, potions):
    self.pokemons = pokemons,
    self.name = name
    self.potions = potions
    self.current_pokemon = None


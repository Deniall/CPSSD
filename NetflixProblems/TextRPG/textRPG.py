import random
from random import randint

North = 0
South = 0
East = 0
West = 0
        
class Character:
    def __init__(self):
        self.name = ""
        self.health = 1
        self.health_max = 1
    def do_damage(self, enemy):
        randomizer = randint(0,2)
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health)
        enemy.health = enemy.health - damage
        if damage == 0:
            if randomizer == 0:
                print "%s swings blindly at %s and misses, making %s laugh in a mocking tone." % (self.name, enemy.name, enemy.name)
            if randomizer == 1:
                print "%s gets distracted by the emptyness and lonliness of the world and thus misses the attack." % (self.name)
            if randomizer == 2:
                print "%s, trying to replicate a scene from a movie they watched long ago, fails and misses." % (self.name)
        
        else: print "%s cleaves %s a nice, clean hit and readies for another attack." % (self.name, enemy.name)
        return enemy.health <= 0

class Enemy(Character):
  def __init__(self, player):
    names = ['Goblin', 'Minotaur', 'Falcon wasp hybrid', 'Crocodile with human legs', "crazed Daniel O' Donnell fan"]
    Character.__init__(self)
    self.name = random.choice(names)
    self.health = randint(1, player.health)
 

        
class Player(Character):
    
    def __init__(self):
        Character.__init__(self)
        self.state = 'normal'
        self.health = 10
        self.health_max = 10
        self.North = 0
        self.South = 0
        self.East = 0
        self.West = 0

    def quit(self):
        print "Suddenly, a large pink snake with teeth emerges from the ground in front of %s, eating them whole. RIP."%(self.name)
        self.health = 0
        

    def help(self): print Commands.keys()

    def tired(self):
        print "%s begins to get very tired." % self.name
        self.health = self.health-1

    def rest(self):
        if self.state != 'normal': print "%s isn't in the mood for sleeping right now." % self.name
        else:
          print "%s makes a makeshift bed on the floor, and lies down.." % self.name
          if randint(0, 1):
            self.enemy = Enemy(self)
            print "%s, dreaming about a society involing pineapples riding animals, is rudely awoken by a %s" % (self.name, self.enemy.name)
            self.state = 'fight'
            self.enemy_attacks()
          else:
            if self.health < self.health_max:
              self.health = self.health + 1
            else: print "%s slept too much; the guilt of his laziness begins to pain him." % self.name; self.health = self.health - 1

    def status(self): print "%s's health: %d/%d" % (self.name, self.health, self.health_max)  
            
    def attack(self):
        if self.state != 'fight': print "%s swats the air, without notable results." % self.name; self.tired()
        else:
          if self.do_damage(self.enemy):
            print "%s executes %s!" % (self.name, self.enemy.name)
            self.enemy = None
            self.state = 'normal'
            if randint(0, self.health) < 10:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                print "%s feels as though he learned something from that fight." % self.name
          else: self.enemy_attacks()

    def enemy_attacks(self):
        if self.enemy.do_damage(self): print "%s cuts you cleanly in half, laughing manically before realising that you were the only interaction it's had with another living thing in months. Depression quickly dawns on the %s. It questions why it attacked you. Is that why it's parents left?... R.I.P" %(self.enemy.name, self.enemy.name)

    def flee(self):
        if self.state != 'fight': print "%s runs in circles for a while." % self.name; self.tired()
        else:
          if randint(1, self.health + 5) > randint(1, self.enemy.health):
            print "%s flees from %s." % (self.name, self.enemy.name)
            self.enemy = None
            self.state = 'normal'
          else: print "%s couldn't escape from %s!" % (self.name, self.enemy.name); self.enemy_attacks()


    def explore(self):
        
        
        scenchoice = randint(0,7)
        if self.state == 'tired':
            print "%s is completely exhausted and cannot go further. Rest up."%(self.name)
            if randint (0,5) == 0:
                self.enemy_attacks()
        if self.state == 'fight':
            print "Your wanderlust distracts you from the middle of the fight you obviosuly forgot you were in, and you take a swift blow to the chin."
            self.health = self.health -1
        
        else:
            print "Choose a direction (N, S, E, W): "
            choice = raw_input()
            self.enemy = Enemy(self)
            if choice == 'N':
                self.North +=1
                if scenchoice == 0:
                    self.enemy = Enemy(self)
                    print "You walk slowly into a clearing. Suddenly, you hear angry snarls from your left. A %s jumps out of seemingly thin air and starts heading your direction."%(self.enemy.name)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 1:
                    self.enemy = Enemy(self)
                    print "You take a break for half a minute to get your bearings, but this is cut short when a %s appaers from a patch of shrubbery nearby. You ready yourself for the fight."%(self.enemy.name)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 2:
                    self.enemy = Enemy(self)
                    print "You become enraged all of a sudden and let a wolf-call into the night. As if to answer your primal call, a %s emerges from the fog. You get ready."%(self.enemy.name)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 3:
                    print "The tiredness and lonliness starts to take it's toll on you. You begin to hallucinate a %s coming out of a bush and doing the Riverdance. This makes you laugh until you reaslise it isn't actually a vision and you're about to be killed. You slap yourself and ready your gear."%(self.enemy.name)                                                                                
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 4:
                    print "You find yourself in a clearing, with some mossy stone blocks here and there reminding you of a previous generation. There isn't much to be seen."                                                                       
                if scenchoice == 5:
                    print "You emerge into a sparsely pockmarked landscape, the pockmarks being puddles full of dirt grimy water. The survivalist in you tells you to drink but general common sense tells you not to."
                if scenchoice == 6:
                    print "You walk for a bit and nothing seems to change. Have you been walking in circles? You're sure you've seen that rock formation before.."                                                                       
                if scenchoice == 7:
                    print "You walk, and walk, and walk.."
            if choice == 'S':
                self.South +=1
                if scenchoice == 0:
                    print "You walk slowly into a clearing. Suddenly, you hear angry snarls from your left. A %s jumps out of seemingly thin air and starts heading your direction."%(self.enemy.name)
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 1:
                    print "You take a break for half a minute to get your bearings, but this is cut short when a %s appaers from a patch of shrubbery nearby. You ready yourself for the fight."%(self.enemy.name)
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 2:
                    print "You become enraged all of a sudden and let a wolf-call into the night. As if to answer your primal call, a %s emerges from the fog. You get ready."%(self.enemy.name)
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 3:
                    print "The tiredness and lonliness starts to take it's toll on you. You begin to hallucinate a %s coming out of a bush and doing the Riverdance. This makes you laugh until you reaslise it isn't actually a vision and you're about to be killed. You slap yourself and ready your gear."%(self.enemy.name)                                                                                
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 4:
                    print "You find yourself in a clearing, with some mossy stone blocks here and there reminding you of a previous generation. There isn't much to be seen."                                                                       
                if scenchoice == 5:
                    print "You emerge into a sparsely pockmarked landscape, the pockmarks being puddles full of dirt grimy water. The survivalist in you tells you to drink but general common sense tells you not to."
                if scenchoice == 6:
                    print "You walk for a bit and nothing seems to change. Have you been walking in circles? You're sure you've seen that rock formation before.."                                                                       
                if scenchoice == 7:
                    print "You walk, and walk, and walk.."
            if choice == 'E':
                self.East +=1
                if scenchoice == 0:
                    print "You walk slowly into a clearing. Suddenly, you hear angry snarls from your left. A %s jumps out of seemingly thin air and starts heading your direction."%(self.enemy.name)
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 1:
                    print "You take a break for half a minute to get your bearings, but this is cut short when a %s appaers from a patch of shrubbery nearby. You ready yourself for the fight."%(self.enemy.name)
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 2:
                    print "You become enraged all of a sudden and let a wolf-call into the night. As if to answer your primal call, a %s emerges from the fog. You get ready."%(self.enemy.name)
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 3:
                    print "The tiredness and lonliness starts to take it's toll on you. You begin to hallucinate a %s coming out of a bush and doing the Riverdance. This makes you laugh until you reaslise it isn't actually a vision and you're about to be killed. You slap yourself and ready your gear."%(self.enemy.name)                                                                                
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 4:
                    print "You find yourself in a clearing, with some mossy stone blocks here and there reminding you of a previous generation. There isn't much to be seen."                                                                       
                if scenchoice == 5:
                    print "You emerge into a sparsely pockmarked landscape, the pockmarks being puddles full of dirt grimy water. The survivalist in you tells you to drink but general common sense tells you not to."
                if scenchoice == 6:
                    print "You walk for a bit and nothing seems to change. Have you been walking in circles? You're sure you've seen that rock formation before.."                                                                       
                if scenchoice == 7:
                    print "You walk, and walk, and walk.."
            if choice == 'W':
                self.West +=1
                if scenchoice == 0:
                    print "You walk slowly into a clearing. Suddenly, you hear angry snarls from your left. A %s jumps out of seemingly thin air and starts heading your direction."%(self.enemy.name)
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 1:
                    print "You take a break for half a minute to get your bearings, but this is cut short when a %s appaers from a patch of shrubbery nearby. You ready yourself for the fight."%(self.enemy.name)
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 2:
                    print "You become enraged all of a sudden and let a wolf-call into the night. As if to answer your primal call, a %s emerges from the fog. You get ready."%(self.enemy.name)
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 3:
                    print "The tiredness and lonliness starts to take it's toll on you. You begin to hallucinate %s coming out of a bush and doing the Riverdance. This makes you laugh until you reaslise it isn't actually a vision and you're about to be killed. You slap yourself and ready your gear."%(self.enemy.name)                                                                                
                    self.enemy = Enemy(self)
                    self.state = 'fight'
                    self.enemy_attacks()
                if scenchoice == 4:
                    print "You find yourself in a clearing, with some mossy stone blocks here and there reminding you of a previous generation. There isn't much to be seen."                                                                       
                if scenchoice == 5:
                    print "You emerge into a sparsely pockmarked landscape, the pockmarks being puddles full of dirt grimy water. The survivalist in you tells you to drink but general common sense tells you not to."
                if scenchoice == 6:
                    print "You walk for a bit and nothing seems to change. Have you been walking in circles? You're sure you've seen that rock formation before.."                                                                       
                if scenchoice == 7:
                    print "You walk, and walk, and walk.."
        
    def dance(self):
        if self.state == 'fight': print "Your incredible Michael Flatley-esque moves leave your opponent in a trance-like state. However, you have just delayed the inevitable. The %s, now slightly jealous of your moves, readies for another attack."%(self.enemy.name)
        if self.state == 'normal': print "You tap your feet against the ground half-heartedly but your soul isn't in it. Maybe wait for a fight.."
Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  'dance': Player.dance,
  }

p = Player()
p.name = raw_input("What is your character's name? ")
print "(type help to get a list of actions)\n"
print "%s materialises from nothing with no particular purpose in this world." % p.name

if p.North == 10:
    print "You come across something rare: A relic of the old world, an old automotive car. You open the hood because that's what everyone seems to do in post-apocolyptic stories and a crudely-rigged car bomb explodes, tearing you apart. RIP"
    p.health = 0
if p.South == 10:
    p.health = 0
if p.East == 10:
    p.health = 0
if p.West == 10:
    p.health = 0
 
while(p.health > 0):
    line = raw_input("> ")
    args = line.split()
    if p.North == 10:
        print "You come across something rare: A relic of the old world, an old automotive car. You open the hood because that's what everyone seems to do in post-apocolyptic stories and a crudely-rigged car bomb explodes, tearing you apart. RIP"
        p.health = 0
        break
    if p.South == 10:
        p.health = 0
        break
    if p.East == 10:
        p.health = 0
        break
    if p.West == 10:
        p.health = 0
        break
    if len(args) > 0:
        commandFound = False
    for c in Commands.keys():
        if args[0] == c[:len(args[0])]:
            Commands[c](p)
            commandFound = True
            break
    if not commandFound:
        print "%s doesn't understand the command." % p.name
 

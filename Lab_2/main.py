import json

def write(data, filename):
	data = json.dumps(data)
	data = json.loads(str(data))
	with open(filename, 'w', encoding = 'UTF-8') as file:
		json.dump(data, file)


def read(filename):
	with open(filename, 'r', encoding = 'UTF-8') as file:
		return json.load(file)


class NPC():
	def __init__(self, attack, health, armor):
		self.attack = attack
		self.health = health
		self.armor = armor

	def heal(self, point):
		self.health = self.health+point
		if self.health > 100:
			self.health = 100
			print("Person was heal to full hp")
			return
		else:
			print("Person was heal (", (self.health), "hp )")
			return

	def damage(self, point):
		self.health = self.health - (point-self.armor)
		if self.health > 0:
			print ("Person take", (point), "damage!")
			return 
		else:
			print("YOU DIED")
			return


user1 = NPC(10,100,2)
a = user1.__dict__
write(a, 'data.json')
b = read('data.json')
user2=NPC(b['attack'],b['health'],b['armor'])
damage = (input('Skol`ko uronu nanesti? '))
user2.damage(int(damage))
print(user2.__dict__)
heal = (input('Skol`ko hp vostanovit`? '))
user2.heal(int(heal))
print(user2.__dict__)
#user1 = NPC(10,100,2)
#a = {'attack': [], 'health':[], 'armor':[]}
#a['attack'].append(user1.attack)
#a['health'].append(user1.health)
#a['armor'].append(user1.armor)
#write(a, 'data.json')
#b = read('data.json')
#print(b);
#user2 = NPC(b['attack'].__object__,b['health'].__object__,b['armor'].__object__)
#print(user2.attack, user2.health, user2.armor)
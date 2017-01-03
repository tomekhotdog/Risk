import random as rand

MAX_ATTACKERS = 3
MAX_DEFENDERS = 2

class Die:
	def __init__(self):
		self.active = True
		self.value = rand.randint(1,6)

	def roll(self):
		self.value = rand.randint(1,6) if self.active else 0

	def remove(self):
		self.active = False
		self.value = 0

class Duel:
	def __init__(self, attackers, defenders):
		self.num_attackers = attackers
		self.num_defenders = defenders
		self.reset()

	def reset(self):
		self.remaining_attackers = self.num_attackers
		self.remaining_defenders = self.num_defenders

		# Generate dice
		self.attackers = [Die() for die in range(min(MAX_ATTACKERS, self.num_attackers))]
		self.defenders = [Die() for die in range(min(MAX_DEFENDERS, self.num_defenders))]

	def reroll(self):
		for i in range(len(self.attackers)):
			if i >= self.remaining_attackers:
				self.attackers[i].remove()
			self.attackers[i].roll()

		for i in range(len(self.defenders)):
			if i >= self.remaining_defenders:
				self.defenders[i].remove()
			self.defenders[i].roll()

		# Sort dice lists
		self.attackers.sort(key=lambda d: d.value, reverse=True)
		self.defenders.sort(key=lambda d: d.value, reverse=True)

		# Can battle if attackers and defenders remain
	def can_battle(self):
		return self.remaining_attackers > 0 and self.remaining_defenders > 0

	def battle(self):
		while self.can_battle():
			self.reroll()

			# Evaluate dice scores
			dice_pairs = min(
				min(self.remaining_attackers, MAX_ATTACKERS), 
				min(self.remaining_defenders, MAX_DEFENDERS))

			for i in range(dice_pairs):
				if self.defenders[i].value >= self.attackers[i].value:
					self.remaining_attackers -= 1
				else:
					self.remaining_defenders -= 1

class Experiments:
	def execute_experiment(self, attackers, defenders, experiments):
		duel = Duel(attackers, defenders)
		successes = 0.0
		failures = 0.0

		for i in range(experiments):
			duel.battle()
			if duel.remaining_defenders == 0:
				successes += 1
			else:
				failures += 1
			duel.reset()

		success_rate = successes / (successes + failures)
		failure_rate = 1 - success_rate

		return (success_rate, failure_rate)

	def execute_experiments(self):
		experiments = 100000

		for attackers in range(1,11):
			for defenders in range(1, 11):
				success_rate, failure_rate = self.execute_experiment(attackers, defenders, experiments)
				print('attackers vs defenders: ' + str(attackers) + ' v ' + str(defenders))
				print( 'Success Rate: ' + str(success_rate))
				print('Failure Rate: ' + str(failure_rate))


print('DiceCalculations')
e = Experiments()
e.execute_experiments()
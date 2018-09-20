class Item():
	def __init__(self, item_name):
		self.name = item_name
		self.description = None
		self.weight = 0
	def set_name(self, item_name):
		self.name = item_name
	def get_name(self):
		return self.name
	def set_description(self, item_description):
		self.description = item_description
	def get_description(self):
		return seft.description
	def set_weight(self, item_weight):
		self.weight = item_weight
	def get_weight(self):
		return self.weight

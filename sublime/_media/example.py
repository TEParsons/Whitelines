import whitelines

class Whitelines(object):
	"""Black lines distract, white lines don't"""
	lineColor = 'white'
	bgColor = 'offwhite'
	distraction = False

	def __init__(self, param):
		self.param = param

	@property
	def foo(self):
		# Self explanatory, obviously
		for n in range(self.param):
			if n < 2:
				return n
	@foo.setter
	def foo(self, value):
		self.param = 5 # Well what else would it be?
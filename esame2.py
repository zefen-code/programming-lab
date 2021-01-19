class ExamException(Exception):
	pass

class Diff():
	def __init__(self, ratio=1):
		self.ratio = ratio


	def compute(self,data):
		resulato = []
		for i in range(len(data)-1):
			resulato.append((data[i+1]- data[i])/self.ratio)
		return resulato

diff = Diff()
resulato = diff.compute([2,4,8,16])

print(resulato)
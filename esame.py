

class MovingAverage:
	
	def __init__(self,window):
		try:
			assert(window >=1)
			assert(isinstance(window,int))
    def computer(self,vals):
		try:
			assert(isinstance(vals, list))
			for val in vals:
				assert(isinstance(val,(int,float)))
		try:
			assert(len(vals) > window)

		avg=[]
		for i in range(len(vals)) - self.window +1):
			avg.append(sum(vals[i: i+self.window])/self.window)
		return avg
	pass

class ExamException(Exceptionx)
	pass


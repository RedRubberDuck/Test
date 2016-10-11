import threading


class  myThread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name=name
	def run(self):
		print "Run:"+self.name
		summ=0
		for i in range(10000):
			summ+=i
		print "End:"+self.name

t1=myThread("1")
t1.start()
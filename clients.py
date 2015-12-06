import sys, socket, struct, random

class Client():

	def __init__(self, port):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1.5)
		self.ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		self.port = port
		#self.message = message
		#print "Client started"
		s.connect(("0.0.0.0", self.port))
		#s.sendall(self.message)
		#try:
		#	recv_data = s.recv(1000)
		#	print recv_data
		#except socket.timeout:
		#	print "Something went wrong\n"

		valid = False

		while 1:

			while not valid:
				self.message = raw_input(">: ")
				if "READ_FILE" in self.message:
					valid = True
				else:
					print "Invalid Command"
			s.sendall(self.message)
			try:
				recv_data = s.recv(4096)
				print recv_data
				valid = False;
			except socket.timeout:
				print "Something went wrong\n"


#	def connect():
#		print "Client started"
#		s.connect(("127.0.0.1", self.port))
#		s.sendall(self.message);

if __name__ == '__main__':

	port = int(sys.argv[1])
	Client(port)

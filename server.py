import sys, SocketServer, threading, os, re
import Queue

DFS_ROOT_DIR = "~/DFS-FILES/"

class ThreadPoolMixIn(SocketServer.ThreadingMixIn):

    pool_size = 10 #No. of threads in the pool
    student_id = "07988616e4e32911bc9f6a7571184b611fc93406d027a5c828a87664735ed383"
    current_dir = DFS_ROOT_DIR

    #Main server loop
    def serve_forever(self):
        #Create the request queue
        self.request_queue = Queue.Queue(self.pool_size)
        for t in range(self.pool_size):
            t = threading.Thread(target = self.process_request_thread) #Initialize threads
            #print "Starting pool thread ", t.name
            t.start()

        while 1:
            self.handle_request() #Get the ball rolling

    #Start handling the requests sent to the server
    def handle_request(self):
        #requests are esentially socket objects
        request, client_address = self.get_request()
        #Place in the queue
        self.request_queue.put((request,client_address))

    #Get a request from the queue
    def process_request_thread(self):
        while 1:
            #ThreadingMixIn.process_request_thread(self, self.request_queue.get())
            try:
                request, client_address = self.request_queue.get()
            except Queue.Empty:
                pass
            #Fufill request
            self.finish_request(request, client_address)


    def find_file(self, path):
        return os.path.exists(path)


    def read_file(self, path):
        #print path
        if not os.path.isfile(path):
            full_dir = os.path.expanduser(path)

            if not self.find_file(full_dir):
                return "No such file or directory"

            #File is found, change the directory
            path1, file = os.path.split(full_dir)
            try:
                os.chdir(path1)
            except OSError:
                #The other one should've caught this
                return "No such file or directory"
        else:
            file = path

        fo = open(file, "r")
        data = fo.read()
        fo.close()
        return data

    #This is where the work is done
    def finish_request(self, request, client_address):
        while 1:
            #Recieve data from client
            data = request.recv(1024)
            root_dir = os.path.expanduser(DFS_ROOT_DIR)
            os.chdir(root_dir)

            #N/B: Requests will of the form <COMMAND> <DIR>
            #e.g. READ_FILE ~/DFS-FILES/loremipsum.txt
            #<COMMANDS> :  READ_FILE
            #              WRITE_FILE
            #              CH_DIR

            if data.startswith("READ_FILE"):
                r = re.compile("READ_FILE (.*?)$")
                res = r.search(data)
                path = res.group(1)
                response = self.read_file(path);
                request.sendto(response, client_address);

    def shutdown(self):
        server.server_close()
        #Force shutdown, this is the only method which works
        os._exit(os.EX_OK)


class ThreadedRequestHandler(SocketServer.BaseRequestHandler):
    pass

    #Open a thread for each client and handle requests
    """
    def handle(self):
        data = self.request.recv(1024)
        curr_thread = threading.current_thread()
        response = "{} - {}".format(curr_thread.name, data)
        self.request.sendall(response)
    """

class Server(ThreadPoolMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":

    HOST = "0.0.0.0"
    PORT = int(sys.argv[1])
    server = Server((HOST, PORT), ThreadedRequestHandler)
    print "Server started - ", HOST, PORT
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()

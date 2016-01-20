#Architecture Note

This implementation is slightly wrong - I have used the directory sever as a "intermediary"; it sets up the file servers by providing configuration details and it relays commands to
these servers. What I should've done was return details to the client which then connects directly to the file server. My current model is a bit constrained due to issues sending 
ServerSocket objects back and forward, and it's partly a remenant of a previous iteration whereby I built all of the modules (i.e. the directory and file servers) together - at 
the time I was told I was on the right track.

#Description
This is a simple Distributed File System built for my project in CS4032 Distributed Systems, implementing a File System (mandatory), Directory Service, File Locking & Caching 

I've tried to document my code as I went along, so look there for details on the implementation itself.

Currently, to run it, you first have to run the two file servers, then the directory server, and finally the simple test client. This is because I've configured the directory server
to send initialization settings to the two file servers (i.e. what folders each server is handling).

On my machine, the basic file structure looks something like this:

	~/DFS-FILES 
	|		test/
	|		|	test1.txt
	|		|	test2.txt	
	|
	|		loremipsum.txt
	|		test1.txt

	#The first file server covers the directory ~/DFS-FILES, while the second file server covers ~/DFS-FILES/test/
	#It's just a basic test, but it's works on the small scale

NOTE: Contrary to the commit message, the locking does work (kinda). It hasnt been tested to scale since there's no testing suite this year (at the time of writing).

The commands below are the commands I run for testing, in multiple terminal windows. I may get around to writing a shell script for it, but it's tricky with multiple windows

	python fileserver.py 2049 #port
	python fileserver.py 2050
	
	python server.py 2048
	python client.py 2048

The test client and the directory server will only accept the following commands, which are entered in the test client:

	READ FILE <path> 
	WRITE FILE <path> <data>
	CD <path>
	PWD 
	LS
	QUIT
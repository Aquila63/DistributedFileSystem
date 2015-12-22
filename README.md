This is a simple Distributed File System built for my project in CS4032 Distributed Systems.

Currently, to run, you first have to run the two file servers, then the directory server, and finally the simple test client.

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

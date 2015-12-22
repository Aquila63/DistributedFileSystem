This is a simple Distributed File System built for my project in CS4032 Distributed Systems.

Currently, to run, you first have to run the two file servers, then the directory server, and finally the simple test client.

The test client and the directory server will only accept the following commands, which are entered in the test client:

		READ FILE <path> 
		WRITE FILE <path> <data>
		CHDIR <path>
		PWDIR 
		LS

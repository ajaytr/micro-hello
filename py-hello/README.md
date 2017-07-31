# Python HTTP server over UNIX sockets

To run, in this directory execute:

    python3 main.py &    # Start the server in the background
    curl --unix-socket /tmp/py-hello.sock http:/pyhello/

Which should respond with

    Python says: Hello World!


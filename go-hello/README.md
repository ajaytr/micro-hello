# Golang HTTP server over UNIX sockets

This folder is a copy of

    https://github.com/pkumar0508/golang-http-uds/

To run this, install [Golang](https://golang.org/dl/).
Then, in this directory:

    go build
    ./go-hello &    # Start the server in the background
    curl --unix-socket /tmp/golang-hello.sock http://gohello/

Which should respond with

    The gopher smiles, and you are filled with determination.


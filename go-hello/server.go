package main

// With direction from
// https://gist.github.com/teknoraver/5ffacb8757330715bcbcc90e6d46ac74

import (
	"io"
	"log"
	"net"
	"net/http"
	"os"
)

func SayHello(w http.ResponseWriter, req *http.Request) {
	io.WriteString(w,
		"The gopher smiles, and you are "+
			"filled with determination.\n")
}

func main() {
	http.HandleFunc("/", SayHello)

	socket := "/tmp/golang-hello.sock"
	os.Remove(socket)
	uds, err := net.Listen("unix", socket)
	if err != nil {
		panic(err)
	}

	log.Fatal(http.Serve(uds, nil))
}

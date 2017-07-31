# micro-hello
**Micro-services with nginx**

In this example, we connect multiple micro-services
to nginx via Unix Domain Sockets, with nginx acting
as a reverse proxy.

Requests get routed to the appropriate service depending
on their resource id in the URL, eg:

`http://127.0.0.1:8000/python` redirects to the python server and

`http://127.0.0.1:8000/golang` redirects to the golang server
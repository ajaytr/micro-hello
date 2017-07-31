# nginx conf file

First stop your existing nginx daemon:

    nginx -s stop

Then restart using this conf file:

    nginx -t -c ./nginx-hello.conf
    
**Note:** Your .sock files _MUST_ have write
permissions or be in the same user-group as nginx
workers else you will get a `502 Bad Gateway` error.

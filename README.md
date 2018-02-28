# Project 1 – CSE 4344 (Spring 2018)

This project is about implmenting a multihtreaded web server and a web client that communicate using HTTP. Both server and client programs are coded in Python 3.6.3.

### Project Requirements
- Server has to be able to handle multiple client requests concurrently.
- Server works only with HTTP get messages.
- Upon calling the server program, the user can specify a port number for the server as an argument. Otherwise, the server will listen on port 8080 by default.
- Server should log the incoming client requests.
- Server should display client details such as "client address."
- Server should respond with a default file in the case the client has not requested any file.
- If the file the client asks for exists in the server, it responds with  “HTTP/1.1 200 OK” and the file. Otherwise, it should respond with  “HTTP/1.1 404 Not Found.”
- Client should be able to connect to the server and request a file on the server.
- Upon receiving a response from the server, the client should display the status of the response along with the file content if the file that was requested exists.
- Client should also display server details such as "server address."
- Client by default listens to port 8080 unless user has specified another port number.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6
```

### Running

How to run server.py

```
python3 server.py [<port_number>]

<port_number> - Optional. Upon not specifiying this, server will use 8080.
```

How to run client.py

```
python3 client_code_name [<server_IPaddress/name>] [<port_number>] [<requested_file_name>]

<server_IPaddress/name> - Optional. If provided, has to be 'localhost' or '127.0.0.1.' Upon not specifiying this, client will use '127.0.0.1.'

<port_number> - Optional. Upon not specifiying this, client will use 8080.

<requested_file_name> - Optional. Upon not specifying, server will respond with a default html file.


--- Important ---
Arguments have to be provided in the order specified above. For example, you cannot omit <server_IPaddress/name> and have <port_number> as the first argument.
```


* **Don Kuruppu**

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc


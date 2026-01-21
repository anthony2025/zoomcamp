## Setup port forwarding from wsl to windows

netsh interface portproxy add v4tov4 listenport=5432 listenaddress=127.0.0.1 connectport=5432 connectaddress=127.17.127.68
netsh interface portproxy show all
netsh interface portproxy delete v4tov4 listenport=5432 listenaddress=0.0.0.0

Address         Port        Address         Port
--------------- ----------  --------------- ----------
127.0.0.1       8085        127.17.127.68   8085
127.0.0.1       8081        127.17.127.68   8081
127.0.0.1       8080        127.17.127.68   8080

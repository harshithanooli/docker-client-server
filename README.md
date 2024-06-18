Docker Client Server Project

Socket programming was developed in Python to establish communication both the server and client applications. Within this setup, the server is responsible for creating a 1KB file containing random text data. Subsequently, it transmits this file to the client alongside its checksum. Upon reception, the client saves the file in the "/clientdata" directory and confirms the integrity of the data by verifying the checksum.

Here are the steps to be followed :

1. I used the below directory structure
dockerproject/
├── server/
│   ├── Dockerfile
│   └── server.py
├── client/
│   ├── Dockerfile
│   └── client.py
├── docker-compose.yml

2. Complete all the programs and Dockerfiles, that are - server.py, client.py, Dockerfile for server and client, and docker-compose.yml file.

3. Now navigate to dockerproject directory and execute the "docker-compose build" command to build server and client docker containers.

4. Now execute "docker-compose up" command to spin up the contaners. This command would the print the output that checksums are matched.

5. Check for the text file received by client using below commands.
    "docker ps" - gives the client container id
    "docker exec -it client_conatiner_id /bin/bash"

6. Now enter "ls" command to see all the files in the client data folder and check for the text file received.

7. Same file would be present in Volumes/clientvol inside the Docker Desktop app.
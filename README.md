# CloudApp
This repo will contain our semester project.

Ignore every file not in kafka, kafkaclient, chatserver, test. These were files for testing our project and 
ended up not working.
This project is not linked up how we desired but we do have working components. 

List of commands before running docker and docker-compose:
- sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
- echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
- sudo apt-get update
- sudo apt-get install -y mongodb-org
- sudo service mongod start

Traverse to the test directory.
Build the dockerfile and run it
run the docker-compose.yml
- sudo docker-compose up
This will link zookeeper, kafka, and mongo. Once sudo docker-compose up is ran type
- mongo
into the console which will start an instance of mongodb.

The directories kafka, kafkaclient, chatserver are essentially lab 4. These files are ran using the exact same commands 
as presented in lab 4. 

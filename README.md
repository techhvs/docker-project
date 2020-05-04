# docker-project
This Project is Based on Docker technology basically and involve following other technologies.
This is webapp in which i tried to build Sentence similarity telling model in which we will input to string and we will 
predict how much similar those sentence are .
+ Used Docker
+ Python 
+ Flask
+ Html for frontend 

HOW TO USE :
Install DOcker on your OS.
  (You have to configure your Yum brfore Installing docker )
 -- yum install docker ce --nobest
 
For this you will need a Python Image 
   (download through Docker Hub Official Image is available)

For Checking python image is available or not 
(use  docker ps command to list all images)

Now open the terminal and type.
  docker build -t dockapp:v1
  
 for checking new image (type docker images in terminal)
 
 Now for building Container run the following command
 (docker container run -d -p 8080:80 dockapp:v1)
 
 As the new container is launched now get on to your browser and type you
 IP Of base os with the port number and it will run.

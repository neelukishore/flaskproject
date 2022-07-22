# git commands
#cd flaskproject
 git branch
 git branch -a
 git checkout flask_sqlite
 git branch
 cp -rf ../flaskclass2/* .
 
 vi .gitignore
 git add .
 git commit -m "flaskclass2 appilcation added"
 git push -u origin flask_sqlite

 #docker commands
 create a Dockerfile with application code
 docker images
 docker build -it my-app:1.2 .
 doker run -it -p 5000:5000 my-app:1.2 (check if docker container launches & run successfully)
 docker ps -a 
 docker tag my-app:1.2 riyan0622/flask-app:v1
 docker push riyan0622/flask-app:v1

 #kubernates
 create deployment yaml
 kubectl apply -f deployment.yaml
 kubectl get pod -o wide
 kubectl logs <podname>
 create service

 kubectl create service <service-name>
 kubectl expose deployment <deployname> --type=NodePort --port=5000
 kubectl describe service <servicename>
 kubectl describe deployment <deployname>
 kubectl port-forward service/<servicename> 5000:5000
 minikube service servicename
 minikube dashboard

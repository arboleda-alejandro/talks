1) Inspect the logs and detect the issue. Is the application working? 
2) Connect to server pod and check process...then check if it's running successfully with nc local host. Then describe the svc open_me.txt
3) Fix the Service. Its the service the issue? No.
4) Do we have a network policy?  k get netpol -A 
5) Delete the netpol: k delete netpol -n chalenge-3 restrict-egress-except-ip
6) Try again...
7) What could be happening? Let's inspect the deployment! we realized it connects through the NodePort
8) Could it be SecurityGroups? No! NACL!
9) Edit NACL: open_me_2.txt
10) Configure priority greater than 100
11) Solved

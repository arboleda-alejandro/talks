1) Inspect the logs and detect the issue
2) Try to nc to the destination node and port through the service
3) see the network timeout
4) is destination up and running? check for services in the destination
4.1) to the pod: k exec -it -n challenge-3 deployment/client -- nc -vz -w 3 [ip] [port]
4.2) to she service: k exec -it -n challenge-3 deployment/client -- nc -vz -w 3 [ip] [port] #Este deberia fallar
4.3) Arreglar El servicio y repetir...Funciona, pero el log? log sigue mostrando error, pod client sigue fallando
5) Inspeccionemos el pod ... se intenta conectar es a traves del nodo!
6) Intentemos nc a través del nodo: 
k exec -it -n challenge-3 deployment/client -- nc -vz -w 3 172.31.90.115 31234

7) Este falla! cual es ese nodo? es el mismo? Es otro! que puede estar bloqueando ese trafico?
8) k get netpol -A -....vacio
9) k get pods -A | grep -i cilium! que es cilium?
10) k get -n challenge-3 ciliumnet..
11) la borramos
12) repetimos nc al nodo?
13) sigue fallando?
14) SG? tene sentido? explicar por que no
15) NACL? Yes! edit it with the prioroty
16) NACL: https://us-east-1.console.aws.amazon.com/vpcconsole/home?region=us-east-1#NetworkAclDetails:networkAclId=acl-05dc52787f0c66f63

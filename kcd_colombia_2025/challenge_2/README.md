1) check logs of the pod
2) connect to the pod with exec -it
3) cat /proc/1/cmdline
4) Execute code line by line to see the error
5) try to edit manifest, change runAsUser: 0 inside container
6) check replicaset Created, describe it
7) It's not possible to change it to 0...admissionPolicy
8) Solution, add the capability to securityContext
9)   
capabilities:
  add: ["NET_BIND_SERVICE"] 

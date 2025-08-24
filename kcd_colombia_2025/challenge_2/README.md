1) check logs of the pod
2) connect to the pod with exec -it
2.1) try ps, netstat... does not work
3) cat /proc/1/cmdline
4) Execute code line by line to see the error
5) try to edit manifest, change runAsUser: 0 inside container
5.1) check capabilities? cat /proc/1/status
7) It's not possible to solve it to 0...why? there is a drop-all ?
7.1 kyverno logs drop | grep -i all
8) Solution, add the capability to securityContext
9)   
capabilities:
  add: ["NET_BIND_SERVICE"] 

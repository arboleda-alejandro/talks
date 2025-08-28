1) check logs of the pod
2) connect to the pod with exec -it
3) try ps, netstat... does not work
4) cat /proc/1/cmdline
4) Execute code line by line with python to see the error
5) try to edit deployment, change runAsUser: 0 inside container
6) check capabilities? cat /proc/1/status
7) It's not possible to solve it to 0...why? there is a drop-all ?
8) kyverno logs drop | grep -i all
9) open_me.txt
10) Solution, add the capability to securityContext
11) add the capability: open_me_2.txt 

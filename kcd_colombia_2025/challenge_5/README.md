1) Check the pod in the ns
1) Check logs of the pod
2) Connect to the pod with exec -it
3) try ps, netstat... does not work
4) cat /proc/1/cmdline
5) Execute code line by line to see the error
6) We have root permissions...we have capabilities as well...
7) syscalls? let's check
8) in one terminal, scan with Gadget. Delete the pod First.
9) k gadget run audit_seccomp -n challenge-5 
10) syscall missing! let's connect to the node!
11) access to the node
12) Add BIND to the list of syscalls
13) Check Deployment
14) once fixed, run kubectl gadget run advise_seccomp -n challenge-5
15) Recreate pod
16) Control + C
17) We have the seccompProfile

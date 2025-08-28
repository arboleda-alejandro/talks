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
9) syscall missing! let's connect to the node!
9.1) access to the node: https://us-east-1.console.aws.amazon.com/systems-manager/session-manager/i-0f9620c47d654a6e5?region=us-east-1#:
10) Add BIND to the list
11) Check Deployment
12) once fixed, run kubectl gadget run advise_seccomp -n challenge-5
13) Recreate pod
13) Control + C
14) We have the seccompProfile

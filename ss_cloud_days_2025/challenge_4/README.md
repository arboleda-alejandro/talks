1) We have root permissions (check security context )...we have capabilities as well...
2) in one terminal, scan with Gadget using this command: k gadget run audit_seccomp -n challenge-4, then delete the pod (to speed up detection of syscalls)
3) syscall missing! let's connect to the node!
4) access to the node
5) Add bind to the list of syscalls
6) Check Deployment
7) once fixed, run kubectl gadget run advise_seccomp -n challenge-4
8) Recreate pod
9) Control + C
10) We have the seccompProfile generated (if we need for other usecases)

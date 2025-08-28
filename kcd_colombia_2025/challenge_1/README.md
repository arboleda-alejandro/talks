1. View Logs
2. View Logs of specific container... which script are we executing?
3. Can we exec into container?
4. No, then, let's use debug command
5. open_me: kubectl run init-debug --image=arboledaalejandro/init-container-buggy:3.3.0 --restart=Never --rm -it --command -- bash
6. Execute manually the entry point
7. Fix it, edit the deployment! open solution.txt
8. where is the real entry point defined for final solution?

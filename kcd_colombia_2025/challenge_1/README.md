1. View Logs
2. View Logs of specific container
3. Can we exec into container?
4. No, then, let's use debug command
5. kubectl run init-debug --image=arboledaalejandro/init-container-buggy:3.1.0 --restart=Never --rm -it --command -- bash
6. Execute manually the entry point
7. where is the real entry point defined for final solution?

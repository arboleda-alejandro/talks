kubectl exec frontend-pod -n challenge-3 -- sh -c '
  for i in 1 2 3 4 5 6 7 8 9 10; do
    sh -c "while true; do curl -s backend-service:8080/api/data; sleep 0.1; done" &
  done
  wait
'

# Quick & Dirty Load Test for forcing Curam OCP pod autoscaling

## Deploy to OCP

```shell
oc new-project locust-test
oc new-app https://github.com/daisleyj/curam-test.git --strategy=docker
oc expose svc/curam-test
```


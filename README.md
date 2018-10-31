Test Routes
===========
Simple script to test route split using A/B deployment in an OpenShift installation.

More information:
https://docs.openshift.com/container-platform/3.9/dev_guide/deployments/advanced_deployment_strategies.html#advanced-deployment-a-b-deployment

Usage
===========
```
./test-routes.py https://httpd-v1-farid-split.ocp-a.zu2.dev.travelport.io/ 10
```

The script is very basic and expects the text returned from the route to be used as a key for keeping stats.

Simple usage is to have different deployments return 'v1' or 'v2' for example.

Requirements
===========
The prettytable python module is its only requirement.


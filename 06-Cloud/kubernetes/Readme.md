# Kubernetes
Kubernetes is for multiple computers what Linux delivers for a single PC. It is a vast set of APIs and functions to create distributed runtime environments for applications. It can run anything that you can package into Docker container(s). It is agnostic to development technologies and cloud providers. So it is a good bet to run software on maintainable environments.

## Pre-requisites
* Running Kubernetes (K8s) cluster
* K3s is a good example to setup a cluster locally quickly
* Make sure you have a cluster config YAML file available
* for all examples you can create/use the same virtual environment like so
  ```bash
  deactivate # turn off any other virtual environment
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

# Examples

## Documenting Clusters
When you have a running cluster, it would be nice, to generate a webpage, that shows you all apps currently deployed. This example is creating HTML tables with app names and ingress paths.

### How to run
Activate virtual environment from above.
  ```bash
  cd documenting_clusters
  python convert_ingress_html.py
  ```


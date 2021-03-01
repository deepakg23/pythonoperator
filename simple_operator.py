import kopf
import kubernetes
import yaml
import logging
import sys
import time

log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)

@kopf.on.create('example.org', 'v1', 'deepak')
def create_fn(body, spec, **kwargs):
    log.info("Operator create function called")
    print(f"A handler is called with body: {body}")
    
    # Get info from resource object
    size = spec['size'] 
    name = body['metadata']['name'] 
    namespace = body['metadata']['namespace'] 
    image = 'nginx'
      
    if not size: 
        raise kopf.HandlerFatalError(f"size must be set. Got {size}.") 
    # Pod template 
    pod = {'apiVersion': 'v1', 'metadata': {'name' : name, 'labels': {'app': 'deepak'}},'spec': {'containers': [ { 'image': image, 'name': name }]}}
    
    # Make the Pod for resource object 
    kopf.adopt(pod, owner=body)  
   
    # Object used to communicate with the API Server 
    api = kubernetes.client.CoreV1Api() 

    # Create Pod 
    obj = api.create_namespaced_pod(namespace, pod) 
    print(f"Pod {obj.metadata.name} created") 
    
    # Update status 
    msg = f"Pod created for resource object {name}" 
    return {'message': msg}

@kopf.on.delete('example.org', 'v1', 'deepak') 
def delete(body, **kwargs):
    log.info("Operator delete function called") 
    msg = f"nginx {body['metadata']['name']} and its Pod deleted" 
    return {'message': msg} 

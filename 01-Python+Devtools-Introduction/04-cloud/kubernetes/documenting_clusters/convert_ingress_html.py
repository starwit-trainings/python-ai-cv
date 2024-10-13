from kubernetes import client, config

ingress_data = {}

def query_cluster():
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

    #v1 = client.CoreV1Api()
    #print("Listing pods with their IPs:")
    #ret = v1.list_pod_for_all_namespaces(watch=False)
    #for i in ret.items:
    #    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    v1 = client.NetworkingV1Api()
    ret = v1.list_ingress_for_all_namespaces()
    for ingress in ret.items:
        extract_ingress_summary(ingress)

def extract_ingress_summary(ingress):
    name = ingress.metadata.name 
    ingress_paths = []
    spec = ingress.spec
    for rule in spec.rules:
        for path_spec in rule.http.paths:
            ingress_paths.append(check_if_tls(spec,rule.host) + rule.host + path_spec.path)
    ingress_data[name] = ingress_paths

def check_if_tls(spec, host):
    if(spec.tls != None):
        for tls_host in spec.tls[0].hosts:
            if(tls_host == host):
                return "https://"
    return "http://"


def generate_html_table():
    result = "<table>"
    result += "<tr>" + "<td>App</td><td>Path</td>"  + "</tr>"
    for entry in ingress_data:
        result += "<tr>"
        for path in ingress_data[entry]:
            result += "<td>" + entry + "</td>"+ "<td><a href=\"" + path + "\">" + path + "</td>"
        result += "</tr>"
    result += "</table>"
    return result

if __name__ == '__main__':
    query_cluster()
    print(generate_html_table())
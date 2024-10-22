import dns.resolver
import pprint as pp

domains = ['yahoo.com', 'google.com', 'python.org', 'starwit.de']

def check_mx(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        for rdata in answers:
            print('Host', rdata.exchange, 'has preference', rdata.preference)
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
    except dns.resolver.NoAnswer:
        print(f"No MX records found for {domain}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def reverse_dns(ip_address):
    domain = dns.reversename.from_address(ip_address)
    print(domain)

def get_nameservers(domain):
    ns_records = dns.resolver.resolve(domain, 'NS')
    for ns in ns_records:
        print(ns.target)

print("******* Domain examples, MX records")
for d in domains:
    check_mx(d)

print("******* Reverse DNS")
reverse_dns('85.13.133.81')

print("******* Nameservers")
for d in domains:
    print(f"Nameservers for {d}:")
    get_nameservers(d)


# This script uses a DNS library to make requests
# btw DNS is still very useful :)

import dns.resolver

answers = dns.resolver.resolve('dnspython.org', 'MX')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)

domain = "starwit-technologies.de"

# Google's public DNS server
resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8']

try:
    # Query for the A record of the domain
    answer = resolver.resolve(domain, 'A')
    # Print the result
    for ip in answer:
        print(f"{domain} has address {ip}")
except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
    print(f"No answer found for {domain}")
except dns.exception.Timeout:
    print(f"Timeout while querying {domain}")
except dns.resolver.YXDOMAIN:
    print(f"Y-X Domain error for {domain}")
except Exception as e:
    print(f"An error occurred: {e}")
import whois # pip install python-whois

def is_registered(domain_name):
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)



domain_name = "google.com"
if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    # print the registrar
    print("Domain registrar:", whois_info.registrar)
    # print the WHOIS server
    print("WHOIS server:", whois_info.whois_server)
    # get the creation time
    print("Domain creation date:", whois_info.creation_date)
    # get expiration date
    print("Expiration date:", whois_info.expiration_date)
    # print all other info
    print(whois_info)

if __name__ == "__main__":
    # list of registered & non registered domains to test our function
    domains = [
        "thepythoncode.com",
        "google.com",
        "github.com",
        "unknownrandomdomain.com",
        "notregistered.co"
    ]
    # iterate over domains
    for domain in domains:
        print(domain, "is registered" if is_registered(domain) else "is not registered")
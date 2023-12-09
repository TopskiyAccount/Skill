input_domain = input()
domain_parts = []
current_subdomain = ''

while True:
    if len(input_domain) > 0:
        character = input_domain[0]
        if character != '.':
            current_subdomain += character
            input_domain = input_domain[1:]
        else:
            domain_parts.append(current_subdomain)
            input_domain = input_domain[1:]
            current_subdomain = ''
    else:
        domain_parts.append(current_subdomain)
        break

for part in reversed(domain_parts):
    print(part)

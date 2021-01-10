import re


def not_parsed():
    return {'parsed': False}

def parsed(street, housenumber):
    return {'parsed': True, 'street': street.strip(), 'housenumber': housenumber.strip()}

def separated_by_comma_rule(address):
    if ',' not in address:
        return not_parsed()

    parts = address.split(',', 1)
    part0_has_digits = any(i.isdigit() for i in parts[0])
    part1_has_digits = any(i.isdigit() for i in parts[1])

    if part0_has_digits and part1_has_digits:
        return parsed(max(parts[0], parts[1], key=len), min(parts[0], parts[1], key=len))
    elif part0_has_digits:
        return parsed(parts[1], parts[0])
    else:
        return parsed(parts[0], parts[1])

def everything_after_first_digit_is_housenumber_rule(address):     
    parts = re.split(r'(^[^\d]+)', address)[1:]
    if len(parts) != 2:
        return not_parsed()

    street = parts[0]
    housenumber = parts[1] if len(parts) > 1 else None
    return parsed(street, housenumber)

def parse_address(address):
    if address is None:
        return None
    
    parse_rules = [
        separated_by_comma_rule,
        everything_after_first_digit_is_housenumber_rule
    ]

    for rule in parse_rules:
        result = rule(address)
        if result['parsed']:
            return { 'street': result['street'], 'housenumber': result['housenumber'] }
    
    # address couldn't be parsed
    return None


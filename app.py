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

def starts_with_number_rule(address):     
    if not address[0].isdigit():
        return not_parsed()
    
    parts = address.split(' ', 1)
    return parsed(parts[1], parts[0])
    
def housenumber_separator_rule(address):     
    # TODO: add complete list of lower-cased separators in different languages
    separators = [' no ', ' nr. ']
    
    for sep in separators:
        idx = address.lower().find(sep)
        if idx != -1:
            return parsed(address[0:idx], address[idx + 1:])

    return not_parsed()

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
        starts_with_number_rule,
        housenumber_separator_rule,
        everything_after_first_digit_is_housenumber_rule
    ]

    for rule in parse_rules:
        result = rule(address)
        if result['parsed']:
            return { 'street': result['street'], 'housenumber': result['housenumber'] }
    
    # address couldn't be parsed
    return None


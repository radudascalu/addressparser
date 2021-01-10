import re

def parse_address(address):
    if address is None:
        return None

    parts = re.split(r'(^[^\d]+)', address)[1:]
    return {
        'street': parts[0].strip(),
        'housenumber': parts[1].strip() if len(parts) > 1 else None
    }
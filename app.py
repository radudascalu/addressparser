def parse_address(address):
    if address is None:
        return None

    parts = address.split(' ')
    return {
        "street": parts[0],
        "housenumber": parts[1] if len(parts) > 1 else None
    }

if __name__ == "__main__":
    print(parse_address('Blaufeldweg 123B'))
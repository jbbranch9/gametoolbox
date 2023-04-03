import unicodedata 

def arrow(direction: str, weight: int = 2) -> str:
        
    directions = {
        'NW': 'NORTH WEST',
        'W': 'LEFTWARDS',
        'SW': 'SOUTH WEST',
        'S': 'DOWNWARDS',
        'SE': 'SOUTH EAST',
        'E': 'RIGHTWARDS',
        'NE': 'NORTH EAST',
        'N': 'UPWARDS',
        None: None,
        }
    
    weights = (
        None,
        'LIGHT',
        '',
        'MEDIUM',
        'HEAVY',
        'VERY HEAVY',
        )
    
    assert weight in range(len(weights))
    assert direction in directions.keys()

    if weight == 0:
        return " "
    elif direction is None:
        return unicodedata.lookup("MIDDLE DOT")
    else:
        return unicodedata.lookup(f"WIDE-HEADED {directions[direction]} {weights[weight]} BARB ARROW".replace("  "," "))


def main():
    print(arrow("N"))


if __name__ == "__main__":
    main()

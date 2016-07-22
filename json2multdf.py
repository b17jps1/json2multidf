import json
import pandas


def decrease_levels(nested_dict):
    
    list_of_levels = [[nested_dict.items()]]

    for level in list_of_levels:
        new_level = list()
        for subdict in level:
            for key, value in subdict:
                if isinstance(value, dict):
                    new_level.append(value.items())
                else:
                    print key
        
        if new_level != list():
            list_of_levels.append(new_level)
    return None


if __name__ == '__main__':
    
    json_file = 'data/fake_data.json'

    with open(json_file, 'r') as d:
        for line in d:
            result = decrease_levels(json.loads(line))


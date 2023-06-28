def visits_from_russia(geo_logs: list) -> list:
    geo_logs_russia = []
    for visit in geo_logs:
        if "Россия" in list(visit.values())[0]:
            geo_logs_russia.append(visit)
    return geo_logs_russia


def unique_dictionary_values(ids: dict) -> list:
    unique_values = set()
    for lists in ids.values():
        for values in lists:
            unique_values.add(values)
    unique_values = list(unique_values)
    unique_values.sort()
    return unique_values


def list_to_dict(basic_list: list) -> dict:
    basic_list.reverse()
    final_dictionary = basic_list[0]
    basic_list.pop(0)
    for value in basic_list:
        final_dictionary = {value: final_dictionary}
    return final_dictionary
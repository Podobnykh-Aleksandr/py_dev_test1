import unittest
from parameterized import parameterized
from main import visits_from_russia, unique_dictionary_values, list_to_dict

FIXTURE_test_visits = [
    (
        [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ],
        [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
    ),
    (
        [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Архангельск', 'Россия']}
        ],
        [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Архангельск', 'Россия']}
        ]
    ),
    (
        [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Курск', 'Россия']},
            {'visit5': ['Архангельск', 'Россия']}
        ],
        [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Курск', 'Россия']},
            {'visit5': ['Архангельск', 'Россия']}
        ]
    )
]
FIXTURE_dictionary_values = [
    (
        {
            'user1': [213, 213, 213, 15, 213],
            'user2': [54, 54, 119, 119, 119],
            'user3': [213, 98, 98, 35]
        },
        [15, 35, 54, 98, 119, 213]
    ),
    (
        {
            'user1': [456, 553, 213, 111, 111],
            'user2': [45, 55, 111, 119, 119],
        },
        [45, 55, 111, 119, 213, 456, 553]
    ),
    (
        {
            'user1': [213, 45, 213, 15, 213],
            'user2': [45, 54, 19, 19, 119],
            'user3': [67, 54, 112, 19, 119],
            'user4': [213, 19, 98, 35]
        },
        [15, 19, 35, 45, 54, 67, 98, 112, 119, 213])
]
FIXTURE_list_to_dict = [
    (
        ['2018-01-01', 'yandex', 'cpc', 100],
        {'2018-01-01': {'yandex': {'cpc': 100}}}
     ),
    (
        ['2018-01-01', 'yandex'],
        {'2018-01-01': 'yandex'}
    ),
    (
        ['2018-01-01', 'yandex', 'cpc', 100, 'pop', 'it'],
        {'2018-01-01': {'yandex': {'cpc': {100: {'pop': 'it'}}}}}
    )
]


class TestFunc(unittest.TestCase):
    @parameterized.expand(FIXTURE_test_visits)
    def test_visits_from_russia(self, geo_logs, reference):
        result = visits_from_russia(geo_logs)

        self.assertListEqual(result, reference)

    @parameterized.expand(FIXTURE_dictionary_values)
    def test_unique_dictionary_values(self, ids, reference):
        result = unique_dictionary_values(ids)

        self.assertListEqual(result, reference)

    @parameterized.expand(FIXTURE_list_to_dict)
    def test_visits_list_to_dict(self, basic_list, reference):
        result = list_to_dict(basic_list)

        self.assertDictEqual(result, reference)
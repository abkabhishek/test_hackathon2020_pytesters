from core.common import Com
import requests
import operator
import json
from collections import OrderedDict

class APITest(object):
    driver = None

    def __init__(self, driver):
        self.response_code = self.response.status_code
        self.response = requests.get(url="https://api.covid19india.org/data.json")
        APITest.driver = driver
        self.com = Com(driver)

    def get_url(self):
        print(self.response_code)

    """Returns output in dictionary format """
    """{'Punjab': {'fertility_ratio': 3.140361536094432, 'confirmed': '126737', 'active': '6592', 'recovered': '116165'}, 
        'Maharashtra': {'fertility_ratio': 2.6332720413283233, 'confirmed': '1576062', 'active': '189715', 'recovered': '1344368'}, 
        'Gujarat': {'fertility_ratio': 2.2987921815664807, 'confirmed': '157474', 'active': '14605', 'recovered': '139249'}, 'West Bengal': {'fertility_ratio': 1.8937507184183304, 'confirmed': '313188', 'active': '32500', 'recovered': '274757'}} """

    def fetch_get_details(self, valuecount):
        states_data = {}
        state_fertility = {}
        result = {}
        if self.response_code == 200:
            response_json = self.response.json()
            states = response_json['statewise']
            for state in states:
                states_data[state['state']] = state
                confir = int(states_data[state['state']]['confirmed'])
                deat = int(states_data[state['state']]['deaths'])
                if confir:
                    states_data[state['state']]['fertility_ratio'] = (deat / confir) * 100
                else:
                    states_data[state['state']]['fertility_ratio'] = 0
            for item in states_data.items():
                state_fertility[item[0]] = item[1]['fertility_ratio']
            order_state_fertility = OrderedDict(state_fertility)
            order_state_fertility = dict(
                sorted(order_state_fertility.items(), key=operator.itemgetter(1), reverse=True))
            for item in order_state_fertility.items():
                result[item[0]] = {'fertility_ratio': item[1], 'confirmed': states_data[item[0]]['confirmed'],
                                   'active': states_data[item[0]]['active'],
                                   'recovered': states_data[item[0]]['recovered']}
                valuecount -= 1
                if valuecount < 0:
                    break
            print(result)
        else:
            print('Invalid response', self.response_code)

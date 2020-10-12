from ./astroquery.jplhorizons.core import Horizons
from ./astropy.time.core import Time
from ./astropy.time.core import TimeDelta
import ./yaml
import time
import sys
import json

from pprint import pprint

def lambda_handler(event, context):
    to_target = event['to']
    from_target = event['from']
    TIME_DELTA = 600  # ten minutes

    with open('targets.yml', 'r') as stream:
        targets = yaml.load(stream)

    center = f'500@{targets[from_target]}'

    t1 = Time.now()
    dt = TimeDelta(time_delta, format='sec')
    t2 = t1 + dt
    epochs = {
              'start': t1.isot,
              'stop': t2.isot,
              'step': time_delta - 1  # split into 1 second intervals
              }
    distances = _distance_data(targets[to_target], center, epochs)
    pprint(distances)
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }


def _distance_data(target, center, epochs):
    obj = Horizons(id=target, location=center, epochs=epochs, id_type='id')
    return obj.vectors()

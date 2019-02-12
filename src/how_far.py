from astroquery.jplhorizons import Horizons
from astropy.time import Time
from astropy.time import TimeDelta
import click
import yaml
import time
import sched
import sys

au_to_km = 149598000
time_delta = 600  # ten minutes

with open('targets.yml', 'r') as stream:
    targets = yaml.load(stream)

choices = click.Choice([k for k in targets.keys()])


@click.group()
def how_far():
    """
    How far from here to there?

    how_far is a click application that gathers data from the JPL Horizons database and displays
    a realtime output of the distance between to planetery bodies.
    """
    to


@how_far.command()
@click.argument('target', type=choices, required=True)
@click.option('--from_', '-f', type=choices, default='Earth')
def to(target, from_):
    center = f'500@{targets[from_]}' if not 'Earth' else targets[from_]
    # coordinates need to be in the format '###@###' unless the target is Geocenter
    while True:
        t1 = Time.now()
        dt = TimeDelta(time_delta, format='sec')
        t2 = t1 + dt
        epochs = {
                  'start': t1.isot,
                  'stop': t2.isot,
                  'step': time_delta - 1  # split into 1 second intervals
                  }
        print(center)
        distances = _distance_data(targets[target], center, epochs)
        s = sched.scheduler(time.time, time.sleep)
        for row in distances:
            t = Time(row['datetime_jd'], format='jd', scale='utc')
            range = row['range'] * au_to_km
            s.enterabs(t.unix, 1, _display, argument=(target, from_, range))
        s.run(blocking=True)
        # blocking is true to stop the loop repeating before all scheduled events have run


def _distance_data(target, center, epochs):
    obj = Horizons(id=target, location=center, epochs=epochs, id_type='id')
    return obj.vectors()


def _display(target, center, distance):
    d = '{:,.2f}'.format(distance)
    sys.stdout.write(f"\r{target} is currently {d} km's away from {center}")
    sys.stdout.flush()

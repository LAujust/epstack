from .utils import *


def retrieve_data(ra, dec, radius, start, end, url="https://ep.bao.ac.cn/ep/data_center/api/wxt_observation_data/"):
    data = {
        "ra": ra,
        "dec": dec,
        "radius": radius,
        "start_datetime": start,
        "end_datetime": end
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError('Status code%s'%response.status_code)
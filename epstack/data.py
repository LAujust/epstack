from .utils import *


def retrieve_epdata(ra=None, dec=None, radius=None, start=None, end=None, url="https://ep.bao.ac.cn/ep/data_center/api/wxt_observation_data/"):
    data = {k: v for k, v in locals().items() if v is not None}
    del data['url']

    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError('Status code%s'%response.status_code)
from speedtest import Speedtest

from stoel import main
from stoel.main import save


def test_speedtest():
    assert main.netspeed(Speedtest())


def test_save():
    r = {
        "download": 187920148.1309138,
        "upload": 24749673.293800928,
        "ping": 30.058,
        "server": {
            "url": "http://ookla.arxus.eu:8080/speedtest/upload.php",
            "lat": "50.8500",
            "lon": "4.3500",
            "name": "Brussels",
            "country": "Belgium",
            "cc": "BE",
            "sponsor": "Arxus NV",
            "id": "26887",
            "host": "ookla.arxus.eu:8080",
            "d": 41.15658721175747,
            "latency": 30.058,
        },
        "timestamp": "2022-03-29T06:13:26.074367Z",
        "bytes_sent": 31399936,
        "bytes_received": 235673692,
        "share": None,
        "client": {
            "ip": "84.196.68.119",
            "lat": "51.2192",
            "lon": "4.3917",
            "isp": "Telenet",
            "isprating": "3.7",
            "rating": "0",
            "ispdlavg": "0",
            "ispulavg": "0",
            "loggedin": "0",
            "country": "BE",
        },
    }
    save(r)

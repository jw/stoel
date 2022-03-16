from speedtest import Speedtest

from teleslet import main


def test_speedtest():
    assert main.netspeed(Speedtest())

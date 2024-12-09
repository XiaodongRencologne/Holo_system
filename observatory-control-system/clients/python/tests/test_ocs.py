import pytest
from astropy.coordinates import SkyCoord, EarthLocation, Angle
from astropy import units as u
from ocs import observatory_control_system
import datetime, time
import random
import socket, struct


def test_status():
    #
    ocs = observatory_control_system(
        url="https://127.0.0.1:5600",
        server_cert="../../tls/server.cert.pem",
        client_cert="../../tls/client.cert.pem",
        client_key="../../tls/client.key.pem",
    )
    ocs.get_status()
    print(ocs.status)


# track coord


def test_track():
    ocs = observatory_control_system(
        url="https://127.0.0.1:5600",
        server_cert="../../tls/server.cert.pem",
        client_cert="../../tls/client.cert.pem",
        client_key="../../tls/client.key.pem",
    )
    star_position = SkyCoord(140, 30, unit=(u.deg, u.deg), frame="icrs")
    response = ocs.track(star_position)


def test_move():
    ocs = observatory_control_system(
        url="https://127.0.0.1:5600",
        server_cert="../../tls/server.cert.pem",
        client_cert="../../tls/client.cert.pem",
        client_key="../../tls/client.key.pem",
    )
    # move to an az/ele
    ocs.move_to(80.0, 40.0)
    #


def test_azi_scan():
    # azimuth_scan
    ocs = observatory_control_system(
        url="https://127.0.0.1:5600",
        server_cert="../../tls/server.cert.pem",
        client_cert="../../tls/client.cert.pem",
        client_key="../../tls/client.key.pem",
    )
    start_dt = datetime.datetime.now() + datetime.timedelta(seconds=10)
    start_time = float(f"{time.mktime(start_dt.timetuple()):3.5f}")
    ocs.azimuth_scan(
        start_time,
        elevation=60,
        azimuth_range=[110, 130],
        num_scans=20,
        turnaround_time=30,
        speed=0.8,
    )


def test_path_horizon():
    # azimuth_scan
    ocs = observatory_control_system(
        url="https://127.0.0.1:5600",
        server_cert="../../tls/server.cert.pem",
        client_cert="../../tls/client.cert.pem",
        client_key="../../tls/client.key.pem",
    )
    start_dt = datetime.datetime.now() + datetime.timedelta(seconds=10)
    data = {
        "start_time": float(f"{time.mktime(start_dt.timetuple()):3.5f}"),
        "coordsys": "Horizon",
        "points": [
            [0, 103 + random.randint(0, 9), 50 + random.randint(0, 9), 0.5, 0.5],
            [15, 106 + random.randint(0, 9), 55 + random.randint(0, 9), 0.5, 0.5],
            [30, 109 + random.randint(0, 9), 60 + random.randint(0, 9), 0.5, 0.5],
            [45, 112 + random.randint(0, 9), 65 + random.randint(0, 9), 0.5, 0.5],
        ],
    }
    #
    ocs.scan_pattern(data)


def test_position_broadcast():
    ocs = observatory_control_system(
        url="https://127.0.0.1:5600",
        server_cert="../../tls/server.cert.pem",
        client_cert="../../tls/client.cert.pem",
        client_key="../../tls/client.key.pem",
    )
    udp_host = "127.0.0.1"
    udp_port = 5601
    response = ocs.position_broadcast(udp_host, udp_port)
    print(response)
    # listen for data on host.name:5601 for ten cycles
    # setup udp socket and listen for data
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the host and port
    sock.bind((udp_host, udp_port))
    print(f"Listening for UDP data on {udp_host}:{udp_port}")
    i = 0
    while i < 10:
        # Receive data from the socket
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        data_parsed = list(struct.unpack("<" + "".join(["Lddddddddd"] * 10), data))
        entries = [data_parsed[i : i + 10] for i in range(0, 100, 10)]
        print(f"Received message: {entries} from {addr}")
        i += 1
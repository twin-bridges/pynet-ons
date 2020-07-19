import os
import pytest
from jnpr.junos import Device


@pytest.fixture(scope="module")
def pyez_connect():
    """Establish a PyEZ connection."""
    password = os.environ["JNPR_PASSWORD"]
    srx2 = {"host": "srx2.lasthop.io", "user": "pyclass", "password": password}
    device = Device(**srx2)
    device.open()
    return device

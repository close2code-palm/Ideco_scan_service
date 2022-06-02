"""Scans machinery
run_scan perfoming scan by
multiple calls scan_port"""

import asyncio
import ipaddress
# import syslog
from typing import List, Tuple


async def scan_port(ip: ipaddress, port: int) -> Tuple[str, int]:
    """Handling one connection per call"""
    connection = asyncio.open_connection(ip, port)
    # syslog.syslog(syslog.LOG_DEBUG, f'Scanning port {port} on {ip}')
    try:
        await asyncio.wait_for(
            connection, timeout=4)
        # syslog.syslog(f'Port {port} is open')  # As it usually the case, INFO here
        return 'open', port
    except (asyncio.TimeoutError, OSError, ConnectionRefusedError) as err:
        # syslog.syslog(syslog.LOG_DEBUG, 'Port closed')
        return 'closed', port


async def run_scan(ip: ipaddress, start_port: int, end_port: int) -> List[Tuple[str, int]]:
    """Makes full scan with given parameters"""
    # syslog.syslog(f'Started scanning {ip}')
    tasks = [asyncio.create_task(scan_port(ip, p)) for p in range(start_port, end_port + 1)]
    responses = await asyncio.gather(*tasks)
    # syslog.syslog(f'Finished scanning {ip}')
    return responses

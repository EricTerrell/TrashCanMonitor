"""
  TrashCanMonitor
  (C) Copyright 2021, Eric Bergman-Terrell

  This file is part of TrashCanMonitor.

  SyncAndVerify is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    SyncAndVerify is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    See the GNU General Public License: <http://www.gnu.org/licenses/>.
"""

import datetime
import json
import sys
import time
import dns.resolver
import requests
from pythonping import ping

header = False


def print_usage_and_exit():
    print('usage: {seconds between samples: e.g. 60} {log file path: e.g. c:\\temp\\trashcan-stats.csv}')
    sys.exit(1)


def record_stats(target, timeout, count, output):
    global header

    prefix = 'http://192.168.12.1'

    headers = {'Accept': 'application/json',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'User-Agent': 'TrashCanMonitor'}

    device_info = json.loads(requests.get(f'{prefix}/dashboard_device_info_status_web_app.cgi', headers=headers).text)
    radio_status = json.loads(requests.get(f'{prefix}/fastmile_radio_status_web_app.cgi', headers=headers).text)
    statistics = json.loads(requests.get(f'{prefix}/statistics_status_web_app.cgi', headers=headers).text)

    result = ping(target, timeout, count)

    data = [
        ['datetime',
         datetime.datetime.now()],

        ['ping_time',
         result.rtt_avg_ms],

        ['link_status_5g',
         device_info['link_status_5G'][0]['linkStatus']],

        ['link_status_lte',
         device_info['link_status_LTE'][0]['linkStatus']],

        ['cellular_bytes_received',
         radio_status['cellular_stats'][0]['BytesReceived']],

        ['cellular_bytes_sent',
         radio_status['cellular_stats'][0]['BytesSent']],

        ['cell_5g_stats_PhysicalCellID',
         radio_status['cell_5G_stats_cfg'][0]['stat']['PhysicalCellID']],

        ['cell_5g_stats_SNRCurrent',
         radio_status['cell_5G_stats_cfg'][0]['stat']['SNRCurrent']],

        ['cell_5g_stats_RSRPCurrent',
         radio_status['cell_5G_stats_cfg'][0]['stat']['RSRPCurrent']],

        ['cell_5g_stats_RSRQCurrent',
         radio_status['cell_5G_stats_cfg'][0]['stat']['RSRQCurrent']],

        ['cell_5g_stats_RSRPStrengthIndexCurrent',
         radio_status['cell_5G_stats_cfg'][0]['stat']['RSRPStrengthIndexCurrent']],

        ['cell_5g_stats_Downlink_NR_ARFCN',
         radio_status['cell_5G_stats_cfg'][0]['stat']['Downlink_NR_ARFCN']],

        ['cell_5g_stats_Band',
         radio_status['cell_5G_stats_cfg'][0]['stat']['Band']],

        ['cell_lte_stats_PhysicalCellID',
         radio_status['cell_LTE_stats_cfg'][0]['stat']['PhysicalCellID']],

        ['cell_lte_stats_SNRCurrent',
         radio_status['cell_LTE_stats_cfg'][0]['stat']['SNRCurrent']],

        ['cell_lte_stats_RSRPCurrent',
         radio_status['cell_LTE_stats_cfg'][0]['stat']['RSRPCurrent']],

        ['cell_lte_stats_RSRQCurrent',
         radio_status['cell_LTE_stats_cfg'][0]['stat']['RSRQCurrent']],

        ['cell_lte_stats_RSRPStrengthIndexCurrent',
         radio_status['cell_LTE_stats_cfg'][0]['stat']['RSRPStrengthIndexCurrent']],

        ['cell_lte_stats_DownlinkEarfcn',
         radio_status['cell_LTE_stats_cfg'][0]['stat']['DownlinkEarfcn']],

        ['cell_lte_stats_Band',
         radio_status['cell_LTE_stats_cfg'][0]['stat']['Band']],

        ['cellular_stats_bytes_sent',
         statistics['WAN'][0]['EthernetBytesSent']],

        ['cellular_stats_bytes_received',
         statistics['WAN'][0]['EthernetBytesReceived']],

        ['cellular_stats_packets_sent',
         statistics['WAN'][0]['EthernetPacketsSent']],

        ['cellular_stats_packets_received',
         statistics['WAN'][0]['EthernetPacketsReceived']],

        ['cellular_stats_packets_errored',
         statistics['WAN'][0]['X_ALU_PacketsErrored']],

        ['cellular_stats_packets_dropped',
         statistics['WAN'][0]['X_ALU_PacketsDropped']]
    ]

    column_names = []
    values = []

    for item in data:
        column_names.append(item[0])
        values.append(str(item[1]))

    if not header:
        header_line = ','.join(column_names)
        print(header_line)
        output.write(f'{header_line}\n')

        header = True

    values_line = ','.join(values)

    print(values_line)
    output.write(f'{values_line}\n')
    output.flush()


def main():
    if len(sys.argv) != 3:
        print_usage_and_exit()

    output_file_path = sys.argv[2]
    wait_seconds = int(sys.argv[1])

    print()
    print(f'wait_seconds:     {wait_seconds}')
    print(f'output_file_path: {output_file_path}')
    print()

    output = open(output_file_path, "w")

    target_domain = 'example.com'

    timeout_seconds = 10
    simultaneous_pings = 1

    result = dns.resolver.query(target_domain, 'A')

    if result.rrset is not None:
        ping_ip_address = result.rrset.items[0].address

        while True:
            record_stats(ping_ip_address, timeout_seconds, simultaneous_pings, output)
            time.sleep(wait_seconds)


main()

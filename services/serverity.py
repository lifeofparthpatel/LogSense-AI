from typing import List

def classify_serverity(log: List[str]):
    serverity = {'CRITICAL': 0, 'ERROR': 0, 'WARNING': 0, 'INFO': 0}
    for entry in log:
        if 'CRITICAL' in entry:
            serverity['CRITICAL'] += 1
        elif 'ERROR' in entry:
            serverity['ERROR'] += 1
        elif 'WARNING' in entry:
            serverity['WARNING'] += 1
        elif 'INFO' in entry:
            serverity['INFO'] += 1
    return serverity
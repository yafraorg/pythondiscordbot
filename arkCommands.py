#

import os
import random
import subprocess

def status():
    result = subprocess.run(['arkmanager', 'status', '@all'], stdout=subprocess.PIPE)
    return result


def dig():
    result = subprocess.run(['gamedig', '--type', 'arkse', '--host', 'localhost', '--port', '27015'], stdout=subprocess.PIPE)
    return result

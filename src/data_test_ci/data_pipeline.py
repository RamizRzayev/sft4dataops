#from typing import Any, Dict, List
#import psycopg2.extras as p
from data_test_ci.utils.db import WarehouseConnection
from data_test_ci.utils.sde_config import get_warehouse_creds
import os

def run_sql_scripts() -> None:
    full_path = os.path.join(os.path.dirname(__file__), 'sql')
    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        for file in sorted(os.listdir(full_path)):
            with open(os.path.join(full_path, file),'r') as f:
                curr.execute(f.read())



def run() -> None:
    run_sql_scripts()


if __name__ == '__main__':
    run()

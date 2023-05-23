import os

from data_test_ci.utils.db import DBConnection


def get_warehouse_creds() -> DBConnection:
    return DBConnection(
        user=os.getenv('WAREHOUSE_USER', 'sdeuser'),
        password=os.getenv('WAREHOUSE_PASSWORD', 'sdepassword1234'),
        db=os.getenv('WAREHOUSE_DB', 'finance'),
        host=os.getenv('WAREHOUSE_HOST', 'localhost'),
        port=int(os.getenv('WAREHOUSE_PORT', 5432)),
    )

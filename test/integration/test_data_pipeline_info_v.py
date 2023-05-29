#import psycopg2.extras as p 
from data_test_ci.data_pipeline import run
from data_test_ci.utils.db import WarehouseConnection
from data_test_ci.utils.sde_config import get_warehouse_creds

class TestDataPipeline_info_v:


    def setup_method(self, test_data_pipeline):
        None
        #comment         
    def teardown_method(self, test_data_pipeline):
        None



    def test_data_pipeline(self):
        run()
        names_expected=['dept_name','emp_name']
        with WarehouseConnection(
                get_warehouse_creds()
        ).managed_cursor() as curr:

            curr.execute("Select * from info_v")
            column_names = list(map(lambda x: x[0], curr.description))

        assert column_names == names_expected

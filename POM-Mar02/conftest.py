import pytest
from pyjavaproperties import Properties

from pages.basepage import Base
from testresources import Constants

prod = Properties()
obj_list = []

@pytest.fixture(scope='function', autouse=True)
def base_fixture():
    try:
        prodpath = open(Constants.ENVIRONMENT_PROPERTIES)
        prod.load(prodpath)
        base = Base()
        obj_list.append(base)
    except Exception:
        pass
    yield locals()
    print("ending the testcase")
    base.quitbrowser()



# scope = default, function, module, class
# arithmetic operation
# user input
# operation
# result


import pytest


if __name__ == "__main__":
    pytest.main(["-vs", "./interface/test_interface.py", "-m=smoke or age"])
    # 根目录下的all.py 可以去执行文件夹内的测试用例
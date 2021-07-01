import  pytest
import time
# def test_005_interface():
#     print("chinese")


class TestInterface():


    def test_003_interface_qq(self):
        time.sleep(2)
        assert None
        print("测试interface ing")
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_004_interface(self):
        time.sleep(2)
        print("seleium 测试")
    @pytest.mark.age
    def test_006_interface_qq(self):
        time.sleep(2)
        print("web 测试")

    def test_007_interface(self):
        time.sleep(2)
        assert  None
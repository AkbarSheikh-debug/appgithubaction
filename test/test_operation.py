from src.math_operation import add,sub


def test_add():
  assert add(2,3)==5
  assert add(-1,1)==0
  
def test_sun():
  assert sub(5,3)==2
  assert sub(4,3)==1
  assert sub(3,3)==0
  assert sub(5,3)==2
  
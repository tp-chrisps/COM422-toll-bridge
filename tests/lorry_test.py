from lorry import Lorry

def test_create_lorry_unit():
    lorry = Lorry("abc", 5000)
    assert lorry.reg == "abc" and lorry.weight == 5000

def test_lorry_calculate_fee_happy_unit():
    lorry = Lorry("abc", 8000)
    assert lorry.CalculateFee() == 10.0

def test_lorry_calculate_fee_sad_unit():
    lorry = Lorry("abc", 8001)
    assert lorry.CalculateFee() == 15.0

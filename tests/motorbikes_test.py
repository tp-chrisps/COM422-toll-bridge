from motorbikes import Motorbike
def test_calculate_fee_motorbikes():
    motorbikes = Motorbike("ab22", 300)
    assert motorbikes.CalculateFee() == 3


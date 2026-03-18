from cars import Cars

def test_car_weight_correct():
    testcar = Cars('reg', 1590)
    assert testcar.calculateFee() == 5

def test_car_weight_under():
    testcar = Cars('reg', 1500)
    assert testcar.calculateFee() == 5

def test_car_weight_over():
    testcar = Cars('reg', 1800)
    assert testcar.calculateFee() == 5.2

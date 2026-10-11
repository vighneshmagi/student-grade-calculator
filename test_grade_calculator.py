def test_total_and_percentage():
    marks = [85, 78, 92, 88, 75]
    total = sum(marks)
    percentage = total / 5

    assert total == 418
    assert percentage == 83.6
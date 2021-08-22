while True:
    dais = 1
    stat = float(input('Стартовый результат :'))
    finis = float(input('Финальный результат:'))
    if stat <= 0 or finis < 0:
        print('Рузультат должен быть больше нуля')
    else:
        while stat < finis:
            stat += stat * 0.1
            dais += 1
        print(f'Спортсмен достигнет результата через {dais} дней')
        break




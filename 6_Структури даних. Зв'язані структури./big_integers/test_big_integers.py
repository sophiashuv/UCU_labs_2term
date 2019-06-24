from big_integers import BigInteger


class TestBigInteger:
    # setUp
    bigint1 = BigInteger('1')
    bigint2 = BigInteger('0')
    bigint3 = BigInteger('125')
    bigint4 = BigInteger('-35')
    bigint5 = BigInteger('-5000')
    bigint6 = BigInteger('8')
    bigint7 = BigInteger('8')
    bigint8 = BigInteger('35')

    # test_compare
    assert (bigint6 == bigint7) == True
    assert (bigint4 != bigint8) == True
    assert (bigint1 > bigint2) == True
    assert (bigint6 > bigint4) == True
    assert (bigint1 > bigint2) == True
    assert (bigint6 >= bigint4) == True
    assert (bigint6 >= bigint7) == True
    assert (bigint2 < bigint1) == True
    assert (bigint4 < bigint6) == True
    assert (bigint2 < bigint1) == True
    assert (bigint4 <= bigint6) == True
    assert (bigint7 <= bigint6) == True

    # test_add
    assert (bigint6 + bigint7 == BigInteger('16'))
    assert (bigint4 + bigint8 == BigInteger('0'))
    assert (bigint1 + bigint2 == BigInteger('1'))
    assert (bigint6 + bigint4 == BigInteger('-27'))
    assert (bigint8 + bigint7 == BigInteger('43'))
    assert (bigint3 + bigint5 == BigInteger('-4875'))

    # test_sub
    assert (bigint6 - bigint7 == BigInteger('0'))
    assert (bigint4 - bigint8 == BigInteger('-70'))
    assert (bigint1 - bigint2 == BigInteger('1'))
    assert (bigint6 - bigint4 == BigInteger('43'))
    assert (bigint8 - bigint7 == BigInteger('27'))
    assert (bigint3 - bigint5 == BigInteger('5125'))

    # test_mul
    assert (bigint6 * bigint7 == BigInteger('64'))
    assert (bigint4 * bigint8 == BigInteger('-1225'))
    assert (bigint1 * bigint2 == BigInteger('0'))
    assert (bigint6 * bigint4 == BigInteger('-280'))
    assert (bigint6 * bigint7 == BigInteger('64'))
    assert (bigint3 * bigint5 == BigInteger('-625000'))

    # test_floordiv
    assert (bigint4 // bigint8 == BigInteger('-1'))
    assert (bigint6 // bigint4 == BigInteger('-1'))
    assert (bigint3 // bigint5 == BigInteger('-1'))
    assert (bigint5 // bigint3 == BigInteger('-41'))

    # test_mod

    assert (bigint4 % bigint8 == BigInteger('0'))
    assert (bigint6 % bigint4 == BigInteger('-27'))
    assert (bigint3 % bigint5 == BigInteger('-4875'))
    assert (bigint5 % bigint3 == BigInteger('125'))

    # est_pow
    assert (bigint5 ** BigInteger("1") == BigInteger('-5000'))
    assert (bigint5 ** BigInteger("2") == BigInteger('25000000'))
    assert (bigint5 ** BigInteger("3") == BigInteger('-125000000000'))

    # test_and
    assert (bigint1 & bigint2 == BigInteger('0'))
    assert (BigInteger('8') & BigInteger('8') == BigInteger('8'))
    assert (BigInteger('8') & BigInteger('35') == BigInteger('0'))

    # test_or
    assert (BigInteger('1') | BigInteger('0') == BigInteger('1'))
    assert (BigInteger('8') | BigInteger('8') == BigInteger('8'))
    assert (BigInteger('8') | BigInteger('35') == BigInteger('43'))

    # test_xor
    assert (BigInteger('1') ^ BigInteger('0') == BigInteger('1'))
    assert (BigInteger('8') ^ BigInteger('8') == BigInteger('0'))
    assert (BigInteger('8') ^ BigInteger('35') == BigInteger('43'))

    # test_rshift
    assert (BigInteger('1') >> BigInteger('0') == BigInteger('1'))
    assert (BigInteger('8') >> BigInteger('8') == BigInteger('0'))
    assert (BigInteger('8') >> BigInteger('35') == BigInteger('0'))

    # test_lshift
    assert (BigInteger('1') << BigInteger('0') == BigInteger('1'))
    assert (BigInteger('8') << BigInteger('8') == BigInteger('2048'))
    assert (BigInteger('8') << BigInteger('35') == BigInteger('274877906944'))

    # test_operations
    assert ((BigInteger('8') == BigInteger('8')) == (BigInteger('8').comparable(BigInteger('8'), "==")))
    assert ((BigInteger('8') != BigInteger('8')) == (BigInteger('8').comparable(BigInteger('8'), "!=")))
    assert ((BigInteger('8') > BigInteger('8')) == (BigInteger('8').comparable(BigInteger('8'), ">")))
    assert ((BigInteger('8') >= BigInteger('8')) == (BigInteger('8').comparable(BigInteger('8'), ">=")))
    assert ((BigInteger('8') < BigInteger('8')) == (BigInteger('8').comparable(BigInteger('8'), "<")))
    assert ((BigInteger('8') <= BigInteger('8')) == (BigInteger('8').comparable(BigInteger('8'), "<=")))
    assert ((BigInteger('8') + BigInteger('8')) == (BigInteger('8').arithmetic(BigInteger('8'), "+")))
    assert ((BigInteger('8') * BigInteger('8')) == (BigInteger('8').arithmetic(BigInteger('8'), "*")))
    assert ((BigInteger('8') // BigInteger('8')) == (BigInteger('8').arithmetic(BigInteger('8'), "//")))
    assert ((BigInteger('8') % BigInteger('8')) == (BigInteger('8').arithmetic(BigInteger('8'), "%")))
    assert ((BigInteger('8') ** BigInteger('8')) == (BigInteger('8').arithmetic(BigInteger('8'), "**")))
    assert ((BigInteger('8') & BigInteger('8')) == (BigInteger('8').bitwise_ops(BigInteger('8'), "&")))
    assert ((BigInteger('8') | BigInteger('8')) == (BigInteger('8').bitwise_ops(BigInteger('8'), "|")))
    assert ((BigInteger('8') ^ BigInteger('8')) == (BigInteger('8').bitwise_ops(BigInteger('8'), "^")))
    assert ((BigInteger('8') >> BigInteger('8')) == (BigInteger('8').bitwise_ops(BigInteger('8'), ">>")))
    assert ((BigInteger('8') << BigInteger('8')) == (BigInteger('8').bitwise_ops(BigInteger('8'), "<<")))
    print('Passed.')


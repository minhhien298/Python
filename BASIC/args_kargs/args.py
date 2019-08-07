def test_var_args(normal_arg, *argv):
    print("first normal arg:", normal_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test', "love")
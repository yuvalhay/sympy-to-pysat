def sympy_to_pysat(statement, dict, bool_val=True):
    if not is_cnf(to_cnf(statement, simplify=bool_val, force=bool_val)):
        print("statement is not CNF")
        return 0
    else: cnf_s = to_cnf(statement, simplify=bool_val, force=bool_val)

    cnf_args = cnf_s.args
    and_clause = []
    for arg in cnf_args:
        str_arg = str(arg)
        str_arg_splited = str_arg.split(" | ")
        or_clause = []
        for symbol in str_arg_splited:
            if "~" in symbol:
                or_clause.append(-dict[symbol[1:]])  
            else: or_clause.append(dict[symbol])

        and_clause.append(or_clause)
    
    return and_clause

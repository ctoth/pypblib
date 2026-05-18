from pypblib import pblib


def main():
    assert pblib.GEQ != pblib.LEQ
    assert str(pblib.WeightedLit(1, 2)) == "(1, 2)"

    formula = []
    max_var = pblib.Pb2cnf().encode_at_most_k([1, 2], 1, formula, 3)
    assert isinstance(max_var, int)
    assert formula

    config = pblib.PBConfig()
    constraint = pblib.PBConstraint([pblib.WeightedLit(1, 1)], pblib.LEQ, 1)
    database = pblib.VectorClauseDatabase(config)
    auxvars = pblib.AuxVarManager(2)
    pblib.Pb2cnf(config).encode(constraint, database, auxvars)
    assert database.get_num_clauses() >= 0


if __name__ == "__main__":
    main()

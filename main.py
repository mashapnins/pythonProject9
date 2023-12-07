from sympy.logic.boolalg import to_cnf
from sympy.logic.boolalg import Or, And, Implies, Not, Equivalent
from sympy.logic.boolalg import truth_table

def build_truth_table(formula):
    formula = to_cnf(formula, True)
    variables = formula.atoms()
    rows = list(truth_table(formula, variables))

    header = list(variables) + [formula]
    table = [header]

    for row in rows:
        values = [row[var] for var in variables] + [row[formula]]
        table.append(values)

    return table

def main():
    formula = input("Введите логическую формулу: ")
    truth_table = build_truth_table(formula)

    # Вывод заголовка
    header = truth_table[0]
    for col in header:
        print(f"{col:^10}", end=" | ")
    print()

    # Вывод разделительной строки
    print("-" * (10 * len(header) + len(header) - 1))

    # Вывод данных таблицы
    for row in truth_table[1:]:
        for col in row:
            print(f"{col:^10}", end=" | ")
        print()

if __name__ == "__main__":
    main()

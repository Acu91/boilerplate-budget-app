def tot_spent(categories):
    tot = 0
    for category in categories:
        tot = tot + category.get_expense()

    return tot


def create_spend_chart(categories):
    char = ""
    char = ("Percentage spent by category\n")
    spaces = " "
    i = 100
    while i >= 0:
        for n in range(len(categories)):
            start = int(categories[n].get_expense())
            tot=0
            for category in categories:
                tot = tot + category.get_expense()
            perc = round((start/tot) * 100,0)
            if i > perc:
                spaces = spaces + "   "
            else:
                spaces = spaces + "o  "
        char = (char + str(i).rjust(3) + "|" + spaces + "\n")
        spaces = " "
        i = i - 10

    char = char + "    -"
    for item in range(len(categories)):
        char = char + "---"
    char = char + "\n"

    names = []
    for category in categories:
        names.append(category.budget)

    maxlen = max(names, key=len)
    namestr = ""
    name_vert = ""
    for x in range(len(maxlen)):
        namestr = "     "
        for name in names:
            if x >= len(name):
                namestr = namestr + "   "
            else:
                namestr = namestr + name[x] + "  "

        if (x != len(maxlen) - 1):
            namestr = namestr + "\n"

        name_vert = name_vert + (namestr)

    char = char + name_vert

    return char


class Category:
    def __init__(self, budget):
        self.budget = budget
        self.ledger = list()

    def __str__(self):
        output = ""
        title = ""
        title = f"{self.budget:*^30}\n"

        for item in self.ledger:
            output += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

        output = title + output + "Total: " + str(self.get_balance())

        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total = total + item["amount"]

        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.budget)
            category.deposit(amount, "Transfer from " + self.budget)
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def get_expense(self):
        total = 0
        for i in self.ledger:
            if i["amount"] > 0:
                continue
            total = total + i["amount"]
        return total

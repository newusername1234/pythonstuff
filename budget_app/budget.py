from collections import defaultdict

class Category:
    def __init__(self,name):
        self.ledger = list()
        self.name = name
        self.balance = 0

    def deposit(self,amount,description=''):
        self.balance += amount
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            self.balance -= amount
            return True
        else:
            print(f'Not enough funds\nBalance:{self.balance}')
            return False

    def get_balance(self):
        return self.balance

    def transfer(self,amount,to_category):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': f'Transfer to {to_category.name}'
            })
            self.balance -= amount
            to_category.receive_funds(amount,self.name)
            return True
        else:
            print(f'Not enough funds\nBalance:{self.balance}')
            return False

    def receive_funds(self,amount,from_category):
        self.balance += amount
        self.ledger.append({
                'amount': amount,
                'description': f'Transfer from {from_category}'
            })

    def check_funds(self,amount):
        if amount < self.balance:
            return True
        return False

    def __str__(self):
        output = ''
        stars = f"{'*'*int(((28-len(self.name))/2))}"
        title = f'{stars} {self.name} {stars}\n'
        output += title

        for entry in self.ledger:
            amount,description = entry.values()
            amount = str(amount)[:7]
            description = description[:23]
            length = len(amount) + len(description)
            if length < 30:
                description += ' ' * (30 - length)
            output += f'{description}{amount}\n'

        output += f'Total: {self.balance}'

        return output

def create_spend_chart(categories):
    percentages = defaultdict(lambda: 0)
    total = 0

    for category in categories:
        for entry in category.ledger:
            if entry['amount'] < 0:
                percentages[category.name] += abs(entry['amount'])
                total += abs(entry['amount'])
    
    for key,value in percentages.items():
        percentages[key] = int(round(percentages[key]/total*100,-1))

    graph = 'Percentage spent by category\n'

    y = ''
    for num in range(100,-1,-10):
        if num == 100:
            y += f'{num}|'
        elif 0 < num < 100:
            y += f' {num}|'
        elif num == 0:
            y += f'  {num}|'    
        for percentage in percentages.values():
            if num > percentage:
                y += '   '
            else:
                y += ' o '
        y += '\n'

    x = '    '
    for category in categories:
        x += '---'
    x += '\n'
    
    for i in range(0,len(max([j.name for j in categories],key=len))):
        x += '    '
        for category in categories:
            try:
                x += f' {category.name[i]} '
            except:
                x += '   '
        x += '\n'

    graph += y + x
    return graph
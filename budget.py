class Category:
    groups = []
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.groups.append({self.name: []})

    def __repr__(self):
        title = f"{self.name.center(30, '*')}\n"
        record = ""
        for item in self._transaction(self.groups, self.get_balance(), "Total: "):
            description = item['description'][0:23]
            if item['description'] != "Total: ":
                amount = f"{item['amount']:>7.2f}"
                record += f"{description:<23}{amount}\n"
            else:
                record += f"{description}{item['amount']:.2f}\n"
        return title + record

    def _transaction(self, record, amount, description):
        for item in record:
            if self.name in item:
                item[self.name].append({'amount':float(amount), 'description':'initial deposit'
                                       if description == 'deposit'
                                       else description})
                return item[self.name]
            else:
                pass

    def deposit(self, amount=0, description=''):
        self._transaction(self.groups, f"{amount}", description)
        self.ledger.append({'amount':amount, 'description':description})    
     
    def withdraw(self, amount=0, description=''):
        if self.check_funds(amount):
            self._transaction(self.groups, f'-{amount}', description)
            self.ledger.append({'amount':-amount, 'description':description})
            return True
        else:
            return False
        
    def check_funds(self, amount=0):
        if self.get_balance() < amount:
            return False
        return True
    
    def get_balance(self):
        total = 0
        for items in self.groups:
            if self.name in items:
                for item in items[self.name]:
                    total += item['amount']
        return float(total)
    
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")            
            return True 
        else:
            return False
        
def create_spend_chart(categories):
    texts = [char.name for char in categories]
    rows = {num: [] for num in range(100, -1, -10)}
    name = "Percentage spent by category"
    withd = []
    for item in categories:
        if item.ledger:
            num = item.get_balance()
            for record in item.ledger:
                if record['amount'] > 0:
                    withd.append(record['amount'] - num)
    percent = list(map(lambda am: (abs(am/round(sum(withd), 2)) * 10 // 1) * 10, withd))
    for val in percent:
        for row in rows:
            if val >= row:
                rows[row].append(" o ")
            else:
                rows[row].append("   ")
    val = f"{'':4}"
    count = 0
    while count < len(max(texts, key=len)):
        for char in texts:
            try:
                val += f"{char[count]:>3}"
            except:
                val += f"{' ':>3}"
        count += 1
        val += f"\n{'':>4}"
    line = format("-"*(3 * len(categories) + 1), '>14')
    values = ""
    for item in rows:
        values += f"{item:>3}| {''.join(rows[item])}\n"
    return f"{name}\n{values}{line}\n{val}"



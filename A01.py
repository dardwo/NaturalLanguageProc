from A01module import Employee, ReceivedInvoice, IssuedInvoice

employees = []
with open("employees.csv", "r") as file:
    for line in file:
        name, surname, salary = line.strip().split(",")
        employees.append(Employee(name, surname, float(salary)))

received_invoices = []
with open("received_invoices.csv", "r") as file:
    for line in file:
        date, amount = line.strip().split(",")
        received_invoices.append(ReceivedInvoice(date, float(amount)))

issued_invoices = []
with open("issued_invoices.csv", "r") as file:
    for line in file:
        date, amount = line.strip().split(",")
        issued_invoices.append(IssuedInvoice(date, float(amount)))

yearly_monthly_balance = {}

monthly_salary = 0
for employee in employees:
    monthly_salary += employee.salary

for invoice in received_invoices:
    date_parts = invoice.date.split("-")
    year, month = date_parts[0], date_parts[1]
    key = (year, month)
    yearly_monthly_balance[key] = yearly_monthly_balance.get(key, 0) + invoice.amount

for invoice in issued_invoices:
    date_parts = invoice.date.split("-")
    year, month = date_parts[0], date_parts[1]
    key = (year, month)
    yearly_monthly_balance[key] = yearly_monthly_balance.get(key, 0) - invoice.amount

for (year, month), balance in yearly_monthly_balance.items():
    yearly_monthly_balance[(year, month)] -= monthly_salary

for (year, month), balance in yearly_monthly_balance.items():
    print(f"Bilans przychodów i wydatków za {year}/{month}: {balance:.2f} PLN")

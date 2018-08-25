salary_table = [{"name": "Huy", "rate": 25, "hours": 14},
                {"name": "Hoa", "rate": 20, "hours": 7},
                {"name": "Tam", "rate": 15, "hours": 20}]

total = 0
for d in salary_table:
    payment = d["rate"] * d['hours']
    total += payment
    print(d["name"], "receives", payment)

print("Total budget is", total)

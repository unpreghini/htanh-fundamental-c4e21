import pyexcel

# 1. Prepare data

data = [
    {
        'name': "Huy",
        'age': 29,
    },
    {
        'name': "Duc",
        'age': 19,
    },
    {
        'name': "Quan",
        'age': 17,
    },
]

# 2. Save
pyexcel.save_as(records=data, dest_file_name="Sample.xlsx")

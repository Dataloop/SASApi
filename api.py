import swat, os
from vars import ACCESS_TOKEN, HOST

swat.options.cas.print_messages = True

print("... starting connection ...")
conn = swat.CAS(HOST,443,'sasadm','lnxsas',protocol='https')
print("Connected",conn.session)

casTable = conn.read_csv("./data/test.csv",casout = dict(name="test1", replace=True))

# conn.Models.evaluate(dataset="test1",params=x,y,z out="out1")

conn.table.fetch(data="out1")

# Report generated
# Llevarlo a la webapp


inMemDF = "test1"

# print(conn.table.tableDetails(
#     level="node",
#     caslib="casuser",
#     name=inMemDF
# ))
#
# print(conn.table.tableDetails(
#     level="block",
#     caslib="casuser",
#     name=inMemDF
# ))

node_data = conn.table.tableDetails(
    level = "block",
    caslib = "casuser",
    name = inMemDF
)["TableDetails"]["Rows"]

print(node_data)

# SCRIPT

conn.table.fetch(table=inMemDF, to=10)

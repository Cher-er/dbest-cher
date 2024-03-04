from dbest.executor.executor import SqlExecutor
from config.config import DbestConfig


config = DbestConfig().get_config()
executor_parameter = config['executor_parameter']
dataset = config['dataset']
dataset_loc = config['dataset_loc']

csv_split_char = executor_parameter['csv_split_char']

if dataset == "flights":
    from schema.schema import flights
    dataset = flights
else:
    print("[Error] Unknown dataset")
    exit()

sql_executor = SqlExecutor()
for parameter in executor_parameter:
    sql_executor.execute(f"set {parameter}={executor_parameter[parameter]}")
table_header = ""
for key in dataset.keys():
    table_header += f"{key}{csv_split_char}"
table_header = table_header[:-1]
sql_executor.execute(f"set table_header='{table_header}'")

sql_executor.execute("drop table flights_dep_delay_distance")
sql_executor.execute(f"create table flights_dep_delay_distance(dep_delay real, distance real) from '{dataset_loc}' group by unique_carrier")
predications = sql_executor.execute("select unique_carrier, avg(dep_delay) from flights_dep_delay_distance where 300 <= distance <= 1000 group by unique_carrier")

print(predications)

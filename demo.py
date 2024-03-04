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

# sql_executor.execute("drop table flights_distance_year_date")
sql_executor.execute(f"create table flights_distance_year_date(distance real, year_date categorical) from '{dataset_loc}'")
predications = sql_executor.execute("select avg(distance) from flights_distance_year_date where distance > 0 and year_date = 2023")

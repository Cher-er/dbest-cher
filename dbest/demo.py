from executor.executor import SqlExecutor
from config.config import DbestConfig


config = DbestConfig().get_config()
executor_parameter = config['executor_parameter']

sql_executor = SqlExecutor()
for parameter in executor_parameter:
    print(parameter)
    # sql_executor.execute(f"")

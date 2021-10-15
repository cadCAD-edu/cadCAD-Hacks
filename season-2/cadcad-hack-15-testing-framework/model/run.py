# cadCAD simulation engine modules
from cadCAD.engine import ExecutionMode, ExecutionContext
from cadCAD.engine import Executor

# cadCAD global simulation configuration list
from cadCAD import configs
import model.config

import pandas as pd


def run():
    exec_context = ExecutionContext()
    simulation = Executor(exec_context=exec_context, configs=configs)
    raw_result, tensor_field, sessions = simulation.execute()
    # Convert raw results to a Pandas DataFrame
    df = pd.DataFrame(raw_result)

    # Insert cadCAD parameters for each configuration into DataFrame
    for config in configs:
        # Get parameters from configuration
        parameters = config.sim_config['M']
        # Get subset index from configuration
        subset_index = config.subset_id
        
        # For each parameter key value pair
        for (key, value) in parameters.items():
            # Select all DataFrame indices where subset == subset_index
            dataframe_indices = df.eval(f'subset == {subset_index}')
            # Assign each parameter key value pair to the DataFrame for the corresponding subset
            df.loc[dataframe_indices, key] = value

    return df


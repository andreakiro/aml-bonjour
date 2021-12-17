

from task_3.pipelines.data_engineering.nodes import separate_data
from kedro.pipeline import Pipeline, node

from .nodes import separate_data

def create_pipeline(**kwargs):
    separate_train_node = node(
        func=separate_data,
        inputs="train_raw",
        outputs=["train_amateur_raw", "train_expert_raw"],
        name="separate_train_node"
    )

    return Pipeline([
        separate_train_node,
    ])
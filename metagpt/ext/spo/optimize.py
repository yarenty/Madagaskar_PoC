from metagpt.ext.spo.components.optimizer import PromptOptimizer
from metagpt.ext.spo.utils.llm_client import SPO_LLM


if __name__ == "__main__":

    SPO_LLM.initialize(
        optimize_kwargs={"model": "claude-3-5-sonnet-20240620", "temperature": 0.7},
        evaluate_kwargs={"model": "gpt-4o-mini", "temperature": 0.3},
        execute_kwargs={"model": "gpt-4o-mini", "temperature": 0}
    )

    optimizer = PromptOptimizer(
        optimized_path="workspace",
        initial_round=1,
        max_rounds=10,
        template="Poem.yaml",
        name="Poem",
        iteration=True,
    )

    optimizer.optimize()
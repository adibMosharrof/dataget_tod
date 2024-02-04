from dotmap import DotMap
from dataclass_csv import DataclassReader
from pathlib import Path
from prompt_manager import NlgPrompt

from tod_csv_data import TodCsvData


class DataGenerator:
    def __init__(self, cfg):
        self.cfg = cfg
        self.prompt_manager = NlgPrompt()

    def read_csv(self) -> list[TodCsvData]:
        with open(self.cfg.csv_file) as f:
            reader = DataclassReader(f, TodCsvData)
            return [r for r in reader]

    def run(self):
        data = self.read_csv()
        all_prompts = []
        for row in data[: self.cfg.num_rows]:
            prompt = self.prompt_manager.get_prompt(
                row.domains,
                row.schema,
                row.context,
            )
            all_prompts.append(prompt)
        out_path = Path(f"{self.cfg.output_dir}/prompts_{self.cfg.num_rows}.txt")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            separator = "".join(["\n", "-" * 20, "\n"])
            f.write(separator.join(all_prompts))


if __name__ == "__main__":
    cfg = DotMap(
        csv_file="data/v0_context_type_nlg_api_call_scale_grad_False_multi_task_False_1_1_1_schema_True_user_actions_True_sys_actions_False_turns_26_service_results_True_dialogs_1_domain_setting_all_train_domains_1.0.csv",
        num_rows=5,
        output_dir="output",
    )
    dg = DataGenerator(cfg)
    dg.run()

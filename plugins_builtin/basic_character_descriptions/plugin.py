from models.context import Context
from models.system_prompt import SystemPrompt
from plugin_system.abc.system_prompt_module import SystemPromptPlugin
from plugin_system.hook import plugin_hook


class BasicCharacterDescriptions(SystemPromptPlugin):
    config: dict

    def plugin_setup(self) -> None:
        config = self.pm.get_plugin_config(self.__class__.__name__)
        if config:
            self.config = config

    @plugin_hook
    def generate_system_prompts(self, ctx: Context) -> list[SystemPrompt]:  # noqa: ARG002
        prompts = []
        # config should be a simply kv dict, this plugin simply parses this to a SystemPrompt part
        for name, description in self.config.items():
            prompts.append(SystemPrompt(name=name, text=description))
        return prompts

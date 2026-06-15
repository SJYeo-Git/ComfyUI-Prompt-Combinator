from .prompt_combinator import PromptCombinator
from .prompt_combinator import PromptCombinatorMerger
from .prompt_combinator import PromptCombinatorExportGallery
from .prompt_combinator import PromptCombinatorRandomPrompt
from .prompt_combinator import PromptCombinatorDateTime
from .prompt_combinator import PromptCombinatorLooperAll

NODE_CLASS_MAPPINGS = {
    "PromptCombinator": PromptCombinator,
    "PromptCombinatorMerger": PromptCombinatorMerger,
    "PromptCombinatorExportGallery": PromptCombinatorExportGallery,
    "PromptCombinatorRandomPrompt": PromptCombinatorRandomPrompt,
    "PromptCombinatorDateTime": PromptCombinatorDateTime,
    "PromptCombinatorLooperAll": PromptCombinatorLooperAll,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptCombinator": "🔢 Prompt Combinator",
    "PromptCombinatorMerger": "🔢 Prompt Combinator Merger",
    "PromptCombinatorExportGallery": "🔢 Prompt Combinator Export Gallery",
    "PromptCombinatorRandomPrompt": "🔢 Pick Random Prompt from Prompt Combinator",
    "PromptCombinatorDateTime": "🔢 Prompt Combinator Date Time",
    "PromptCombinatorLooperAll": "🔢 Prompt Combinator Looper (All at Once)",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

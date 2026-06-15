from .prompt_combinator import PromptCombinator
from .prompt_combinator import PromptCombinatorMerger
from .prompt_combinator import PromptCombinatorExportGallery
from .prompt_combinator import PromptCombinatorRandomPrompt
from .prompt_combinator import PromptCombinatorLooper

NODE_CLASS_MAPPINGS = {
    "PromptCombinator": PromptCombinator,
    "PromptCombinatorMerger": PromptCombinatorMerger,
    "PromptCombinatorExportGallery": PromptCombinatorExportGallery,
    "PromptCombinatorRandomPrompt": PromptCombinatorRandomPrompt,
    "PromptCombinatorLooper": PromptCombinatorLooper,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptCombinator": "🔢 Prompt Combinator",
    "PromptCombinatorMerger": "🔢 Prompt Combinator Merger",
    "PromptCombinatorExportGallery": "🔢 Prompt Combinator Export Gallery",
    "PromptCombinatorRandomPrompt": "🔢 Pick Random Prompt from Prompt Combinator",
    "PromptCombinatorLooper": "🔢 Prompt Combinator Looper",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

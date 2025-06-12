from pathlib import Path

import pymmcore_widgets
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

WIDGETS_ROOT = Path(pymmcore_widgets.__file__).parent.parent.parent
SUBMODULE_ROOTS = {"pymmcore-widgets/": str(WIDGETS_ROOT)}


def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, files: Files
) -> str:
    # make sure snippets inside submodules can find their relative paths
    if "-8<-" in markdown:
        mdx_configs = config["mdx_configs"]
        snippets_config = mdx_configs.setdefault("pymdownx.snippets", {})
        base_path = snippets_config.setdefault("base_path", [])
        for key, root in SUBMODULE_ROOTS.items():
            if page.url.startswith(key):
                if root not in base_path:
                    base_path.append(root)
            elif root in base_path:
                base_path.remove(root)

    return markdown

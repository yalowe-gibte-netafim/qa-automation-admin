import json

    
def inject_storage(page, storage):

    page.add_init_script(
        f"""
        (() => {{
            const storage = {json.dumps(storage)};

            for (const [key, value] of Object.entries(storage)) {{
                localStorage.setItem(key, String(value));
            }}
        }})();
        """
    )

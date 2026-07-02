import json


def inject_oidc_session(
    page,
    access_token: str,
    id_token: str,
    refresh_token: str,
    expires_at: str,
):
    payload = {
        "access_token": access_token,
        "id_token": id_token,
        "refresh_token": refresh_token,
        "expires_at": expires_at,
    }

    payload_json = json.dumps(payload)

    page.add_init_script(
        f"""
        (() => {{
            const payload = {payload_json};

            for (const [key, value] of Object.entries(payload)) {{
                localStorage.setItem(key, String(value));
            }}
        }})();
        """
    )
class UsersLocators:
    # PAGE_TITLE = "text=USERS INFO"
    EMAIL_FILTER =  'input[aria-label="Email Filter Input"]'  # נשפר אחרי Inspect
    ENTERPRISE_FILTER = "input[aria-label='Enterprise Filter Input']"
    USERS_ROWS = "table tbody tr"
    IMPERSONATE_BUTTON = "text=Impersonate"
    USERS_ROWS = '[role="row"]'
    USER_EMAIL_CELL = 'div[col-id="emailAddress"]'
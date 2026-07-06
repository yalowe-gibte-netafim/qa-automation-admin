class UsersLocators:
    # PAGE_TITLE = "text=USERS INFO"
    EMAIL_FILTER =  'input[aria-label="Email Filter Input"]'  # נשפר אחרי Inspect
    ENTERPRISE_FILTER = "input[aria-label='Enterprise Filter Input']"
    IMPERSONATE_BUTTON = "text=Impersonate"
    USER_EMAIL_CELL_AG = '.ag-row div[col-id="emailAddress"]'
    USER_ENTERPRISE_CELL_AG = '.ag-row div[col-id="enterpriseName"]'
    PAGE_TITLE = "h1.dashboard-title"

    PAGE_TITLE = "dashboard-title ng-star-inserted"
    USER_NAME_INPUT = ['data-testid="form--user-name-field"']
    FIRST_NAME_INPUT = ['data-testid="form--first-name-field"']
    LAST_NAME_INPUT = ['data-testid="form--last-name-field"']
    EMAIL_INPUT = ['data-testid="form--email-field"']
    PHONE_INPUT = ['data-testid="form--phone-field"']
    ENTERPRISE_INPUT = ['data-testid="form--enterprise-field"']
    IMPERSONATE_BUTTON = "button:has-text('Impersonate')"
    CANCEL_BUTTON = ['data-testid="form--on-back-clicked-btn"']
    SAVE_BUTTON = ['data-testid="form--button-submit"']
# Copy to site_config.py (git-ignored), fill in, then run `python3 build.py`.
# Address and phone are deliberately not kept here: they are shown on the Play listing.
# Leave an optional field as "" to leave it out of the Terms page.
# Anything left as "" in a REQUIRED field shows as [NOT SET] and build.py warns.

TRADER = {
    # REQUIRED. Your full legal name (or registered business name).
    "legal_name": "",

    # REQUIRED. Contact email (must be monitored; users and regulators use it).
    "email": "",

    # REQUIRED. Country whose law governs the terms, e.g. "India", "Ireland".
    "governing_law_country": "",

    # OPTIONAL. Fill in only if you have one.
    "vat_number": "",
    "business_registration_number": "",
}

# Date shown as "Last updated" on the Terms page.
TERMS_LAST_UPDATED = "November 7, 2026"

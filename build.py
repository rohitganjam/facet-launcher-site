import os

ROOT = "/Volumes/NVME/repo/facet-launcher-site"
with open(f"{ROOT}/assets/mark.svg.txt") as f:
    MARK_PATHS = f.read().strip()

def mark_svg(size):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 108 108" xmlns="http://www.w3.org/2000/svg">{MARK_PATHS}</svg>'

def nav(active):
    def link(href, full_label, short_label, key):
        cls = ' class="active"' if key == active else ''
        return f'<a href="{href}"{cls}><span class="full-label">{full_label}</span><span class="short-label">{short_label}</span></a>'
    return f'''<header class="site-nav">
  <div class="wrap">
    <a class="brand" href="index.html">{mark_svg(28)}<span class="brand-text">Facet Launcher</span></a>
    <nav class="links">
      {link("index.html", "Home", "Home", "home")}
      {link("features.html", "Features", "Features", "features")}
      {link("privacy-policy.html", "Privacy Policy", "Privacy", "privacy")}
    </nav>
  </div>
</header>'''

DISCORD_INVITE = "https://discord.gg/BRjwWZ23E"

CTA_SECTION = f'''<section class="closing-cta">
  <div class="wrap">
    <h2>Join the community</h2>
    <p>Facet Launcher is in active development. Come chat, share feedback, or follow along on Discord.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="{DISCORD_INVITE}">Join Discord</a>
    </div>
  </div>
</section>'''

FOOTER = f'''<footer class="site-footer">
  <div class="wrap">
    <span>&copy; 2026 Facet Launcher.</span>
    <div>
      <a href="{DISCORD_INVITE}">Discord</a>
      <a href="privacy-policy.html">Privacy Policy</a>
    </div>
  </div>
</footer>'''

def page(title, description, nav_key, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{nav(nav_key)}
{body}
{FOOTER}
</body>
</html>
'''

# ---------- index.html ----------
highlights = [
    ("F", "#375381", "Facets", "Up to 3 full personas &mdash; each with its own apps, dock, clock, and calendar &mdash; switched with a swipe."),
    ("C", "#2C6860", "30+ clock styles", "From minimal typography to shape-based faceted marks, each fully re-themeable."),
    ("A", "#2C7D52", "Smart app drawer", "List or grid, an alphabet rail, and search across apps and contacts."),
    ("W", "#22384F", "Widgets", "A dedicated space for widgets &mdash; drag, resize, and arrange freely."),
]
highlight_html = "\n".join(f'''    <div class="highlight-card">
      <div class="dot" style="background:{color}">{letter}</div>
      <h3>{title}</h3>
      <p>{desc}</p>
    </div>''' for letter, color, title, desc in highlights)

index_body = f'''<section class="hero">
  <div class="wrap">
    <div class="mark" style="margin:0 auto 24px">{mark_svg(96)}</div>
    <h1>A launcher built around how you use your phone</h1>
    <p class="tagline">Facet Launcher is a fast, minimal Android home screen that adapts to how you actually use your phone - work, personal or focus, each its own facet.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="features.html">See features</a>
      <a class="btn btn-secondary" href="{DISCORD_INVITE}">Join Discord</a>
    </div>
  </div>
</section>
<section class="wrap">
  <div class="highlights">
{highlight_html}
  </div>
</section>
<section class="feature-section">
  <div class="wrap inner">
    <div class="feature-text">
      <span class="eyebrow">Facets</span>
      <h2>Your phone, on switch</h2>
      <p>Set up a Work facet with only the apps you need at your desk. A Personal facet with everything else. A Focus facet with almost nothing at all. Swipe to browse live previews of each, tap to switch instantly.</p>
      <p>Every facet can override its own apps list, dock, clock style and calendar, or simply inherit the defaults.</p>
    </div>
    <div class="shots single">
      <div class="shot-frame"><img src="assets/screenshots/facets.png" alt="Facet Launcher's facet switcher showing two facets side by side"></div>
    </div>
  </div>
</section>
<section class="see-more">
  <div class="wrap">
    <a class="btn btn-primary" href="features.html">See all features</a>
  </div>
</section>'''

# ---------- features.html ----------
features_body = f'''<section class="hero" style="padding:56px 24px 24px">
  <div class="wrap">
    <h1 style="font-size:36px">Everything Facet Launcher does</h1>
    <p class="tagline" style="margin-bottom:0">A closer look at what's actually built and available today.</p>
  </div>
</section>

<section class="feature-section" id="facets" style="border-top:none">
  <div class="wrap inner">
    <div class="feature-text">
      <span class="eyebrow">Facets</span>
      <h2>Switch your whole setup in one tap</h2>
      <p>Up to three facets, each a fully independent launcher configuration: its own favorites, list mode, clock style, and calendar settings. Long-press an empty part of the home screen to browse live preview cards and switch instantly, or drop into Settings to reorder, rename, or fine-tune each one.</p>
      <ul>
        <li>Live preview cards render each facet's real clock, favorites, and calendar</li>
        <li>Per-facet override for apps list, dock content, clock &amp; calendar style</li>
      </ul>
    </div>
    <div class="shots single">
      <div class="shot-frame"><img src="assets/screenshots/facets.png" alt="Two facet preview cards side by side in the facet switcher"></div>
    </div>
  </div>
</section>

<section class="feature-section reverse" id="clock">
  <div class="wrap inner">
    <div class="feature-text">
      <span class="eyebrow">Home &amp; clock</span>
      <h2>30+ clock styles, fully re-themeable</h2>
      <p>From clean typographic layouts to shape-based marks, every clock template supports its own font, color, weight and alignment,  independent of the calendar strip beneath it. Drag to resize and reposition, or hand-pick a style per facet.</p>
    </div>
    <div class="shots">
      <div class="shot-frame"><img src="assets/screenshots/clock-gallery-2.png" alt="Clock style gallery showing Chip, Duotone Overlap, and Corner Frame templates"></div>
      <div class="shot-frame small"><img src="assets/screenshots/clock-resize.png" alt="Dragging to resize and reposition the clock on the home screen"></div>
    </div>
  </div>
</section>

<section class="feature-section" id="drawer">
  <div class="wrap inner">
    <div class="feature-text">
      <span class="eyebrow">App drawer</span>
      <h2>List or grid, your call</h2>
      <p>A letter-indexed list with an alphabet rail for easy navigation, or a dense grid if you prefer. Type to search across your apps and, optionally, your Settings and Contacts, with quick actions like call or message right from the result.</p>
    </div>
    <div class="shots">
      <div class="shot-frame"><img src="assets/screenshots/drawer-list.png" alt="App drawer in list view with the alphabet rail"></div>
      <div class="shot-frame"><img src="assets/screenshots/drawer-grid.png" alt="App drawer in grid view"></div>
    </div>
  </div>
</section>

<section class="feature-section reverse" id="widgets">
  <div class="wrap inner">
    <div class="feature-text">
      <span class="eyebrow">Widgets</span>
      <h2>Widgets have their own home</h2>
      <p>Widgets get their own dedicated surface &mdash; a swipe away from your home screen &mdash; instead of crowding your app list. Add up to 20, drag to reposition, and resize freely.</p>
    </div>
    <div class="shots single">
      <div class="shot-frame"><img src="assets/screenshots/widgets.png" alt="The Widgets screen showing a calendar and music player widget"></div>
    </div>
  </div>
</section>

<section class="feature-section" id="privacy">
  <div class="wrap inner">
    <div class="feature-text">
      <span class="eyebrow">Privacy</span>
      <h2>Nothing leaves your device</h2>
      <p>Facet Launcher doesn't request internet access at all. There's no server, no account, no analytics, no ads. Everything runs entirely on your phone.</p>
      <p><a href="privacy-policy.html">Read the full privacy policy &rarr;</a></p>
    </div>
    <div class="shots single">
      <div class="shot-frame"><img src="assets/screenshots/clock-style-settings.png" alt="Clock and calendar style settings screen"></div>
    </div>
  </div>
</section>'''

# ---------- privacy-policy.html ----------
policy_body = '''<main class="wrap policy policy-main">
  <h1>Facet Launcher &mdash; Privacy Policy</h1>
  <p class="updated">Last updated: September 12, 2026</p>

  <div class="summary">
    <strong>In short:</strong> Facet Launcher does not have internet access. Nothing you do in the app &mdash; your apps, contacts, calendar, usage patterns, notifications, or settings &mdash; ever leaves your device. There are no accounts, no ads, no analytics, and no third-party tracking of any kind.
  </div>

  <h2>What this app is</h2>
  <p>Facet Launcher is a home-screen launcher for Android. It replaces your phone's default home screen with app organization, a clock, and calendar widgets, all customizable through facets.</p>

  <h2>Data collection and transmission</h2>
  <p>Facet Launcher does not request the <code>INTERNET</code> permission. The app cannot make network requests, and has no server, backend, or cloud component of any kind. Every feature described below runs entirely on your device.</p>

  <h2>Permissions the app uses, and why</h2>
  <ul>
    <li><strong>Usage access</strong> (<code>PACKAGE_USAGE_STATS</code>) &mdash; powers the app drawer's optional "Most used" sort, which ranks your installed apps by how often you open them. This ranking is computed on-device each time it's shown and is never stored beyond what's needed to display it, or sent anywhere.</li>
    <li><strong>Calendar</strong> (<code>READ_CALENDAR</code>) &mdash; lets the home screen show your upcoming events, if you turn this on in Settings. Calendar data is read directly from your device's calendar provider and displayed locally; it is never copied, stored separately, or transmitted.</li>
    <li><strong>Contacts</strong> (<code>READ_CONTACTS</code>) &mdash; powers an optional contact search feature in the app drawer, if you turn it on in Settings. Contact data is queried on-device at search time and never stored or transmitted.</li>
    <li><strong>Notification access</strong> &mdash; powers optional app-icon notification badges. The app reads only which app a notification came from and how many are unread, never notification content, and never stores or transmits this beyond what's needed to draw the badge.</li>
    <li><strong>Uninstall shortcut</strong> (<code>REQUEST_DELETE_PACKAGES</code>) &mdash; lets you uninstall an app from its long-press menu. This opens Android's own uninstall confirmation dialog; the app never uninstalls anything without your explicit confirmation in that system dialog.</li>
    <li><strong>Expand notification shade</strong> (<code>EXPAND_STATUS_BAR</code>) &mdash; lets a swipe-down gesture on the home screen open your notification shade, the same way it would on any home screen.</li>
  </ul>

  <h2>Data storage</h2>
  <p>Your settings, facets, dock and favorites layout, and widget placements are stored in a local database on your device, using Android's standard app-private storage. This data is not accessible to other apps and is not transmitted anywhere. Uninstalling Facet Launcher removes it, following normal Android behavior.</p>

  <h2>Backup and restore</h2>
  <p>If you use the app's backup feature, it creates a JSON file containing your settings and layout, which you choose where to save using Android's own file picker (for example, to your device storage or a cloud storage app you've installed). Facet Launcher does not upload this file anywhere itself &mdash; where it ends up is entirely controlled by you, through the system file picker.</p>

  <h2>Third parties</h2>
  <p>Facet Launcher does not integrate any third-party analytics, advertising, or crash-reporting services. No data is shared with any third party, because no data leaves your device in the first place.</p>

  <h2>Children's privacy</h2>
  <p>Facet Launcher does not knowingly collect any data from anyone, including children, since the app does not collect or transmit data at all.</p>

  <h2>Changes to this policy</h2>
  <p>If this policy changes, an updated version will be posted at this same URL with a revised "Last updated" date.</p>

  <h2>Contact</h2>
  <p>Questions about this policy can be sent to the developer via the <a href="https://discord.gg/BRjwWZ23E">Facet Launcher Discord server</a>.</p>
</main>'''

pages = {
    "index.html": page("Facet Launcher", "A minimal Android launcher built around how you use your phone &mdash; switch your whole setup in one tap.", "home", index_body + CTA_SECTION),
    "features.html": page("Features — Facet Launcher", "Facets, 30+ clock styles, a smart app drawer, and a dedicated widgets screen.", "features", features_body + CTA_SECTION),
    "privacy-policy.html": page("Privacy Policy — Facet Launcher", "Facet Launcher has no internet access and collects no data. Read the full privacy policy.", "privacy", policy_body),
}

for name, content in pages.items():
    with open(f"{ROOT}/{name}", "w") as f:
        f.write(content)
    print("wrote", name)

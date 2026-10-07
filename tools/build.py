"""Builds index.html, services.html and 404.html from src/ partials.
Usage: python3 tools/build.py   (run from the repo root)"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
PHONE, TEL = "817-938-7654", "tel:+18179387654"

SERVICES = [
    dict(id="cleaning", icon="i-clean", title="Window cleaning",
         short="Inside and out, with screens, tracks and frames done by hand.",
         paras=["Every visit covers the glass on both sides, plus the sills, frames, screens and tracks. "
                "The whole window ends up clean, not just the middle of the pane.",
                "A complete window and screen clean is $20 off right now. And if it rains within three days, "
                "call us and we'll come back and clean them again."],
         list_title="What's included",
         items=["Glass, inside and outside", "Window sills and frames", "Screens", "Tracks",
                "Rainy-day guarantee for three days"]),
    dict(id="repair", icon="i-repair", title="Glass repair",
         short="One cracked pane or a run of windows and doors.",
         paras=["A crack spreads, and a broken pane lets the heat in and the security down. "
                "Our glass technicians repair windows and doors quickly and safely.",
                "No job is too large or too small: a single pane, several windows at once, "
                "or glass on a commercial building."],
         list_title="Good for",
         items=["A single cracked or broken pane", "Several windows or doors at once",
                "Storefront and office glass"]),
    dict(id="argon", icon="i-argon", title="Argon glass replacement",
         short="Gas-filled panes that keep heat and street noise out.",
         paras=["Argon is a gas sealed between the panes of insulated windows. It slows heat moving "
                "through the glass and takes the edge off outside noise.",
                "The benefit only lasts if the unit is fitted right, so an experienced technician "
                "installs every argon pane we replace."],
         list_title="Why argon",
         items=["Better thermal insulation", "Less outside noise", "Fitted by experienced glass technicians"]),
    dict(id="foggy", icon="i-fog", title="Foggy window repair",
         short="Haze trapped between the panes means a failed seal.",
         paras=["When a double-pane window looks misty between the glass, the seal has failed and moisture "
                "got inside. No amount of wiping helps, because the fog is on the inside.",
                "We'll look at the window during your free estimate and tell you plainly whether it needs "
                "a repair or new argon glass."],
         list_title="Signs you need it",
         items=["Haze you can't wipe off from either side", "Drops of water between the panes",
                "A milky film that comes and goes with the weather"]),
    dict(id="fixtures", icon="i-fixture", title="Fixture cleaning",
         short="Chandeliers, ceiling fans, cabinet tops and mirrors.",
         paras=["The high, fiddly jobs most people put off because they mean balancing on a ladder: "
                "chandeliers, light fixtures, ceiling fans and the tops of cabinets.",
                "We do glass tables and mirrors on the same visit, so the room looks finished, "
                "not just the windows."],
         list_title="We clean",
         items=["Chandeliers and light fixtures", "Ceiling fans", "Cabinet tops", "Glass tables and mirrors"]),
]


def arch(s, cls="pane-arch", key=False):
    k = f' data-vt-key="svc-{s["id"]}"' if key else ""
    return (f'<div class="{cls}"{k}><svg aria-hidden="true"><use href="#{s["icon"]}"/></svg></div>')


def mega():
    cards = "".join(
        f'<li><a class="mega-card" href="services.html#{s["id"]}" data-vt="svc-{s["id"]}">{arch(s, "mega-arch")}'
        f'<span class="mega-title">{s["title"]}</span><span class="mega-text">{s["short"]}</span></a></li>'
        for s in SERVICES)
    return (f'<div class="mega" id="mega"><div class="alignwide"><ul class="mega-grid">{cards}</ul>'
            f'<div class="mega-foot"><a href="services.html">All services</a>'
            f'<span>Also gutters, power washing and commercial glass</span>'
            f'<a href="./#quote">Get a free estimate</a></div></div></div>')


def panes():
    return '<div class="panes">' + "".join(
        f'<a class="pane wp-reveal" href="services.html#{s["id"]}" data-vt="svc-{s["id"]}">{arch(s)}'
        f'<h3>{s["title"]}</h3><p>{s["short"]}</p><span class="more">Learn more</span></a>'
        for s in SERVICES) + "</div>"


def service_rows():
    out = []
    for i, s in enumerate(SERVICES):
        items = "".join(f"<li>{x}</li>" for x in s["items"])
        paras = "".join(f"<p>{p}</p>" for p in s["paras"])
        flip = " is-flipped" if i % 2 else ""
        out.append(
            f'<section class="svc-row{flip}" id="{s["id"]}"><div class="alignwide wp-block-media-text">'
            f'<div class="wp-block-media-text__media">{arch(s, "row-arch", key=True)}</div>'
            f'<div class="wp-block-media-text__content wp-reveal"><p class="is-style-text-annotation">0{i + 1}</p>'
            f'<h2>{s["title"]}</h2>{paras}<h3 class="list-title">{s["list_title"]}</h3>'
            f'<ul class="wp-block-list is-style-checkmark-list">{items}</ul>'
            f'<div class="wp-block-buttons"><div class="wp-block-button"><a class="wp-block-button__link wp-element-button" '
            f'href="./?service={s["id"]}#quote">Get a free estimate</a></div>'
            f'<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" '
            f'href="{TEL}">Call {PHONE}</a></div></div></div></div></section>')
    return "\n".join(out)


def jumps():
    return '<nav class="jump" aria-label="Services on this page">' + "".join(
        f'<a href="#{s["id"]}"><svg aria-hidden="true"><use href="#{s["icon"]}"/></svg>{s["title"]}</a>'
        for s in SERVICES) + "</nav>"


def page(body, title, desc, current):
    head = (SRC / "head.html").read_text()
    head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head, flags=re.S)
    head = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>" + desc, head)
    if current != "home":
        head = head.replace('<link rel="preload" as="image" href="assets/img/crew-southlake.webp">\n', "")
    header = (SRC / "header.html").read_text().replace("<!--MEGA-->", mega())
    header = header.replace(f'data-nav="{current}"', f'data-nav="{current}" aria-current="page"')
    return (head + f'<body class="wp-site-blocks page-{current}">\n' + (SRC / "sprite.html").read_text()
            + header + body + (SRC / "footer.html").read_text())


home = (SRC / "home.html").read_text().replace("<!--PANES-->", panes())
services = (SRC / "services.html").read_text().replace("<!--JUMPS-->", jumps()).replace("<!--ROWS-->", service_rows())
notfound = (SRC / "404.html").read_text()
about = (SRC / "about.html").read_text()
contact = (SRC / "contact.html").read_text()

(ROOT / "index.html").write_text(page(home, "Window Cleaning and Glass Repair in Southlake, TX | Squeaky Clean Windows",
    "Window cleaning inside and out, glass repair, argon glass replacement and foggy window repair for homes and businesses in Southlake, Keller and across Dallas-Fort Worth. Call 817-938-7654.", "home"))
(ROOT / "services.html").write_text(page(services, "Services: Window Cleaning, Glass Repair, Argon Glass | Squeaky Clean Windows",
    "Window cleaning, glass repair, argon glass replacement, foggy window repair and fixture cleaning in Southlake and across Dallas-Fort Worth.", "services"))
(ROOT / "404.html").write_text(page(notfound, "Page not found | Squeaky Clean Windows",
    "This page could not be found.", "404"))
(ROOT / "about.html").write_text(page(about, "About Us | Squeaky Clean Windows and Glass Restoration",
    "Squeaky Clean Windows and Glass Restoration, started by Chuck Davis, cleans and repairs glass for homes and businesses across Dallas-Fort Worth.", "about"))
(ROOT / "contact.html").write_text(page(contact, "Contact and Free Estimate | Squeaky Clean Windows",
    "Request a free estimate for window cleaning or glass repair in Southlake and across DFW. Call 817-938-7654.", "contact"))
print("built about, contact, index.html, services.html, 404.html")

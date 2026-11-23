#!/usr/bin/env python3
"""Generates the KSI Servis redesign pages into site/. Run: python3 build.py"""
from pathlib import Path

OUT = Path(__file__).parent / "site"
PHONE = "031 329 250"
PHONE_T = "+38631329250"

ARR = '<svg class="arr" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHEV = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 9l6 6 6-6"/></svg>'
PH_ICO = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'

ZAGON = [
    ("zagon-crpalisc-odprtega-tipa", "Zagon črpališč odprtega tipa", "npr. Amarex, Ama-Porter", "assets/img/crpalisce_odprtega_tipa_amarex.png"),
    ("zagon-crpalisc-zaprtega-tipa", "Zagon črpališč zaprtega tipa", "npr. Compacta, Mini-Compacta", "assets/img/crpalisce_zaprtega_tipa_compacta_mini-compacta.png"),
    ("zagon-crpalk-s-frekvencno-regulacijo", "Zagon črpalk s frekvenčno regulacijo", "Pump-Drive", "assets/img/pump-drive1.png"),
    ("zagon-naprave-za-zvisanje-tlaka", "Zagon naprave za zvišanje tlaka", "Hyamat", "assets/img/hyamat.png"),
    ("centriranje-elasticne-sklopke", "Centriranje in uravnavanje elastične sklopke", "in poizkusni zagon", "assets/img/centriranje_elasticne_sklopke2.png"),
]

PUMPS = [
    ("p1", "Etanorm s frekvenčno regulacijo Pump-Drive", "Namenjena za široko uporabo, kjer se spreminjajo zahteve po pretoku."),
    ("p2", "Etanorm SYT", "Horizontalna, enostopenjska izvedba za procesno industrijo in vroče medije."),
    ("p3", "Etaline s frekvenčno regulacijo Pump-Drive", "Za ogrevanje, klimatizacijo in industrijo."),
    ("p4", "CPKN, Mega CPK", "Horizontalna črpalka za kemijsko in petrokemijsko industrijo ter rafinerije."),
    ("p5", "Multitec", "Večstopenjska, horizontalna ali vertikalna izvedba za oskrbo z vodo, pitno vodo in industrijo."),
    ("p6", "Etanorm", "Horizontalna, enostopenjska izvedba po EN 733 za najširše sisteme oskrbe z vodo."),
    ("p7", "Amarex z Level-Control Basic", "Potopna črpalka za umazano in odpadno vodo, komunalne čistilne naprave in industrijo."),
]


def head(title, desc):
    return f"""<!doctype html>
<html lang="sl" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preload" href="assets/fonts/satoshi-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/satoshi-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css?v=5">
<script>
(function () {{
  if (!/[?&]r=/.test(location.search)) return;
  var s = document.createElement('script');
  s.async = true;
  s.referrerPolicy = 'no-referrer';
  s.setAttribute('data-landing', location.href);
  s.src = 'https://phplaravel-758037-6569212.cloudwaysapps.com/v/script.js';
  document.head.appendChild(s);
}})();
</script>
</head>
"""


def nav(active):
    def on(k):
        return ' class="on"' if k == active else ""
    mega_items = "".join(
        f'<a href="{s}.html"><span>{t}<small>{sub}</small></span>{ARR}</a>' for s, t, sub, _ in ZAGON
    )
    mob_sub = "".join(f'<a href="{s}.html">{t}</a>' for s, t, _, _ in ZAGON)
    return f"""<div class="loader"><div class="loader-in"><img src="assets/img/ksiservis_logo_2022.png" alt="KSI Servis"><div class="loader-bar"><i></i></div></div></div>
<header class="nav">
  <a class="logo" href="index.html" aria-label="KSI Servis, domov"><img src="assets/img/ksiservis_logo_2022.png" alt="KSI Servis, pooblaščeni servisni partner" width="272" height="70"></a>
  <ul class="menu">
    <li><a href="index.html"{on('home')}>Domov</a></li>
    <li class="has-mega"><button aria-haspopup="true">Storitve {CHEV}</button></li>
    <li><a href="daljinski-nadzor.html"{on('nadzor')}>Daljinski nadzor</a></li>
    <li><a href="reference.html"{on('ref')}>Reference</a></li>
    <li><a href="kontakt.html"{on('kontakt')}>Kontakt</a></li>
  </ul>
  <div class="nav-cta">
    <a class="btn btn-blue" href="tel:{PHONE_T}"><span class="live"></span><span class="btn-txt">24/7&nbsp;&nbsp;</span>{PHONE}</a>
    <button class="burger" aria-label="Meni" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>
<div class="mega" role="menu">
  <a class="mega-feature" href="servis-crpalk.html">
    <div><h3>Servis črpalk</h3><p>Na vaši lokaciji, večje posege opravimo v naši delavnici.</p></div>
    <img src="assets/img/pumps/p7.png" alt="">
    <span class="btn btn-blue" style="align-self:flex-start;position:relative">Vse storitve {ARR}</span>
  </a>
  <div class="mega-list">{mega_items}<a href="daljinski-nadzor.html"><span>Daljinski nadzor<small>črpališča v realnem času</small></span>{ARR}</a></div>
</div>
<nav class="mnav">
  <div>
    <a href="index.html">Domov</a>
    <a href="servis-crpalk.html">Servis črpalk</a>
    <div class="sub">{mob_sub}</div>
    <a href="daljinski-nadzor.html">Daljinski nadzor</a>
    <a href="reference.html">Reference</a>
    <a href="kontakt.html">Kontakt</a>
  </div>
  <a class="btn btn-blue" href="tel:{PHONE_T}" style="font-size:22px;height:68px;justify-content:center"><span class="live"></span>{PHONE}</a>
</nav>
"""


CTA = f"""<section class="cta">
  <div class="wrap">
    <a class="phone" href="tel:{PHONE_T}">{PHONE}</a>
    <div class="cta-row" style="margin-top:clamp(36px,6vh,70px)">
      <p class="lead rv">Našo posebno številko lahko pokličete ne glede na čas, vse dni v tednu.</p>
      <div class="rv" style="display:flex;gap:12px;flex-wrap:wrap;justify-content:flex-end">
        <a class="btn btn-white" href="tel:{PHONE_T}">{PH_ICO} Pokličite zdaj</a>
        <a class="btn" style="background:rgba(255,255,255,.14);color:#fff" href="kontakt.html">Pišite nam {ARR}</a>
      </div>
    </div>
  </div>
  <svg class="cta-wave" viewBox="0 0 1600 300" preserveAspectRatio="none" fill="none" stroke="#fff" stroke-width="2">
    <path class="wave-path" d="M0 150 Q100 90 200 150 T400 150 T600 150 T800 150 T1000 150 T1200 150 T1400 150 T1600 150 T1800 150 T2000 150"/>
    <path class="wave-path" d="M0 200 Q100 150 200 200 T400 200 T600 200 T800 200 T1000 200 T1200 200 T1400 200 T1600 200 T1800 200 T2000 200" opacity=".6"/>
    <path class="wave-path" d="M0 250 Q100 215 200 250 T400 250 T600 250 T800 250 T1000 250 T1200 250 T1400 250 T1600 250 T1800 250 T2000 250" opacity=".35"/>
  </svg>
</section>"""


def footer():
    zl = "".join(f'<li><a href="{s}.html">{t}</a></li>' for s, t, _, _ in ZAGON)
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="foot-logo" href="index.html"><img src="assets/img/ksiservis_logo_2022.png" alt="KSI Servis"></a>
        <p style="max-width:34ch">KSI Servis, prodaja ter montaža črpalk in rezervnih delov, d.o.o.<br>Edini pooblaščeni servisni partner KSB v Sloveniji.</p>
      </div>
      <div><h5>Storitve</h5><ul><li><a href="servis-crpalk.html">Servis črpalk</a></li>{zl}<li><a href="daljinski-nadzor.html">Daljinski nadzor</a></li></ul></div>
      <div><h5>Podjetje</h5><ul><li><a href="reference.html">Reference</a></li><li><a href="kontakt.html">Kontakt</a></li><li>Matična št.: 6217443</li><li>ID za DDV: SI54958539</li></ul></div>
      <div><h5>Kontakt</h5><ul><li>Dragomelj 136<br>1230 Domžale, Slovenija</li><li><a href="tel:+38613666171">+386 (0)1 36 66 171</a></li><li><a href="mailto:info@ksb-servis.si">info@ksb-servis.si</a></li><li><a href="tel:{PHONE_T}" style="color:#fff;font-weight:700">24/7: {PHONE}</a></li></ul></div>
    </div>
    <div class="foot-bottom"><span>© KSI Servis d.o.o., 2026. Vse pravice pridržane.</span><div><a href="#">Piškotki</a><a href="#">Splošni pogoji prodaje</a></div></div>
  </div>
</footer>
<script src="assets/vendor/gsap.min.js"></script>
<script src="assets/vendor/ScrollTrigger.min.js"></script>
<script src="assets/vendor/lenis.min.js"></script>
<script src="assets/js/site.js?v=5"></script>
</body>
</html>"""


def page(fname, key, title, desc, body):
    html = head(title, desc) + f'<body data-page="{key}">\n' + nav(key) + "<main>\n" + body + "\n</main>\n" + CTA + footer()
    (OUT / fname).write_text(html, encoding="utf-8")
    print("wrote", fname)


# ---------- icons ----------
ICO = {
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0 5 5L22 13.6a7 7 0 0 1-9.3 2.3L6 22.6a2.1 2.1 0 0 1-3-3l6.7-6.7A7 7 0 0 1 12 3.6z"/>',
    "plug": '<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0zM12 18v4"/>',
    "power": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "rotate": '<path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 3v5h-5"/>',
    "logic": '<path d="M4 6h6v4H4zM14 14h6v4h-6zM7 10v4h10M17 10V6h-3"/>',
    "gauge": '<path d="M12 14l4-4M3.3 17a10 10 0 1 1 17.4 0"/><circle cx="12" cy="14" r="1.6"/>',
    "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM14 2v6h6M8 13h8M8 17h5"/>',
}


def ico(k, cls="step-ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">{ICO[k]}</svg>'


IMPELLER = """<svg class="card-art" viewBox="0 0 200 200" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
<circle cx="100" cy="100" r="92" opacity=".25"/><g class="impeller">
<circle cx="100" cy="100" r="16"/>
<path d="M100 84C120 60 150 50 176 56"/><path d="M116 100C140 120 150 150 144 176"/><path d="M100 116C80 140 50 150 24 144"/><path d="M84 100C60 80 50 50 56 24"/>
<path d="M111 89C140 80 165 92 182 110"/><path d="M111 111C120 140 108 165 90 182"/><path d="M89 111C60 120 35 108 18 90"/><path d="M89 89C80 60 92 35 110 18"/>
</g></svg>"""

GAUGE = """<svg class="card-art" viewBox="0 0 200 200" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
<path d="M30 140a75 75 0 1 1 140 0"/><path d="M48 128a55 55 0 1 1 104 0" opacity=".35"/>
<path d="M100 120l38-46"/><circle cx="100" cy="120" r="8"/>
<path d="M40 100h10M100 40v10M160 100h-10M58 58l7 7M142 58l-7 7"/></svg>"""

PARTS = """<svg class="card-art" viewBox="0 0 200 200" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="60" cy="60" r="34"/><circle cx="60" cy="60" r="14"/>
<path d="M120 30h50v50h-50z"/><path d="M135 45h20v20h-20z" opacity=".4"/>
<circle cx="150" cy="150" r="30"/><path d="M150 120v60M120 150h60" opacity=".4"/>
<path d="M30 130l40 40M30 170l40-40" opacity=".0"/><path d="M26 140h70v30H26z"/><path d="M40 140v30M54 140v30M68 140v30M82 140v30" opacity=".4"/></svg>"""


# ---------- HOME ----------
def home():
    pumps_imgs = "".join(
        f'<img class="pump{" tall" if k == "p3" else ""}" src="assets/img/pumps/{k}.png" alt="Črpalka KSB {t}" data-title="{t}" data-desc="{d}">'
        for k, t, d in PUMPS
    )
    pcards = "".join(
        f'''<article class="pcard"><div class="glow"></div><span class="num">{i+1:02d}</span><div class="imgbox"><img src="assets/img/pumps/{k}.png" alt="{t}" loading="lazy"></div><div><h3>{t}</h3><p>{d}</p></div></article>'''
        for i, (k, t, d) in enumerate(PUMPS)
    )
    zlist = "".join(
        f'<a href="{s}.html"><span class="n">{i+1:02d}</span><div><h3>{t}</h3><small>{sub}</small></div><span class="go">{ARR}</span></a>'
        for i, (s, t, sub, _) in enumerate(ZAGON)
    )
    zimgs = "".join(f'<img src="{im}" alt="" style="mix-blend-mode:multiply">' for _, _, _, im in ZAGON)
    steps = [
        ("plug", "Priklop senzorike na krmilno omaro, plovna stikala ali merilna sonda"),
        ("power", "Priklop krmilne omare na električno omrežje in kontrola napajalne napetosti"),
        ("rotate", "Priklop črpalke in preverjanje pravilne smeri vrtenja"),
        ("logic", "Preverjanje krmilne logike, paralelno in ciklično delovanje"),
        ("gauge", "Merjenje toka pod bremenom in določanje delovne točke"),
        ("doc", "Poročilo o zagonu z ugotovitvami in pripombami za izboljšanje delovanja"),
    ]
    steps_html = "".join(
        f'<div class="step rv{" report" if i == 5 else ""}">{ico(k)}<div><span class="k">{i+1:02d}</span><h4>{t}</h4></div></div>'
        for i, (k, t) in enumerate(steps)
    )
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1 class="d1"><span class="line"><span>Pooblaščeni</span></span><span class="line"><span>servis črpalk</span></span><span class="line"><span class="blue">KSB.</span></span></h1>
      <p class="lead hero-sub hero-in">Črpalke servisiramo na vaši lokaciji, večje posege opravimo pri nas. Z originalnimi rezervnimi deli in znanjem proizvajalca.</p>
      <div class="hero-actions hero-in">
        <a class="btn btn-blue" href="tel:{PHONE_T}">{PH_ICO} Pokličite servis</a>
        <a class="btn btn-ghost" href="servis-crpalk.html">Naše storitve {ARR}</a>
      </div>
    </div>
    <div class="stage hero-in">
      <div class="stage-disc"></div>
      <svg class="stage-ring" viewBox="0 0 400 400" fill="none" stroke="currentColor"><circle cx="200" cy="200" r="198" stroke-dasharray="2 10" stroke-width="1.5"/><circle cx="200" cy="200" r="170" stroke-dasharray="80 30" stroke-width=".8" opacity=".6"/></svg>
      {pumps_imgs}
      <div class="stage-cap"><span class="count">01 / 07</span><div><h4>{PUMPS[0][1]}</h4><p>{PUMPS[0][2]}</p></div></div>
    </div>
  </div>
  <div class="wrap"><div class="hero-foot hero-in">
    <div><b>Edini pooblaščeni</b><span>servisni partner KSB v Sloveniji</span></div>
    <div><b>Na vaši lokaciji</b><span>intervencije na terenu po vsej državi</span></div>
    <div><b>Originalni deli</b><span>najbolj iskane imamo na zalogi</span></div>
    <div><b><span class="live" style="display:inline-block;margin-right:8px"></span>24/7 dežurna linija</b><span><a href="tel:{PHONE_T}">{PHONE}</a></span></div>
  </div></div>
</section>

<section class="statement">
  <div class="wrap statement-grid">
    <div class="statement-side rv">
      <div class="badge"><span class="badge-mark"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span>Pooblaščeni servisni<br>partner KSB</div>
      <p class="gray" style="font-size:17px;max-width:30ch">KSB je vodilni proizvajalec črpalk, armatur in pripadajočih sistemov v jugovzhodni Evropi.</p>
    </div>
    <p class="d3 reveal-words">Dolgoletne izkušnje pri vzdrževanju in servisiranju črpalk smo združili v tim strokovnjakov, ki rešijo tudi najzahtevnejše servisne posege.</p>
  </div>
</section>

<section class="water">
  <div class="water-media" data-par="8"><img src="assets/img/slider/bg.jpg" alt="Gladina vode"></div>
  <div class="wrap inner">
    <h2 class="d2 rv">Da voda teče.<br>Brez izpadov.</h2>
    <p class="lead rv">Tekoče vzdrževanje v skladu z vašim terminskim planom pomeni minimalen čas popravila in najkrajši izpad delovanja celotne naprave.</p>
  </div>
</section>

<section class="services" style="padding-top:clamp(110px,16vh,200px)">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="d2 rv">Vse za vašo črpalko. Na enem mestu.</h2>
      <p class="lead gray rv">Od prvega zagona do rednega vzdrževanja in dobave originalnih rezervnih delov.</p>
    </div>
    <div class="bento">
      <a class="card big rv" href="servis-crpalk.html">
        <div><h3>Servis</h3><p>Pooblaščeni servis črpalk KSB. Črpalke servisiramo na vaši lokaciji, večje posege opravimo pri nas.</p></div>
        <img class="pump-img" src="assets/img/pumps/p1.png" alt="">
        <span class="more">Več o servisu {ARR}</span>
      </a>
      <div class="card rv">{GAUGE}<div style="margin-top:44%"><h3>Vzdrževanje</h3><p>Zagotovite si tekoče vzdrževanje črpalke in s tem najkrajši čas izpada delovanja celotne naprave.</p></div></div>
      <div class="card rv">{PARTS}<div style="margin-top:44%"><h3>Rezervni deli</h3><p>Sporočite nam, kaj potrebujete. Najbolj pogosto iskane rezervne dele imamo na zalogi.</p></div></div>
      <div class="card wide rv">
        <div style="flex:1"><h3>Pogodba o servisu</h3><p>Redno servisiranje in dobava rezervnih delov v najkrajšem času. Po dogovoru jih hranimo na zalogi za vas.</p><a class="more" href="kontakt.html">Pošljite povpraševanje {ARR}</a></div>
        <ul class="lst">
          <li>Popravilo črpalk, ventilov in sistemov ter intervencije na terenu</li>
          <li>Svetovanje in analiza pri odpravljanju tehničnih napak</li>
          <li>Garancijska popravila črpalk in ventilov</li>
          <li>Prodaja novih in nadomestnih črpalk ter ventilov</li>
          <li>Originalni rezervni deli črpalk in ventilov</li>
          <li>Servisni pregled in nastavitve že vgrajene opreme</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="lineup">
  <div class="wrap lineup-head">
    <h2 class="d2 rv">Črpalke, ki jih poznamo do zadnjega vijaka.</h2>
    <p class="lead rv">Od procesne industrije do komunalnih čistilnih naprav. Servisiramo celoten program KSB.</p>
  </div>
  <div class="track-wrap"><div class="track">{pcards}
    <div class="lineup-end"><h3 class="d4">Ne najdete svojega modela?</h3><p style="color:#9aa7b6">Pokličite nas. Servisiramo tudi starejše serije in ostale črpalke, armature ter sisteme KSB.</p><a class="btn btn-blue" href="tel:{PHONE_T}" style="align-self:flex-start">{PH_ICO} {PHONE}</a></div>
  </div></div>
</section>

<section class="zagon">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <h2 class="d2 rv">Zagon in nastavitev delovanja.</h2>
      <p class="lead gray rv">Zagon s strani pooblaščenega servisa vam zagotovi zanesljivo reševanje morebitnih reklamacij v času garancije in tudi kasneje.</p>
    </div>
    <div class="zgrid">
      <div class="zsticky rv"><div class="zvis">{zimgs}<div class="zprog"><i></i></div></div></div>
      <div class="zlist">{zlist}</div>
    </div>
  </div>
</section>

<section class="steps">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <h2 class="d2 rv">Kaj zajema zagon črpališča.</h2>
      <p class="lead gray rv">Po opravljenem posegu prejmete zapisnik, s katerim dokazujete, da je zagon opravila pooblaščena oseba.</p>
    </div>
    <div class="steps-grid">{steps_html}</div>
  </div>
</section>

<section class="quote">
  <div class="wrap quote-grid">
    <div class="coupling rv">
      <svg viewBox="0 0 600 600" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <rect x="40" y="250" width="200" height="100" rx="6" fill="#005da4"/>
        <rect x="70" y="232" width="140" height="18" rx="3" fill="#00467c"/>
        <g id="shaft-spin"></g>
        <rect x="240" y="285" width="40" height="30" fill="#9aa7b6"/>
        <rect x="280" y="240" width="34" height="120" rx="4" fill="#08131f"/>
        <g id="half-r">
          <rect x="318" y="240" width="34" height="120" rx="4" fill="#2f86d0"/>
          <rect x="352" y="285" width="40" height="30" fill="#9aa7b6"/>
          <rect x="392" y="250" width="170" height="100" rx="6" fill="#005da4"/>
          <rect x="420" y="232" width="110" height="18" rx="3" fill="#00467c"/>
        </g>
        <line x1="20" y1="300" x2="580" y2="300" stroke="#005da4" stroke-width="1.5" stroke-dasharray="8 8" opacity=".5"/>
        <g transform="translate(200 410)">
          <rect x="0" y="0" width="200" height="140" rx="10" fill="#fff"/>
          <g transform="translate(0 0)"><path d="M30 100a70 70 0 0 1 140 0" stroke="#dde4ec" stroke-width="10"/>
          <path id="needle" d="M100 100L100 42" stroke="#08131f" stroke-width="4"/><circle cx="100" cy="100" r="7" fill="#08131f"/></g>
          <text x="100" y="128" text-anchor="middle" font-family="Satoshi" font-weight="700" font-size="18" fill="#08131f"><tspan id="readout">0.48</tspan> mm</text>
          <g id="ok"><circle cx="178" cy="22" r="12" fill="#3ddc84"/><path d="M172 22l4 4 8-8" stroke="#fff" stroke-width="2.6"/></g>
        </g>
      </svg>
    </div>
    <div>
      <p class="d3 rv">Strošek za strokovno uravnavanje elastične sklopke je zanemarljiv glede na možne posledice.</p>
      <p class="lead gray rv" style="margin-top:28px;max-width:40ch">Najpogostejši vzrok okvar na črpalkah je nestrokovno ravnanje z elastično sklopko. Znani so primeri, ko so črpalke odpovedale že po nekaj dneh.</p>
      <a class="btn btn-ink rv" style="margin-top:36px" href="centriranje-elasticne-sklopke.html">Centriranje sklopke {ARR}</a>
    </div>
  </div>
</section>

<section class="monitor">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <h2 class="d2 rv">Vaše črpališče. Na zaslonu.</h2>
      <p class="lead rv">Daljinski nadzor pokaže stanje vsake črpalke, alarme in obratovalne ure, še preden pride do izpada.</p>
    </div>
    <div class="screen rv">
      <div class="screen-bar"><i></i><i></i><i></i><div class="tabs"><button>Zemljevid</button><button>Pregled črpališča</button><button>Alarmi</button><button>Histogram</button></div></div>
      <div class="screen-view">
        <img src="assets/img/daljinski_nadzor1.jpg" alt="Daljinski nadzor, zemljevid črpališč">
        <img src="assets/img/daljinski_nadzor2.jpg" alt="Daljinski nadzor, pregled">
        <img src="assets/img/daljinski_nadzor3.jpg" alt="Daljinski nadzor, alarmi">
        <img src="assets/img/Histogram.jpg" alt="Histogram obratovanja">
      </div>
    </div>
    <div class="mon-feats">
      <div class="rv"><b>Lokacije</b><span>Vsa črpališča na enem zemljevidu.</span></div>
      <div class="rv"><b>Alarmi</b><span>Takojšnje obvestilo ob napaki.</span></div>
      <div class="rv"><b>Meritve</b><span>Tok, obratovalne ure in vklopi.</span></div>
      <div class="rv"><a class="btn btn-blue" href="daljinski-nadzor.html">Več o nadzoru {ARR}</a></div>
    </div>
  </div>
</section>

<section class="refs">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <h2 class="d2 rv">Iz naše delavnice.</h2>
      <p class="lead gray rv">Primeri servisnih posegov na črpalkah KSB.</p>
    </div>
    {refs_html()}
    <div class="rv" style="margin-top:40px"><a class="btn btn-ghost" href="reference.html">Vse reference {ARR}</a></div>
  </div>
</section>

<section class="values"><div class="marq"><span>Hitri</span><span>Natančni</span><span>Strokovni</span><span>Zanesljivi</span><span>Temeljiti</span></div></section>
"""
    page("index.html", "home", "KSI Servis | Pooblaščeni servis črpalk KSB", "Edini pooblaščeni servisni partner KSB v Sloveniji. Servis, zagon, vzdrževanje in rezervni deli za črpalke.", body)


def refs_html():
    refs = [
        ("popravilo_potopne_crpalke_krt_d.png", "Popravilo potopne črpalke", "KRT D 200-315/294 UG-3", "januar 2013",
         [("Nazivni premer tlačnega priključka", "DN200"), ("Moč motorja", "27 kW"), ("Teža črpalke", "470 kg")],
         ["zamenjava drsnih tesnil", "zamenjava ležajev", "meritve izolacijske upornosti"]),
        ("popravilo_horizontalne_vecstopenjske_crpalke_multitec_b50.png", "Popravilo horizontalne večstopenjske črpalke", "Multitec B 50/15B-03.1-20.62", "januar 2013",
         [("Nazivni premer", "DNS 80 / DNT 50"), ("Moč motorja", "75 kW"), ("Teža črpalke", "970 kg")],
         ["zamenjava drsnih tesnil", "zamenjava ležajev"]),
    ]
    out = '<div class="ref-grid">'
    for img, t, m, d, spec, tags in refs:
        sp = "".join(f"<div><span>{a}</span><span>{b}</span></div>" for a, b in spec)
        tg = "".join(f"<span>{x}</span>" for x in tags)
        out += f'<article class="ref rv"><div class="ref-img"><img data-par="6" src="assets/img/{img}" alt="{t}"></div><div class="ref-body"><span class="date">{d}</span><div><h3>{t}</h3><div class="model">{m}</div></div><div class="spec">{sp}</div><div class="tags">{tg}</div></div></article>'
    return out + "</div>"


# ---------- SUBPAGE helpers ----------
def phero(crumb, h1_lines, lead, img, extra=""):
    lines = "".join(f'<span class="line"><span>{l}</span></span>' for l in h1_lines)
    im = f'<div class="phero-img hero-in"><div class="disc"></div><img src="{img}" alt=""></div>' if img else "<div></div>"
    return f"""<section class="phero"><div class="wrap">
  <div class="crumbs hero-in"><a href="index.html">Domov</a><span>/</span>{crumb}</div>
  <div class="phero-grid"><div><h1 class="d2">{lines}</h1><p class="lead hero-in">{lead}</p>{extra}</div>{im}</div>
</div></section>"""


def more_svc(cur):
    cards = "".join(
        f'<a class="svc{" cur" if s == cur else ""}" href="{s}.html"><div class="im"><img src="{im}" alt="" loading="lazy"></div><div><h4>{t}</h4><small>{sub}</small></div>{ARR}</a>'
        for s, t, sub, im in ZAGON
    )
    return f"""<section class="more-svc"><div class="wrap">
  <h2 class="d3 rv">Zagon in nastavitev delovanja.</h2>
  <div class="svc-row">{cards}</div>
</div></section>"""


def included(title, items):
    li = "".join(f'<li class="rv"><span class="n">{i+1:02d}</span><span>{t}</span></li>' for i, t in enumerate(items))
    return f'<section class="included"><div class="wrap"><h2 class="d3 rv">{title}</h2><ul class="inc-list">{li}</ul></div></section>'


def guide(title, items, warn=None, figs=""):
    g = "".join(f'<div class="gitem rv"><h4>{h}</h4><p>{p}</p></div>' for h, p in items)
    w = f'<div class="gitem warn rv"><h4>{warn[0]}</h4><p>{warn[1]}</p></div>' if warn else ""
    return f"""<section class="guide"><div class="wrap guide-grid">
  <aside class="guide-side rv"><h2 class="d4">{title}</h2>
    <div class="note"><b>Potrebujete pomoč?</b>Če dokumentacije niste dobili ali niste prepričani, pokličite KSI Servis.<br><a class="btn btn-blue" style="margin-top:18px;height:54px" href="tel:{PHONE_T}">{PH_ICO} {PHONE}</a></div>
  </aside>
  <div class="gitems">{g}{figs}{w}</div>
</div></section>"""


ZAGON_INC = [
    "Priklop senzorike na krmilno omaro, priklop plovnih stikal ali merilne sonde",
    "Priklop krmilne omare na električno omrežje, kontrola napajalne napetosti",
    "Priklop črpalke na krmilno omaro in preverjanje pravilne smeri vrtenja črpalke",
    "Preverjanje pravilnosti delovanja krmilne logike, paralelno in ciklično delovanje",
    "Merjenje toka črpalke pod bremenom, določanje trenutne delovne točke",
    "Izdelava »Poročila o zagonu« z ugotovitvami in pripombami za izboljšanje delovanja",
]
CABLE_OPEN = "Če niste popolnoma prepričani, kako pravilno povezati omenjene kable v krmilno omarico, priklop kablov prepustite našemu serviserju. Zagotovite nam samo dovolj dolge kable, ustrezno položene v kabelske kanale in zaščitne cevi, ki pravilno označeni čakajo pri krmilni omarici na priklop. Za priklop na električno napajanje priporočamo uporabo fleksibilnega kabla ustreznega preseka."
CABINET = "Krmilna omarica mora biti pritrjena v objektu na premišljeno izbrani legi, ki nam omogoča nemoteno odpiranje omarice in varno delo na električnih priključnih sponkah v njeni notranjosti."
POWER_WARN = ("Brez napajanja ni zagona", "Za zagon seveda potrebujemo električno energijo, zato vas prosimo, da nas ne kličete na servisni poseg, če predhodno nimate zagotovljenega napajanja krmilne omarice iz električnega omrežja.")
RELAY = "Za prenos podatkov daljinske signalizacije je potrebno zagotoviti ustrezen signalni kabel in ga povezati na priključne sponke digitalnih relejskih izhodov naprave. Relejske izhode bomo ustrezno parametrirali ob zagonu naprave. Pomembno je, da že vnaprej vemo uporabljeno logiko nadzornega sistema za signale delovanja in napake na napravi."


def crumb(t):
    return f'<a href="servis-crpalk.html">Servis črpalk</a><span>/</span><span>{t}</span>'


def subpages():
    # servis
    svc_list = [
        "Popravilo črpalk, ventilov in sistemov ter intervencije na terenu",
        "Svetovanje, pomoč in analiza pri odpravljanju tehničnih napak",
        "Garancijska popravila črpalk in ventilov",
        "Prodaja nadomestnih črpalk in ventilov",
        "Prodaja originalnih rezervnih delov črpalk in ventilov",
        "Prodaja novih črpalk",
        "Zagon črpalk in naprav ob prvi vgradnji",
        "Servisni pregled in nastavitve delovanja že vgrajene opreme",
    ]
    body = phero('<span>Servis črpalk</span>', ["Servis", "črpalk."], "Pooblaščeni servis KSB. Črpalke servisiramo na vaši lokaciji, večje posege opravimo v naši delavnici v Dragomlju.", "assets/img/pumps/p6.png",
                 f'<div class="hero-actions hero-in" style="display:flex;gap:12px;margin-top:36px;flex-wrap:wrap"><a class="btn btn-blue" href="tel:{PHONE_T}">{PH_ICO} {PHONE}</a><a class="btn btn-ghost" href="kontakt.html">Povpraševanje {ARR}</a></div>')
    body += included("Servisne storitve.", svc_list)
    body += f"""<section class="guide"><div class="wrap">
  <div class="ref-grid" style="margin-top:0">
    <div class="card rv" style="min-height:auto;gap:24px"><h3>Strokoven zagon novih naprav</h3><p style="max-width:52ch">Za nove črpalke in sisteme nudimo zagon črpalk in opreme, predvsem črpalk s frekvenčno regulacijo Pump-Drive, naprav za dvig tlaka Hyamat, črpalk za industrijo Etanorm in CPK, črpalk in naprav za odpadne vode Amarex ter vse ostale opreme.</p><p style="max-width:52ch">Po opravljenem posegu izdamo Zapisnik o uspešno opravljenem zagonu, s katerim dokazujete, da je zagon opravila pooblaščena oseba.</p></div>
    <div class="card big rv" style="min-height:auto;gap:24px;grid-row:auto"><h3>Pogodba o servisu in vzdrževanju</h3><p style="max-width:52ch">Zagotovite si redno servisiranje črpalk in dobavo rezervnih delov v najkrajšem času. Po posebnem dogovoru jih imamo za vas na zalogi.</p><p style="max-width:52ch">Prednost za vas je tekoče vzdrževanje v skladu z vašim terminskim planom, minimalen čas popravila in najkrajši izpad delovanja celotne naprave.</p><a class="btn btn-white" style="align-self:flex-start" href="kontakt.html">Sklenite pogodbo {ARR}</a></div>
  </div>
  <div class="figs" style="margin-top:14px">
    <figure class="rv" style="padding:0;overflow:hidden;min-height:420px;position:relative"><img data-par="5" src="assets/img/ksb_servis1.jpg" alt="Servisna delavnica KSI Servis" style="position:absolute;inset:-6% 0;width:100%;height:112%;object-fit:cover;max-height:none;mix-blend-mode:normal"></figure>
    <figure class="rv" style="padding:0;overflow:hidden;min-height:420px;position:relative"><img data-par="5" src="assets/img/ksb_servis2.jpg" alt="Delovni prostor servisa" style="position:absolute;inset:-6% 0;width:100%;height:112%;object-fit:cover;max-height:none;mix-blend-mode:normal"></figure>
  </div>
</div></section>"""
    body += more_svc(None)
    page("servis-crpalk.html", "servis", "Servis črpalk | KSI Servis", "Pooblaščeni servis črpalk KSB: popravila, garancijska popravila, rezervni deli, zagoni in vzdrževanje.", body)

    # odprti
    s, t, sub, im = ZAGON[0]
    body = phero(crumb(t), ["Zagon črpališč", "odprtega tipa."], "Zagon fekalnih črpališč odprtega tipa z zbiralnim jaškom, npr. Amarex in Ama-Porter.", im)
    body += included("Kaj vse je zajeto v zagon črpališča?", ZAGON_INC)
    body += guide("Priprava na zagon z zbiralnim jaškom.", [
        ("Montaža črpalk", "Črpalke morajo biti pravilno zmontirane in umeščene v cevovod po priloženih navodilih proizvajalca in ustrezni montažni shemi. Če dokumentacije niste dobili, vas prosimo, da pokličete KSI Servis za pomoč."),
        ("Plovna stikala", "Plovna stikala za avtomatsko delovanje črpališča morajo biti nameščena v zbiralnem jašku na poziciji, pri kateri ni ovir za njihovo prosto gibanje oziroma plavanje v črpani tekočini. Stikala morajo biti obvezno pritrjena na inox palico ali podobno podporno konstrukcijo. Omogočen jim mora biti zadosten prosti hod oziroma višinska razlika med vklopom in izklopom."),
        ("Položaj stikal", "Položaj plovnih stikal v zbiralnem jašku (delovno in alarmno stikalo) mora biti predhodno dogovorjen z izvajalcem strojnih inštalacij. Izklop črpalk naj se vedno vrši na takšnem nivoju črpane tekočine, da so črpalke s svojim večjim delom še vedno potopljene, saj jim je s tem zagotovljeno ustrezno hlajenje pogonskega elektromotorja. Alarmno stikalo naj dovolj zgodaj opozarja na nevarno visok nivo fekalne vode v zbiralnem jašku."),
        ("Priprava jaška", "Zaželeno je, da je ob zagonu zbiralni jašek napolnjen z vodo, nikakor pa ne s fekalijami. Če so v jašku že bile fekalije, ga je treba pred zagonom očistiti, izprati s čisto vodo in dezinficirati z aktivnim klorom ali kisikom. Za potrebe zagona in merjenja obratovalnih tokov črpalk je treba zagotoviti način za hitro polnjenje zbiralnega jaška z vodo."),
        ("Kabli in oznake", "Kabli črpalk morajo biti napeljani do krmilne omare in ustrezno označeni, npr. »Črpalka 1« in »Črpalka 2«. Enako velja za plovna stikala, pri katerih moramo vedeti, katero je na najnižji, sredinski in najvišji poziciji. Pri sistemu s tremi plovnimi stikali: »Plovec 1« najnižja pozicija, »Plovec 2« sredinska pozicija in »Plovec 3« najvišja, alarmna pozicija."),
        ("Krmilna omarica", CABINET),
        ("Priklop kablov", CABLE_OPEN),
    ], POWER_WARN)
    body += more_svc(s)
    page(f"{s}.html", "servis", f"{t} | KSI Servis", "Zagon fekalnih črpališč odprtega tipa z zbiralnim jaškom.", body)

    # zaprti
    s, t, sub, im = ZAGON[1]
    body = phero(crumb(t), ["Zagon črpališč", "zaprtega tipa."], "Zagon fekalnih črpališč zaprtega tipa s fekalnim boxom, npr. Compacta in Mini-Compacta.", im)
    body += included("Kaj vse je zajeto v zagon črpališča?", ZAGON_INC)
    body += guide("Priprava na zagon s fekalnim boxom.", [
        ("Montaža boxa", "Fekalni box mora biti pravilno zmontiran in umeščen v cevovod po priloženih navodilih proizvajalca in ustrezni montažni shemi. Če dokumentacije niste dobili, vas prosimo, da pokličete KSI Servis za pomoč."),
        ("Dostopen prostor", "Prostor okrog fekalnega jaška mora biti dostopen, nikakor ne potopljen v vodo ali zalit s fekalijami. Če je prostor poplavljen, je treba vodo izčrpati. Če so ga zalile fekalije, jih izčrpajte, prostor pa ustrezno dezinficirajte."),
        ("Polnjenje z vodo", "Pomembno je, da je ob zagonu zbiralni box možno hitro napolniti z vodo, v nobenem primeru pa ne s fekalijami. Če so v boxu že bile fekalije, ga je treba pred zagonom očistiti, izprati s čisto vodo in dezinficirati z aktivnim klorom ali kisikom."),
        ("Kabli in oznake", "Kabli črpalk morajo biti napeljani do krmilne omare in ustrezno označeni, npr. »Črpalka 1« in »Črpalka 2«. Enako velja za krmilna plovna stikala in merilce nivoja, pri katerih moramo zanesljivo vedeti oziroma lahko izslediti, kateri kabel nas povezuje z določenim merilnim ali krmilnim elementom naprave."),
        ("Krmilna omarica", CABINET),
        ("Priklop kablov", CABLE_OPEN),
    ], POWER_WARN)
    body += more_svc(s)
    page(f"{s}.html", "servis", f"{t} | KSI Servis", "Zagon fekalnih črpališč zaprtega tipa s fekalnim boxom.", body)

    # frekvenca
    s, t, sub, im = ZAGON[2]
    body = phero(crumb(t), ["Zagon črpalk", "s frekvenčno", "regulacijo."], "Zagon in parametriranje frekvenčnih pretvornikov Pump-Drive za optimalno delovno točko.", "assets/img/pumps/p1.png")
    body += included("Kaj vse je zajeto v zagon?", [
        "Priklop senzorike na napravo, priklop senzorja tlaka",
        "Priklop naprave na električno omrežje, kontrola napajalne napetosti",
        "Parametriranje naprave za delovanje v skladu s projektantskimi podatki",
        "Priklop črpalke na napravo in preverjanje pravilne smeri vrtenja",
        "Merjenje toka črpalke pod bremenom, določanje trenutne delovne točke",
        "Izdelava »Poročila o zagonu« z ugotovitvami in pripombami za izboljšanje delovanja",
    ])
    body += guide("Zagon frekvenčnih pretvornikov.", [
        ("Črpalni agregat", "Če so frekvenčni pretvorniki dobavljeni kot črpalni agregat, so tovarniško že zmontirani na črpalkah in parametrirani za točno določen tip črpalke, upoštevajoč ob naročilu definirano delovno točko. Treba jih je le pravilno priklopiti na napajalno napetost, priporočamo zaščitne cevi in fleksibilen napajalni kabel ustreznega preseka. Ob zagonu dodatno preverimo vnesene parametre in poiščemo optimalno delovno točko."),
        ("Stenska montaža", "Frekvenčne pretvornike za stensko montažo je treba s priloženim priborom montirati na steno objekta, upoštevajoč tehnične varnostne zahteve in navodila proizvajalca, zlasti glede hlajenja. Pri dolgi napajalni liniji je treba vgraditi linijske dušilke, napajalni kabli do motorja pa naj bodo oklopljeni in pravilno ozemljeni. S tem preprečimo širjenje elektromagnetnih motenj na ostale elektronske naprave v objektu."),
        ("Selektivnost in FID stikala", "Vsak frekvenčni pretvornik mora biti priključen na napajanje preko lastne varovalke ustreznih električnih karakteristik. Če uporabljate zaščitna diferencialna (FID) stikala, bodite previdni pri izboru diferenčnega toka, saj imajo pretvorniki v vhodnem filtrskem delu kondenzatorsko baterijo s skupno točko, povezano na maso naprave. Za nasvet pokličite KSI Servis."),
        ("Start in stop", "Start in stop frekvenčnih pretvornikov je treba izvesti z digitalnim vhodom »Enable«, namenjenim zagonu in izklopu. Frekvenčnega pretvornika nikakor ne smemo zaganjati s pogostim vklapljanjem in izklapljanjem napajalne napetosti."),
        ("Daljinska signalizacija", RELAY),
    ], figs='<div class="figs rv"><figure><img src="assets/img/pump-drive1.png" alt="Pump-Drive"><figcaption>Pump-Drive na črpalki</figcaption></figure><figure><img src="assets/img/ksb_slika8.png" alt="Črpalka s frekvenčno regulacijo"><figcaption>Črpalka s frekvenčno regulacijo</figcaption></figure></div>')
    body += more_svc(s)
    page(f"{s}.html", "servis", f"{t} | KSI Servis", "Zagon črpalk s frekvenčno regulacijo Pump-Drive.", body)

    # tlak
    s, t, sub, im = ZAGON[3]
    body = phero(crumb(t), ["Zagon naprave", "za zvišanje tlaka."], "Zagon hidropostaj Hyamat, vključno s protipožarnimi napravami in simulacijo hidrantnega odjema.", im)
    body += included("Kaj vse je zajeto v zagon?", [
        "Priklop senzorike na napravo, senzorja tlaka in senzorja suhega teka",
        "Priklop naprave na električno omrežje, kontrola napajalne napetosti",
        "Parametriranje naprave za delovanje po projektni nalogi",
        "Preverjanje pravilne smeri vrtenja črpalke",
        "Merjenje toka črpalke pod bremenom, določanje trenutne delovne točke",
        "Izdelava »Poročila o zagonu« z ugotovitvami in pripombami za izboljšanje delovanja",
    ])
    body += guide("Priprava hidropostaje.", [
        ("Tovarniška konfiguracija", "Naprave za zvišanje tlaka so sestavljene in tovarniško parametrirane glede na naročeno konfiguracijo hidropostaje: število črpalk, način delovanja, zaščita proti suhemu teku, dodatne posebne zaščite in delovni pogoji po zahtevi naročnika."),
        ("Sistem in simulacija odjema", "Hidropostajo je treba pravilno umestiti v cevovod. Za zagon mora biti sistem napolnjen z vodo, z enostavno možnostjo simulacije odjema, s katero preverimo zanesljivost delovanja. Zlasti za protipožarne hidropostaje potrebujemo možnost priklopa gasilske cevi in simulacijo hidrantnega odjema vode."),
        ("Električni priklop", "V krmilni omari naprave je treba pravilno izvesti priklop na električno napajanje. Priporočamo zaščitne cevi in fleksibilen napajalni kabel ustreznega preseka."),
        ("Parametri in delovna točka", "Ob zagonu dodatno preverimo pravilnost vseh vnesenih parametrov naprave in nastavimo optimalno delovno točko."),
        ("Daljinska signalizacija", RELAY),
    ])
    body += more_svc(s)
    page(f"{s}.html", "servis", f"{t} | KSI Servis", "Zagon naprav za zvišanje tlaka Hyamat.", body)

    # centriranje
    s, t, sub, im = ZAGON[4]
    body = phero(crumb("Centriranje elastične sklopke"), ["Centriranje", "elastične", "sklopke."], "Najpogostejši vzrok okvar na črpalkah je nestrokovno ravnanje z elastično sklopko oziroma opustitev njenega uravnavanja.", "assets/img/ksb_slika3.png")
    body += f"""<section class="quote"><div class="wrap quote-grid">
  <div class="figs rv" style="margin:0"><figure><img src="assets/img/shema1.png" alt="Shema centriranja"><figcaption>Kontrola z ravnilom</figcaption></figure><figure><img src="assets/img/shema2.png" alt="Shema uravnavanja"><figcaption>Kontrola s šablono</figcaption></figure><figure style="grid-column:span 2"><img src="assets/img/centriranje_elasticne_sklopke2.png" alt="Centriranje elastične sklopke"><figcaption>Uravnavanje elastične sklopke</figcaption></figure></div>
  <div><p class="d3 rv">Strošek je zanemarljiv glede na možne posledice.</p>
  <div class="body rv" style="margin-top:28px"><p>Dolgoletne izkušnje nam kažejo, da je najpogostejši vzrok okvar na črpalkah nestrokovno ravnanje z elastično sklopko oziroma opustitev nastavitve uravnavanja le-te.</p><p>Znani so nam primeri, ko so črpalke odpovedale že po nekaj dneh samo zaradi neznanja oziroma nekvalitetno izvedenega prvega zagona. Strošek za strokovno izvedeno montažo črpalke in uravnavanje elastične sklopke je zanemarljiv glede na možne posledice.</p></div>
  <a class="btn btn-blue rv" style="margin-top:36px" href="tel:{PHONE_T}">{PH_ICO} Naročite centriranje</a></div>
</div></section>"""
    body += more_svc(s)
    page(f"{s}.html", "servis", "Centriranje in uravnavanje elastične sklopke | KSI Servis", "Strokovno centriranje in uravnavanje elastične sklopke ter poizkusni zagon.", body)

    # daljinski nadzor
    body = phero('<span>Daljinski nadzor</span>', ["Daljinski", "nadzor."], "Stanje vseh črpališč, alarmi in meritve obratovanja na enem zaslonu. Kjerkoli ste.", None)
    body += f"""<section class="monitor" style="padding-top:clamp(70px,10vh,120px)"><div class="wrap">
  <h2 class="d3 rv">Primer daljinskega nadzora črpališča.</h2>
  <div class="screen rv">
    <div class="screen-bar"><i></i><i></i><i></i><div class="tabs"><button>Zemljevid</button><button>Pregled črpališča</button><button>Alarmi</button><button>Histogram</button></div></div>
    <div class="screen-view"><img src="assets/img/daljinski_nadzor1.jpg" alt="Zemljevid črpališč"><img src="assets/img/daljinski_nadzor2.jpg" alt="Pregled črpališča"><img src="assets/img/daljinski_nadzor3.jpg" alt="Alarmi"><img src="assets/img/Histogram.jpg" alt="Histogram"></div>
  </div>
  <div class="mon-feats"><div class="rv"><b>Zemljevid</b><span>Vsa črpališča in njihovo stanje na enem mestu.</span></div><div class="rv"><b>Alarmi</b><span>Napake in visok nivo javi takoj.</span></div><div class="rv"><b>Histogram</b><span>Povprečni tok in obratovanje po črpalkah.</span></div><div class="rv"><b>Relejski izhodi</b><span>Parametriramo jih ob zagonu naprave.</span></div></div>
</div></section>"""
    page("daljinski-nadzor.html", "nadzor", "Daljinski nadzor | KSI Servis", "Daljinski nadzor črpališč: zemljevid, alarmi in meritve.", body)

    # reference
    body = phero('<span>Reference</span>', ["Reference."], "Izbrani servisni posegi na črpalkah KSB iz naše delavnice.", "assets/img/pumps/p5.png")
    body += f'<section class="refs" style="padding-top:clamp(60px,8vh,100px)"><div class="wrap">{refs_html()}</div></section>'
    page("reference.html", "ref", "Reference | KSI Servis", "Reference servisnih posegov KSI Servis.", body)

    # kontakt
    body = f"""<section class="contact"><div class="wrap">
  <div class="crumbs hero-in"><a href="index.html">Domov</a><span>/</span><span>Kontakt</span></div>
  <h1 class="d2"><span class="line"><span>Pokličite.</span></span><span class="line"><span class="gray">Pridemo.</span></span></h1>
  <div class="c-grid">
    <div class="c-info">
      <div class="c-247 rv"><div><b style="color:rgba(255,255,255,.75)">Dežurna številka, vse dni v tednu</b><a href="tel:{PHONE_T}">{PHONE}</a></div><span class="live"></span></div>
      <div class="rv"><b>Naslov</b><p>Dragomelj 136<br>1230 Domžale, Slovenija</p></div>
      <div class="rv"><b>Telefon</b><a href="tel:+38613666171">+386 (0)1 36 66 171</a><p style="font-size:17px;color:var(--gray);margin-top:4px">Faks: +386 (0)1 36 66 670</p></div>
      <div class="rv"><b>E-pošta</b><a href="mailto:info@ksb-servis.si">info@ksb-servis.si</a></div>
      <div class="rv"><b>Podjetje</b><p style="font-size:17px">KSI Servis, prodaja ter montaža črpalk in rezervnih delov, d.o.o.</p></div>
      <div class="full rv" style="font-size:16px;color:var(--gray);display:flex;gap:30px;flex-wrap:wrap"><span>Matična št.: 6217443</span><span>ID za DDV: SI54958539</span><span>TRR: SI56 2900 0005 0656 070 (UniCredit Banka)</span></div>
    </div>
    <form class="form rv">
      <h3>Pošljite povpraševanje</h3>
      <div class="field"><label for="f1">Ime in priimek</label><input id="f1" required></div>
      <div class="field"><label for="f2">Podjetje</label><input id="f2"></div>
      <div class="field"><label for="f3">E-pošta</label><input id="f3" type="email" required></div>
      <div class="field"><label for="f4">Telefon</label><input id="f4" type="tel"></div>
      <div class="field full"><label for="f5">Storitev</label><select id="f5"><option>Servis ali popravilo</option><option>Zagon naprave</option><option>Rezervni deli</option><option>Pogodba o vzdrževanju</option><option>Daljinski nadzor</option><option>Drugo</option></select></div>
      <div class="field full"><label for="f6">Sporočilo in tip črpalke</label><textarea id="f6" placeholder="npr. Etanorm 065-040-250, puščanje tesnila"></textarea></div>
      <button class="btn btn-blue" type="submit">Pošlji povpraševanje {ARR}</button>
      <p class="ok">Hvala. Odgovorili vam bomo v najkrajšem možnem času.</p>
    </form>
  </div>
  <div class="map rv"><iframe loading="lazy" title="Lokacija KSI Servis" src="https://www.openstreetmap.org/export/embed.html?bbox=14.555%2C46.085%2C14.605%2C46.105&amp;layer=mapnik&amp;marker=46.0948%2C14.5807"></iframe></div>
</div></section>"""
    page("kontakt.html", "kontakt", "Kontakt | KSI Servis", "Kontakt KSI Servis, Dragomelj 136, Domžale. Dežurna številka 031 329 250.", body)


if __name__ == "__main__":
    home()
    subpages()

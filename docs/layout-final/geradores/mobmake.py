"""F03 · Mobile interativo: deriva a R01 (desktop final) para 390 x 844, layout 1 (arte no topo).
Uso: python -I mobmake.py <dir com R01 gerada> <dir de saída>"""
import sys, re
SRC, OUT = sys.argv[1], sys.argv[2]

K, TX, TY = 0.42, -162, 155          # câmera de repouso: gravura inteira no topo
ZS, FX, FY = 1.0, 195, 150         # câmera de zoom: estrela no alto, ficha embaixo

REPL = [
    # tamanho da tela
    ('position:relative;width:1280px;height:800px;', 'position:relative;width:390px;height:844px;'),
    # câmera
    ("if (!sel) return { tx: -44, ty: -52, s: 1.07, k: 1, sx: 420, sy: 400 };",
     f"if (!sel) return {{ tx: {TX}, ty: {TY}, s: {K}, k: 1, sx: 195, sy: 220 }};"),
    ("const tx = Math.max(1280 - 1280 * S, Math.min(0, 420 - S * sel.x));",
     f"const tx = Math.max(390 - 1280 * {ZS}, Math.min(0, {FX} - {ZS} * sel.x));"),
    ("const ty = Math.max(800 - 800 * S, Math.min(0, 400 - S * sel.y));",
     f"const ty = Math.min(0, {FY} - {ZS} * sel.y);"),
    ("return { tx, ty, s: S, k: 1.18, sx: tx + S * sel.x, sy: ty + S * sel.y };",
     f"return {{ tx, ty, s: {ZS}, k: 1.18, sx: tx + {ZS} * sel.x, sy: ty + {ZS} * sel.y }};"),
    # no toque não existe "passar o mouse": um toque na legenda já abre a estrela
    ("lg(id) { this.setState({ hl: id }); this.open(id); }",
     "lg(id) { this.setState({ hl: id }); this.open(id); }"),
    # divisória deitada e losango
    ('left: 384px; top: 70px; bottom: 40px; width: 1px; z-index: 3; background: linear-gradient(180deg,',
     'display: none; left: 22px; right: 22px; top: 380px; height: 1px; z-index: 3; background: linear-gradient(90deg,'),
    ('left: 378px; top: 415px; width: 12px; height: 12px;', 'display: none; left: 189px; top: 374px; width: 12px; height: 12px;'),
    # texto embaixo da arte
    ('left: 48px; top: 96px; width: 310px; z-index: 4', 'left: 22px; top: 48px; width: 346px; z-index: 4'),
    ('font-size: 62px; line-height: 1.1', 'font-size: 34px; line-height: 1.1; white-space: nowrap'),
    ('YAGO<br>RICCOMI</h1>', 'YAGO RICCOMI</h1>'),
    ('style="display: block; margin: 26px 0 18px"', 'style="display: block; margin: 8px 0 10px"'),
    ('font-size: 18px; line-height: 1.45; color: var(--soft); width: 300px', 'font-size: 15px; line-height: 1.38; color: var(--soft); width: 346px'),
    # topo e créditos
    ('left: 48px; right: 44px; top: 24px;', 'left: 22px; right: 22px; top: 18px;'),
    ('font-size: 14px; letter-spacing: 0.26em; margin-right: auto', 'font-size: 11px; letter-spacing: 0.26em; margin-right: auto'),
    ('right: 44px; bottom: 34px; z-index: 8', 'right: 22px; top: 16px; z-index: 8'),
    ('font-weight: 600; font-size: 17px; color: var(--soft); text-decoration: underline', 'font-weight: 600; font-size: 14px; color: var(--soft); text-decoration: underline'),
    ('Gravura: Johannes Hevelius, Uranographia (1690) ↗', 'Gravura: Hevelius, 1690 ↗'),
    # texto recolhível (modelo 2: seta no fim da linha)
    ('<p style="margin: 0; font-family: var(--ft); font-style: italic; font-weight: 500; font-size: 15px; line-height: 1.38; color: var(--soft); width: 346px">{{v.lead}}</p>',
     '<div class="clw"><input type="checkbox" id="leadtg" class="tg2" aria-label="Mostrar o texto completo"><p class="tx2" style="margin: 0; font-family: var(--ft); font-style: italic; font-weight: 500; font-size: 15px; line-height: 1.38; color: var(--soft); width: 346px">{{v.lead}}</p><label for="leadtg" class="cc2" aria-hidden="true"><span class="ar2"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span></label></div>'),
    # legenda
    ('.legend{position:absolute;left:48px;bottom:34px;display:flex;gap:14px;', '.legend{position:absolute;left:22px;right:22px;top:516px;display:flex;flex-direction:column;gap:6px;'),
]

MCSS = '''
/* ===== Mobile (F03) ===== */
.root:not(.is-zoom) .scene{clip-path:none}
/* Alvo de toque: a estrela desenhada fica pequena (escala 0,42), então o botão cresce por fora
   para ~44 px na tela (WCAG 2.5.5 / 2.5.8), sem mudar o desenho. */
.pstar::before{content:"";position:absolute;inset:-5px;border-radius:50%}
.root:not(.is-zoom) .pstar{transform:scale(1.6)}
.pstar:focus-visible{outline:none}
.pstar:focus-visible::before{outline:2px solid var(--gold);outline-offset:-4px}
/* Nome da estrela sempre visível no zoom (não há hover no toque) */
.is-zoom .pstar.on .nm{opacity:1}
/* Ficha do projeto vira gaveta (bottom sheet) */
.panel{left:0!important;right:0!important;top:auto!important;bottom:0!important;width:auto!important;max-height:56%!important;overflow:auto;
 padding:26px 22px 22px!important;border-radius:20px 20px 0 0!important;border-left:0!important;border-right:0!important;border-bottom:0!important}
.panel::before{content:"";position:sticky;display:block;top:-16px;margin:-14px auto 12px;width:40px;height:4px;border-radius:2px;background:color-mix(in srgb,var(--gold) 60%,transparent)}
.panel .kick{padding-right:56px}
.panel h2{font-size:28px!important}
.panel .logo{right:62px!important;width:44px!important;height:44px!important}
.x{width:44px!important;height:44px!important;right:12px!important;top:12px!important}
.pn .btn,.btn{min-height:44px;box-sizing:border-box}
/* Legenda: alvos maiores para o dedo */
/* Texto recolhível, modelo 2: três linhas e uma seta no fim da última */
.clw{position:relative}
.tg2{position:absolute;opacity:0;width:1px;height:1px;pointer-events:none}
.tx2{display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:3;overflow:hidden;padding-right:34px;box-sizing:border-box;-webkit-mask-image:linear-gradient(180deg,#000 45%,transparent);mask-image:linear-gradient(180deg,#000 45%,transparent)}
.tg2:checked~.tx2{display:block;-webkit-mask-image:none;mask-image:none}
.cc2{position:absolute;right:-8px;bottom:-10px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--gold);-webkit-tap-highlight-color:transparent}
.tg2:checked~.cc2{position:static;margin:-6px -8px -10px auto}
.ar2{display:inline-flex;transition:transform .35s ease}.tg2:checked~.cc2 .ar2{transform:rotate(180deg)}
.tg2:focus-visible~.cc2{outline:2px solid var(--gold);outline-offset:-4px;border-radius:50%}
.clw:has(.tg2:checked){background:rgba(var(--veil),.94);box-shadow:0 0 0 14px rgba(var(--veil),.94),0 30px 40px 14px rgba(var(--veil),.75)}
@media (prefers-reduced-motion: reduce){.ar2{transition:none}}
/* 9B: pílulas de largura igual em duas colunas */
.legend ul{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.legend li{margin:0!important}
.lgi{width:100%;text-align:left;line-height:1.1;font-size:14px!important;min-height:44px!important;padding:0 12px 0 11px!important}
.lgh{margin:0 0 8px!important;font-size:10px!important}
.legend li{line-height:1}
'''

def mobile(s):
    for a, b in REPL:
        n = s.count(a)
        assert n >= 1, ('não achei', a[:70])
        s = s.replace(a, b)
    s = s.replace('</style>', MCSS + '</style>', 1)
    s = s.replace('"$preview": {"width": 1280, "height": 800}', '"$preview": {"width": 390, "height": 844}')
    return s

for src, dst in (('R01-W11Refino.dc.html', 'F03-MobileInterativo.dc.html'), ('prev-r01.html', 'prev-F03.html')):
    try:
        t = open(f'{SRC}/{src}', encoding='utf-8').read()
    except FileNotFoundError:
        continue
    open(f'{OUT}/{dst}', 'w', encoding='utf-8').write(mobile(t))
    print('ok', dst)

import re, sys, os, json, html
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ident, texts
from logos import LOGOS
def mono(t):
    import urllib.parse
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="29" fill="#140b33" stroke="#e8d4a0" stroke-width="2"/><text x="32" y="41" text-anchor="middle" font-family="Georgia,serif" font-size="24" fill="#e8d4a0">{t}</text></svg>'
    return 'data:image/svg+xml,'+urllib.parse.quote(svg)
PROJ, OUT = sys.argv[1], sys.argv[2]
LOCAL_IMG = sys.argv[3] if len(sys.argv) > 3 else None
BLOB = '/_blob/2b3cb1c9a9b32722e4215e7151293297'
w11 = open(f'{PROJ}/W11-CeuAberto.dc.html', encoding='utf-8').read()

# campo de estrelas do W11, com cores trocadas por variáveis
sf = re.search(r'<div aria-hidden="true"><span.*?</div>', w11).group(0)
sf = sf.replace('#e8d4a0', 'var(--gold)').replace('#d9ccff', 'var(--line)')

POS = {'g': (481, 442), 'd': (543, 430), 'l': (518, 259), 'e': (559, 529), 'f': (761, 407), 's': (856, 351),
       'z': (794, 686), 't': (992, 417), 'p': (859, 212), 'm': (609, 116), 'h': (778, 766)}
EDGES = [('g','d'),('d','l'),('l','f'),('f','s'),('s','t'),('t','z'),('z','e'),('e','d'),('f','z'),('g','e'),('s','p'),('l','m'),('e','h')]
LAW = []   # g, l, f, t viraram estrelas de seção
TINY = ['h']

# Projetos (o texto vem da voz escolhida, em texts.py)
PROJECTS = [
  dict(id='d', greek='δ', star='Kaus Media', name='Alexa no Windows', repo='comandos-em-meu-computador', stack=['JavaScript', 'AWS Lambda', 'MQTT', 'PowerShell'], logo=LOGOS['d']),
  dict(id='m', greek='ν', star='Ain al Rami', name='Vencord Auto-Repair', repo='vencord-autorepair', stack=['PowerShell', 'Batch', 'Pester'], logo=mono('VA')),
  dict(id='e', greek='ε', star='Kaus Australis', name='Fodinha - cardgame', repo='jogo-de-cartas', stack=['React', 'Node', 'Socket.IO', 'TypeScript'], logo=LOGOS['e'], use='https://game.yagoriccomi.com.br'),
  dict(id='s', greek='σ', star='Nunki', name='Snake Thai', repo='snake-thai', stack=['React Native', 'Expo', 'Express', 'Next.js', 'Supabase', 'Zod'], logo=LOGOS['s']),
  dict(id='p', greek='μ', star='Polis', name='Stream P2P', repo='stream-p2p', stack=['Node', 'WebRTC', 'WebSocket', 'Tauri 2', 'Discord'], logo=LOGOS['p']),
  dict(id='z', greek='ζ', star='Ascella', name='Minecraft descentralizado', repo='docker-minecraft-server', stack=['Docker', 'PowerShell', 'Syncthing', 'Tailscale'], logo=mono('MC')),
]
# Seções: estrelas violetas
SECTIONS = [
  dict(id='l', greek='λ', star='Kaus Borealis, o alto do arco', name='Sobre', kind='sobre'),
  dict(id='f', greek='φ', star='Sagittarius', name='Trajetória', kind='traj'),
  dict(id='t', greek='τ', star='Sagittarius', name='Formação', kind='form'),
  dict(id='g', greek='γ', star='Alnasl, a ponta da flecha', name='Contato', kind='cont'),
]
for p in PROJECTS: p['kind'] = 'proj'
# link de uso: campo "Website" do Sobre do repositório no GitHub (lido na hora de gerar)
import subprocess
for p in PROJECTS:
    try:
        h = subprocess.run(['gh', 'api', 'repos/yagoriccomi/' + p['repo'], '--jq', '.homepage // ""'], capture_output=True, text=True, timeout=20).stdout.strip()
        if h: p['use'] = h; p['useLabel'] = '▶ Abrir o app'; continue
        # sem site: última release
        r = subprocess.run(['gh', 'api', 'repos/yagoriccomi/' + p['repo'] + '/releases/latest', '--jq', '.html_url + " " + .tag_name'], capture_output=True, text=True, timeout=20)
        if r.returncode == 0 and r.stdout.strip():
            url, tag = r.stdout.split()
            p['use'] = url; p['useLabel'] = '⤓ Baixar ' + tag
    except Exception: pass
STARS = PROJECTS + SECTIONS
for i, p in enumerate(STARS):
    p['x'], p['y'] = POS[p['id']]
    p['delay'] = [0.0, 1.0, 0.9, 1.7, 1.4, 0.45, 1.2, 0.3, 2.0, 0.7][i]

FONTS = {f[1]: f[0] for f in ident.FONTS}
PALS = {p[1]: p[0] for p in ident.PALS}
S = 2.2   # zoom

CSS = '''
body{margin:0}
.root{--fd:Cinzel,serif;--ft:"Cormorant Garamond",serif;--fu:Sora,system-ui,sans-serif;--fdw:600;--fdt:0.04em;
 --bg1:#1a0e42;--bg0:#06040d;--gold:#e8d4a0;--vio:#b8a4ff;--line:#d9ccff;--ink:#f4f2fa;--soft:#ebe4fb;--muted:#cfc6ee;--imgf:none;--veil:6,4,13;
 position:relative;width:1280px;height:800px;overflow:clip;color:var(--ink);font-family:var(--fu);
 background:radial-gradient(ellipse at 68% 48%,var(--bg1),var(--bg0) 72%)}
'''+ident.css_vars()+'''
a{color:var(--line)}a:hover{color:#fff}
@keyframes twinkle{0%{opacity:0.25}100%{opacity:1}}
@keyframes glow{0%{opacity:0.6;transform:scale(0.96)}100%{opacity:1;transform:scale(1.04)}}
@keyframes fly{0%{transform:translate(1420px,-120px);opacity:0}6%{opacity:1}94%{transform:translate(240px,800px);opacity:1}100%{transform:translate(240px,800px);opacity:0}}
@keyframes reveal{0%{clip-path:inset(0 100% 0 0)}100%{clip-path:inset(0 0 0 0)}}
@keyframes draw{0%{stroke-dashoffset:1}100%{stroke-dashoffset:0}}
@keyframes appear{0%{opacity:0}100%{opacity:1}}
@keyframes blink{0%,100%{transform:scale(1);opacity:0.8}50%{transform:scale(1.32);opacity:1}}
@keyframes ping{0%{transform:scale(0.5);opacity:0.9}80%,100%{transform:scale(2.8);opacity:0}}
@keyframes rise{0%{opacity:0;transform:translateY(14px)}100%{opacity:1;transform:translateY(0)}}
.comet{position:absolute;left:0;top:0;width:0;height:0;z-index:5;opacity:0;animation:fly 1.8s cubic-bezier(.4,0,.6,1) 0.2s 1 both}
.fig{animation:reveal 2.6s ease-in-out 1.2s 1 both;filter:var(--imgf)}
.ln{stroke:var(--line);stroke-opacity:0.7;stroke-width:1.4;stroke-dasharray:1;vector-effect:non-scaling-stroke;animation:draw 0.8s ease-out both}
.in{animation:appear 0.7s ease-out both}
.cap{animation:appear 1s ease-out 3.6s both}
.root p{text-align:justify;hyphens:auto;-webkit-hyphens:auto}
.root .kicker,.root .lgh,.root .kick,.root .nm,.root h1,.root h2,.root h3{text-align:left;hyphens:manual}
.scene{position:absolute;left:0;top:0;width:1280px;height:800px;transform-origin:0 0;will-change:transform}
.root:not(.is-zoom) .scene{clip-path:inset(-200px -400px -200px 401px)}
.sky{position:absolute;left:0;top:0;width:1280px;height:800px;transform-origin:50% 50%}
@keyframes camA{from{transform:translate(var(--fx),var(--fy)) scale(var(--fs))}to{transform:translate(var(--tx),var(--ty)) scale(var(--ts))}}
@keyframes camB{from{transform:translate(var(--fx),var(--fy)) scale(var(--fs))}to{transform:translate(var(--tx),var(--ty)) scale(var(--ts))}}
@keyframes skyA{from{transform:scale(var(--fk))}to{transform:scale(var(--tk))}}
@keyframes skyB{from{transform:scale(var(--fk))}to{transform:scale(var(--tk))}}
.ca .scene{animation:camA var(--dur) cubic-bezier(.66,0,.24,1) both}
.cb .scene{animation:camB var(--dur) cubic-bezier(.66,0,.24,1) both}
.ca .sky{animation:skyA var(--dur) cubic-bezier(.66,0,.24,1) both}
.cb .sky{animation:skyB var(--dur) cubic-bezier(.66,0,.24,1) both}
@keyframes fadeOut{from{opacity:1}to{opacity:0}}
@keyframes fadeInA{from{opacity:0}to{opacity:1}}
@keyframes fadeInB{from{opacity:0}to{opacity:1}}
.zveil{position:absolute;inset:0;z-index:6;pointer-events:none;opacity:0}
.is-zoom .zveil{opacity:1}
.is-zoom.ca .zveil{animation:fadeInA .9s ease .8s both}
.is-zoom.cb .zveil{animation:fadeInB .9s ease .8s both}
.is-out .zveil{animation:fadeOut .5s ease both}
.is-zoom .hero{opacity:0;pointer-events:none;animation:fadeOut .45s ease both}
.is-out .hero{animation:fadeInA .7s ease 1s both}
.law{position:absolute;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:radial-gradient(circle,#fff 15%,var(--line) 55%);box-shadow:0 0 10px var(--line)}
.tiny{position:absolute;width:7px;height:7px;margin:-3.5px 0 0 -3.5px;border-radius:50%;background:radial-gradient(circle,#fff 20%,var(--line) 60%);box-shadow:0 0 8px var(--line);opacity:.8}
.pstar{position:absolute;width:64px;height:64px;margin:-32px 0 0 -32px;padding:0;border:0;background:none;cursor:pointer;border-radius:50%;color:inherit;font:inherit;transition:opacity .4s}
.pstar:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.pstar svg.st{position:absolute;left:0;top:0;width:64px;height:64px;overflow:visible;transition:opacity .35s ease}
.pstar.sec svg.st{left:10px;top:10px;width:44px;height:44px}
.pstar .h{fill:url(#hg)}.pstar.sec .h{fill:url(#hv)}
.pstar .r{fill:url(#rg)}.pstar.sec .r{fill:url(#rv)}
.pstar svg.still{opacity:0;filter:brightness(1.3)}
.pstar svg.dim{opacity:0}
.is-zoom .pstar:not(.on) svg.anim{opacity:0}
.is-zoom .pstar:not(.on) svg.dim{opacity:.5}
.is-zoom .pstar:not(.on):hover svg.dim{opacity:0}
.pstar:hover svg.anim,.pstar:focus-visible svg.anim,.pstar.hl svg.anim,__LIT_svg.anim__{opacity:0}
.pstar:hover svg.still,.pstar:focus-visible svg.still,.pstar.hl svg.still,__LIT_svg.still__{opacity:1}
@keyframes pulse{0%,100%{transform:translateZ(0) scale(1);opacity:1}50%{transform:translateZ(0) scale(.4);opacity:.55}}
.pstar .ring{display:none}
.pstar .nm{transition:opacity .3s;position:absolute;left:50%;bottom:58px;transform:translateX(-50%);white-space:nowrap;font-family:var(--ft);font-style:italic;font-weight:600;font-size:17px;color:var(--ink);text-shadow:0 1px 2px #000,0 0 4px rgb(var(--veil)),0 0 8px rgb(var(--veil)),0 0 14px rgb(var(--veil)),0 0 24px rgb(var(--veil));opacity:0;transition:opacity .3s;pointer-events:none}
.pstar:hover .nm,.pstar:focus-visible .nm,.pstar.hl .nm,__LIT_.nm__{opacity:1}
.is-zoom .pstar .nm{display:none}
.is-zoom .pstar.on{opacity:1}
.is-zoom .pstar.on .ring{animation:none;opacity:.9;transform:scale(1.9)}
.panel{position:absolute;left:720px;top:140px;width:470px;z-index:7;padding:34px 36px 30px;border-radius:4px;background:linear-gradient(160deg,rgba(var(--veil),0.9),rgba(var(--veil),0.78));border:1px solid color-mix(in srgb,var(--gold) 45%,transparent);box-shadow:0 30px 80px rgba(0,0,0,.45);animation:rise .7s ease-out 1.5s both;font-family:var(--ft)}
.panel .kick{margin:0 0 10px;padding-right:120px;font-family:var(--fu);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold)}
.panel h2{margin:0;padding-right:120px;font-family:var(--fd);font-weight:var(--fdw);letter-spacing:var(--fdt);font-size:36px;line-height:1.1;color:var(--ink)}
.panel .rule{display:block;margin:16px 0 18px}
.panel p.txt{margin:0;font-size:21px;line-height:1.45;color:var(--soft)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 0;padding:0;list-style:none}
.chips li{font-family:var(--fu);font-size:12px;padding:5px 11px;border-radius:999px;border:1px solid color-mix(in srgb,var(--line) 45%,transparent);color:var(--muted)}
.acts{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:26px}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:999px;font-family:var(--fu);font-size:14px;font-weight:600;cursor:pointer;text-decoration:none}
.btn.pri{background:var(--gold);color:rgb(var(--veil));border:0}
.btn.sec{background:none;color:var(--ink);border:1px solid color-mix(in srgb,var(--ink) 40%,transparent)}
.btn.sec:hover{border-color:var(--ink);color:#fff}
.x{position:absolute;right:14px;top:14px;width:40px;height:40px;border-radius:50%;border:1px solid color-mix(in srgb,var(--ink) 30%,transparent);background:none;color:var(--ink);font-size:16px;cursor:pointer}
.x:hover{border-color:var(--gold);color:var(--gold)}.x:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.panel .logo{position:absolute;right:66px;top:14px;width:64px;height:64px;border-radius:14px;object-fit:contain}
.btn.use{min-height:50px;padding:0 24px;font-size:16px;background:var(--gold);color:rgb(var(--veil));border:0;box-shadow:0 0 24px color-mix(in srgb,var(--gold) 55%,transparent)}
.btn.use.off{display:none}
.btn.use:hover{filter:brightness(1.1)}
.btn.repo{min-height:50px;padding:0 22px;font-size:15px;background:none;color:var(--soft);border:1px solid color-mix(in srgb,var(--gold) 45%,transparent)}
.btn.repo:hover{border-color:var(--gold);color:#fff}
.pn{display:flex;justify-content:space-between;gap:10px;margin-top:22px;padding-top:14px;border-top:1px solid color-mix(in srgb,var(--line) 20%,transparent)}
.btn.ghost{min-height:40px;padding:0 4px;background:none;border:0;color:var(--muted);font-family:var(--ft);font-style:italic;font-weight:500;font-size:17px}
.btn.ghost:hover{color:#fff}.btn:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.btn.lnk{background:none;border:0;padding:0 6px;color:var(--line);text-decoration:underline;text-underline-offset:4px}
.legend{position:absolute;left:48px;bottom:34px;display:flex;gap:14px;z-index:4;font-family:var(--ft)}
.legend ul{list-style:none;margin:0;padding:0}
.lgh{margin:0 0 4px;display:flex;align-items:center;gap:8px;font-family:var(--fu);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
.lgc:last-child .lgh{color:var(--vio)}
.lgi{border:0;background:none;padding:3px 0;cursor:pointer;font-family:var(--ft);font-style:italic;font-size:17px;color:var(--muted);text-shadow:0 1px 2px #000,0 0 8px rgb(var(--veil))}
.lgi:hover,.lgi:focus-visible,.lgi.hl{color:var(--gold)}.lgi.sec:hover,.lgi.sec:focus-visible,.lgi.sec.hl{color:var(--vio)}
.lgi:focus-visible{outline:1px solid currentColor;outline-offset:3px}
.lgi{display:inline-flex;align-items:center;gap:9px;text-decoration:underline dotted color-mix(in srgb,currentColor 45%,transparent);text-decoration-thickness:1px;text-underline-offset:5px;transition:color .25s,transform .25s,text-decoration-color .25s}
.lgi::before{content:"";flex:none;width:10px;height:10px;background:var(--gold);clip-path:polygon(50% 0,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0 50%,40% 40%);animation:twk 2.8s ease-in-out infinite;transition:transform .25s,filter .25s}
.lgi.sec::before{background:var(--vio)}
li:nth-child(2) .lgi::before{animation-delay:.5s}li:nth-child(3) .lgi::before{animation-delay:1.1s}li:nth-child(4) .lgi::before{animation-delay:1.7s}li:nth-child(5) .lgi::before{animation-delay:.8s}li:nth-child(6) .lgi::before{animation-delay:2.2s}
.lgi:hover,.lgi:focus-visible,.lgi.hl{transform:translateX(4px);text-decoration-style:solid;text-decoration-color:currentColor}
.lgi:hover::before,.lgi:focus-visible::before,.lgi.hl::before{animation:none;transform:scale(1.6) rotate(45deg);filter:drop-shadow(0 0 4px currentColor)}
@keyframes twk{0%,12%,88%,100%{opacity:.45;transform:scale(.8)}50%{opacity:1;transform:scale(1.15)}}
@media (prefers-reduced-motion: reduce){.lgi::before{animation:none;opacity:.9}}
/* Legenda em pílulas: a borda arredondada diz "isto é um botão" */
.legend li{margin:0 0 4px}.lgi{min-height:30px;font-size:15px;box-sizing:border-box;padding:0 11px 0 9px;gap:7px;border:1px solid color-mix(in srgb,var(--gold) 55%,transparent);border-radius:999px;background:rgba(var(--veil),.55);text-decoration:none;color:var(--soft)}.lgi.sec{border-color:color-mix(in srgb,var(--vio) 55%,transparent)}.lgi:hover,.lgi:focus-visible,.lgi.hl{border-color:currentColor;background:rgba(var(--veil),.85);box-shadow:0 0 12px color-mix(in srgb,currentColor 35%,transparent)}.lgi:focus-visible{outline-offset:2px}
.legend i{display:inline-block;clip-path:polygon(50.0% 0.0%,53.1% 42.6%,71.2% 28.8%,57.4% 46.9%,100.0% 50.0%,57.4% 53.1%,71.2% 71.2%,53.1% 57.4%,50.0% 100.0%,46.9% 57.4%,28.8% 71.2%,42.6% 53.1%,0.0% 50.0%,42.6% 46.9%,28.8% 28.8%,46.9% 42.6%)}
.panel.tall{top:96px}
.panel h3{margin:22px 0 8px;font-family:var(--fu);font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);font-weight:600}
.panel p.txt + p.txt{margin-top:12px}
.tl{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px}
.tl li{display:grid;grid-template-columns:130px 1fr;column-gap:14px;font-size:18px;line-height:1.3}
.tl .when{grid-row:span 2;font-family:var(--fu);font-size:12px;color:var(--gold);padding-top:4px}
.tl strong{font-weight:600;color:var(--ink)}
.tl .where{font-size:16px;font-style:italic;color:var(--muted)}
.cl{list-style:none;margin:22px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.cl .btn{font-size:15px}
.city{margin:16px 0 0;font-family:var(--fu);font-size:13px;color:var(--muted)}
.navb{border:0;background:none;cursor:pointer;color:var(--soft);font-family:var(--ft);font-weight:600;font-size:19px;padding:10px 0}
.navb:hover{color:#fff}.navb:focus-visible{outline:2px solid var(--gold);outline-offset:4px}
.kicker{margin:0 0 14px;font-family:var(--fu);font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold)}
@media (prefers-reduced-motion: reduce){.comet,.fig,.ln,.in,.cap,.pstar .ring,.sky span,.scene>div[aria-hidden]{animation:none!important}}
'''

for _x in ('svg.anim', 'svg.still', '.nm'):
    CSS = CSS.replace('__LIT_' + _x + '__', ','.join(f'.root:has(.lgi[data-k="{p["id"]}"]:hover) .pstar[data-k="{p["id"]}"] {_x}' for p in STARS))
FONT_LINK = ident.families()

def lines():
    out = []
    for i, (u, v) in enumerate(EDGES):
        (x1, y1), (x2, y2) = POS[u], POS[v]
        out.append(f'<line class="ln" pathLength="1" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="animation-delay: {2.4 + i*0.12:.2f}s"/>')
    return '<svg aria-hidden="true" width="1280" height="800" style="position: absolute; left: 0; top: 0">' + ''.join(out) + '</svg>'

def static_stars():
    out = []
    for i, k in enumerate(LAW):
        x, y = POS[k]
        out.append(f'<span class="law in" style="left: {x}px; top: {y}px; animation-delay: {1.0 + i*0.25:.2f}s"></span>')
    for i, k in enumerate(TINY):
        x, y = POS[k]
        out.append(f'<span class="tiny in" style="left: {x}px; top: {y}px; animation-delay: {2.0 + i*0.2:.2f}s"></span>')
    return '<div aria-hidden="true">' + ''.join(out) + '</div>'

COMET = re.search(r'<div aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 0; height: 0; z-index: 5; opacity: 0; animation: fly[^"]*">(.*?</div></div>)', w11).group(1)[:-6]
COMET = (COMET.replace('#9d7bff', 'var(--vio)').replace('#f6ecd0', 'var(--gold)'))
# cores com alfa hex não funcionam com var(); troca por color-mix simples
COMET = re.sub(r'var\(--vio\)([0-9a-f]{2})', lambda m: f'color-mix(in srgb, var(--vio) {round(int(m.group(1),16)/2.55)}%, transparent)', COMET)
COMET = re.sub(r'var\(--gold\)([0-9a-f]{2})', lambda m: f'color-mix(in srgb, var(--gold) {round(int(m.group(1),16)/2.55)}%, transparent)', COMET)

RULE = '<svg class="rule" aria-hidden="true" width="180" height="12"><line x1="0" y1="6" x2="76" y2="6" style="stroke: var(--gold)" stroke-opacity="0.6"/><rect x="86" y="2" width="8" height="8" transform="rotate(45 90 6)" fill="none" style="stroke: var(--gold)"/><line x1="104" y1="6" x2="180" y2="6" style="stroke: var(--gold)" stroke-opacity="0.6"/></svg>'
def panel(flag, inner, extra='', tall=False):
    return ('  <sc-if value="{{' + flag + '}}" hint-placeholder-val="{{ false }}">\n'
            '    <section class="panel' + (' tall' if tall else '') + '" aria-live="polite" aria-labelledby="pn-title">\n'
            '      <button type="button" class="x" aria-label="Fechar e voltar ao céu" onClick="{{close}}">✕</button>\n'
            '      <p class="kick">Estrela {{sel.greek}} · {{sel.star}}</p>\n'
            '      <h2 id="pn-title">{{sel.title}}</h2>\n      ' + RULE + '\n' + inner +
            '      <div class="acts">\n'
            + extra + '      </div>\n'
            '      <div class="pn"><button type="button" class="btn ghost" onClick="{{prev}}">← {{prevName}}</button><button type="button" class="btn ghost" onClick="{{next}}">{{nextName}} →</button></div>\n'
            '    </section>\n  </sc-if>\n')
PANELS = (
  panel('isProj', '      <img class="logo" src="{{sel.logo}}" alt="" width="64" height="64">\n      <p class="txt">{{sel.text}}</p>\n      <ul class="chips" aria-label="Stack"><sc-for list="{{sel.stack}}" as="tech" hint-placeholder-count="4"><li>{{tech}}</li></sc-for></ul>\n',
        '        <a class="btn use {{sel.useCls}}" href="{{sel.use}}" target="_blank" rel="noopener">{{sel.useLabel}}</a>\n        <a class="btn repo" href="{{sel.url}}" target="_blank" rel="noopener">Repositório ↗</a>\n') +
  panel('isSobre', '      <sc-for list="{{sel.body}}" as="par" hint-placeholder-count="2"><p class="txt">{{par}}</p></sc-for>\n') +
  panel('isTraj', '      <ol class="tl"><sc-for list="{{path}}" as="e" hint-placeholder-count="5"><li><span class="when">{{e.when}}</span><strong>{{e.what}}</strong><span class="where">{{e.where}}</span></li></sc-for></ol>\n', tall=True) +
  panel('isForm', '      <ul class="tl"><sc-for list="{{degrees}}" as="e" hint-placeholder-count="2"><li style="grid-template-columns: 1fr"><strong>{{e.what}}</strong><span class="where">{{e.where}}</span></li></sc-for></ul>\n      <h3>Cursos Alura · 2022</h3>\n      <ul class="chips" style="margin-top: 0" aria-label="Cursos"><sc-for list="{{courses}}" as="c" hint-placeholder-count="10"><li>{{c}}</li></sc-for></ul>\n', tall=True) +
  panel('isCont', '      <p class="txt">{{sel.text}}</p>\n      <ul class="cl" aria-label="Links de contato">\n        <li><a class="btn pri" href="mailto:{{links.email}}">✉ {{links.email}}</a></li>\n        <li><a class="btn sec" href="{{links.github}}" target="_blank" rel="noopener">GitHub ↗</a></li>\n        <li><a class="btn sec" href="{{links.linkedin}}" target="_blank" rel="noopener">LinkedIn ↗</a></li>\n      </ul>\n      <p class="city">{{links.city}}</p>\n')
)

def body(img):
    return f'''<div class="root {{{{rootCls}}}}">
  <div class="sky" style="{{{{skyStyle}}}}">{sf}</div>
  <div class="scene" style="{{{{sceneStyle}}}}">
    <div aria-hidden="true" style="position: absolute; left: 481px; top: 22px; width: 852px; height: 852px; border-radius: 50%; background: radial-gradient(circle, color-mix(in srgb, var(--vio) 26%, transparent), transparent 70%); animation: glow 5s ease-in-out infinite alternate"></div>
    <img class="fig" alt="" aria-hidden="true" src="{img}" width="1014" height="845" style="position: absolute; left: 400px; top: 26px; width: 1014px; height: 845px">
    {lines()}
    {static_stars()}
    <svg aria-hidden="true" width="0" height="0" style="position: absolute"><defs><radialGradient id="rg"><stop offset="0.15" stop-color="#fff"/><stop offset="0.6" style="stop-color: var(--gold)"/></radialGradient><radialGradient id="hg"><stop offset="0" style="stop-color: var(--gold); stop-opacity: .85"/><stop offset=".45" style="stop-color: var(--gold); stop-opacity: .3"/><stop offset="1" style="stop-color: var(--gold); stop-opacity: 0"/></radialGradient><radialGradient id="hv"><stop offset="0" style="stop-color: var(--vio); stop-opacity: .85"/><stop offset=".45" style="stop-color: var(--vio); stop-opacity: .3"/><stop offset="1" style="stop-color: var(--vio); stop-opacity: 0"/></radialGradient><radialGradient id="rv"><stop offset="0.15" stop-color="#fff"/><stop offset="0.6" style="stop-color: var(--vio)"/></radialGradient></defs></svg>
    <div role="list" aria-label="Estrelas do mapa">
      <sc-for list="{{{{stars}}}}" as="item" hint-placeholder-count="10">
        <div role="listitem" class="in" style="position: absolute; left: 0; top: 0; animation-delay: {{{{item.inDelay}}}}">
          <button type="button" class="pstar {{{{item.cls}}}}" data-k="{{{{item.id}}}}" style="left: {{{{item.x}}}}px; top: {{{{item.y}}}}px" aria-label="{{{{item.aria}}}}" onClick="{{{{item.open}}}}"><span class="ring" aria-hidden="true" style="animation-delay: {{{{item.blinkDelay}}}}"></span><svg class="st anim" viewBox="0 0 64 64" aria-hidden="true"><g><animate attributeName="opacity" calcMode="spline" keyTimes="0;.28;.56;.62;.9;1" values="1;1;.5;.5;1;1" keySplines=".42 0 .58 1;.42 0 .58 1;.42 0 .58 1;.42 0 .58 1;.42 0 .58 1" dur="{{{{item.pd}}}}" begin="{{{{item.begin}}}}" repeatCount="indefinite"/><circle class="h" cx="32" cy="32" r="29"><animate attributeName="r" calcMode="spline" keyTimes="0;.28;.56;.62;.9;1" values="29;29;12;12;29;29" keySplines=".42 0 .58 1;.42 0 .58 1;.42 0 .58 1;.42 0 .58 1;.42 0 .58 1" dur="{{{{item.pd}}}}" begin="{{{{item.begin}}}}" repeatCount="indefinite"/></circle><polygon class="r" points="32.00,9.00 33.53,28.30 41.90,22.10 35.70,30.47 55.00,32.00 35.70,33.53 41.90,41.90 33.53,35.70 32.00,55.00 30.47,35.70 22.10,41.90 28.30,33.53 9.00,32.00 28.30,30.47 22.10,22.10 30.47,28.30"><animate attributeName="points" calcMode="spline" keyTimes="0;.28;.56;.62;.9;1" values="32.00,9.00 33.53,28.30 41.90,22.10 35.70,30.47 55.00,32.00 35.70,33.53 41.90,41.90 33.53,35.70 32.00,55.00 30.47,35.70 22.10,41.90 28.30,33.53 9.00,32.00 28.30,30.47 22.10,22.10 30.47,28.30;32.00,9.00 33.53,28.30 41.90,22.10 35.70,30.47 55.00,32.00 35.70,33.53 41.90,41.90 33.53,35.70 32.00,55.00 30.47,35.70 22.10,41.90 28.30,33.53 9.00,32.00 28.30,30.47 22.10,22.10 30.47,28.30;32.00,22.80 32.61,30.52 35.96,28.04 33.48,31.39 41.20,32.00 33.48,32.61 35.96,35.96 32.61,33.48 32.00,41.20 31.39,33.48 28.04,35.96 30.52,32.61 22.80,32.00 30.52,31.39 28.04,28.04 31.39,30.52;32.00,22.80 32.61,30.52 35.96,28.04 33.48,31.39 41.20,32.00 33.48,32.61 35.96,35.96 32.61,33.48 32.00,41.20 31.39,33.48 28.04,35.96 30.52,32.61 22.80,32.00 30.52,31.39 28.04,28.04 31.39,30.52;32.00,9.00 33.53,28.30 41.90,22.10 35.70,30.47 55.00,32.00 35.70,33.53 41.90,41.90 33.53,35.70 32.00,55.00 30.47,35.70 22.10,41.90 28.30,33.53 9.00,32.00 28.30,30.47 22.10,22.10 30.47,28.30;32.00,9.00 33.53,28.30 41.90,22.10 35.70,30.47 55.00,32.00 35.70,33.53 41.90,41.90 33.53,35.70 32.00,55.00 30.47,35.70 22.10,41.90 28.30,33.53 9.00,32.00 28.30,30.47 22.10,22.10 30.47,28.30" keySplines=".42 0 .58 1;.42 0 .58 1;.42 0 .58 1;.42 0 .58 1;.42 0 .58 1" dur="{{{{item.pd}}}}" begin="{{{{item.begin}}}}" repeatCount="indefinite"/></polygon></g></svg><svg class="st dim" viewBox="0 0 64 64" aria-hidden="true"><circle class="h" cx="32" cy="32" r="12"/><polygon class="r" points="32.00,22.80 32.61,30.52 35.96,28.04 33.48,31.39 41.20,32.00 33.48,32.61 35.96,35.96 32.61,33.48 32.00,41.20 31.39,33.48 28.04,35.96 30.52,32.61 22.80,32.00 30.52,31.39 28.04,28.04 31.39,30.52"/></svg><svg class="st still" viewBox="0 0 64 64" aria-hidden="true"><circle class="h" cx="32" cy="32" r="37.7"/><polygon class="r" points="32.00,2.10 33.99,27.19 44.87,19.13 36.81,30.01 61.90,32.00 36.81,33.99 44.87,44.87 33.99,36.81 32.00,61.90 30.01,36.81 19.13,44.87 27.19,33.99 2.10,32.00 27.19,30.01 19.13,19.13 30.01,27.19"/></svg><span class="nm">{{{{item.name}}}}</span></button>
        </div>
      </sc-for>
    </div>
  </div>
  <div class="zveil" aria-hidden="true" style="background: {{{{veilBg}}}}; left: -14px; top: 0px; position: absolute"></div>
  <div class="comet" aria-hidden="true">{COMET}</div>
  <div class="hero" style="position: absolute; left: 48px; right: 44px; top: 24px; display: flex; gap: 26px; align-items: baseline; z-index: 8"><span style="font-family: var(--fd); font-weight: 600; font-size: 14px; letter-spacing: 0.26em; margin-right: auto; color: var(--gold)">URANOGRAPHIA</span></div>
  <div class="hero" style="position: absolute; right: 44px; bottom: 34px; z-index: 8"><a href="https://polona.pl/preview/5ac16003-101f-4ff1-96ad-3bd3709cc48c" target="_blank" rel="noopener" title="Ver a obra original na Biblioteca Nacional da Polônia (Polona)" style="font-family: var(--ft); font-style: italic; font-weight: 600; font-size: 17px; color: var(--soft); text-decoration: underline; text-decoration-color: color-mix(in srgb, var(--gold) 60%, transparent); text-underline-offset: 4px; text-shadow: 0 1px 2px #000, 0 0 8px rgb(var(--veil)), 0 0 16px rgb(var(--veil))">Gravura: Johannes Hevelius, Uranographia (1690) ↗</a></div>
  <div class="hero" aria-hidden="true" style="position: absolute; left: 384px; top: 70px; bottom: 40px; width: 1px; z-index: 3; background: linear-gradient(180deg, transparent, color-mix(in srgb, var(--gold) 70%, transparent) 12%, color-mix(in srgb, var(--gold) 70%, transparent) 88%, transparent)"></div><div class="hero" aria-hidden="true" style="position: absolute; left: 378px; top: 415px; width: 12px; height: 12px; z-index: 3; border: 1px solid var(--gold); transform: rotate(45deg); background: rgb(var(--veil))"></div>
  <div class="hero" style="position: absolute; left: 48px; top: 96px; width: 310px; z-index: 4">
    <h1 style="margin: 0; font-family: var(--fd); font-weight: var(--fdw); font-size: 62px; line-height: 1.1; letter-spacing: var(--fdt); padding-top: 8px; margin-top: -8px; background: linear-gradient(100deg, #ffffff, var(--gold) 38%, var(--vio) 72%, #ffffff); -webkit-background-clip: text; background-clip: text; color: transparent">YAGO<br>RICCOMI</h1>
    <svg aria-hidden="true" width="300" height="16" style="display: block; margin: 26px 0 18px"><line x1="0" y1="8" x2="128" y2="8" style="stroke: var(--gold)" stroke-opacity="0.6"/><rect x="144" y="2" width="12" height="12" transform="rotate(45 150 8)" fill="none" style="stroke: var(--gold)"/><line x1="172" y1="8" x2="300" y2="8" style="stroke: var(--gold)" stroke-opacity="0.6"/></svg>
    <p style="margin: 0; font-family: var(--ft); font-style: italic; font-weight: 500; font-size: 18px; line-height: 1.45; color: var(--soft); width: 300px">{{{{v.lead}}}}</p>
  </div>
  <div class="hero legend" role="group" aria-label="Legenda">
    <div class="lgc"><p class="lgh"><i aria-hidden="true" style="width: 15px; height: 15px; background: var(--gold)"></i>Projetos</p><ul><sc-for list="{{{{lgProj}}}}" as="it" hint-placeholder-count="6"><li><button type="button" class="lgi {{{{it.lcls}}}}" data-k="{{{{it.id}}}}" onClick="{{{{it.lg}}}}">{{{{it.name}}}}</button></li></sc-for></ul></div>
    <div class="lgc"><p class="lgh"><i aria-hidden="true" style="width: 12px; height: 12px; background: var(--vio)"></i>O caminho</p><ul><sc-for list="{{{{lgSec}}}}" as="it" hint-placeholder-count="4"><li><button type="button" class="lgi sec {{{{it.lcls}}}}" data-k="{{{{it.id}}}}" onClick="{{{{it.lg}}}}">{{{{it.name}}}}</button></li></sc-for></ul></div>
  </div>
{PANELS}
</div>'''

LOGIC = r'''
const STARS = __STARS__;
const VOICES = __VOICES__;
const PROJ_TEXT = __PROJ_TEXT__;
const DATA = __DATA__;
const FONTS = __FONTS__;
const PALS = __PALS__;
const S = __S__;
function cam(sel) {
  if (!sel) return { tx: -44, ty: -52, s: 1.07, k: 1, sx: 420, sy: 400 };
  const tx = Math.max(1280 - 1280 * S, Math.min(0, 420 - S * sel.x));
  const ty = Math.max(800 - 800 * S, Math.min(0, 400 - S * sel.y));
  return { tx, ty, s: S, k: 1.18, sx: tx + S * sel.x, sy: ty + S * sel.y };
}
const TITLE = { sobre: 't_sobre', traj: 't_traj', form: 't_form', cont: 't_cont' };
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { sel: null, prev: null, n: 0, dur: 1.8, hl: null }; this.lgT = 0; }
  go(id, dur) { this.setState({ prev: this.state.sel, sel: id, n: this.state.n + 1, dur, hl: null }); }
  lg(id) { this.setState({ hl: id }); this.open(id); }
  open(id) { if (id !== this.state.sel) this.go(id, this.state.sel ? 1.6 : 1.8); }
  renderVals() {
    const v = VOICES.find((x) => x.label === this.props.voz) || VOICES[0];
    const find = (id) => STARS.find((p) => p.id === id) || null;
    const sel = find(this.state.sel);
    const a = cam(find(this.state.prev)), b = cam(sel);
    const vars = '--fx: ' + a.tx + 'px; --fy: ' + a.ty + 'px; --fs: ' + a.s + '; --tx: ' + b.tx + 'px; --ty: ' + b.ty + 'px; --ts: ' + b.s + '; --dur: ' + this.state.dur + 's';
    const f = FONTS[this.props.fonte] || 'f2';
    const p = PALS[this.props.paleta] || 'pa';
    const n = this.state.n;
    const phase = n === 0 ? '' : (n % 2 ? ' ca' : ' cb');
    const kind = sel ? sel.kind : '';
    const full = (q) => ({
      ...q,
      title: q.kind === 'proj' ? q.name : v[TITLE[q.kind]],
      text: q.kind === 'proj' ? PROJ_TEXT[v.proj][q.id] : (q.kind === 'cont' ? v.contato : ''),
      body: q.kind === 'sobre' ? v.sobre : [],
      url: q.repo ? 'https://github.com/yagoriccomi/' + q.repo : '#',
      useCls: q.use ? '' : 'off', useLabel: q.useLabel || '', use: q.use || '#', logo: q.logo || '',
    });
    const group = STARS.filter((q) => (q.kind === 'proj') === (kind === 'proj'));
    const gi = group.findIndex((q) => q.id === this.state.sel);
    const nq = group[(gi + 1) % group.length], pq = group[(gi - 1 + group.length) % group.length];
    const short = (q) => q.kind === 'proj' ? q.name : v[TITLE[q.kind]];
    const lgItem = (q) => ({ id: q.id, name: q.name, lcls: q.id === this.state.hl ? 'hl' : '', lg: () => this.lg(q.id) });
    const abc = (a, b) => a.name.localeCompare(b.name, 'pt');
    const first = (k) => STARS.find((q) => q.kind === k).id;
    return {
      rootCls: f + ' ' + p + (sel ? ' is-zoom' : (n ? ' is-out' : '')) + phase,
      sceneStyle: 'transform: translate(' + b.tx + 'px, ' + b.ty + 'px) scale(' + b.s + '); ' + vars,
      skyStyle: 'transform: scale(' + b.k + '); --fk: ' + a.k + '; --tk: ' + b.k + '; --dur: ' + this.state.dur + 's',
      veilBg: 'radial-gradient(circle at ' + b.sx + 'px ' + b.sy + 'px, rgba(var(--veil),0) 0, rgba(var(--veil),0) 110px, rgba(var(--veil),0.62) 520px), linear-gradient(180deg, rgba(var(--veil),0.8), rgba(var(--veil),0) 110px)',
      v,
      isProj: kind === 'proj', isSobre: kind === 'sobre', isTraj: kind === 'traj', isForm: kind === 'form', isCont: kind === 'cont',
      sel: sel ? full(sel) : { greek: '', star: '', title: '', text: '', body: [], stack: [], url: '#', useCls: 'off', useLabel: '', use: '#', logo: '' },
      path: DATA.path, degrees: DATA.degrees, courses: DATA.courses, links: DATA.links,
      stars: STARS.map((q, i) => ({
        ...q,
        cls: (q.kind === 'proj' ? '' : 'sec ') + (q.id === this.state.sel ? 'on' : '') + (q.id === this.state.hl ? ' hl' : ''),
        aria: q.kind === 'proj' ? 'Abrir projeto ' + q.name : 'Abrir ' + q.name,
        inDelay: (0.8 + i * 0.3) + 's',
        blinkDelay: q.delay + 's',
        pd: [4.6, 5.0, 5.3, 4.9, 5.2, 5.7, 5.1, 4.4, 5.5, 4.8][i] + 's',
        begin: '-' + [0, 2.6, 2.1, 3.7, 3.1, 1.2, 4.4, 0.6, 2.9, 1.8][i] + 's',
        open: () => this.open(q.id),
      })),
      nav: {
        proj: () => this.open(first('proj')), sobre: () => this.open('l'), traj: () => this.open('f'),
        form: () => this.open('t'), cont: () => this.open('g'),
      },
      close: () => this.go(null, 1.5),
      next: () => this.go(nq.id, 1.6),
      prev: () => this.go(pq.id, 1.6),
      nextName: sel ? short(nq) : '', prevName: sel ? short(pq) : '',
      lgProj: STARS.filter((q) => q.kind === 'proj').sort(abc).map(lgItem),
      lgSec: STARS.filter((q) => q.kind !== 'proj').sort(abc).map(lgItem),
    };
  }
}
'''

def logic():
    j = lambda x: json.dumps(x, ensure_ascii=False)
    data = dict(path=texts.PATH, degrees=texts.DEGREES, courses=texts.COURSES, links=texts.LINKS)
    return (LOGIC.replace('__STARS__', j(STARS)).replace('__VOICES__', j(texts.VOICES))
                 .replace('__PROJ_TEXT__', j(texts.PROJ_TEXT)).replace('__DATA__', j(data))
                 .replace('__FONTS__', j(FONTS)).replace('__PALS__', j(PALS)).replace('__S__', str(S)))

props = {
  "$preview": {"width": 1280, "height": 800},
  "fonte": {"editor": "enum", "options": list(FONTS), "default": "EB Garamond", "section": "Identidade"},
  "paleta": {"editor": "enum", "options": list(PALS), "default": list(PALS)[0], "section": "Identidade"},
  "voz": {"editor": "enum", "options": [x['label'] for x in texts.VOICES], "default": texts.VOICES[0]['label'], "section": "Textos"},
}
props_attr = json.dumps(props, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')

dc = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>W11 · Refino</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="{FONT_LINK}">
<style>{CSS}</style>
</helmet>
{body(BLOB)}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{props_attr}'>
{logic()}
</script>
</body>
</html>
'''
os.makedirs(OUT, exist_ok=True)
open(f'{OUT}/R01-W11Refino.dc.html', 'w', encoding='utf-8').write(dc)

# ---- prévia local: mini-renderizador (holes, sc-if, sc-for) em JS puro ----
tpl = body(LOCAL_IMG or BLOB)
preview = rf'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="{FONT_LINK}"><style>{CSS}</style></head>
<body><div id="app"></div>
<template id="tpl">{tpl}</template>
<script>
class DCLogic {{ constructor(p){{this.props=p||{{}};this.state={{}};}} setState(s){{Object.assign(this.state,s);render();}} }}
{logic()}
const params = new URLSearchParams(location.search);
const comp = new Component({{fonte: params.get('f') || undefined, paleta: params.get('p') || undefined}});
if (params.get('sel')) comp.state.sel = params.get('sel');
const get = (ctx, path) => path.trim().split('.').reduce((o, k) => (o == null ? o : o[k]), ctx);
function fill(str, ctx) {{ return str.replace(/\{{\{{\s*([^}}]+?)\s*\}}\}}/g, (m, p) => {{ const v = p.trim()==='false'?false:get(ctx,p); return typeof v === 'function' ? '' : (v == null ? '' : String(v)); }}); }}
let handlers = [];
function expand(src, ctx) {{
  src = src.replace(/<sc-if value="\{{\{{\s*([\w.]+)\s*\}}\}}"[^>]*>([\s\S]*?)<\/sc-if>/g, (m, c, b) => get(ctx, c) ? b : '');
  src = src.replace(/<sc-for list="\{{\{{\s*([\w.]+)\s*\}}\}}" as="(\w+)"[^>]*>([\s\S]*?)<\/sc-for>/g, (m, l, as, b) =>
     (get(ctx, l) || []).map((it, i) => expand(b, Object.assign({{}}, ctx, {{[as]: it, $index: i}}))).join(''));
  src = src.replace(/onclick="\{{\{{\s*([\w.]+)\s*\}}\}}"/gi, (m, p) => {{ handlers.push(get(ctx, p)); return 'data-h="' + (handlers.length - 1) + '"'; }});
  return fill(src, ctx);
}}
const app = document.getElementById('app');
const T = document.getElementById('tpl').innerHTML.replace(/&amp;/g,'&');
let root = null;
function render() {{
  handlers = [];
  const html = expand(T, comp.renderVals());
  const tmp = document.createElement('div'); tmp.innerHTML = html;
  const fresh = tmp.firstElementChild;
  if (!root) {{ app.appendChild(fresh); root = fresh; }}
  else {{
    // preserva o DOM da cena para a transição funcionar
    root.className = fresh.className;
    root.querySelector('.scene').setAttribute('style', fresh.querySelector('.scene').getAttribute('style'));
    root.querySelector('.sky').setAttribute('style', fresh.querySelector('.sky').getAttribute('style'));
    root.querySelector('.zveil').setAttribute('style', fresh.querySelector('.zveil').getAttribute('style'));
    const nb = root.querySelectorAll('.pstar'), fb = fresh.querySelectorAll('.pstar');
    nb.forEach((b, i) => {{ b.className = fb[i].className; b.dataset.h = fb[i].dataset.h; }});
    root.querySelectorAll('.lgi').forEach((b, i) => {{ const f = fresh.querySelectorAll('.lgi')[i]; b.className = f.className; b.dataset.h = f.dataset.h; }});
    const op = root.querySelector('.panel'); const np = fresh.querySelector('.panel');
    if (op && np) op.replaceWith(np); else if (op) op.remove(); else if (np) root.appendChild(np);
  }}
}}
document.addEventListener('click', (e) => {{ const el = e.target.closest('[data-h]'); if (el) {{ const h = handlers[+el.dataset.h]; if (h) h(); }} }});
render();
</script></body></html>'''
open(f'{OUT}/prev-r01.html', 'w', encoding='utf-8').write(preview)
print('ok', len(dc))

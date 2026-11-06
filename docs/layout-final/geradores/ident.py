# Opções de identidade compartilhadas por R01 (tweaks), R03 (fontes) e R04 (cores)
# fonte: (classe, rótulo, display, peso, tracking, texto, ui, nota)
FONTS = [
  ('fa', 'Cinzel + Cormorant (atual)', 'Cinzel', 600, '0.04em', 'Cormorant Garamond', 'Sora', 'romano de inscrição + Garamond'),
  ('fb', 'IM Fell English (Fonte 2)', 'IM Fell English SC', 400, '0.02em', 'IM Fell English', 'Sora', 'tipos de Oxford, c. 1670'),
  ('f1', 'IM Fell Great Primer', 'IM Fell Great Primer SC', 400, '0.03em', 'IM Fell DW Pica', 'Sora', 'mesma coleção Fell, corpo maior e mais calmo'),
  ('f2', 'EB Garamond', 'EB Garamond', 500, '0.07em', 'EB Garamond', 'Sora', 'Garamond do séc. XVI, redesenho fiel'),
  ('f3', 'Libre Caslon', 'Libre Caslon Display', 400, '0.03em', 'Libre Caslon Text', 'Sora', 'Caslon inglês, séc. XVIII'),
  ('f4', 'Sorts Mill Goudy', 'Sorts Mill Goudy', 400, '0.05em', 'Sorts Mill Goudy', 'Sora', 'Goudy de 1915, tinta de prensa'),
  ('f5', 'Alegreya SC + Alegreya', 'Alegreya SC', 500, '0.04em', 'Alegreya', 'Sora', 'caligráfica, ritmo de manuscrito'),
  ('f6', 'Cardo', 'Cardo', 700, '0.05em', 'Cardo', 'Sora', 'feita para textos clássicos e humanistas'),
]
# Paletas: todas com base violeta; muda o acento (o "ouro") e o tom do fundo
BASE = dict(bg1='#1a0e42', bg0='#06040d', gold='#e8d4a0', vio='#b8a4ff', line='#d9ccff',
            ink='#f4f2fa', soft='#ebe4fb', muted='#cfc6ee', veil='6,4,13')
PALS = [
  ('pa', 'Violeta e ouro (atual)', {}, 'complementar clássico: o amarelo frente ao violeta'),
  ('pe', 'Violeta e âmbar', dict(bg1='#1d0f45', gold='#f2ab62', vio='#c2a8ff'), 'complementar dividido, puxado para o laranja'),
  ('pf', 'Violeta e lima', dict(bg1='#170f40', bg0='#05040c', gold='#cfe887', vio='#a995ff', line='#d6ccff'), 'complementar dividido, puxado para o verde'),
  ('pg', 'Violeta e menta', dict(bg1='#160e46', bg0='#05040f', gold='#8fe5cf', vio='#b39cff', line='#d3ccff'), 'tríade fria: violeta, menta e lavanda'),
  ('ph', 'Violeta e coral', dict(bg1='#22103f', bg0='#08040d', gold='#ff9f8f', vio='#c9a2ff', line='#e2d0ff', soft='#f1e4fb'), 'análoga quente: rosa e violeta'),
  ('pi', 'Ameixa e cobre', dict(bg1='#2a0f3a', bg0='#0a040c', gold='#e8a276', vio='#d89ce8', line='#ecd3f2', soft='#f2e4f3', muted='#d7c1df', veil='10,4,12'), 'violeta avermelhado com metal quente'),
]
def pal(vars_):
    v = dict(BASE); v.update(vars_); return v

def families():
    fams = ['Sora:wght@400;600', 'Cinzel:wght@500;600;700',
            'Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600',
            'IM+Fell+English+SC', 'IM+Fell+English:ital@0;1', 'IM+Fell+Great+Primer+SC', 'IM+Fell+DW+Pica:ital@0;1',
            'EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500', 'Libre+Caslon+Display', 'Libre+Caslon+Text:ital,wght@0,400;0,700;1,400',
            'Sorts+Mill+Goudy:ital@0;1', 'Alegreya+SC:wght@500', 'Alegreya:ital,wght@0,400;0,500;1,400;1,500',
            'Cardo:ital,wght@0,400;0,700;1,400']
    return 'https://fonts.googleapis.com/css2?' + '&amp;'.join('family=' + f for f in fams) + '&amp;display=swap'

def css_vars():
    out = []
    for c, _, d, w, t, tx, ui, _n in FONTS:
        out.append(f".{c}{{--fd:'{d}',serif;--ft:'{tx}',serif;--fu:'{ui}',system-ui,sans-serif;--fdw:{w};--fdt:{t}}}")
    for c, _, v, _n in PALS:
        v = pal(v)
        out.append(f".{c}{{--bg1:{v['bg1']};--bg0:{v['bg0']};--gold:{v['gold']};--vio:{v['vio']};--line:{v['line']};--ink:{v['ink']};--soft:{v['soft']};--muted:{v['muted']};--veil:{v['veil']}}}")
    return '\n'.join(out)

def lum(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)
def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)

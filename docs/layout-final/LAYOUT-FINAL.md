# Layout final: desktop e mobile

Especificação para construir as duas telas aprovadas no canvas de design (página **Final**). As pranchas de referência são:

- **F01 · Desktop final**: 1280 × 800.
- **F03 · Mobile interativo**: 390 × 844. É o refino 9B, com o texto recolhível do modelo 2.

O canvas está em <https://claude.ai/code/artifact/655e7eeb-cb29-4996-966a-a34b62835749> (versão 176).

Os scripts que geram as duas telas estão em [`geradores/`](geradores/). Eles são a fonte exata de cada número deste documento; veja a seção 6.

---

## 1. Base comum

### 1.1 Tokens

| Token | Valor | Uso |
|---|---|---|
| `--gold` | `#e8d4a0` | projetos, títulos de grupo, divisória, botões primários |
| `--vio` | `#b8a4ff` | seções ("O caminho") |
| `--line` | `#d9ccff` | linhas da constelação, links |
| `--ink` | `#f4f2fa` | texto forte |
| `--soft` | `#ebe4fb` | texto de corpo |
| `--muted` | `#cfc6ee` | texto secundário |
| `--veil` | `6,4,13` (RGB) | véus e fundos translúcidos: `rgba(var(--veil), a)` |
| `--bg1` / `--bg0` | `#1a0e42` / `#06040d` | fundo: `radial-gradient(ellipse at 68% 48%, var(--bg1), var(--bg0) 72%)` |
| `--fd` | EB Garamond, peso 500, `letter-spacing: .07em` | nome (h1), títulos da ficha |
| `--ft` | EB Garamond, itálico | corpo, legenda, nomes de estrela |
| `--fu` | Sora | rótulos em caixa alta, botões |

### 1.2 Cena (mesma nos dois layouts)

A cena é um plano de **1280 × 800** em coordenadas fixas. A câmera move a cena inteira com `transform: translate(tx, ty) scale(s)`, com `transform-origin: 0 0`.

- **Gravura:** Johannes Hevelius, *Firmamentum Sobiescianum sive Uranographia* (1690), placa de Sagitário, em `left: 400px; top: 26px; 1014 × 845`. Fonte: Polona, Biblioteca Nacional da Polônia, <https://polona.pl/preview/5ac16003-101f-4ff1-96ad-3bd3709cc48c>.
- **Estrelas** (centro, em px da cena):

| id | Estrela | Destino | x | y |
|---|---|---|---|---|
| d | δ Kaus Media | Alexa no Windows | 543 | 430 |
| m | ν Ain al Rami | Vencord Auto-Repair | 609 | 116 |
| e | ε Kaus Australis | Fodinha - cardgame | 559 | 529 |
| s | σ Nunki | Snake Thai | 856 | 351 |
| p | μ Polis | Stream P2P | 859 | 212 |
| z | ζ Ascella | Minecraft descentralizado | 794 | 686 |
| l | λ Kaus Borealis | Sobre (seção) | 518 | 259 |
| f | φ | Trajetória (seção) | 761 | 407 |
| t | τ | Formação (seção) | 992 | 417 |
| g | γ Alnasl | Contato (seção) | 481 | 442 |
| h | (decorativa) | — | 778 | 766 |

- **Linhas:** g–d, d–l, l–f, f–s, s–t, t–z, z–e, e–d, f–z, g–e, s–p, l–m, e–h. Traço `var(--line)`, opacidade .7, 1,4 px, `vector-effect: non-scaling-stroke`.
- **Botão de estrela:** um `<button>` de 64 × 64 centralizado no ponto, com `aria-label` próprio. Projetos usam desenho dourado de 64 px; seções usam violeta de 44 px.
- **Nome da estrela** acima dela (Cormorant itálico 600, 17 px), visível no hover, no foco e quando a pílula correspondente está ativa.

### 1.3 Zoom ao abrir uma estrela

- Animação da câmera: `cubic-bezier(.66, 0, .24, 1)`, 1,8 s na primeira abertura e 1,6 s entre estrelas.
- Durante o zoom, o bloco de texto e a legenda somem (`opacity: 0`, .45 s).
- Um véu escurece o céu e deixa um "foco" de 110 px ao redor da estrela:
  `radial-gradient(circle at sx sy, transparent 0 110px, rgba(veil,.62) 520px)`, mais uma faixa escura de 110 px no topo.
- A ficha mostra o kicker ("Estrela σ · Nunki"), o título, o texto, a stack em chips, os botões **Abrir o app / Baixar** e **Repositório ↗**, e a navegação ← anterior / próxima →. O fechar (✕) volta ao céu.

### 1.4 Legenda em pílulas

Há dois grupos: **Projetos** (dourado) e **O caminho** (violeta). Cada um tem um rótulo em Sora 11 px, caixa alta, `letter-spacing: .2em`, com uma estrela de 16 pontas antes.

Cada item é um `<button class="lgi">` em forma de pílula:

- borda `1px solid color-mix(in srgb, var(--gold) 55%, transparent)` (violeta no grupo "O caminho"), `border-radius: 999px`, fundo `rgba(var(--veil), .55)`;
- Cormorant itálico, cor `--soft`;
- dentro, à esquerda, uma estrelinha de 4 pontas (10 px) que pisca: `@keyframes twk{0%,12%,88%,100%{opacity:.45;scale:.8} 50%{opacity:1;scale:1.15}}`, 2,8 s, com atrasos diferentes por item;
- **hover, foco e ativo:** a borda assume a cor cheia, o fundo vai a .85, ganha brilho `0 0 12px`, a pílula anda 4 px para a direita e a estrelinha cresce 1,6× e gira 45°;
- passar o mouse na pílula também acende a estrela dela no céu;
- **um clique ou toque** abre a estrela: `lg(id) { setState({ hl: id }); open(id) }`;
- com `prefers-reduced-motion`, a estrelinha fica parada.

### 1.5 Textos

- **Topo à esquerda:** `URANOGRAPHIA` (EB Garamond 500, `letter-spacing: .26em`, dourado).
- **Nome:** `YAGO RICCOMI` em EB Garamond com gradiente `linear-gradient(100deg, #fff, var(--gold) 38%, var(--vio) 72%, #fff)` recortado no texto.
- **Texto principal** (o mesmo nos dois layouts; vem de `hero.lead` em `src/i18n.ts`):
  > Desenvolvedor de software e estudante de Direito. Construo sites, APIs e apps com React, Node e TypeScript. Uso meus estudos em cibersegurança e LGPD para garantir a proteção dos meus clientes. Este é o meu céu: as estrelas douradas são projetos; as violetas, o caminho até aqui.
- **Créditos da gravura:** um link para a Polona, em Cormorant itálico 600, cor `--soft`, sublinhado dourado a 60% com `text-underline-offset: 3px` e sombra para leitura sobre a arte.
- **Regras de redação:** sempre o cargo mais completo ("Desenvolvedor de software"), sem conectivos repetidos na mesma frase e sem textos de instrução na tela. Só o texto de corpo com mais de uma linha é justificado (`text-align: justify; hyphens: auto`). Títulos, rótulos, nomes de estrela e pílulas ficam alinhados à esquerda.

---

## 2. Desktop (1280 × 800)

Divisão 30/70: texto à esquerda, céu à direita, separados por uma divisória dourada vertical.

| Elemento | Posição e medidas |
|---|---|
| Câmera em repouso | `translate(-44px, -52px) scale(1.07)` |
| Recorte do céu em repouso | `clip-path: inset(-200px -400px -200px 401px)` na cena: nada da arte aparece à esquerda da divisória |
| Divisória | `left: 384px; top: 70px; bottom: 40px; width: 1px`, `linear-gradient(180deg, transparent, gold 70% em 12%…88%, transparent)` |
| Losango da divisória | 12 × 12, borda dourada, girado 45°, em `left: 378px; top: 415px` |
| Barra do topo | `left: 48px; right: 44px; top: 24px`; `URANOGRAPHIA` em 14 px |
| Bloco do texto | `left: 48px; top: 96px; width: 310px` |
| Nome | 62 px, `line-height: 1.1`, em duas linhas (`YAGO` / `RICCOMI`) |
| Ornamento sob o nome | linha + losango, 300 × 16, `margin: 26px 0 18px` |
| Texto principal | Cormorant itálico 500, 18 px, `line-height: 1.45`, largura 300 px, justificado |
| Legenda | `left: 48px; bottom: 34px`; dois grupos lado a lado, `gap: 14px` |
| Pílula | `min-height: 30px`, 15 px, `padding: 0 11px 0 9px`, `gap: 7px`, 4 px entre pílulas |
| Créditos | `right: 44px; bottom: 34px`, 17 px: "Gravura: Johannes Hevelius, Uranographia (1690) ↗" |
| Zoom | escala `S = 2.2`; a estrela vai para (420, 400), limitada às bordas da cena |
| Ficha | `left: 720px; top: 140px; width: 470px`, fundo `rgba(veil, .9 → .78)`, borda dourada a 45%, raio 4 px |

**Folgas conferidas:** o texto termina em 516 px e a legenda começa em 543 px. A legenda termina em 359 px na horizontal, a 25 px da divisória, o que cobre o deslocamento de 4 px do hover.

---

## 3. Mobile (390 × 844)

Leitura no alto, céu no meio, toque embaixo. A tela não rola.

| Elemento | Posição e medidas |
|---|---|
| Câmera em repouso | `translate(-162px, 155px) scale(0.42)`; a estrela mais à esquerda fica a 40 px da borda |
| Recorte do céu | nenhum (`clip-path: none`) |
| Divisória vertical e losango | ocultos |
| Barra do topo | `left: 22px; right: 22px; top: 18px`; `URANOGRAPHIA` em 11 px à esquerda |
| Créditos | no topo, à direita (`right: 22px; top: 16px`), 14 px, texto curto: "Gravura: Hevelius, 1690 ↗" |
| Bloco do texto | `left: 22px; top: 48px; width: 346px` |
| Nome | 34 px, uma linha só (`white-space: nowrap`): `YAGO RICCOMI` |
| Ornamento sob o nome | `margin: 8px 0 10px` |
| Texto principal | 15 px, `line-height: 1.38`, largura 346 px, **recolhível** (seção 4) |
| Estrelas em repouso | desenho ampliado 1,6× (`scale(1.6)`); área de toque estendida 5 px para fora do botão |
| Legenda | `left: 22px; right: 22px; top: 516px`; grupos empilhados (`flex-direction: column; gap: 6px`) |
| Pílulas | grade de 2 colunas de largura igual (`grid-template-columns: 1fr 1fr; gap: 8px`), `min-height: 44px`, 14 px, `text-align: left; line-height: 1.1` (nomes longos quebram em duas linhas) |
| Zoom | escala 1,0; a estrela vai para (195, 150), na faixa livre do alto: `tx = max(390 − 1280, min(0, 195 − x))`, `ty = min(0, 150 − y)` |
| Ficha | gaveta presa ao pé: `bottom: 0`, `max-height: 56%`, raio `20px 20px 0 0`, alça de 40 × 4 px no topo, rolagem interna |
| Botões da ficha | fechar 44 × 44, botões com `min-height: 44px`, título 28 px, logo 44 px |
| Nome da estrela no zoom | sempre visível (no toque não existe hover) |

**Folgas conferidas:** o texto recolhido vai de 119 a 181 px. A legenda ocupa de 516 a 810 px. No zoom, a estrela fica a 150 px do topo e a ficha começa em cerca de 358 px.

---

## 4. Texto recolhível no mobile (modelo 2)

O texto completo fica recolhido em **três linhas**, que vão sumindo no fim. A **seta** fica colada à direita da última linha visível.

```html
<div class="clw">
  <input type="checkbox" id="leadtg" class="tg2" aria-label="Mostrar o texto completo">
  <p class="tx2">…texto principal…</p>
  <label for="leadtg" class="cc2" aria-hidden="true">
    <span class="ar2"><svg viewBox="0 0 24 24" width="22" height="22"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
  </label>
</div>
```

```css
.clw{position:relative}
.tg2{position:absolute;opacity:0;width:1px;height:1px;pointer-events:none}
.tx2{display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:3;overflow:hidden;padding-right:34px;
     mask-image:linear-gradient(180deg,#000 45%,transparent)}
.tg2:checked~.tx2{display:block;mask-image:none}
.cc2{position:absolute;right:-8px;bottom:-10px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;color:var(--gold)}
.tg2:checked~.cc2{position:static;margin:-6px -8px -10px auto}
.ar2{display:inline-flex;transition:transform .35s ease}
.tg2:checked~.cc2 .ar2{transform:rotate(180deg)}
.tg2:focus-visible~.cc2{outline:2px solid var(--gold);outline-offset:-4px;border-radius:50%}
.clw:has(.tg2:checked){background:rgba(var(--veil),.94);
  box-shadow:0 0 0 14px rgba(var(--veil),.94),0 30px 40px 14px rgba(var(--veil),.75)}
@media (prefers-reduced-motion: reduce){.ar2{transition:none}}
```

- **Aberto:** o texto inteiro aparece sobre um véu escuro que cobre o alto do céu. A seta vai para o fim do texto e gira para cima.
- O céu e as pílulas **não se movem** quando o texto abre.
- **No app React,** prefira um `<button aria-expanded>` controlando um estado `open` em vez do checkbox; o visual é o mesmo.

---

## 5. Acessibilidade (os dois layouts)

- Todo alvo de toque no mobile tem 44 px ou mais: pílulas, seta, fechar e botões da ficha (WCAG 2.5.5 / 2.5.8).
- Estrelas, pílulas e seta são elementos nativos (`button` / `input` + `label`), com nome acessível e foco visível em dourado.
- A ficha usa `aria-live="polite"` e `aria-labelledby` no título.
- A clicabilidade é sinalizada só por forma, cor e movimento: borda de pílula, estrelinha que pisca, seta, hover e foco. Não há texto de instrução na tela.
- Com `prefers-reduced-motion: reduce`, param o cometa, o desenho das linhas, a estrelinha das pílulas e a rotação da seta.

---

## 6. Como regerar as pranchas

Os scripts em [`geradores/`](geradores/) produzem os arquivos do canvas:

| Arquivo | Papel |
|---|---|
| `refino.py` | Gera o desktop (`R01-W11Refino.dc.html`, copiado como `F01-Desktop.dc.html`). Contém o CSS, a marcação, a câmera e a lógica. |
| `mobmake.py` | Deriva o mobile do desktop (`F03-MobileInterativo.dc.html`) por substituições exatas de texto (lista `REPL`) e acrescenta o CSS do mobile (`MCSS`). |
| `texts.py` | Textos por voz ("Carta celeste" é a escolhida). |
| `ident.py` | Fontes e paletas. |
| `logos.py` | Logos dos projetos (data URIs). |

```bash
python -I refino.py <pasta do projeto do canvas> <saída> [imagem local]
python -I mobmake.py <pasta com a R01 gerada> <saída>
```

`refino.py` lê o campo de estrelas e o cometa de `W11-CeuAberto.dc.html`, na pasta do projeto do canvas. Ele também consulta o `gh` para descobrir o link de uso de cada projeto (o campo **Website** do repositório ou a última release).

Se o desktop mudar alguma medida que o mobile substitui, `mobmake.py` para com `AssertionError: não achei …`. Nesse caso, atualize a entrada correspondente em `REPL`.

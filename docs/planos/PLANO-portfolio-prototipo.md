# PLANO DE EXECUÇÃO — portfolio-prototipo

| Campo | Valor |
|---|---|
| **Tarefa** | `portfolio-prototipo` |
| **Origem** | descrição livre ("Não quero revisar os textos antes de ter um protótipo no ar.") |
| **Tipo** | História |
| **Modo de execução** | 🔁 Loop (sem confirmação) |
| **Data** | 2026-10-30 |
| **Branch** | `feature/portfolio-prototipo` |

## 1. Enunciado Canônico

- **Problema:** o portfólio só existe como plano; Yago não quer revisar textos sem ver o site.
- **Resultado esperado:** protótipo navegável PT (`/`) e EN (`/en/`), pré-renderizado, publicado no GitHub Pages, com textos rascunhados.
- **Como validar:** `npm run build` gera `dist/index.html` e `dist/en/index.html` com conteúdo; testes passam; após deploy, a URL do Pages abre as duas páginas.

## 2. Escopo

**Vou fazer:** scaffold Vite + React + TS; dicionário PT/EN tipado; seções hero, sobre, projetos, trajetória, formação, contato; CSS com tokens e animação em CSS puro; SSG próprio (decisão 011); testes Vitest + Playwright (E2E, axe, visual só no CI); workflow de deploy no Pages.

**NÃO vou fazer** [#8]: 4 protótipos de estilo (ticket 001 segue aberto); revisão dos textos (002/008); domínio próprio (009, depende de Yago); imagens dos projetos; analytics; OG image.

## 3. Premissas Assumidas

| # | Premissa | Por quê | Se estiver errada… |
|---|---|---|---|
| P1 | Textos rascunhados por Claude, tom irreverente, fatos só do currículo/GitHub | pedido do usuário [#98] | editar `src/i18n.ts` |
| P2 | Um estilo só: "editorial jurídico + terminal" (Fraunces + JetBrains Mono, fundo quase preto, acento verde-ácido) | mistura dois dos 4 estilos e traduz Tech + Direito; 4 protótipos atrasariam o "no ar" [#7] | trocar tokens em `src/styles.css`; ticket 001 continua aberto |
| P3 | `BASE_PATH=/curriculum-vitae/` no CI até o DNS (009) ficar pronto; `SITE_URL` configurável | `base: '/'` só funciona com domínio próprio | trocar 2 variáveis no workflow |
| P4 | Deploy a partir de `main`; PR aberto, merge do usuário publica | Regra 6 (não mergear) | rodar o workflow manualmente na branch |
| P5 | Sugestão de idioma do navegador fica de fora do 1º corte | YAGNI [#8]; botão PT/EN cobre | adicionar `useEffect` no `App` |

## 4. Decisão Visual

- **Superfície visual:** sim. **Mockup:** não; o próprio protótipo é o mockup (é o que Yago pediu).
- **Tokens:** cores e fontes em `:root` [#3]; só tema escuro; `prefers-reduced-motion` respeitado; contraste AA verificado pelo axe.

## 5. Terreno

Repo vazio (só LICENSE). Pages já ativo em modo workflow. Tudo é criação.

## 6. Passos Atômicos

| # | Arquivo alvo | O que muda | Prática | Como verificar |
|---|---|---|---|---|
| 1 | `package.json`, configs, `.gitignore` | scaffold | [#31] | `npm install` |
| 2 | `src/i18n.ts` | dicionário PT/EN tipado | [#3] | `tsc` |
| 3 | `src/App.tsx`, `src/styles.css` | seções e estilo | [#7][#13] | `npm run dev` |
| 4 | `src/main.tsx`, `src/entry-server.tsx`, `prerender.mjs` | SSG `/` e `/en/` | 011 | `npm run build` |
| 5 | `src/*.test.tsx`, `e2e/` | testes | [#41][#43] | `npm test`, `npx playwright test` |
| 6 | `.github/workflows/deploy.yml` | CI + deploy | [#84] | Actions verde |

## 7. Impacto em Dados e Contratos

Sem banco/API. Config: `BASE_PATH`, `SITE_URL` (env de build). LGPD: só e-mail público e cidade (decisão 002).

## 8. Plano de Testes

| Nível | O que cobre | Falha coberta |
|---|---|---|
| Unidade | `App` renderiza PT e EN; chaves iguais nos dicionários | chave faltando no EN |
| E2E | `/` e `/en/`: lang, title, hreflang, troca de idioma, axe WCAG AA, screenshot (CI) | link de idioma quebrado, contraste |

**Comando:** `npm test && npm run build && npx playwright test`

## 9. Riscos e Rollback

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Hidratação divergente | Média | aviso no console | idioma só pela URL |
| Base errada no Pages | Média | CSS/JS 404 | `BASE_PATH` no workflow + E2E com base |

**Rollback:** `git revert` do merge; Pages republica a versão anterior.

# ENTREGA — portfolio-prototipo (2026-10-30)

- **No ar:** https://yagoriccomi.github.io/curriculum-vitae/ (PT) e `/en/` (EN). `/en` responde 301 para `/en/`.
- **Commits:** 113c5e3..366b31a, enviados direto para `main` a pedido do usuário. Sem PR.
- **CI:** run 41137795194. Os jobs `test` e `deploy` terminaram com sucesso.
- **Verificação:** a primeira rodada reprovou (FAIL). Os problemas foram:
  - `/en/index.html` abria em PT;
  - WCAG 3.1.2 e 2.2.2;
  - na impressão, partes da página saíam invisíveis.

  O commit 366b31a corrigiu tudo, e a segunda rodada aprovou (PASS).

## Pendências
- Revisar os textos em `src/i18n.ts` (tickets 002 e 008).
- Identidade visual: os 4 protótipos (ticket 001). O estilo atual é uma premissa (P2).
- DNS (ticket 009). Depois dele, trocar `BASE_PATH` para `/` e `SITE_URL` para `https://www.yagoriccomi.com.br` em `deploy.yml`, e configurar o domínio no Pages.
- Baseline visual: trazer `e2e/__screenshots__/*-linux.png` do artefato `playwright` para o repo. Até lá, o teste visual não compara nada.
- Menu de navegação no celular (hoje ele fica escondido).

# PLANO DE EXECUÇÃO — layout-final

| Campo | Valor |
|---|---|
| Tarefa | layout-final |
| Origem | Descrição livre e layout aprovado |
| Tipo | Melhoria |
| Modo | Loop, sem confirmação |
| Data | 2026-11-06 |
| Branch | main; trabalho local sem commit/push |

## 1. Enunciado Canônico
- Problema: a interface atual ainda é o protótipo anterior.
- Resultado: implementar F01 desktop e F03 mobile com céu interativo e conteúdo bilíngue.
- Como validar: build, testes e navegador em 1280×800 e 390×844; estrelas, pílulas, fichas, fechar, navegação, texto recolhível e idioma funcionando.

## 2. Escopo
Implementar a especificação `docs/layout-final/LAYOUT-FINAL.md` disponível na worktree `claude/sagitario-renascentista-canvas-6a2b38`; consultar os cinco geradores vizinhos. Integrar textos aprovados dessa branch e justificação do corpo. Reaproveitar prerender e dados existentes [#6].
Fora: backend, Jira, deploy, novos temas, reformulação de identidade, commit, push e PR [#8].

## 3. Premissas Assumidas
| Premissa | Motivo | Correção |
|---|---|---|
| F01/F03 são os mockups finais | aprovação explícita na especificação [#98] | ajustar apenas mediante nova referência |
| Paleta escura fixa aprovada | não redesenhar o projeto [#8] | tema claro apenas se solicitado |
| Alterações locais compatíveis devem permanecer | arquivos já modificados antes desta execução [#84] | revisão do diff, sem restore/reset |
| Execução local; sem agendamento recorrente | Loop foi pedido como modo autônomo desta entrega | agendar somente com periodicidade definida |
| Nível alto para implementação e verificação | modo Loop | ajustar se necessário |

## 4. Decisão Visual
Superfície visual: sim. Mockup novo: não; F01/F03 já aprovados. Skill design-de-interface-projeto acionada. Tokens da especificação, botões nativos e foco visível; movimento reduzido. Sem chamadas de dados em runtime planejadas; assets devem ser locais quando disponíveis, com falha de imagem comunicada se necessário. Não adicionar estados assíncronos fictícios [#7].

## 5. Terreno
| Arquivo/módulo | Papel | Mudança |
|---|---|---|
| src/App.tsx, src/styles.css | interface atual | céu, câmera, fichas, responsividade |
| src/i18n.ts | conteúdo PT/EN | integrar conteúdo aprovado da branch |
| src/App.test.tsx, e2e/site.spec.ts | regressão | atualizar contratos visuais/interações |
| public/ | assets | gravura e fontes conforme fontes disponíveis |
| package.json, package-lock.json | dependências já alteradas | somente se fonte aprovada exigir |
| prerender.mjs, entry-server.tsx | páginas estáticas bilíngues | preservar SSR |
Convenções: React/TypeScript, CSS nativo, Vitest/Playwright [#5][#13].

## 6. Passos Atômicos
1. Conferir geradores, assets e testes para fechar os detalhes da referência [#98].
2. Implementar céu e fichas React com fontes e dados aprovados [#7].
3. Adaptar CSS desktop/mobile e acessibilidade sem bibliotecas novas desnecessárias [#8].
4. Atualizar testes dos fluxos críticos [#43][#47].
5. Verificação independente, correções e conferência dos comandos relatados [#34].

## Fatias
| Fatia | Nível | Dependência | Branch | Estado |
|---|---|---|---|---|
| Interface e conteúdo | alto | nenhuma; módulo único acoplado | worktree-agent-a5197eed; integrada localmente na main | revisada: pronta |
| Verificação independente | alto | implementação | leitura da worktree e cópia temporária | PASS; comandos repetidos na main |
Sem paralelizar edições no mesmo módulo. Referências estão em outra worktree; não alterar essa worktree.

## 7. Dados e Contratos
Sem banco, migration, API, segredo ou variável nova. Contatos públicos existentes preservados; sem novos dados pessoais.

## 8. Testes
Unidade/integração: abrir/fechar ficha, anterior/próxima, expansão do texto, idioma. E2E: desktop/mobile, teclado, movimento reduzido, ausência de overflow, acessibilidade. Comandos: `npm test`, `npm run build`, `npm run e2e`.

## 9. Riscos e Rollback
Assets do canvas podem não existir localmente: investigar fontes sem inventar URLs. Câmera/SSR: evitar uso de window durante render no servidor. Telas pequenas: permitir acesso ao conteúdo sem cortar controles. Rollback: desfazer apenas os hunks desta tarefa após revisão; nunca descartar alterações anteriores [#84].

## 10. Definição de Pronto
- [x] Layout e fluxos implementados; comparação pixel a pixel não realizada
- [x] Build, testes e navegador conferidos
- [x] Verificação independente concluída
- [x] Relatório de entrega local escrito
Commit/PR/Jira não aplicáveis nesta execução; ferramentas de consulta de uso não disponíveis.

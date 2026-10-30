import { readFileSync, writeFileSync, mkdirSync, rmSync } from 'node:fs'
import { render } from './dist-ssr/entry-server.js'

// ponytail: SITE_URL aponta para o Pages até o domínio próprio (ticket 009).
const site = (process.env.SITE_URL ?? 'https://www.yagoriccomi.com.br').replace(/\/$/, '')
const url = { pt: `${site}/`, en: `${site}/en/` }
const esc = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;')
const template = readFileSync('dist/index.html', 'utf8')

for (const lang of ['pt', 'en']) {
  const { html, t } = render(lang)
  const head = [
    `<title>${esc(t.title)}</title>`,
    `<meta name="description" content="${esc(t.description)}" />`,
    `<link rel="canonical" href="${url[lang]}" />`,
    `<link rel="alternate" hreflang="pt-BR" href="${url.pt}" />`,
    `<link rel="alternate" hreflang="en" href="${url.en}" />`,
    `<link rel="alternate" hreflang="x-default" href="${url.pt}" />`,
    `<meta property="og:type" content="website" />`,
    `<meta property="og:title" content="${esc(t.title)}" />`,
    `<meta property="og:description" content="${esc(t.description)}" />`,
    `<meta property="og:url" content="${url[lang]}" />`,
    `<meta property="og:locale" content="${lang === 'pt' ? 'pt_BR' : 'en_US'}" />`,
  ].join('\n    ')
  const out = template
    .replace('<!--lang-->', t.htmlLang)
    .replace('<!--head-->', head)
    .replace('<!--app-->', html)
  const dir = lang === 'pt' ? 'dist' : 'dist/en'
  mkdirSync(dir, { recursive: true })
  writeFileSync(`${dir}/index.html`, out)
}
rmSync('dist-ssr', { recursive: true })
console.log(JSON.stringify({ event: 'prerender', site, pages: Object.values(url) }))

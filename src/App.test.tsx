import { afterEach, describe, expect, it, vi } from 'vitest'
vi.stubGlobal('ResizeObserver', class { observe() {} disconnect() {} })
import { cleanup, fireEvent, render, screen } from '@testing-library/react'
import { App } from './App'
import { dict, langFromPath } from './i18n'
afterEach(cleanup)
const shape = (o: unknown): unknown => Array.isArray(o) ? o.map(shape) : o && typeof o === 'object' ? Object.fromEntries(Object.entries(o).map(([k, v]) => [k, shape(v)])) : typeof o

describe('i18n', () => {
  it('preserva estrutura bilíngue e rotas', () => {
    expect(shape(dict.en)).toEqual(shape(dict.pt))
    for (const p of ['/en', '/en/', '/en/index.html', '/curriculum-vitae/en/']) expect(langFromPath(p)).toBe('en')
    for (const p of ['/', '/index.html', '/curriculum-vitae/']) expect(langFromPath(p)).toBe('pt')
  })
})
describe('atlas', () => {
  it.each(['pt', 'en'] as const)('renderiza céu e idioma %s', lang => {
    render(<App lang={lang} />)
    expect(screen.getByRole('heading', { level: 1 }).textContent).toBe('YAGO RICCOMI')
    expect(screen.getByRole('link', { name: `${dict[lang].switchShort}: ${dict[lang].switchLabel}` }).getAttribute('href')).toBe(lang === 'pt' ? '/en/' : '/')
    expect(document.querySelectorAll('[data-star]')).toHaveLength(10)
    expect(document.querySelectorAll('.constellation line')).toHaveLength(13)
    expect(document.querySelector('.comet')?.getAttribute('aria-hidden')).toBe('true')
    expect(dict[lang].hero.lead).not.toContain('Rio Claro')
  })
  it('abre por pílula, navega, fecha por teclado e restaura foco', () => {
    render(<App lang="pt" />)
    const button = screen.getByRole('button', { name: /^Alexa no Windows$/ })
    button.focus(); fireEvent.click(button)
    expect(screen.getByRole('heading', { name: 'Alexa no Windows' })).toBe(document.activeElement)
    expect(screen.getByRole('link', { name: 'Repositório ↗' }).getAttribute('href')).toContain('comandos-em-meu-computador')
    fireEvent.click(screen.getByRole('button', { name: 'Próxima: Vencord Auto-Repair' }))
    expect(screen.getByRole('heading', { name: 'Vencord Auto-Repair' })).toBeTruthy()
    expect(document.querySelector('.logo text')?.textContent).toBe('VA')
    fireEvent.keyDown(document.activeElement!, { key: 'ArrowLeft' })
    expect(screen.getByRole('heading', { name: 'Alexa no Windows' })).toBeTruthy()
    fireEvent.keyDown(document.activeElement!, { key: 'Escape' })
    expect(document.querySelector('.panel')).toBeNull()
    expect(document.activeElement).toBe(button)
  })
  it('abre seções, expande texto e comunica erro da imagem', () => {
    render(<App lang="pt" />)
    const toggle = screen.getByRole('button', { name: 'Mostrar o texto completo' })
    fireEvent.click(toggle); expect(toggle.getAttribute('aria-expanded')).toBe('true')
    fireEvent.click(toggle); expect(toggle.getAttribute('aria-expanded')).toBe('false')
    fireEvent.click(screen.getByRole('button', { name: 'Abrir Formação' }))
    expect(screen.getByRole('heading', { name: dict.pt.education.heading })).toBeTruthy()
    expect(screen.getByText(dict.pt.education.degrees[0])).toBeTruthy()
    fireEvent.click(screen.getByRole('button', { name: 'Fechar e voltar ao céu' }))
    fireEvent.click(screen.getByRole('button', { name: 'Abrir Contato' }))
    expect(screen.getByRole('link', { name: 'yago.riccomi.s@gmail.com' }).getAttribute('href')).toBe('mailto:yago.riccomi.s@gmail.com')
    fireEvent.error(document.querySelector('.engraving')!)
    expect(screen.getByRole('status').textContent).toContain('Gravura indisponível')
  })
})

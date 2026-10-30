import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import { App } from './App'
import { dict, langFromPath } from './i18n'

const shape = (o: unknown): unknown =>
  Array.isArray(o) ? o.map(shape) : o && typeof o === 'object'
    ? Object.fromEntries(Object.entries(o).map(([k, v]) => [k, shape(v)])) : typeof o

describe('i18n', () => {
  it('EN tem a mesma estrutura do PT (nada faltando)', () => {
    expect(shape(dict.en)).toEqual(shape(dict.pt))
  })
  it('idioma vem só da URL', () => {
    expect(langFromPath('/')).toBe('pt')
    expect(langFromPath('/en/')).toBe('en')
    expect(langFromPath('/curriculum-vitae/en/')).toBe('en')
    expect(langFromPath('/curriculum-vitae/')).toBe('pt')
  })
})

describe('App', () => {
  it.each(['pt', 'en'] as const)('renderiza %s com link para o outro idioma', (lang) => {
    const { unmount } = render(<App lang={lang} />)
    expect(screen.getByRole('heading', { level: 1 }).textContent).toContain(dict[lang].hero.title[0])
    expect(screen.getByRole('link', { name: `${dict[lang].switchShort}: ${dict[lang].switchLabel}` }).getAttribute('href')).toBe(lang === 'pt' ? '/en/' : '/')
    expect(screen.getAllByRole('heading', { level: 3 }).length).toBeGreaterThanOrEqual(4)
    unmount()
  })
})

import { test, expect } from '@playwright/test'
import AxeBuilder from '@axe-core/playwright'

const pages = [
  { path: './', lang: 'pt-BR', h1: 'Código', other: 'EN' },
  { path: './en/', lang: 'en', h1: 'Code', other: 'PT' },
]

for (const p of pages) {
  test.describe(p.path, () => {
    test('HTML já vem pré-renderizado com metas', async ({ request }) => {
      const html = await (await request.get(p.path)).text()
      expect(html).toContain(`<html lang="${p.lang}">`)
      expect(html).toContain(`>${p.h1}</span>`)
      expect(html).toMatch(/hreflang="pt-BR"[\s\S]*hreflang="en"[\s\S]*hreflang="x-default"/)
      expect(html).toContain('rel="canonical"')
    })

    test('hidrata sem erro e troca de idioma', async ({ page }) => {
      const errors: string[] = []
      page.on('console', (m) => m.type() === 'error' && errors.push(m.text()))
      page.on('pageerror', (e) => errors.push(e.message))
      await page.goto(p.path)
      await expect(page.getByRole('heading', { level: 1 })).toContainText(p.h1)
      await page.getByRole('link', { name: new RegExp(`^${p.other}:`) }).click()
      await expect(page.locator('html')).not.toHaveAttribute('lang', p.lang)
      expect(errors).toEqual([])
    })

    test('sem violações WCAG 2.1 AA', async ({ page }) => {
      await page.goto(p.path)
      const { violations } = await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
        .analyze()
      expect(violations.map((v) => `${v.id}: ${v.nodes.length}`)).toEqual([])
    })

    test('visual', async ({ page }) => {
      test.skip(process.platform !== 'linux', 'baseline só no CI Linux')
      await page.goto(p.path)
      await page.evaluate(() => document.fonts.ready)
      await expect(page).toHaveScreenshot(`${p.lang}.png`, { fullPage: true })
    })
  })
}

import { test, expect } from '@playwright/test'
import AxeBuilder from '@axe-core/playwright'

for (const p of [{ path: './', lang: 'pt-BR', other: 'EN' }, { path: './en/', lang: 'en', other: 'PT' }]) {
  test.describe(p.path, () => {
    test('HTML pré-renderizado e hidratação bilíngue', async ({ page, request }) => {
      const html = await (await request.get(p.path)).text()
      expect(html).toContain(`<html lang="${p.lang}">`)
      expect(html).toContain('RICCOMI')
      expect(html).toContain('data-star="d"')
      expect(html).toMatch(/hreflang="pt-BR"[\s\S]*hreflang="en"[\s\S]*hreflang="x-default"/)
      expect(html).toContain('rel="canonical"')
      const errors: string[] = []
      page.on('pageerror', e => errors.push(e.message))
      page.on('console', m => { if (m.type() === 'error') errors.push(m.text()) })
      await page.goto(p.path)
      await expect(page.getByRole('heading', { level: 1 })).toHaveText('YAGO RICCOMI')
      await page.getByRole('link', { name: new RegExp(`^${p.other}:`) }).click()
      await expect(page.locator('html')).not.toHaveAttribute('lang', p.lang)
      expect(errors).toEqual([])
    })
    for (const viewport of [{ width: 1280, height: 800 }, { width: 390, height: 844 }]) {
      test(`céu, fichas, teclado e acessibilidade ${viewport.width}`, async ({ page }) => {
        await page.setViewportSize(viewport)
        await page.goto(p.path)
        await page.evaluate(() => document.fonts.ready)
        expect(await page.locator('.engraving').evaluate((i: HTMLImageElement) => i.complete && i.naturalWidth > 0)).toBe(true)
        expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true)
        if (viewport.width === 390) {
          const toggle = page.locator('.lead-toggle')
          const before = await page.locator('.legend').boundingBox()
          await toggle.click(); await expect(toggle).toHaveAttribute('aria-expanded', 'true')
          expect((await page.locator('.legend').boundingBox())!.y).toBeGreaterThanOrEqual(before!.y)
          await toggle.click(); await expect(toggle).toHaveAttribute('aria-expanded', 'false')
          await expect.poll(() => page.evaluate(() => document.documentElement.scrollHeight <= innerHeight)).toBe(true)
        }
        const pill = page.locator('.lgi').filter({ hasText: 'Fodinha' })
        await pill.click()
        await expect(page.locator('#panel-title')).toHaveText('Fodinha - cardgame')
        await expect(page.locator('#panel-title')).toBeFocused()
        await expect(page.getByRole('link', { name: /^(Abrir o app|Open app)/ })).toHaveAttribute('href', 'https://game.yagoriccomi.com.br')
        await page.keyboard.press('ArrowRight')
        await expect(page.locator('#panel-title')).toHaveText('Snake Thai')
        await page.keyboard.press('ArrowLeft')
        await expect(page.locator('#panel-title')).toHaveText('Fodinha - cardgame')
        const panelScan = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa']).analyze()
        expect(panelScan.violations.map(v => v.id)).toEqual([])
        await page.keyboard.press('Escape')
        await expect(page.locator('.panel')).toHaveCount(0)
        await expect(pill).toBeFocused()
        const { violations } = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa']).analyze()
        expect(violations.map(v => v.id)).toEqual([])
        expect(await page.locator('.scene').evaluate(e => getComputedStyle(e).transitionDuration)).toBe('0s')
      })
    }
  })
}

for (const route of ['./', './en/']) for (const width of [320, 390]) {
  test(`toques reais e expansão estável ${route} ${width}`, async ({ page }) => {
    await page.setViewportSize({ width, height: width === 320 ? 568 : 844 })
    await page.goto(route)
    await page.evaluate(() => document.fonts.ready)
    const boxes = async () => Promise.all(['.sky-frame', '.legend'].map(s => page.locator(s).boundingBox()))
    const before = await boxes()
    await page.locator('.lead-toggle').click()
    expect(await boxes()).toEqual(before)
    await page.locator('.lead-toggle').click()
    expect(await boxes()).toEqual(before)
    for (const star of await page.locator('.pstar').all()) {
      await star.scrollIntoViewIfNeeded()
      const id = await star.getAttribute('data-star')
      const label = (await star.getAttribute('aria-label'))!.replace(/^(Abrir|Open) /, '')
      const r = (await star.boundingBox())!
      for (const [dx, dy] of [[0,0],[-18,0],[18,0],[0,-18],[0,18]]) {
        expect(await page.evaluate(({ x, y }) => document.elementFromPoint(x, y)?.closest('.pstar')?.getAttribute('data-star'), { x: r.x + r.width / 2 + dx, y: r.y + r.height / 2 + dy })).toBe(id)
      }
      await page.mouse.click(r.x + r.width / 2, r.y + r.height / 2)
      await expect(page.locator('#panel-title')).toHaveText(id === 'l' ? /Quem traça este mapa|Who draws this map/ : id === 'f' ? /A rota até aqui|The road so far/ : id === 't' ? /Onde aprendi|Where I learned/ : id === 'g' ? /Para onde a flecha aponta|Where the arrow points/ : label)
      await page.locator('.close').click()
    }
  })
}

const sizes = [[320,568],[360,800],[390,844],[430,932],[768,1024],[1024,768],[1366,768],[1920,1080],[2560,1440],[844,390]]
for (const route of ['./', './en/']) for (const [width, height] of sizes) {
  test(`geometria ${route} ${width}x${height}`, async ({ page }, info) => {
    await page.setViewportSize({ width, height })
    await page.goto(route)
    await page.evaluate(() => document.fonts.ready)
    const geometry = async () => page.evaluate(() => {
      const rect = (selector: string) => document.querySelector(selector)!.getBoundingClientRect()
      const hero = rect('.hero'), legend = rect('.legend'), sky = rect('.sky-frame')
      const intersects = (a: DOMRect, b: DOMRect) => a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top
      const stars = [...document.querySelectorAll<HTMLElement>('.pstar')].map(e => {
        const r = e.getBoundingClientRect()
        const hit = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2)
        return { fits: r.left >= sky.left - 1 && r.right <= sky.right + 1 && r.top >= sky.top - 1 && r.bottom <= sky.bottom + 1,
          clear: !intersects(r, hero) && !intersects(r, legend), size: Math.min(r.width, r.height), reachable: r.top >= innerHeight || !!hit?.closest('.pstar') }
      })
      return { overlap: intersects(hero, legend), stars, overflow: document.documentElement.scrollWidth > innerWidth }
    })
    await expect.poll(async () => (await geometry()).stars.every(s => s.fits)).toBe(true)
    const result = await geometry()
    expect(result.overlap).toBe(false)
    expect(result.overflow).toBe(false)
    expect(result.stars.every(s => s.clear && s.size >= 43.9 && s.reachable)).toBe(true)
    if (width <= 1000) {
      for (const control of await page.locator('.lgi, .lang, .lead-toggle').all()) {
        const r = (await control.boundingBox())!
        expect(Math.min(r.width, r.height)).toBeGreaterThanOrEqual(44)
      }
      await page.locator('.lead-toggle').click()
      await expect.poll(async () => (await geometry()).stars.every(s => s.clear && s.fits)).toBe(true)
      await page.locator('.lead-toggle').click()
    }
    if ([390,1366,2560,844].includes(width)) await page.screenshot({ path: info.outputPath('overview.png'), fullPage: true })
    await page.locator('[data-star="e"]').scrollIntoViewIfNeeded()
    await page.locator('[data-star="e"]').click()
    await expect(page.locator('.panel')).toBeVisible()
    await page.setViewportSize({ width: height, height: width })
    await expect.poll(async () => page.locator('.panel').evaluate(e => {
      const r = e.getBoundingClientRect()
      return r.left >= 0 && r.right <= innerWidth && r.top >= 0 && r.bottom <= innerHeight
    })).toBe(true)
    await expect(page.locator('.close')).toBeInViewport()
    await page.locator('.close').click()
    await expect(page.locator('.panel')).toHaveCount(0)
  })
}

test('câmera usa durações aprovadas sem movimento reduzido', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'no-preference' })
  await page.setViewportSize({ width: 1280, height: 800 })
  await page.goto('./')
  await page.locator('.lgi').filter({ hasText: 'Fodinha' }).click()
  expect(await page.locator('.scene').evaluate(e => getComputedStyle(e).transitionDuration)).toBe('1.8s')
  await page.keyboard.press('ArrowRight')
  expect(await page.locator('.scene').evaluate(e => getComputedStyle(e).transitionDuration)).toBe('1.6s')
})

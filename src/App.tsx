import { useEffect, useRef, useState, type CSSProperties } from 'react'
import { dict, links, type Lang } from './i18n'

const BASE = import.meta.env.BASE_URL
const baseStars = [
  { id: 'd', x: 543, y: 430, greek: 'δ', star: 'Kaus Media', project: 4 },
  { id: 'm', x: 609, y: 116, greek: 'ν', star: 'Ain al Rami', project: 5 },
  { id: 'e', x: 559, y: 529, greek: 'ε', star: 'Kaus Australis', project: 0 },
  { id: 's', x: 856, y: 351, greek: 'σ', star: 'Nunki', project: 1 },
  { id: 'p', x: 859, y: 212, greek: 'μ', star: 'Polis', project: 2 },
  { id: 'z', x: 794, y: 686, greek: 'ζ', star: 'Ascella', project: 3 },
  { id: 'l', x: 518, y: 259, greek: 'λ', star: 'Kaus Borealis', section: 'about' },
  { id: 'f', x: 761, y: 407, greek: 'φ', star: 'Sagittarius', section: 'path' },
  { id: 't', x: 992, y: 417, greek: 'τ', star: 'Sagittarius', section: 'education' },
  { id: 'g', x: 481, y: 442, greek: 'γ', star: 'Alnasl', section: 'contact' },
] as const
const points = [...baseStars, { id: 'h', x: 778, y: 766 }]
const edges = ['gd', 'dl', 'lf', 'fs', 'st', 'tz', 'ze', 'ed', 'fz', 'ge', 'sp', 'lm', 'eh']
const apps: Record<string, string> = { e: 'https://game.yagoriccomi.com.br', p: 'https://stream.yagoriccomi.com.br' }
const polygon = '32,9 33.53,28.3 41.9,22.1 35.7,30.47 55,32 35.7,33.53 41.9,41.9 33.53,35.7 32,55 30.47,35.7 22.1,41.9 28.3,33.53 9,32 28.3,30.47 22.1,22.1 30.47,28.3'

export function App({ lang }: { lang: Lang }) {
  const t = dict[lang]
  const pt = lang === 'pt'
  const [selected, setSelected] = useState<string | null>(null)
  const [highlight, setHighlight] = useState<string | null>(null)
  const [expanded, setExpanded] = useState(false)
  const [imageFailed, setImageFailed] = useState(false)
  const [duration, setDuration] = useState(1.8)
  const opener = useRef<HTMLElement | null>(null)
  const title = useRef<HTMLHeadingElement>(null)
  const panel = useRef<HTMLElement>(null)
  const sky = useRef<HTMLDivElement>(null)
  const [frame, setFrame] = useState({ width: 896, height: 800, left: 384, top: 0, mobile: false })
  useEffect(() => {
    const element = sky.current!
    const measure = () => {
      setFrame({ width: element.clientWidth, height: element.clientHeight, left: element.offsetLeft, top: element.offsetTop, mobile: window.innerWidth <= 1000 })
    }
    measure()
    const observer = new ResizeObserver(measure)
    observer.observe(element)
    observer.observe(element.parentElement!.querySelector('.hero')!)
    return () => observer.disconnect()
  }, [])
  // Desktop overview camera from the approved canvas (F01, 1280×800: scale 1.07 at -44,-52), used only while
  // every star's hit target stays inside the sky frame. Mobile keeps the fitted camera: F03's scale (.42)
  // would make neighbouring 44px touch targets overlap.
  const vw = frame.left + frame.width + 24, vh = frame.top + frame.height + 72
  const k = Math.min(vw / 1280, vh / 800), cs = 1.07 * k, ctx = vw - 1324 * k, cty = (vh - 800 * k) / 2 - 52 * k
  const half = Math.max(32 * cs, 22) + 1
  const canvasFits = !frame.mobile && vw >= 1200 && baseStars.every(s => s.x * cs + ctx - half >= frame.left && s.x * cs + ctx + half <= frame.left + frame.width && s.y * cs + cty - half >= frame.top && s.y * cs + cty + half <= frame.top + frame.height)
  const stars = baseStars.map(s => frame.mobile ? { ...s, ...(s.id === 'g' ? { x: 401 } : s.id === 'e' ? { y: 570 } : s.id === 'f' ? { x: 730, y: 440 } : {}) } : s)
  const mapPoints = [...stars, points[points.length - 1]]
  const sel = stars.find(s => s.id === selected)
  const name = (s: typeof stars[number]) => 'project' in s ? t.projects.items[s.project].name : t.nav[s.section]
  const open = (id: string) => {
    if (!selected) opener.current = document.activeElement as HTMLElement
    setDuration(selected ? 1.6 : 1.8)
    setSelected(id)
  }
  const close = () => { setSelected(null) }
  const group = stars.filter(s => ('project' in s) === !!(sel && 'project' in sel))
  const index = group.findIndex(s => s.id === selected)
  const previous = group[(index - 1 + group.length) % group.length]
  const next = group[(index + 1) % group.length]
  useEffect(() => {
    if (selected) { title.current?.focus({ preventScroll: true }); panel.current?.scrollTo?.(0, 0) }
    else opener.current?.focus({ preventScroll: true })
  }, [selected])
  // Fit the map bounds, leaving room for unscaled 44px hit targets at every edge.
  const fit = Math.min((frame.width - 48) / (frame.mobile ? 591 : 511), (frame.height - 48) / 650, frame.width / (frame.mobile ? 655 : 575), frame.height / 714)
  const scale = sel ? (frame.mobile ? 1 : 2.2) : canvasFits ? cs : fit
  const sx = sel ? (frame.mobile ? frame.left + frame.width / 2 : frame.left + frame.width * .08) : frame.left + frame.width / 2
  const sy = sel ? (frame.mobile ? 150 : frame.top + frame.height / 2) : frame.top + frame.height / 2
  const tx = !sel && canvasFits ? ctx : sx - scale * (sel ? sel.x : frame.mobile ? 696.5 : 736.5)
  const ty = !sel && canvasFits ? cty : sy - scale * (sel ? sel.y : 441)
  const style = {
    '--tx': `${tx}px`, '--ty': `${ty}px`, '--scale': scale,
    '--hit-scale': Math.max(1, 44 / (64 * scale)),
    '--sx': `${sx}px`, '--sy': `${sy}px`, '--duration': `${duration}s`,
    '--fl': `${frame.left}px`, '--frt': `${frame.top}px`, '--fh': `${frame.height}px`,
  } as CSSProperties
  const project = sel && 'project' in sel ? t.projects.items[sel.project] : null

  return <>
    <a className="skip" href="#main">{pt ? 'Pular para o conteúdo' : 'Skip to content'}</a>
    <main id="main" tabIndex={-1} className={`atlas${sel ? ' is-zoom' : ''}`} style={style} onKeyDown={e => {
      if (!sel) return
      if (e.key === 'Escape') { e.preventDefault(); close() }
      if (e.key === 'ArrowLeft') { e.preventDefault(); open(previous.id) }
      if (e.key === 'ArrowRight') { e.preventDefault(); open(next.id) }
    }}>
      <div className="starfield" aria-hidden="true">{Array.from({ length: 90 }, (_, i) => <i key={i} style={{ left: `${(i * 37.13) % 100}%`, top: `${(i * 61.7) % 100}%`, animationDelay: `${i % 5}s` }} />)}</div>
      <div className="sky-frame" ref={sky} aria-hidden="true" />
      <div className="sky-clip"><div className="scene">
        <img className="engraving" src={`${BASE}sky/hevelius-sagittarius.png`} width="1014" height="845" alt="" aria-hidden="true" onError={() => setImageFailed(true)} />
        <svg className="constellation" width="1280" height="800" aria-hidden="true">{edges.map(edge => {
          const a = mapPoints.find(p => p.id === edge[0])!, b = mapPoints.find(p => p.id === edge[1])!
          return <line key={edge} x1={a.x} y1={a.y} x2={b.x} y2={b.y} pathLength="1" />
        })}</svg>
        <span className="tiny" style={{ left: 778, top: 766 }} aria-hidden="true" />
        <div role="group" aria-label={pt ? 'Estrelas do mapa' : 'Map stars'}>{stars.map(s => <button key={s.id} type="button" data-star={s.id}
          className={`pstar${'section' in s ? ' sec' : ''}${selected === s.id ? ' on' : ''}${highlight === s.id ? ' hl' : ''}`}
          style={{ left: s.x, top: s.y }} aria-label={`${pt ? 'Abrir' : 'Open'} ${name(s)}`} aria-controls="star-panel" aria-expanded={selected === s.id} onClick={() => open(s.id)}>
          <svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="23" /><polygon points={polygon} /></svg><span className="star-name">{s.greek} {s.star}</span>
        </button>)}</div>
      </div></div>
      <div className="comet" aria-hidden="true" />
      <div className="zoom-veil" aria-hidden="true" />
      <div className="divider overview" aria-hidden="true" />
      <header className="top"><span className="overview brand">URANOGRAPHIA</span><a className="lang glass" href={pt ? `${BASE}en/` : BASE} hrefLang={pt ? 'en' : 'pt-BR'} lang={pt ? 'en' : 'pt-BR'} aria-label={`${t.switchShort}: ${t.switchLabel}`}>{t.switchShort}</a></header>
      <div className="hero overview" inert={!!sel}>
        <h1>YAGO <span>RICCOMI</span></h1><div className="ornament" aria-hidden="true">◇</div>
        <div className={`lead-wrap${expanded ? ' expanded' : ''}`}><p id="hero-lead" className="lead">{t.hero.lead}</p><button type="button" className="lead-toggle" aria-controls="hero-lead" aria-expanded={expanded} aria-label={pt ? (expanded ? 'Recolher texto' : 'Mostrar o texto completo') : (expanded ? 'Collapse text' : 'Show full text')} onClick={() => setExpanded(!expanded)}><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" strokeWidth="2" /></svg></button></div>
      </div>
      <nav className="legend overview" inert={!!sel} aria-label={pt ? 'Legenda' : 'Legend'}>{[true, false].map(projects => <div className={projects ? 'lgc' : 'lgc sections'} key={String(projects)}><h2>{projects ? t.nav.projects : pt ? 'O caminho' : 'The journey'}</h2><ul>{stars.filter(s => ('project' in s) === projects).sort((a, b) => name(a).localeCompare(name(b), lang)).map(s => <li key={s.id}><button type="button" className="lgi" onMouseEnter={() => setHighlight(s.id)} onMouseLeave={() => setHighlight(null)} onFocus={() => setHighlight(s.id)} onBlur={() => setHighlight(null)} onClick={() => open(s.id)} aria-controls="star-panel" aria-expanded={selected === s.id}>{name(s)}</button></li>)}</ul></div>)}</nav>
      <a className="credit overview" inert={!!sel} href="https://polona.pl/preview/5ac16003-101f-4ff1-96ad-3bd3709cc48c" target="_blank" rel="noopener noreferrer"><span className="credit-long">{pt ? 'Gravura' : 'Engraving'}: Johannes Hevelius, Uranographia (1690) ↗</span><span className="credit-short">{pt ? 'Gravura' : 'Engraving'}: Hevelius, 1690 ↗</span></a>
      {imageFailed && <p role="status" className="asset-error">{pt ? 'Gravura indisponível. Consulte a obra original nos créditos.' : 'Engraving unavailable. See the original in the credits.'}</p>}
      <div aria-live="polite">{sel && <section id="star-panel" ref={panel} className="panel glass" aria-labelledby="panel-title">
        <button type="button" className="close" onClick={close} aria-label={pt ? 'Fechar e voltar ao céu' : 'Close and return to the sky'}>×</button>
        {project && (sel.id === 'm' || sel.id === 'z' ? <svg className="logo monogram" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="29" /><text x="32" y="41" textAnchor="middle">{sel.id === 'm' ? 'VA' : 'MC'}</text></svg> : <img className="logo" src={`${BASE}sky/logo-${sel.id}.webp`} width="64" height="64" alt="" />)}
        <p className="kick">{pt ? 'Estrela' : 'Star'} {sel.greek} · {sel.star}</p>
        <h2 id="panel-title" ref={title} tabIndex={-1}>{project ? project.name : 'section' in sel ? t[sel.section].heading : ''}</h2><div className="ornament" aria-hidden="true">◇</div>
        {project && <><p className="prose">{project.text}</p><ul className="chips" aria-label={t.projects.stackLabel}>{project.stack.map(s => <li key={s}>{s}</li>)}</ul><div className="actions">{apps[sel.id] && <a className="btn primary" href={apps[sel.id]} target="_blank" rel="noopener noreferrer">{pt ? 'Abrir o app' : 'Open app'} ↗</a>}<a className="btn" href={`${links.github}/${project.repo}`} target="_blank" rel="noopener noreferrer">{t.projects.repoLabel} ↗</a></div></>}
        {sel.id === 'l' && t.about.body.map(p => <p className="prose" key={p}>{p}</p>)}
        {sel.id === 'f' && <ol className="timeline">{t.path.items.map(e => <li key={e.when}><span className="when">{e.when}</span><strong>{e.what}</strong><span className="where">{e.where}</span></li>)}</ol>}
        {sel.id === 't' && <><ul className="degrees">{t.education.degrees.map(d => <li key={d}>{d}</li>)}</ul><h3>{t.education.coursesHeading}</h3><ul className="chips">{t.education.courses.map(c => <li key={c}>{c}</li>)}</ul></>}
        {sel.id === 'g' && <><p className="prose">{t.contact.lead}</p><ul className="contact"><li><a className="btn primary" href={`mailto:${links.email}`}>{links.email}</a></li><li><a className="btn" href={links.github}>GitHub ↗</a></li><li><a className="btn" href={links.linkedin}>LinkedIn ↗</a></li></ul><p className="city">{t.contact.city}</p></>}
        <nav className="panel-nav" aria-label={pt ? 'Navegação da ficha' : 'Card navigation'}><button type="button" aria-label={`${pt ? 'Anterior' : 'Previous'}: ${name(previous)}`} onClick={() => open(previous.id)}>← {name(previous)}</button><button type="button" aria-label={`${pt ? 'Próxima' : 'Next'}: ${name(next)}`} onClick={() => open(next.id)}>{name(next)} →</button></nav>
      </section>}</div>
    </main>
  </>
}

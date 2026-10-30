import { dict, links, type Lang } from './i18n'

const BASE = import.meta.env.BASE_URL

export function App({ lang }: { lang: Lang }) {
  const t = dict[lang]
  const other = lang === 'pt' ? `${BASE}en/` : BASE

  return (
    <>
      <a className="skip" href="#main">{lang === 'pt' ? 'Pular para o conteúdo' : 'Skip to content'}</a>
      <header className="top">
        <a className="mark" href={lang === 'pt' ? BASE : `${BASE}en/`}>YRS<span>§</span></a>
        <nav aria-label={lang === 'pt' ? 'Seções' : 'Sections'}>
          <a href="#sobre">{t.nav.about}</a>
          <a href="#projetos">{t.nav.projects}</a>
          <a href="#trajetoria">{t.nav.path}</a>
          <a href="#formacao">{t.nav.education}</a>
          <a href="#contato">{t.nav.contact}</a>
        </nav>
        <a className="lang" href={other} hrefLang={lang === 'pt' ? 'en' : 'pt-BR'} lang={lang === 'pt' ? 'en' : 'pt-BR'} aria-label={`${t.switchShort}: ${t.switchLabel}`}>
          {t.switchShort}
        </a>
      </header>

      <main id="main">
        <section className="hero" aria-labelledby="hero-title">
          <p className="kicker">{t.hero.kicker}</p>
          <h1 id="hero-title">
            <span className="w1">{t.hero.title[0]}</span>
            <span className="plus" aria-hidden="true">{t.hero.title[1]}</span>
            <span className="visually-hidden"> {lang === 'pt' ? 'e' : 'and'} </span>
            <span className="w2">{t.hero.title[2]}</span>
          </h1>
          <p className="lead">{t.hero.lead}<span className="caret" aria-hidden="true" /></p>
          <a className="cta" href="#projetos">{t.hero.cta} →</a>
        </section>

        <section id="sobre" aria-labelledby="h-sobre">
          <h2 id="h-sobre"><span aria-hidden="true">01</span>{t.about.heading}</h2>
          {t.about.body.map((p) => <p key={p} className="prose">{p}</p>)}
        </section>

        <section id="projetos" aria-labelledby="h-projetos">
          <h2 id="h-projetos"><span aria-hidden="true">02</span>{t.projects.heading}</h2>
          <ul className="cards">
            {t.projects.items.map((p, i) => (
              <li key={p.repo} className="card">
                <p className="card-n" aria-hidden="true">Art. {i + 1}º</p>
                <h3>{p.name}</h3>
                <p>{p.text}</p>
                <p className="visually-hidden">{t.projects.stackLabel}:</p>
                <ul className="stack">{p.stack.map((s) => <li key={s}>{s}</li>)}</ul>
                <a href={`${links.github}/${p.repo}`} rel="noopener">
                  {t.projects.repoLabel}: {p.repo} ↗
                </a>
              </li>
            ))}
          </ul>
        </section>

        <section id="trajetoria" aria-labelledby="h-traj">
          <h2 id="h-traj"><span aria-hidden="true">03</span>{t.path.heading}</h2>
          <ol className="timeline">
            {t.path.items.map((e) => (
              <li key={e.when}>
                <span className="when">{e.when}</span>
                <strong>{e.what}</strong>
                <span className="where">{e.where}</span>
              </li>
            ))}
          </ol>
        </section>

        <section id="formacao" aria-labelledby="h-form">
          <h2 id="h-form"><span aria-hidden="true">04</span>{t.education.heading}</h2>
          <ul className="degrees">{t.education.degrees.map((d) => <li key={d}>{d}</li>)}</ul>
          <h3>{t.education.coursesHeading}</h3>
          <ul className="courses">{t.education.courses.map((c) => <li key={c}>{c}</li>)}</ul>
        </section>

        <section id="contato" aria-labelledby="h-contato">
          <h2 id="h-contato"><span aria-hidden="true">05</span>{t.contact.heading}</h2>
          <p className="prose">{t.contact.lead}</p>
          <ul className="contact">
            <li><a href={`mailto:${links.email}`}>{links.email}</a></li>
            <li><a href={links.github} rel="noopener">GitHub ↗</a></li>
            <li><a href={links.linkedin} rel="noopener">LinkedIn ↗</a></li>
            <li>{t.contact.city}</li>
          </ul>
        </section>
      </main>

      <footer className="foot"><p>{t.footer}</p></footer>
    </>
  )
}

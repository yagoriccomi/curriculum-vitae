import { renderToString } from 'react-dom/server'
import { App } from './App'
import { dict, type Lang } from './i18n'

export const render = (lang: Lang) => ({ html: renderToString(<App lang={lang} />), t: dict[lang] })

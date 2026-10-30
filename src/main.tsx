import { hydrateRoot } from 'react-dom/client'
import { App } from './App'
import { langFromPath } from './i18n'
import './styles.css'

hydrateRoot(document.getElementById('root')!, <App lang={langFromPath(location.pathname)} />)

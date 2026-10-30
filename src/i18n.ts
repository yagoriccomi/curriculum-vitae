// Rascunho (premissa P1): textos a revisar no ticket 002/008.
export type Lang = 'pt' | 'en'

const pt = {
  htmlLang: 'pt-BR',
  title: 'Yago Riccomi: Código + Direito',
  description:
    'Portfólio de Yago Riccomi Silveira, desenvolvedor web e estudante de Direito em Rio Claro/SP. Projetos em React, Node, TypeScript e Docker.',
  nav: { about: 'Sobre', projects: 'Projetos', path: 'Trajetória', education: 'Formação', contact: 'Contato' },
  switchLabel: 'Read in English',
  switchShort: 'EN',
  hero: {
    kicker: '§ 1º — Das partes',
    title: ['Código', '+', 'Direito'],
    lead: 'Escrevo software que funciona e estudo as leis que dizem o que ele pode fazer. Às vezes, nessa ordem.',
    cta: 'Ver os autos (projetos)',
  },
  about: {
    heading: 'Sobre',
    body: [
      'Sou Yago, de Rio Claro/SP. Técnico em Desenvolvimento de Sistemas pela Etec, passei por estágio de TI, freelas de desenvolvimento web e até venda de planos de telefonia (sim, sei negociar prazo).',
      'Hoje curso o 2º ano de Direito. Parece desvio de rota; é atalho: quem entende de contrato, LGPD e responsabilidade escreve sistemas que não viram processo.',
    ],
  },
  projects: {
    heading: 'Projetos',
    stackLabel: 'Stack',
    repoLabel: 'Repositório',
    items: [
      {
        name: 'Fodinha online',
        repo: 'jogo-de-cartas',
        text: 'Jogo de cartas multiplayer no navegador. Salas por código, até 10 jogadores (bots completam a mesa) e servidor autoritativo, porque confiar no cliente é nulidade absoluta.',
        stack: ['React', 'Node', 'Socket.IO', 'TypeScript'],
      },
      {
        name: 'Snake Thai',
        repo: 'snake-thai',
        text: 'Gestão de alunos de uma academia: app mobile, API e painel web. Notificações, autenticação e monitoramento de erros.',
        stack: ['React Native', 'Expo', 'Express', 'Next.js', 'Supabase', 'Zod'],
      },
      {
        name: 'Minecraft descentralizado',
        repo: 'docker-minecraft-server',
        text: 'Servidor de Minecraft que roda na máquina de qualquer amigo. O mapa sincroniza por P2P e há proteção contra dois servidores abertos ao mesmo tempo (o famoso split-brain).',
        stack: ['Docker', 'PowerShell', 'Syncthing', 'Tailscale'],
      },
      {
        name: 'Automações do dia a dia',
        repo: 'comandos-em-meu-computador',
        text: 'A Alexa dispara comandos no meu Windows, e um script reaplica o Vencord sozinho depois de cada update do Discord. Preguiça bem aplicada.',
        stack: ['JavaScript', 'PowerShell'],
      },
    ],
  },
  path: {
    heading: 'Trajetória',
    items: [
      { when: '2025 – hoje', what: 'Direito (2º ano)', where: 'Anhanguera' },
      { when: '10/2023 – 07/2024', what: 'Consultor de negócios', where: 'Cronologica Telefonia – Vivo' },
      { when: '10/2022 – 09/2023', what: 'Desenvolvedor web autônomo', where: 'React, Node, PHP, SQL, AWS, Docker' },
      { when: '03/2022 – 09/2022', what: 'Estagiário de TI', where: 'AutoSim Tecnologia' },
      { when: '09/2020 – 02/2021', what: 'Técnico de manutenção e suporte', where: 'PC-Click Informática' },
    ],
  },
  education: {
    heading: 'Formação',
    degrees: [
      'Bacharelado em Direito — Anhanguera, cursando (2º ano)',
      'Técnico em Desenvolvimento de Sistemas integrado ao Ensino Médio — Etec Prof. Armando Bayeux da Silva, 2019–2021',
    ],
    coursesHeading: 'Cursos Alura (2022)',
    courses: [
      'Pacote Office avançado (Word, Excel, PowerPoint, Outlook, Publisher)',
      'Servidores: Linux, e-mail, rede local e DNS',
      'Docker',
      'Python',
      'Node.js',
      'HTTP',
      'TypeScript',
      'React.js',
      'React Native',
    ],
  },
  contact: {
    heading: 'Contato',
    lead: 'Tem vaga, projeto ou dúvida sobre se o seu termo de uso vale alguma coisa? Fala comigo.',
    city: 'Rio Claro, SP',
  },
  footer: 'Feito com React, CSS puro e um pouco de cafeína.',
}

export type Dict = typeof pt

const en: Dict = {
  htmlLang: 'en',
  title: 'Yago Riccomi: Code + Law',
  description:
    'Portfolio of Yago Riccomi Silveira, web developer and law student in Rio Claro, Brazil. Projects in React, Node, TypeScript and Docker.',
  nav: { about: 'About', projects: 'Projects', path: 'Experience', education: 'Education', contact: 'Contact' },
  switchLabel: 'Ler em português',
  switchShort: 'PT',
  hero: {
    kicker: '§ 1 — The parties',
    title: ['Code', '+', 'Law'],
    lead: 'I write software that works and study the laws that say what it may do. Sometimes in that order.',
    cta: 'See the case files (projects)',
  },
  about: {
    heading: 'About',
    body: [
      "I'm Yago, from Rio Claro, Brazil. Systems development technician from Etec; I've done an IT internship, freelance web development and even sold phone plans (yes, I can negotiate a deadline).",
      "I'm now in my 2nd year of Law school. Looks like a detour; it's a shortcut: people who understand contracts, privacy law and liability build systems that don't end up in court.",
    ],
  },
  projects: {
    heading: 'Projects',
    stackLabel: 'Stack',
    repoLabel: 'Repository',
    items: [
      {
        name: 'Fodinha online',
        repo: 'jogo-de-cartas',
        text: 'Multiplayer card game in the browser. Rooms by code, up to 10 players (bots fill the table) and an authoritative server, because trusting the client is void from the start.',
        stack: ['React', 'Node', 'Socket.IO', 'TypeScript'],
      },
      {
        name: 'Snake Thai',
        repo: 'snake-thai',
        text: 'Student management for a gym: mobile app, API and web dashboard. Notifications, authentication and error monitoring.',
        stack: ['React Native', 'Expo', 'Express', 'Next.js', 'Supabase', 'Zod'],
      },
      {
        name: 'Decentralized Minecraft',
        repo: 'docker-minecraft-server',
        text: "A Minecraft server that runs on any friend's machine. The map syncs peer-to-peer, with protection against two servers running at once (the infamous split-brain).",
        stack: ['Docker', 'PowerShell', 'Syncthing', 'Tailscale'],
      },
      {
        name: 'Everyday automations',
        repo: 'comandos-em-meu-computador',
        text: 'Alexa runs commands on my Windows PC, and a script reapplies Vencord after every Discord update. Laziness, well applied.',
        stack: ['JavaScript', 'PowerShell'],
      },
    ],
  },
  path: {
    heading: 'Experience',
    items: [
      { when: '2025 – now', what: 'Law (2nd year)', where: 'Anhanguera' },
      { when: '10/2023 – 07/2024', what: 'Business consultant', where: 'Cronologica Telefonia – Vivo' },
      { when: '10/2022 – 09/2023', what: 'Freelance web developer', where: 'React, Node, PHP, SQL, AWS, Docker' },
      { when: '03/2022 – 09/2022', what: 'IT intern', where: 'AutoSim Tecnologia' },
      { when: '09/2020 – 02/2021', what: 'Maintenance and support technician', where: 'PC-Click Informática' },
    ],
  },
  education: {
    heading: 'Education',
    degrees: [
      'Bachelor of Laws — Anhanguera, in progress (2nd year)',
      'Systems Development technical degree, integrated with high school — Etec Prof. Armando Bayeux da Silva, 2019–2021',
    ],
    coursesHeading: 'Alura courses (2022)',
    courses: [
      'Advanced Office suite (Word, Excel, PowerPoint, Outlook, Publisher)',
      'Servers: Linux, e-mail, local network and DNS',
      'Docker',
      'Python',
      'Node.js',
      'HTTP',
      'TypeScript',
      'React.js',
      'React Native',
    ],
  },
  contact: {
    heading: 'Contact',
    lead: 'Got a job, a project, or a doubt about whether your terms of service hold up? Talk to me.',
    city: 'Rio Claro, Brazil',
  },
  footer: 'Made with React, plain CSS and some caffeine.',
}

export const dict: Record<Lang, Dict> = { pt, en }

export const links = {
  email: 'yago.riccomi.s@gmail.com',
  github: 'https://github.com/yagoriccomi',
  linkedin: 'https://br.linkedin.com/in/yago-riccomi-silveira-8b02a7224',
}

export const langFromPath = (path: string): Lang => (/\/en\/?$/.test(path) ? 'en' : 'pt')

// Textos na voz "Carta celeste" (escolhida no canvas de refino, R05). Fatos só do currículo.
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
    kicker: 'Uranographia · Tabula I',
    title: ['Yago', 'Riccomi'],
    lead: 'Desenvolvedor de software e estudante de Direito. Construo sites, APIs e apps com React, Node e TypeScript. Uso meus estudos em cibersegurança e LGPD para garantir a proteção dos meus clientes. Este é o meu céu: as estrelas douradas são projetos; as violetas, o caminho até aqui.',
    cta: 'Ver as estrelas (projetos)',
  },
  about: {
    heading: 'Quem traça este mapa',
    body: [
      'Sou Yago Riccomi, de Rio Claro/SP. Aprendi a programar no técnico da Etec e, desde então, faço sites, APIs e apps: em estágio, em freelas e nos meus próprios projetos.',
      'Hoje curso o 2º ano de Direito. Não é mudança de rota: entender contrato, LGPD e responsabilidade me ajuda a escrever sistemas que protegem quem usa.',
    ],
  },
  projects: {
    heading: 'Projetos',
    stackLabel: 'Stack',
    repoLabel: 'Repositório',
    items: [
      {
        name: 'Fodinha - cardgame',
        repo: 'jogo-de-cartas',
        text: 'Jogo de cartas multiplayer no navegador. Salas por código, até 10 jogadores (bots completam a mesa) e servidor autoritativo: quem valida cada jogada é o servidor, não o navegador.',
        stack: ['React', 'Node', 'Socket.IO', 'TypeScript'],
      },
      {
        name: 'Snake Thai',
        repo: 'snake-thai',
        text: 'Gestão de alunos de uma academia: app mobile, API e painel web. Notificações, autenticação e monitoramento de erros.',
        stack: ['React Native', 'Expo', 'Express', 'Next.js', 'Supabase', 'Zod'],
      },
      {
        name: 'Stream P2P',
        repo: 'stream-p2p',
        text: 'Transmissão de tela entre amigos, sem login: voz em tempo real, vídeo com o mesmo atraso para todos, app para Windows e bot do Discord. O servidor só apresenta as pessoas; a mídia vai direto de um para o outro.',
        stack: ['Node', 'WebRTC', 'WebSocket', 'Tauri 2', 'Discord'],
      },
      {
        name: 'Minecraft descentralizado',
        repo: 'docker-minecraft-server',
        text: 'Servidor de Minecraft que roda na máquina de qualquer amigo. O mapa sincroniza por P2P, com proteção contra dois servidores abertos ao mesmo tempo.',
        stack: ['Docker', 'PowerShell', 'Syncthing', 'Tailscale'],
      },
      {
        name: 'Alexa no Windows',
        repo: 'comandos-em-meu-computador',
        text: 'Uma skill da Alexa que dispara comandos CMD e PowerShell no meu Windows: falo, e o PC executa.',
        stack: ['JavaScript', 'AWS Lambda', 'MQTT', 'PowerShell'],
      },
      {
        name: 'Vencord Auto-Repair',
        repo: 'vencord-autorepair',
        text: 'Instala o Vencord e o mantém aplicado: um menu .bat e scripts PowerShell reaplicam tudo sozinhos depois de cada atualização do Discord.',
        stack: ['PowerShell', 'Batch', 'Pester'],
      },
    ],
  },
  path: {
    heading: 'A rota até aqui',
    items: [
      { when: '08/2026 – hoje', what: 'Programador de sistemas de informação', where: 'SK Company' },
      { when: '04/2026 – 08/2026', what: 'Assistente administrativo', where: 'JP Soluções Administrativas e Treinamentos' },
      { when: '10/2023 – 07/2024', what: 'Consultor de negócios', where: 'Cronologica Telefonia – Vivo' },
      { when: '10/2022 – 09/2023', what: 'Desenvolvedor web autônomo', where: 'React, Node, PHP, SQL, AWS, Docker' },
      { when: '03/2022 – 09/2022', what: 'Estagiário de TI', where: 'AutoSim Tecnologia' },
      { when: '09/2020 – 02/2021', what: 'Técnico de manutenção e suporte', where: 'PC-Click Informática' },
    ],
  },
  education: {
    heading: 'Onde aprendi',
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
    heading: 'Para onde a flecha aponta',
    lead: 'Tem uma vaga, um projeto ou uma ideia que precisa de código e de cuidado jurídico? Escreva. O e-mail é o caminho mais curto.',
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
    kicker: 'Uranographia · Tabula I',
    title: ['Yago', 'Riccomi'],
    lead: 'Software developer and law student. I build websites, APIs and apps with React, Node and TypeScript. I use my studies in cybersecurity and data protection law to keep my clients safe. This is my sky: the gold stars are projects; the violet ones, the road so far.',
    cta: 'See the stars (projects)',
  },
  about: {
    heading: 'Who draws this map',
    body: [
      "I'm Yago Riccomi, from Rio Claro, Brazil. I learned to code in Etec's technical program and have been building websites, APIs and apps ever since: as an intern, as a freelancer and in my own projects.",
      "I'm now in my 2nd year of Law school. It's not a change of course: understanding contracts, privacy law and liability helps me build systems that protect the people who use them.",
    ],
  },
  projects: {
    heading: 'Projects',
    stackLabel: 'Stack',
    repoLabel: 'Repository',
    items: [
      {
        name: 'Fodinha - cardgame',
        repo: 'jogo-de-cartas',
        text: 'Multiplayer card game in the browser. Rooms by code, up to 10 players (bots fill the table) and an authoritative server: every move is validated by the server, not the browser.',
        stack: ['React', 'Node', 'Socket.IO', 'TypeScript'],
      },
      {
        name: 'Snake Thai',
        repo: 'snake-thai',
        text: 'Student management for a gym: mobile app, API and web dashboard. Notifications, authentication and error monitoring.',
        stack: ['React Native', 'Expo', 'Express', 'Next.js', 'Supabase', 'Zod'],
      },
      {
        name: 'Stream P2P',
        repo: 'stream-p2p',
        text: 'Screen sharing between friends, no login: real-time voice, video with the same delay for everyone, a Windows app and a Discord bot. The server only introduces people; media goes straight from one to another.',
        stack: ['Node', 'WebRTC', 'WebSocket', 'Tauri 2', 'Discord'],
      },
      {
        name: 'Decentralized Minecraft',
        repo: 'docker-minecraft-server',
        text: "A Minecraft server that runs on any friend's machine. The map syncs peer-to-peer, with protection against two servers running at once.",
        stack: ['Docker', 'PowerShell', 'Syncthing', 'Tailscale'],
      },
      {
        name: 'Alexa on Windows',
        repo: 'comandos-em-meu-computador',
        text: 'An Alexa skill that runs CMD and PowerShell commands on my Windows PC: I speak, the PC does it.',
        stack: ['JavaScript', 'AWS Lambda', 'MQTT', 'PowerShell'],
      },
      {
        name: 'Vencord Auto-Repair',
        repo: 'vencord-autorepair',
        text: 'Installs Vencord and keeps it applied: a .bat menu and PowerShell scripts reapply everything after every Discord update.',
        stack: ['PowerShell', 'Batch', 'Pester'],
      },
    ],
  },
  path: {
    heading: 'The road so far',
    items: [
      { when: '08/2026 – now', what: 'Information systems programmer', where: 'SK Company' },
      { when: '04/2026 – 08/2026', what: 'Administrative assistant', where: 'JP Soluções Administrativas e Treinamentos' },
      { when: '10/2023 – 07/2024', what: 'Business consultant', where: 'Cronologica Telefonia – Vivo' },
      { when: '10/2022 – 09/2023', what: 'Freelance web developer', where: 'React, Node, PHP, SQL, AWS, Docker' },
      { when: '03/2022 – 09/2022', what: 'IT intern', where: 'AutoSim Tecnologia' },
      { when: '09/2020 – 02/2021', what: 'Maintenance and support technician', where: 'PC-Click Informática' },
    ],
  },
  education: {
    heading: 'Where I learned',
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
    heading: 'Where the arrow points',
    lead: 'Got a job, a project or an idea that needs both code and legal care? Write to me. E-mail is the shortest route.',
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

export const langFromPath = (path: string): Lang => (/\/en(\/(index\.html)?)?$/.test(path) ? 'en' : 'pt')

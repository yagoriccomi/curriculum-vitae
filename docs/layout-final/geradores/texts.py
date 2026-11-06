# Três vozes de texto para o site (rascunho). Fatos só do currículo / i18n.ts.
LINKS = dict(email='yago.riccomi.s@gmail.com', github='https://github.com/yagoriccomi',
             linkedin='https://br.linkedin.com/in/yago-riccomi-silveira-8b02a7224', city='Rio Claro, SP')

PATH = [
  dict(when='08/2026 – hoje', what='Programador de sistemas de informação', where='SK Company'),
  dict(when='04/2026 – 08/2026', what='Assistente administrativo', where='JP Soluções Administrativas e Treinamentos'),
  dict(when='10/2023 – 07/2024', what='Consultor de negócios', where='Cronologica Telefonia – Vivo'),
  dict(when='10/2022 – 09/2023', what='Desenvolvedor web autônomo', where='React, Node, PHP, SQL, AWS, Docker'),
  dict(when='03/2022 – 09/2022', what='Estagiário de TI', where='AutoSim Tecnologia'),
  dict(when='09/2020 – 02/2021', what='Técnico de manutenção e suporte', where='PC-Click Informática'),
]
DEGREES = [
  dict(what='Bacharelado em Direito', where='Anhanguera · cursando o 2º ano'),
  dict(what='Técnico em Desenvolvimento de Sistemas', where='Etec Prof. Armando Bayeux da Silva · 2019–2021, integrado ao Ensino Médio'),
]
COURSES = ['Docker', 'Node.js', 'TypeScript', 'React.js', 'React Native', 'Python', 'HTTP',
           'Servidores Linux, e-mail, rede e DNS', 'Pacote Office avançado']

# textos de projeto: neutro (vozes A e B) e com humor (voz C, o rascunho original)
PROJ_TEXT = {
  'neutro': {
    'd': 'Uma skill da Alexa que dispara comandos CMD e PowerShell no meu Windows: falo, e o PC executa.',
    'm': 'Instala o Vencord e o mantém aplicado: um menu .bat e scripts PowerShell reaplicam tudo sozinhos depois de cada atualização do Discord.',
    'e': 'Jogo de cartas multiplayer no navegador. Salas por código, até 10 jogadores (bots completam a mesa) e servidor autoritativo: quem valida cada jogada é o servidor, não o navegador.',
    's': 'Gestão de alunos de uma academia: app mobile, API e painel web. Notificações, autenticação e monitoramento de erros.',
    'p': 'Transmissão de tela entre amigos, sem login: voz em tempo real, vídeo com o mesmo atraso para todos, app para Windows e bot do Discord. O servidor só apresenta as pessoas; a mídia vai direto de um para o outro.',
    'z': 'Servidor de Minecraft que roda na máquina de qualquer amigo. O mapa sincroniza por P2P, com proteção contra dois servidores abertos ao mesmo tempo.',
  },
  'humor': {
    'd': 'Uma skill da Alexa que dispara comandos CMD e PowerShell no meu Windows. Falo, e o PC obedece (o que é mais do que eu consigo dizer de mim).',
    'm': 'Instala o Vencord e o mantém aplicado: depois de cada update do Discord, os scripts reaplicam tudo sozinhos. Preguiça bem aplicada.',
    'e': 'Jogo de cartas multiplayer no navegador. Salas por código, até 10 jogadores (bots completam a mesa) e servidor autoritativo, porque confiar no cliente é nulidade absoluta.',
    's': 'Gestão de alunos de uma academia: app mobile, API e painel web. Notificações, autenticação e monitoramento de erros.',
    'p': 'Transmissão de tela entre amigos, sem login: voz em tempo real, vídeo com o mesmo atraso para todos, app para Windows e bot do Discord. O servidor só apresenta as pessoas; a mídia vai direto de um para o outro.',
    'z': 'Servidor de Minecraft que roda na máquina de qualquer amigo. O mapa sincroniza por P2P e há proteção contra dois servidores abertos ao mesmo tempo (o famoso split-brain).',
  },
}

VOICES = [
  dict(id='a', label='Carta celeste', note='o site como um atlas: vocabulário de mapa antigo, humor leve', proj='neutro',
       kicker='Uranographia · Tabula I',
       lead='Desenvolvedor de software e estudante de Direito. Construo sites, APIs e apps com React, Node e TypeScript. Uso meus estudos em cibersegurança e LGPD para garantir a proteção dos meus clientes. Este é o meu céu: as estrelas douradas são projetos; as violetas, o caminho até aqui.',
       hint='Douradas são projetos; violetas contam o caminho. Toque numa delas.',
       t_sobre='Quem traça este mapa', t_traj='A rota até aqui', t_form='Onde aprendi', t_cont='Para onde a flecha aponta',
       sobre=['Sou Yago Riccomi, de Rio Claro/SP. Aprendi a programar no técnico da Etec e, desde então, faço sites, APIs e apps: em estágio, em freelas e nos meus próprios projetos.',
              'Hoje curso o 2º ano de Direito. Não é mudança de rota: entender contrato, LGPD e responsabilidade me ajuda a escrever sistemas que protegem quem usa.'],
       contato='Tem uma vaga, um projeto ou uma ideia que precisa de código e de cuidado jurídico? Escreva. O e-mail é o caminho mais curto.'),
  dict(id='b', label='Direto', note='sem metáforas: frases curtas e profissionais, a arte impressiona sozinha', proj='neutro',
       kicker='Portfólio',
       lead='Desenvolvedor web (React, Node, TypeScript, Docker) e estudante de Direito.',
       hint='Estrelas douradas: projetos. Violetas: sobre mim, trajetória, formação e contato.',
       t_sobre='Sobre', t_traj='Trajetória', t_form='Formação', t_cont='Contato',
       sobre=['Técnico em Desenvolvimento de Sistemas pela Etec, com experiência em estágio de TI, desenvolvimento web autônomo e atendimento comercial.',
              'Curso o 2º ano de Direito e uno as duas áreas: contratos, proteção de dados (LGPD) e responsabilidade de quem desenvolve software.'],
       contato='Disponível para vagas e projetos de desenvolvimento web. Respondo pelo e-mail.'),
  dict(id='c', label='Bem-humorado', note='o tom do rascunho atual, com as piadas jurídicas e do céu', proj='humor',
       kicker='Mapa do céu, versão dev',
       lead='Escrevo software que funciona e estudo as leis que dizem o que ele pode fazer. Às vezes, nessa ordem.',
       hint='As que piscam querem atenção. Pode clicar, elas não mordem.',
       t_sobre='Quem é esse arqueiro', t_traj='Por onde andei', t_form='Onde estudei', t_cont='Manda um sinal',
       sobre=['Sou Yago, de Rio Claro/SP. Técnico pela Etec, já fiz estágio de TI, freelas de web e até vendi plano de telefonia (sim, sei negociar prazo).',
              'Hoje curso o 2º ano de Direito. Parece desvio de rota, mas é atalho: sistema escrito por quem entende de contrato e LGPD tem menos chance de virar processo.'],
       contato='Vaga, projeto ou dúvida sobre se o seu termo de uso vale alguma coisa? A flecha aponta para cá.'),
]

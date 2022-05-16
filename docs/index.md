# Início

```mermaid

graph LR
    subgraph "1º Período"
        POR["Português"]
        MAT["Matemática"]
        INF["Informática Básica"]
        RED["Introd. Redes"]
        ELE["Eletricidade"]
        QVI["Qualidade Vida"]        
    end

    RED --> ISA & TCP
    ELE --> ELD
    INF --> ISA & TCP

    subgraph "2º Período"
        ALG["Algoritmos"]
        ISA["Introdução a Sistemas Abertos"]
        TCP["Arquitetura TCP/IP"]
        ELD["Eletrônica Digital"]
        ING["Inglês Técnico"]
    end
    
    TCP --> INT
    ALG & TCP --> PRE
    ISA --> ASA
    ELD --> CAB

    subgraph "3º Período"
        ASA["Administração de Sistemas Abertos"]
        CAB["Cabeamento Estruturado"]
        INT["Interconexões de Redes"]
        PRE["Programação para Redes"]
        SOC["Sociologia do Trabalho"]
    end

    CAB & INT --> PRI
    ASA & PRE --> SEG
    PRE --> PRW
    CAB --> PPR
    INT --> PPR

    subgraph "4º Período"
        PPR["Planejamento e Projeto de Redes"]
        PRW["Programação Web"]
        SEG["Gerência e Segurança de Redes"]
        PRI["Projeto Integrador"]
        GOR["Gestão Organizacional"]
        ASP["Administração de Sistemas Proprietários"]
        CAD["Desenho Auxiliado pelo Computador"]
    end

    click ASA "https://mange.ifrn.edu.br/curso/tec_sub_redes/administracao-de-sistemas-abertos/"
    click ASP "https://mange.ifrn.edu.br/curso/tec_sub_redes/administracao-de-sistemas-proprietarios/"
    click ALG "https://mange.ifrn.edu.br/curso/tec_sub_redes/algoritmos/"
    click TCP "https://mange.ifrn.edu.br/curso/tec_sub_redes/arquitetura-tcpip/"
    click CAB "https://mange.ifrn.edu.br/curso/tec_sub_redes/cabeamento-estruturado-e-redes-de-acesso/"
    click CAD "https://mange.ifrn.edu.br/curso/tec_sub_redes/cad/"
    click ELE "https://mange.ifrn.edu.br/curso/tec_sub_redes/eletricidade/"
    click ELD "https://mange.ifrn.edu.br/curso/tec_sub_redes/eletronica-digital/"
    click SEG "https://mange.ifrn.edu.br/curso/tec_sub_redes/gerencia-e-seguranca-de-redes/"
    click GOR "https://mange.ifrn.edu.br/curso/tec_sub_redes/gestao-organizacional/"
    click INF "https://mange.ifrn.edu.br/curso/tec_sub_redes/informatica-basica/"
    click ING "https://mange.ifrn.edu.br/curso/tec_sub_redes/ingles-tecnico/"
    click INT "https://mange.ifrn.edu.br/curso/tec_sub_redes/interconexao-de-redes/"
    click ISA "https://mange.ifrn.edu.br/curso/tec_sub_redes/introducao-a-sistemas-abertos/"
    click RED "https://mange.ifrn.edu.br/curso/tec_sub_redes/introducao-as-redes-de-computadores/"
    click POR "https://mange.ifrn.edu.br/curso/tec_sub_redes/lingua-portuguesa/"
    click MAT "https://mange.ifrn.edu.br/curso/tec_sub_redes/matematica/"
    click PPR "https://mange.ifrn.edu.br/curso/tec_sub_redes/planejamento-e-projeto-de-redes/"
    click PRE "https://mange.ifrn.edu.br/curso/tec_sub_redes/programacao-para-redes/"
    click PRW "https://mange.ifrn.edu.br/curso/tec_sub_redes/programacao-web/"
    click PRI "https://mange.ifrn.edu.br/curso/tec_sub_redes/projeto-integrador/"
    click QVI "https://mange.ifrn.edu.br/curso/tec_sub_redes/qualidade-de-vida-e-trabalho/"
    click SOC "https://mange.ifrn.edu.br/curso/tec_sub_redes/sociologia-do-trabalho/"

```

## Programa das disciplinas

- [Administração de Sistemas Abertos ](administracao-de-sistemas-abertos.md)
- [Administração de Sistemas Proprietários ](administracao-de-sistemas-proprietarios.md)
- [Algoritmos ](algoritmos.md)
- [Arquitetura TCP/IP](arquitetura-tcpip.md)
- [Cabeamento Estruturado e Redes de Acesso ](cabeamento-estruturado-e-redes-de-acesso.md)
- [CAD ](cad.md)
- [Eletricidade ](eletricidade.md)
- [Eletrônica Digital ](eletronica-digital.md)
- [Gerência e Segurança de Redes ](gerencia-e-seguranca-de-redes.md)
- [Gestão Organizacional ](gestao-organizacional.md)
- [Informática Básica ](informatica-basica.md)
- [Inglês Técnico ](ingles-tecnico.md)
- [Interconexão de Redes ](interconexao-de-redes.md)
- [Introdução a Sistemas Abertos ](introducao-a-sistemas-abertos.md)
- [Introdução às Redes de Computadores ](introducao-as-redes-de-computadores.md)
- [Língua Portuguesa ](lingua-portuguesa.md)
- [Matemática ](matematica.md)
- [Planejamento e Projeto de Redes ](planejamento-e-projeto-de-redes.md)
- [Programação para Redes ](programacao-para-redes.md)
- [Programação Web](programacao-web.md)
- [Projeto integrador](projeto-integrador.md)
- [Qualidade de Vida e Trabalho ](qualidade-de-vida-e-trabalho.md)
- [Sociologia do Trabalho ](sociologia-do-trabalho.md)

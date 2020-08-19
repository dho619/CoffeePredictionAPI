# CoffeePredictionAPI
Api para o sistema distribuído do TCC, com foco em predição de doenças em folhas de café

Flask seed run
    Atualmente esta populando usuários e áreas para o usuário de id 2 "comum@comum.com", infelizmente o email não consegui criar um que funcionasse para inserção de diversos usuários


Teste:

    Atualmente o teste das rotas funciona da seguinte forma:
        * O caminho do banco precisa estar o do banco de testes
        * O programa deve estar rodando: 'flask run -h 192.168.0.XX'
        * Na pasta raiz do projeto executar 'pytest'


    A pasta teste deve conter:
        * myToken.py: Que contém os tokens e baseURL
        * setup.*: Arquivos de configuração dos pytest
        * test_createBank: Para criar um banco de testes novo
        * test_01_post: testes de criação de registros, menos o de classifications
        * test_02_put: teste de atualização dos registros
        * test_03_get: teste de exibição dos registros
        * test_04_classifications: teste relacionados a classificação das imagens
        * test_99_delete: testes de deletar registros

        Obs: arquivos contendo testes devem começar com 'test' e ter funções que também comecem com 'test'

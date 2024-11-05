# Rodmap-apollo--Sansagrate
Este projeto utiliza o modelo YOLOv8 e a biblioteca OpenCV para realizar a detecção e contagem de pessoas e carros em um vídeo. O código é projetado para identificar objetos que cruzam uma linha específica no vídeo e contar o número de ocorrências.

# Funcionalidades
Detecta pessoas e carros em vídeos usando YOLOv8.
Conta o número de pessoas e carros que cruzam uma linha de contagem.
Exibe o vídeo com a linha de contagem e os contadores em tempo real.

# Estrutura do Projeto
Copiar código
├── backend.processamento.py  # Código principal para contagem de objetos
├── videos/
│   └── seu_video.mp4          # Vídeo de entrada para teste
├── output/
│   └── resultados.txt         # Resultados da contagem, se necessário
├── README.md                  # Documentação do projeto
└── requirements.txt           # Lista de dependências

# Pré-requisitos
Python 3.6 ou superior
YOLOv8 para detecção de objetos
OpenCV para manipulação de vídeos

# Uso
Coloquei o video de referencia na pasta

# Execute o script principal:
bash
Copiar código
python3 backend.processamento.py
O script exibirá o vídeo com uma linha de contagem. Quando uma pessoa ou carro cruzar a linha, o contador será atualizado em tempo real.
Para sair do vídeo, pressione q.

# Parâmetros do Código
video_path: Caminho para o vídeo de entrada.
line_position: Posição vertical da linha de contagem (0.5 significa que a linha está no meio do vídeo).

# Exemplo de Saída
Ao finalizar a execução, o código imprimirá o total de pessoas e carros que cruzaram a linha de contagem:
Copiar código
Total de pessoas: 10
Total de carros: 5

# Referências
OpenCV: Biblioteca de código aberto para visão computacional. Documentação [OpenCV Documentation](https://docs.opencv.org/)
YOLOv8: Modelo de detecção de objetos. GitHub - **ultralytics** [YOLOv8 - GitHub - ultralytics](https://github.com/ultralytics/ultralytics)
[Python Documentation](https://docs.python.org/3/) - Documentação oficial do Python.


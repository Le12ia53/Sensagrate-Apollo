import cv2

def process_video(video_path, line_position):
    # Abre o vídeo
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return 0, 0  # Retorna zero se o vídeo não abrir
    
    # Inicializa contadores
    people_count = 0
    car_count = 0
    
    # Obtém a largura e altura do vídeo para definir a linha (não sei o tipo de video)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    line_y = int(frame_height * line_position)  # Define a posição da linha
    
    # Parâmetros do processamento (subtração de fundo)
    background_subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Sai do loop ao final do vídeo

        # Processei o quadro e extrai as máscaras
        mask = background_subtractor.apply(frame)
        
        # Reduzir o ruído
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, (5, 5))

        # Encontra contornos
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Desenhei a linha de contagem
        cv2.line(frame, (0, line_y), (frame_width, line_y), (0, 255, 255), 2)
        
        for contour in contours:
            # Ignorei contornos pequenos
            if cv2.contourArea(contour) < 500:
                continue
            
            # posicionei do centro do contorno
            x, y, w, h = cv2.boundingRect(contour)
            center_y = y + h // 2

            # Contabilizei objetos que cruzam a linha
            if center_y >= line_y - 2 and center_y <= line_y + 2:
                # incluir uma lógica para identificar tipos, como carros ou pessoas
                people_count += 1  

        # Exibir o quadro (depuração)
        cv2.imshow("Video", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # Liberei o vídeo e fecha janelas
    cap.release()
    cv2.destroyAllWindows()
    
    # Retorna os resultados da contagem
    return people_count, car_count

# Testando a função com um vídeo de exemplo
if __name__ == "__main__":
    video_path = "e:\\Users\\leia\\Downloads\\sensa_countage.avi"  # Caminho do vídeo
    line_position = 0.5  # Linha de contagem no meio do vídeo

    # Executa a contagem de objetos
    people_count, car_count = process_video(video_path, line_position)

    # Exibe o resultado final
    print(f"Total de pessoas: {people_count}")
    print(f"Total de carros: {car_count}")


import cv2
from ultralytics import YOLO

# Carregar o modelo YOLOv8 pré-treinado (YOLOv8s para maior precisão ou YOLOv8n para mais velocidade)
model = YOLO('yolov8n.pt')  # Use yolov8s.pt para um modelo mais preciso

# Função principal para processar o vídeo e contar objetos
def process_video(video_path, line_position=0.5):
    # Carregar o vídeo
    cap = cv2.VideoCapture(video_path)
    
    # Dimensões do vídeo
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    line_y = int(frame_height * line_position)

    # Contadores
    people_count = 0
    car_count = 0

    # Lista para rastrear IDs de objetos que já cruzaram a linha
    crossed_ids = set()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Realizar a detecção usando YOLO
        results = model(frame)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Identificar o tipo de objeto e coordenadas do bounding box
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas do bounding box
                label = result.names[int(box.cls[0])]  # Nome da classe (e.g., 'person' ou 'car')

                # Desenhar o bounding box e o label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Calcular o centro do bounding box
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)

                # Verificar se o centro cruzou a linha de contagem
                if center_y >= line_y - 2 and center_y <= line_y + 2:
                    obj_id = id(box)  # Usar o ID do objeto para rastreamento simples
                    if obj_id not in crossed_ids:
                        crossed_ids.add(obj_id)
                        if label == 'person':
                            people_count += 1
                        elif label == 'car':
                            car_count += 1

        # Desenhar a linha de contagem
        cv2.line(frame, (0, line_y), (frame_width, line_y), (255, 0, 0), 2)

        # Exibir contadores na tela
        cv2.putText(frame, f'Pessoas: {people_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f'Carros: {car_count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Exibir o vídeo com as marcações
        cv2.imshow('Contagem de Objetos', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar o vídeo e fechar janelas
    cap.release()
    cv2.destroyAllWindows()

    # Retornar os resultados da contagem
    return people_count, car_count

# Testando a função com um vídeo 
if __name__ == "__main__":
    video_path = "video.mp4"  # Substitua pelo caminho do vídeo que deseja usar
    people_count, car_count = process_video(video_path)

    # Exibir o resultado final
    print(f"Total de pessoas: {people_count}")
    print(f"Total de carros: {car_count}")


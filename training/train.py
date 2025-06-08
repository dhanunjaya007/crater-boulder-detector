from ultralytics import YOLO

def main():
    # Load YOLOv8 model 
    model = YOLO('yolov8n.pt')  # yolov8n.pt is the tiny pretrained model

    # Train the model
    model.train(
        data='data.yaml',    # Path to your dataset config YAML (classes, train/val paths)
        epochs=50,           # Number of training epochs
        imgsz=640,           # Image size (height = width)
        batch=16,            # Batch size, adjust to your GPU memory
        name='crater_boulder_exp', # Experiment name for saving results
        device='0'           # GPU device (set 'cpu' if no GPU)
    )

if __name__ == "__main__":
    main()

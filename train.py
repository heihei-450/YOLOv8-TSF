from ultralytics import YOLO
import cv2 as cv

if __name__ == '__main__':
    model = YOLO('/home/liu/zjr/zjr_ultralytics_two_stream/model/yolov8m-seg-2stream-add-postfusion-zjr.yaml')  # build a new model from YAML
    # 预训练模型  c
    #pre_model_path = r'/home/liu/zjr/zjr_ultralytics_two_stream/weights/权重以及配置文件/权重/yolov11m-2stream-seg/weights/best.pt'
    """
    更多详细配置在   ultralytics/yolo/cfg/default.yaml
    """
    model.train(data="/home/liu/zjr/zjr_ultralytics_two_stream/dataset/LLVIP.yaml", epochs=100, imgsz=640, device=0, batch=4, amp=False,
                project='/home/liu/zjr/zjr_ultralytics_two_stream/meruns',
                name='yolo11-seg',
                # 是否覆盖原来的目录
                exist_ok=True,
                cache = False,
                # 非确定性
                deterministic=False)

    # 推理
    # model = YOLO(r'D:\project\Python\ultralytics_two_stream\weights\add_jet_0.901.pt')  # load a custom model
    #
    # # Predict with the model
    # results = model([r'D:\project\Python\ultralytics_two_stream\catch_result\论文\color.png',r'D:\project\Python\ultralytics_two_stream\catch_result\论文\depth.png'])  # predict on an image*
    # # 保存结果图
    # res_plotted = results[0].plot(labels=False)
    # # 保存至photo文件夹下
    # cv.imwrite("reslt.png", res_plotted)
from ultralytics import YOLO
import cv2 as cv

if __name__ == '__main__':
    model = YOLO('Yaml Path')  # build a new model from YAML

    """
    更多详细配置在   ultralytics/yolo/cfg/default.yaml
    """
    model.train(data="datasets Path", epochs=100, imgsz=640, device=0, batch=4, amp=False,
                project='run project path',
                name='yolo11-seg',
                # 是否覆盖原来的目录
                exist_ok=True,
                cache = False,
                # 非确定性
                deterministic=False)

    # 推理
    # model = YOLO(r'weight path .pt')  # load a custom model
    #
    # # Predict with the model
    # results = model([r'rgb path',r'depth path'])  # predict on an image*
    # # 保存结果图
    # res_plotted = results[0].plot(labels=False)
    # cv.imwrite("reslt.png", res_plotted)

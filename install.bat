#!/bin/bash
cd src/packages/pybullet-gym && pip3 install -e .
pip3 install gym[box2d]
pip3 install Box2d==2.3.10
pip3 install gym==0.23.1
pip3 install gym-notices==0.0.6
pip3 install tensorflow==2.2.0
pip3 install opencv-python==4.5.5.64
pip3 install matplotlib==3.5.2
pip3 install scikit-learn==1.1.0
pip3 install protobuf==3.20.1
pip3 install numpy==1.22.3
pip3 install imageio==2.19.1
pip3 install python-qt
pip3 install PyQt5==5.12
pip3 install pyqtgraph==0.12.4

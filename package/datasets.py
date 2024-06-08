from package.cleansing import *

class load_heart_disease:
  def __init__(self):
    datas = load_main()

    self.data = [datas[i][1:] for i in range(len(datas))]
    self.target = [datas[i][0] for i in range(len(datas))]

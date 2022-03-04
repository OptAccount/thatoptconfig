class Opt:
    def __init__(self):
        self.train_data = 'train_data/'
        self.valid_data = 'test_data/'
        self.manualSeed = 1111
        self.workers = 4
        self.batch_size = 192
        self.num_iter = 70000
        self.valInterval = 2000
        self.saved_model = 'ocr_model_eng.pth'
        self.FT = False
        self.adam = False
        self.lr = 1
        self.beta1 = 0.9
        self.rho = 0.95
        self.eps = 1e-08
        self.grad_clip = 5
        self.baiduCTC = False
        self.select_data = ['/']
        self.batch_ratio = ['1']
        self.total_data_usage_ratio = 1.0
        self.batch_max_length = 25
        self.imgH = 32
        self.imgW = 100
        self.rgb = False
        self.character = " !\"#$%&'()*+,-./0123456789:;<=>?@[\\]^_{|}~«»ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz№"
        self.sensitive = False
        self.PAD = False
        self.data_filtering_off = False
        self.Transformation = "TPS"
        self.FeatureExtraction = "ResNet"
        self.SequenceModeling = "BiLSTM"
        self.Prediction = "Attn"
        self.num_fiducial = 20
        self.input_channel = 1
        self.output_channel = 512
        self.hidden_size = 256
        self.num_gpu = 1
        self.num_class = 98




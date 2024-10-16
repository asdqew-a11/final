import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib as mpl
import seaborn as sns
import sklearn as skl

if __name__ == "__main__":
    # 설치된 라이브러리 버전 확인
    print(f"pandas: pd {pd.__version__}")
    print(f"numpy : np {np.__version__}")
    print(f"matplotlib : mpl {mpl.__version__}")
    print(f"seaborn : sns {sns.__version__}")
    print(f"sklearn : skl {skl.__version__}")

    #matplotlib에는 한글을 가져오는 기능이 없기 떄문에 하는 한글 출력 작업

    font_path = "c:\Windows\Fonts\malgun.ttf"  
    font_prop = mpl.font_manager.FontProperties(fname=font_path) 
    mpl.rcParams['font.family'] = font_prop.get_name()
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column=['student_id','age']
    df=pd.DataFrame(student_data,columns=column)
    return df

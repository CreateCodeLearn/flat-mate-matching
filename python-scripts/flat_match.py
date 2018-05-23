def flat_match (v_location,v_gender,v_rent,v_lowerage,v_upperage, filepath):
    '''
    Provides the dataset in CSV and based on input data uses booleans
    to subset the data to give the flats ranked according rent with cheapest
    showing first
    '''
    import pandas as pd
    
    def transform_data(dataframe):
        dd = dict()
        index = dataframe.sort_values("rent").index.tolist()
        for i in index:
            dd[i] = dataframe.loc[i].to_dict()
        return dd, index
    
    data = pd.read_csv(filepath, index_col=0) 
    
    boolean_location = data["location"] == v_location
    boolean_gender = data["gender"] == v_gender
    boolean_rent = data["rent"] <= v_rent
    boolean_upperage = data["lowerage"] >= v_lowerage
    boolean_upperage = data["upperage"] <= v_upperage
    
    user_constraints = boolean_location & boolean_gender & boolean_rent & boolean_lowerage & boolean_upperage
    results = data.loc[user_constraints]
    
    return transform_data(results)
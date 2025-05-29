class CleanerData: 
    
    def remove_outliers_with_specified_value(df,  column, value): 
        return df[df[column] != value]
    
    @staticmethod
    def remove_outliers_with_min_max(df,  column, lower_bound, upper_bound): 
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        
    
    @staticmethod
    def fill_missing_values(df,  column, method='mean'):
        if method == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif method == 'median':
            df[column].fillna(df[column].median(), inplace=True)
        elif method == 'mode':
            df[column].fillna(df[column].mode()[0], inplace=True)
        
        return df
    
    @staticmethod
    def convert_columns_to_specified_type(df, origin, dtype): 
        for col in df.columns: 
            if df[col].dtype == origin: df[col] = df[col].astype(dtype)

        return df

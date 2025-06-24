from scipy.stats import f_oneway

def analyze_performance_by_sentiment(df):
    groups = [group['Closed PnL'].values for name, group in df.groupby('classification')]
    anova_result = f_oneway(*groups)
    return anova_result

def correlation_analysis(df):
    correlation = df['value'].corr(df['Closed PnL'])
    return correlation


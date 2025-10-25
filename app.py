import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('Retail_Cleaned.csv')

def plot_dashboard(plot_type):
    plt.figure(figsize=(8,5))
    if plot_type == 'Age Distribution':
        sns.histplot(df['Age'], bins=20, kde=True)
        plt.title('Customer Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
    elif plot_type == 'Gender Distribution':
        sns.countplot(x='Gender', data=df)
        plt.title('Gender Distribution')
        plt.xlabel('Gender')
        plt.ylabel('Count')
    elif plot_type == 'Monthly Sales Trend':
        monthly_sales = df.groupby('Month')['TotalAmount'].sum()
        sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
        plt.title('Monthly Sales Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
    elif plot_type == 'Top 10 Cities':
        top_cities = df['City'].value_counts().nlargest(10)
        sns.barplot(x=top_cities.index, y=top_cities.values)
        plt.title('Top 10 Cities by Customer Count')
        plt.xlabel('City')
        plt.ylabel('Number of Customers')
        plt.xticks(rotation=45)
    elif plot_type == 'Total Sales by Product Category':
        category_sales = df.groupby('ProductCategory')['TotalAmount'].sum().sort_values(ascending=False)
        sns.barplot(x=category_sales.index, y=category_sales.values)
        plt.title('Total Sales by Product Category')
        plt.xlabel('Product Category')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
    elif plot_type == 'Payment Mode Usage':
        payment_counts = df['PaymentMode'].value_counts()
        plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title('Payment Mode Usage')
    elif plot_type == 'Average Spend by Age Group':
        agegroup_spend = df.groupby('AgeGroup')['TotalAmount'].mean()
        sns.barplot(x=agegroup_spend.index.astype(str), y=agegroup_spend.values)
        plt.title('Average Spend per Customer by Age Group')
        plt.xlabel('Age Group')
        plt.ylabel('Average Spend')
    elif plot_type == 'Top 10 Cities by Revenue':
        city_revenue = df.groupby('City')['TotalAmount'].sum().nlargest(10)
        sns.barplot(x=city_revenue.index, y=city_revenue.values)
        plt.title('Top 10 Cities by Revenue')
        plt.xlabel('City')
        plt.ylabel('Total Revenue')
        plt.xticks(rotation=45)
    elif plot_type == 'Product Category vs Payment Mode (Heatmap)':
        pivot_table = df.pivot_table(values='TotalAmount', index='ProductCategory', columns='PaymentMode', aggfunc='sum', fill_value=0)
        sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap='Blues')
        plt.title('Product Category vs Payment Mode (Total Sales)')
        plt.ylabel('Product Category')
        plt.xlabel('Payment Mode')
    plt.tight_layout()
    return plt

demo = gr.Interface(
    fn=plot_dashboard,
    inputs=gr.Radio([
        'Age Distribution',
        'Gender Distribution',
        'Monthly Sales Trend',
        'Top 10 Cities',
        'Total Sales by Product Category',
        'Payment Mode Usage',
        'Average Spend by Age Group',
        'Top 10 Cities by Revenue',
        'Product Category vs Payment Mode (Heatmap)'
    ], label="Select Visualization"),
    outputs="plot",
    title="Retail EDA Dashboard",
    description="Choose a plot to explore the retail data"
)

demo.launch()

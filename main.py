import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def load_data(uploaded_file):
    """Load data from an uploaded Excel File"""
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    return df

def clean_data(df, query):
    """Clean and transform data based on user query."""
    try:
        query = query.lower().strip()
        
        # Remove missing values
        if "remove missing values" in query:
            df = df.dropna()
            return df, "Missing values removed."
        
        # Remove duplicates
        if "remove duplicates" in query:
            df = df.drop_duplicates()
            return df, "Duplicates removed."
        
        # Filter rows based on a condition
        if "filter" in query:
            parts = query.split("filter")
            if len(parts) > 1:
                condition = parts[1].strip()
                try:
                    df = df.query(condition)
                    return df, f"Data filtered with condition: {condition}"
                except Exception as e:
                    return df, f"Error filtering data: {e}"
        
        # Rename columns
        if "rename" in query:
            parts = query.split("rename")
            if len(parts) > 1:
                # Extract the part after "rename"
                rename_part = parts[1].strip()
                # Split into old and new names using "to" as a delimiter
                if "to" in rename_part:
                    old_name, new_name = rename_part.split("to")
                    old_name = old_name.strip()
                    new_name = new_name.strip()
                    
                    # Handle case sensitivity: Match column names case-insensitively
                    matching_columns = [col for col in df.columns if col.lower() == old_name.lower()]
                    
                    if matching_columns:
                        # Use the actual column name from the dataset
                        actual_old_name = matching_columns[0]
                        df = df.rename(columns={actual_old_name: new_name})
                        return df, f"Column '{actual_old_name}' renamed to '{new_name}'."
                    else:
                        return df, f"Column '{old_name}' not found in the dataset."
                else:
                    return df, "Invalid rename query. Use format: 'rename old_name to new_name'."
        
        # Sort data
        if "sort" in query:
            parts = query.split("sort")
            if len(parts) > 1:
                column = parts[1].strip()
                ascending = "descending" not in query
                df = df.sort_values(by=column, ascending=ascending)
                return df, f"Data sorted by '{column}' in {'ascending' if ascending else 'descending'} order."
        
        # Aggregate data
        if "aggregate" in query:
            parts = query.split("aggregate")
            if len(parts) > 1:
                column = parts[1].strip()
                if "sum" in query:
                    df = df.groupby(column).sum().reset_index()
                    return df, f"Data aggregated by '{column}' with sum."
                elif "mean" in query:
                    df = df.groupby(column).mean().reset_index()
                    return df, f"Data aggregated by '{column}' with mean."
        
        # If no valid query is found
        return df, "No valid query found. Please try again."
    
    except Exception as e:
        return df, f"Error processing query: {e}"

def create_scatter_plot(df, x_axis, y_axis):
    """Create a scatter plot."""
    return px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")

def create_line_chart(df, x_axis, y_axis):
    """Create a line chart."""
    return px.line(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")

def create_bar_chart(df, x_axis, y_axis):
    """Create a bar chart."""
    return px.bar(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")

def create_histogram(df, column):
    """Create a histogram."""
    return px.histogram(df, x=column, title=f"Distribution of {column}")

def create_pie_chart(df, column):
    """Create a pie chart."""
    return px.pie(df, names=column, title=f"Pie Chart of {column}")

def create_heatmap(df, x_axis, y_axis, values):
    """Create a heatmap."""
    return px.density_heatmap(df, x=x_axis, y=y_axis, z=values, title=f"Heatmap of {x_axis} vs {y_axis}")

def create_box_plot(df, x_axis, y_axis):
    """Create a box plot."""
    return px.box(df, x=x_axis, y=y_axis, title=f"Box Plot of {x_axis} vs {y_axis}")

def create_violin_plot(df, x_axis, y_axis):
    """Create a violin plot."""
    return px.violin(df, x=x_axis, y=y_axis, title=f"Violin Plot of {x_axis} vs {y_axis}")

def create_area_chart(df, x_axis, y_axis):
    """Create an area chart."""
    return px.area(df, x=x_axis, y=y_axis, title=f"Area Chart of {x_axis} vs {y_axis}")
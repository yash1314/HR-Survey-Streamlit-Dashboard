import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title = 'HR Survey Results', layout = 'wide')

st.header(":blue[HR Survey Dashboard]", anchor = False, divider='rainbow')
st.write('[**Linkedin**](https://www.linkedin.com/in/yash907/), [**Github**](https://github.com/yash1314)')
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.markdown("""**Discover key insights from this HR survey Dashboard. Explore response types, status, departmental feedback, and 
            response counts. Let's uncover valuable insights together!**""")
st.markdown("----------------------------------------------------------------------------")

###----load Dataframe

df = pd.read_excel('hr_surveys.xlsx', sheet_name= 'main_sheet')

###----Displaying Elements

# Total responses

col1, col2 = st.columns([0.6, 0.5])
with col2:
    status_counts = df['Status'].value_counts().tolist()
    status_list = df['Status'].unique().tolist()
    
    color_dict = {
        'Complete': 'Plasma',
        'Incomplete': 'red'}

    total_response_pie = px.pie(names=status_list, values=status_counts, color=status_list,
                                color_discrete_map=color_dict)

    total_response_pie.update_layout(width=400, height=330, title='Response Status')

    st.plotly_chart(total_response_pie, use_container_width=False,
                   template= 'plotly_dark')

with col1:
    st.subheader("**Total Positive Response :**", anchor = False) 
    st.subheader(f":green[{df['Response_Category'].value_counts()['Positive']}]", anchor = False)
    
    st.subheader("**Total Negative Response :**", anchor = False)
    st.subheader(f":red[**{df['Response_Category'].value_counts()['Negative']}**]", anchor = False)

    st.subheader("**Total Neutral Response :**", anchor = False)
    st.subheader(f":blue[**{df['Response_Category'].value_counts()['Neutral']}**]", anchor = False)

st.markdown("----------------------------------------------------------------------------")

# Types of responses

col3, col4 = st.columns([0.1, 0.8])
with col4:
    response_text_list = df['Response Text'].unique().tolist()
    response_text_count = df.groupby('Response Text')['Status'].size()

    color_dict = {
        'Agree': 'blue',
        'Disagree': 'red',
        'Not Applicable': 'gray',
        'Strongly Agree': 'green',
        'Strongly Disagree': 'orange'
    }

    response_types_chart = px.bar( x=response_text_count, y=response_text_list, orientation='h', 
    color=response_text_list,color_discrete_map=color_dict, template = "plotly_dark")

    response_types_chart.update_layout(width=800,height=500, title='Response Types Count', 
                                        xaxis_title='Counts', yaxis_title='Types')

    st.plotly_chart(response_types_chart)
st.markdown("----------------------------------------------------------------------------")

# Department Wise Responses

department = df['Department'].unique().tolist()
dep_selection = st.multiselect('**Department**', department, default = department)

col5, col6 = st.columns([0.1, 0.8])

with col6:
    filtered_df = df[df['Department'].isin(dep_selection)]

    grouped_data = filtered_df.groupby(['Department', 'Response_Category']).size().reset_index(name='Count')

    # Plot using Plotly
    fig = px.bar(grouped_data, x='Count', y='Department', color='Response_Category', orientation='h', 
                title='Department-wise Response Category Count', barmode='group')
    fig.update_layout(width = 850, height = 610)
    st.plotly_chart(fig)

st.success('**Made with passion: Yash Keshari**')
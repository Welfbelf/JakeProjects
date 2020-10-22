import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('adjusted_csv.csv')
df = df[df['upper_pay']< 500000]



# chart = sns.boxplot(
#     data = df, x = 'upper_pay', y = 'new_sector', showfliers = False, orient = 'horizontal'
# )
#
# chart.set_yticklabels(chart.get_yticklabels(), fontsize = 'x-small')
#
# plt.show()

values = df.groupby('state').mean()['upper_pay'].tolist()
states = df.groupby('state').mean().index.tolist()


fips_df = pd.read_csv('fips.csv')

fip_state_name = fips_df['Name'].tolist()
fip_fip = fips_df['State (FIPS)'].tolist()

state_fip_code = []
pointer = 0

for fip_state in fip_state_name:
    for state in states:
        if state.strip() == fip_state.strip():
            state_fip_code.append(fip_fip[pointer])
        else:
            pass
    pointer += 1



print(states)
print(values)

fig = ff.create_choropleth(fips = state_fip_code, values = values, show_state_data= False, show_hover = True)

fig.layout.template = None
fig.show()


